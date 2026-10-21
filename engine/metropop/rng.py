"""Small deterministic RNG wrapper so every story is reproducible."""

from __future__ import annotations

import random
from typing import Iterable, Sequence, TypeVar

T = TypeVar("T")


class Rng:
    def __init__(self, seed: int | None = None) -> None:
        self.seed = seed if seed is not None else random.randint(1, 999_999_999)
        self._random = random.Random(self.seed)

    def pick(self, values: Sequence[T]) -> T:
        if not values:
            raise ValueError("cannot pick from an empty sequence")
        return self._random.choice(list(values))

    def integer(self, low: int, high: int) -> int:
        return self._random.randint(low, high)

    def chance(self, probability: float) -> bool:
        return self._random.random() < probability

    def shuffled(self, values: Iterable[T]) -> list[T]:
        items = list(values)
        self._random.shuffle(items)
        return items

    def sample(self, values: Sequence[T], count: int) -> list[T]:
        count = min(count, len(values))
        return self._random.sample(list(values), count)

    def cycle(self, values: Sequence[T], count: int) -> list[T]:
        """Return ``count`` items, reshuffling when the pool runs out."""
        if not values:
            return []
        result: list[T] = []
        pool: list[T] = []
        while len(result) < count:
            if not pool:
                pool = self.shuffled(values)
            result.append(pool.pop())
        return result
