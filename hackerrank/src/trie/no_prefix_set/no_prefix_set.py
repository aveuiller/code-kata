# Challenge: https://www.hackerrank.com/challenges/no-prefix-set/problem

# !/bin/python3
from dataclasses import dataclass, field

from typing import Dict, Optional


@dataclass
class TrieNode:
    letter: Optional[str]
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    available_word: int = 0


@dataclass
class Trie:
    tree: TrieNode = TrieNode(None)

    def add(self, name: str) -> bool:
        node = self.tree
        for letter in name:
            node = node.children.setdefault(letter, TrieNode(letter))
            if node.available_word > 0:
                return False

        if node.children:
            return False

        node.available_word += 1
        return True


def noPrefix(words):
    trie = Trie()
    result = "GOOD SET"
    for i, word in enumerate(words):
        if not trie.add(word):
            result = f"BAD SET\n{word}"
            break

    print(result)

# Expected
# BAD SET
# aabcde
TEST_CASE_1 = [
    "aab",
    "defgab",
    "abcde",
    "aabcde",
    "cedaaa",
    "bbbbbbbbbb",
    "jabjjjad",
]

# Expected
# BAD SET
# aacghgh
TEST_CASE_2 = [
    "aab",
    "aac",
    "aacghgh",
    "aabghgh",
]


def main():
    # n = int(input().strip())
    #
    # words = []
    #
    # for _ in range(n):
    #     words_item = input()
    #     words.append(words_item)
    words = TEST_CASE_1
    noPrefix(words)


if __name__ == '__main__':
    main()
