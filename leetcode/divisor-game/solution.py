class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

    def assert_first_player_wins(self, n: int) -> bool:
        divisor_count = 0
        for i in range(1, n):
            if n % i == 0:
                divisor_count += 1
        return (divisor_count % 2) != 0

    def play_the_game(self, n: int) -> bool:
        alice_turn = True

        return self.play_next_move(n, alice_turn)

    def play_next_move(self, n: int, alice_turn: bool) -> bool:
        moves = self.available_moves(n)
        if not moves:
            return not alice_turn

        alice_wins = False
        for x in moves:
            # Trying to chose optimal path...
            if ((n - x) % 2) != 0:
                alice_wins = alice_wins or self.play_next_move(n - x, not alice_turn)
                return alice_wins

        # Otherwise, continue on the wrong paths
        for x in moves:
            alice_wins = alice_wins or self.play_next_move(n - x, not alice_turn)

        return alice_wins

    def available_moves(self, n: int) -> List[int]:
        moves = []
        if n <= 1:
            return moves

        for x in range(n - 1, 0, -1):
            if n % x == 0:
                moves.append(x)
        return moves
