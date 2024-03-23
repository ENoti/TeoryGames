from typing import Any


class Test:
    def __init__(self) -> None:
        self.state = 1

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("1111")


class StateButton:
    def __init__(self, actions: list[function]) -> None:
        self.state = 0
        self._actions = actions
    
    def __call__(self, *args: Any, **kwds: Any) -> None:
        self._actions[self.state]()
        
        self.state = (self.state + 1) % len(self._actions)


test = Test()
test()