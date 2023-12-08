# https://adventofcode.com/2023/day/1
import os
from typing import List
from functools import reduce

def load(test_mode: bool = False) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    with open(os.path.join(dirname, input_file)) as f:
        return f.readlines()


class Hand:
    DECK = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    DECK_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def __init__(self, cards: str, bid: str, part_2=True) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.joker = 'J' if part_2 else None
        self.deck = self.DECK_2 if part_2 else self.DECK
        self.score = self._compute_score()

    def _compute_score(self):
        scores = {}
        jokers_count = 0
        for card in set(self.cards):
            if self.joker is not None and card == self.joker:
                jokers_count = self.cards.count(self.joker)
            else:
                score = self.cards.count(card)
                scores.setdefault(score, []).append(card)

        for val in scores.values():
            val.sort(reverse=True)
        
        if jokers_count:
            if not scores:
                scores[0] = [self.joker]

            highest_score = max(scores.keys())
            ranked_up = scores.get(highest_score)[0]
            del scores.get(highest_score)[0]
            if not scores.get(highest_score):
                del scores[highest_score]
            
            scores[highest_score + jokers_count] = [ranked_up]
            if ranked_up != self.joker:
                scores[highest_score + jokers_count].append(self.joker)

        return scores

    def card_value(self, card: str) -> int:
        try:
            return self.deck.index(card)
        except ValueError:
            return -1

    def __lt__(self, __value: object):
        higher_values = []

        local_score = sorted(self.score.keys(), reverse=True)
        other_score = sorted(__value.score.keys(), reverse=True)
        for local_count, other_count in zip(local_score, other_score):
            if local_count < other_count:
                return True
            elif local_count > other_count:
                return False
            else:
                local_values = list(map(self.card_value, self.score[local_count]))
                other_values = list(map(self.card_value, __value.score[other_count]))
                # Joker in one of the hand, is lower
                if (
                        self.joker 
                        and self.card_value(self.joker) in local_values 
                        and not self.card_value(self.joker) in other_values
                    ):
                    return True
                if (
                        self.joker 
                        and self.card_value(self.joker) in other_values
                        and not self.card_value(self.joker) in local_values
                    ):
                    return False
                if len(list(local_values)) < len(list(other_values)):
                    return True
                elif len(list(local_values)) > len(list(other_values)):
                    return False
                else:
                    # Joker in one of the hand, is lower
                    if self.joker and self.joker in local_values and not self.joker in other_values:
                        higher_values.append(True)
                    else:
                        for max_card, max_other_card in zip(local_values, other_values):
                            if max_card < max_other_card:
                                higher_values.append(True)
                            elif max_card > max_other_card:
                                higher_values.append(False)
        # Same value, will count the 
        if not higher_values and self.joker:
            return self.cards.count(self.joker) > __value.cards.count(self.joker)
        try:
            return higher_values[0]
        except IndexError:
            return False

    def __eq__(self, __value: object) -> bool:
        return self.score == __value.score
    
    def __str__(self) -> str:
        return f"Hand: {self.cards} - Score: {sorted(self.score.items(), reverse=True)} - Bid: {self.bid}"

def main_01(cards: List[str], part_2: bool = False) -> int:
    ranks = []
    for i, card in enumerate(cards):
        hand = Hand(*card.split(), part_2=part_2)      
        ranks.append(hand)

    ranks.sort()
    # rank_str = '\n\t'.join(map(str, ranks))
    # print(f"Ranked: {rank_str}")
    return reduce(lambda x, y: x + y, ((i + 1) * ranks[i].bid for i in range(len(ranks))), 0)


if __name__ == '__main__':
    # test = True
    test = False
    print(f"First Response: {main_01(load(test))}")
    print(f"Second Response: {main_01(load(test), part_2=True)}")