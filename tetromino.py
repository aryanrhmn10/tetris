from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass(frozen=True)
class Cell:
    row: int
    col: int


SHAPES = {
    1: [
        [(0, 2), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (2, 2)],
        [(1, 0), (1, 1), (1, 2), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
    ],
    2: [
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (2, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2), (2, 2)],
        [(2, 0), (0, 1), (1, 1), (2, 1)],
    ],
    3: [
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(0, 2), (1, 2), (2, 2), (3, 2)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(0, 1), (1, 1), (2, 1), (3, 1)],
    ],
    4: [[(0, 0), (0, 1), (1, 0), (1, 1)]],
    5: [
        [(0, 1), (0, 2), (1, 0), (1, 1)],
        [(0, 1), (1, 1), (1, 2), (2, 2)],
        [(1, 1), (1, 2), (2, 0), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
    ],
    6: [
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (1, 2), (2, 1)],
        [(1, 0), (1, 1), (1, 2), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 1)],
    ],
    7: [
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 2), (1, 1), (1, 2), (2, 1)],
        [(1, 0), (1, 1), (2, 1), (2, 2)],
        [(0, 1), (1, 0), (1, 1), (2, 0)],
    ],
}

SPAWNS = {
    1: (0, 3),
    2: (0, 3),
    3: (-1, 3),
    4: (0, 4),
    5: (0, 3),
    6: (0, 3),
    7: (0, 3),
}


class Tetromino:
    def __init__(self, kind_id: int):
        self.kind_id = kind_id
        self.state = 0
        self.row_offset, self.col_offset = SPAWNS[kind_id]

    def move(self, row: int, col: int) -> None:
        self.row_offset += row
        self.col_offset += col

    def rotate(self) -> None:
        self.state = (self.state + 1) % len(SHAPES[self.kind_id])

    def undo_rotate(self) -> None:
        self.state = (self.state - 1) % len(SHAPES[self.kind_id])

    def cells(self) -> list[tuple[int, int]]:
        return [
            (row + self.row_offset, col + self.col_offset)
            for row, col in SHAPES[self.kind_id][self.state]
        ]

    def preview_cells(self) -> list[tuple[int, int]]:
        return SHAPES[self.kind_id][self.state]


class PieceBag:
    def __init__(self) -> None:
        self.bag: list[int] = []

    def draw(self) -> Tetromino:
        if not self.bag:
            self.bag = [1, 2, 3, 4, 5, 6, 7]
            random.shuffle(self.bag)
        return Tetromino(self.bag.pop())
