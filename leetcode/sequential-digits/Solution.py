class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        max_len = len(str(high))
        for size in range(len(str(low)), max_len + 1):
            high_bound = 9 if size < max_len else int(str(high)[0])+1
            for base in range(1, high_bound):
                # print(f"{size} - {high_bound} - {base}")
                if base + size > 10:
                    continue
                built = int("".join([str(base + i) for i in range(size)]))
                # print(f"testing {built}")
                if low <= built <= high:
                    results.append(built)
        return results