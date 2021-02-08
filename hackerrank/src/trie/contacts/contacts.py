#!/bin/python3
from dataclasses import dataclass, field

import os
import sys
from typing import Dict, List, Optional

# Challenge: https://www.hackerrank.com/challenges/contacts/problem

@dataclass
class TrieNode:
    letter: Optional[str]
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    available_words: int = 0


@dataclass
class Trie:
    tree: TrieNode = TrieNode(None)

    def add(self, name: str):
        node = self.tree
        for letter in name:
            node = node.children.setdefault(letter, TrieNode(letter))
            node.available_words += 1

    def count(self, partial):
        node = self.tree
        for letter in partial:
            node = node.children.get(letter, None)
            if node is None:
                return 0
        return node.available_words if node is not None else 0


def contacts(queries):
    methods = {
        "add": Trie.add,
        "find": Trie.count
    }
    trie = Trie()
    for method, value in queries:
        result = methods.get(method, None)(trie, value)
        if result is not None:
            print(result)


TEST_CASE_1 = [
    ["add", "hack"],
    ["add", "hackerrank"],
    ["find", "hac"],
    ["find", "hak"]
]


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


if __name__ == '__main__':
    # main()
    contacts(TEST_CASE_1)