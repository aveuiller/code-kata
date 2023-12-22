# https://adventofcode.com/2023/day/20
import os
from enum import Enum
from typing import List, Optional, Dict



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


class Module:
    MODULES = {}
    pulses_queue = []
    rx_low_pulsed = False

    def __init__(self, name: str, destinations: List[str]):
        self.name = name
        self.destinations = destinations
        self.pulses_count = {}
        self.pulses_queue = []

    def pulse(self, pulse_level: Pulse, origin: str) -> None:
        pass

    def receive_pulse(self, pulse_level: Pulse, origin: str):
        self.pulses_count[pulse_level] = self.pulses_count.get(pulse_level, 0) + 1
        Module.pulses_queue.append((self.name, pulse_level, origin))

    def send_pulse(self, pulse_level: Pulse) -> None:
        for mod in self.destinations:
            Module.MODULES[mod].receive_pulse(pulse_level, self.name)

        while Module.pulses_queue:
            name, level, origin = Module.pulses_queue.pop(0)
            if name == 'rx' and level == Pulse.LOW:
                Module.rx_low_pulsed = True
                print(f"{origin} -{level.name}-> {name}")
            Module.MODULES[name].pulse(level, origin)

    def get_count(self, pulse_level: Pulse) -> int:
        return self.pulses_count.get(pulse_level, 0)


class Flip(Module):
    SYMBOL = "%"

    def __init__(self, name: str, destinations: List[str]):
        super().__init__(name, destinations)
        self.state = False

    def pulse(self, pulse_level: Pulse, origin: str) -> None:
        super().pulse(pulse_level, origin)
        if pulse_level == Pulse.LOW:
            self.state = not self.state

            if self.state:
                self.send_pulse(Pulse.HIGH)
            else:
                self.send_pulse(Pulse.LOW)


class Conjunction(Module):
    SYMBOL = "&"

    def __init__(self, name: str, destinations: List[str]):
        super().__init__(name, destinations)
        self.connected = {}

    def pulse(self, pulse_level: Pulse, origin: str) -> None:
        super().pulse(pulse_level, origin)
        self.connected[origin] = pulse_level
        self.send_pulse(Pulse.LOW 
                        if all((x == Pulse.HIGH for x in self.connected.values()))
                        else Pulse.HIGH)
    
    def init_origin(self, name):
        self.connected[name] = Pulse.LOW


class Broadcast(Module):
    SYMBOL = "broadcaster"

    def __init__(self, destinations: List[str]):
        super().__init__(Broadcast.SYMBOL, destinations)

    def pulse(self, pulse_level: Pulse, origin: str) -> None:
        super().pulse(pulse_level, origin)
        self.send_pulse(pulse_level)


class Button(Module):
    SYMBOL = "Button"

    def __init__(self):
        super().__init__(self.SYMBOL, [Broadcast.SYMBOL])

    def pulse(self, pulse_level: Pulse, origin: str) -> None:
        super().pulse(pulse_level, origin)
        self.send_pulse(Pulse.LOW)

    def push(self):
        self.pulse(Pulse.LOW, self.name)


def prepare_modules(modules: List[str]) -> Dict[str, Module]:
    Module.MODULES = {}
    Module.pulses_queue = []
    Module.rx_low_pulsed = False
    result = {}

    conjunctions = []
    for line in modules:
        name = line.split("-")[0].strip().replace("%", "").replace("&", "")
        destinations = line.split(">")[1].replace(" ", "").split(",")
        module = None
        if Broadcast.SYMBOL in line:
            module = Broadcast(destinations)
        elif line.startswith(Conjunction.SYMBOL):
            module = Conjunction(name, destinations)
            conjunctions.append(name)
        elif line.startswith(Flip.SYMBOL):
            module = Flip(name, destinations)

        assert module is not None
        result[module.name] = module
        
        # Handle unspecified modules
        for mod in destinations:
            if mod not in result:
                result[mod] =  Module(mod, [])

    # Configure Conjuction
    for name, mod in result.items():
        for destination in mod.destinations:
            if destination in conjunctions:
                result[destination].init_origin(name)

    Module.MODULES = result
    return result


def main_01(entry_modules: List[str]) -> int:
    modules = prepare_modules(entry_modules)

    modules[Button.SYMBOL] = Button()
    for i in range(1000):
        # print("=====Pushing=====")
        modules[Button.SYMBOL].push()

    low = 0
    high = 0
    for module in modules.values():
        low += module.get_count(Pulse.LOW)
        high += module.get_count(Pulse.HIGH)

    print(f"Low: {low} - High: {high}")
    return low * high


def main_02(entry_modules: List[str]) -> int:
    modules = prepare_modules(entry_modules)

    modules[Button.SYMBOL] = Button()
    i = 0
    while not Module.rx_low_pulsed:
        # print("=====Pushing=====")
        i += 1
        modules[Button.SYMBOL].push()
    
    return i


if __name__ == '__main__':
    test = True
    test = False
    print(f"First Response: {main_01(load(test))}")  # 680278040
    if test:
        print(f"First Response Test 2: {main_01(load(test, name_override='test_input2.txt'))}")  # 11687500
    print(f"Second Response: {main_02(load(test))}")  # 
