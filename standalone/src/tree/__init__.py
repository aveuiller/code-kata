from dataclasses import dataclass, field
from typing import List


@dataclass
class Node:
    value: int
    children: List['Node'] = field(default_factory=list)

    def __str__(self) -> str:
        return f"Node({self.value})"
