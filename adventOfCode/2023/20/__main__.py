# https://adventofcode.com/2023/day/19
import abc
import os
import pprint
import re
import sys
from enum import Enum
from functools import reduce
from typing import List, Optional, Tuple, Dict, Iterator

pp = pprint.PrettyPrinter(depth=4)


def load(test_mode: bool = False, name_override: Optional[str] = None) -> List[str]:
    dirname = os.path.dirname(os.path.abspath(__file__))
    input_file = 'input.txt'
    if test_mode:
        input_file = f"test_{input_file}"
    if name_override:
        input_file = name_override
    with open(os.path.join(dirname, input_file)) as f:
        return f.read().splitlines()


class Pulse(Enum):
    HIGH = 1
    LOW = 0


MODULES = {}


class Module:
    def __init__(self, name: str, destinations: List[str]):
        self.name = name
        self.destinations = destinations
        self.pulses = {}

    def pulse(self, pulse_level: Pulse) -> None:
        self.pulses[pulse_level] = self.pulses.get(pulse_level, 0) + 1

    def send_pulse(self, pulse_level: Pulse) -> None:
        for mod in self.destinations:
            MODULES[mod].pulse(pulse_level)

    def get_count(self, pulse_level: Pulse) -> int:
        return self.pulses.get(pulse_level, 0)


class Flip(Module):
    SYMBOL = "%"

    def __init__(self, name: str, destinations: List[str]):
        super().__init__(name, destinations)
        self.state = False

    def pulse(self, pulse_level: Pulse) -> None:
        super().pulse(pulse_level)
        if pulse_level == Pulse.LOW:
            self.state = not self.state

            if self.state:
                self.send_pulse(Pulse.HIGH)


class Conjunction(Module):
    SYMBOL = "&"

    def __init__(self, name: str, destinations: List[str]):
        super().__init__(name, destinations)
        self.connected = {conn: Pulse.LOW for conn in destinations}

    def pulse(self, pulse_level: Pulse) -> None:
        super().pulse(pulse_level)
        created_pulse = Pulse.LOW if all((x == Pulse.HIGH for x in self.connected.values())) else Pulse.LOW
        self.send_pulse(created_pulse)


class Broadcast(Module):
    SYMBOL = "broadcaster"

    def __init__(self, destinations: List[str]):
        super().__init__(Broadcast.SYMBOL, destinations)

    def pulse(self, pulse_level: Pulse) -> None:
        super().pulse(pulse_level)
        self.send_pulse(pulse_level)


class Button(Module):
    SYMBOL = "Button"

    def __init__(self):
        super().__init__(self.SYMBOL, [Broadcast.SYMBOL])

    def pulse(self, pulse_level: Pulse) -> None:
        super().pulse(pulse_level)
        self.send_pulse(Pulse.LOW)

    def push(self):
        self.pulse(Pulse.LOW)


def main_01(modules: List[str]) -> int:
    for line in modules:
        name = line.split("-")[0].strip().replace("%", "").replace("&", "")
        destinations = line.split(">")[1].replace(" ", "").split(",")
        module = None
        if Broadcast.SYMBOL in line:
            module = Broadcast(destinations)
        elif line.startswith(Conjunction.SYMBOL):
            module = Conjunction(name, destinations)
        elif line.startswith(Flip.SYMBOL):
            module = Flip(name, destinations)

        assert module is not None
        MODULES[module.name] = module

    MODULES[Button.SYMBOL] = Button()
    for i in range(1):
        MODULES[Button.SYMBOL].push()

    low = 0
    high = 0
    for module in MODULES.values():
        low += module.get_count(Pulse.LOW)
        high += module.get_count(Pulse.HIGH)

    print(f"Low: {low} - High: {high}")
    return low * high


def main_02(xmas_sort: List[str]) -> int:
    return 0


if __name__ == '__main__':
    test = True
    # test = False
    print(f"First Response: {main_01(load(test))}")  # 432434
    print(f"Second Response: {main_02(load(test))}")  # 132557544578569
