#pytype output: merged f1 but not f3?
def f1(x) -> Union[int, str]: ...
def f2(x) -> None: ...
def f2(x, y) -> None: ...
def f3(x: int) -> int: ...
def f3(x: Union[bytearray, str, unicode]) -> Union[str, unicode]: ...
