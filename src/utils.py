from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


def find(predicate: Callable[[T], bool], xs: Iterable[T]) -> T | None:
    for x in xs:
        if predicate(x):
            return x
    return None
