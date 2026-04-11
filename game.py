from __future__ import annotations

import pygame

from settings import (
    BOARD_BG,
    BOARD_HEIGHT,
    BOARD_OUTLINE,
    BOARD_WIDTH,
    CELL_SIZE,
    COLORS,
    GRID_COLS,
    GRID_ROWS,
    LEFT_MARGIN,
    PREVIEW_BOX,
    TEXT,
)
from tetromino import PieceBag, Tetromino


class TetrisGame:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.score = 0
        self.game_over = False
        self.bag = PieceBag()
        self.current = self.bag.draw()
        self.next_piece = self.bag.draw()

    def inside(self, row: int, col: int) -> bool:
        return 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS

    def empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] == 0

    def fits(self, piece: Tetromino) -> bool:
        for row, col in piece.cells():
            if not self.inside(row, col):
                return False
            if not self.empty(row, col):
                return False
        return True

    def move_left(self) -> None:
        if self.game_over:
            return
        self.current.move(0, -1)
        if not self.fits(self.current):
            self.current.move(0, 1)

    def move_right(self) -> None:
        if self.game_over:
            return
        self.current.move(0, 1)
        if not self.fits(self.current):
            self.current.move(0, -1)

    def rotate(self) -> None:
        if self.game_over:
            return
        self.current.rotate()
        if not self.fits(self.current):
            self.current.undo_rotate()

    def move_down(self, manual: bool = False) -> None:
        if self.game_over:
            return
        self.current.move(1, 0)
        if not self.fits(self.current):
            self.current.move(-1, 0)
            self.lock_piece()
        elif manual:
            self.score += 1

    def tick_down(self) -> None:
        if not self.game_over:
            self.move_down()
            self.score += 1

    def lock_piece(self) -> None:
        for row, col in self.current.cells():
            if self.inside(row, col):
                self.grid[row][col] = self.current.kind_id

        self.score += self.clear_rows() * 100
        self.current = self.next_piece
        self.next_piece = self.bag.draw()

        if not self.fits(self.current):
            self.trigger_game_over()

    def clear_rows(self) -> int:
        kept_rows = [row[:] for row in self.grid if any(value == 0 for value in row)]
        cleared = GRID_ROWS - len(kept_rows)
        while len(kept_rows) < GRID_ROWS:
            kept_rows.insert(0, [0 for _ in range(GRID_COLS)])
        self.grid = kept_rows
        return cleared

    def trigger_game_over(self) -> None:
        self.game_over = True
        fill_cycle = [1, 2, 3, 4, 5, 6, 7]
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                if self.grid[r][c] == 0:
                    self.grid[r][c] = fill_cycle[(r + c) % len(fill_cycle)]

    def draw(self, screen: pygame.Surface, title_font: pygame.font.Font, body_font: pygame.font.Font) -> None:
        board_rect = pygame.Rect(LEFT_MARGIN, 120, BOARD_WIDTH, BOARD_HEIGHT)
        pygame.draw.rect(screen, BOARD_OUTLINE, board_rect.inflate(8, 8), border_radius=18)
        pygame.draw.rect(screen, BOARD_BG, board_rect, border_radius=16)

        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                rect = pygame.Rect(
                    LEFT_MARGIN + col * CELL_SIZE,
                    120 + row * CELL_SIZE,
                    CELL_SIZE - 1,
                    CELL_SIZE - 1,
                )
                pygame.draw.rect(screen, COLORS[self.grid[row][col]], rect)

        if not self.game_over:
            for row, col in self.current.cells():
                if row >= 0:
                    rect = pygame.Rect(
                        LEFT_MARGIN + col * CELL_SIZE,
                        120 + row * CELL_SIZE,
                        CELL_SIZE - 1,
                        CELL_SIZE - 1,
                    )
                    pygame.draw.rect(screen, COLORS[self.current.kind_id], rect)

    def draw_next_piece(self, screen: pygame.Surface, rect: pygame.Rect) -> None:
        size = CELL_SIZE - 2
        cells = self.next_piece.preview_cells()
        min_row = min(r for r, _ in cells)
        min_col = min(c for _, c in cells)
        max_row = max(r for r, _ in cells)
        max_col = max(c for _, c in cells)
        width = (max_col - min_col + 1) * size
        height = (max_row - min_row + 1) * size
        start_x = rect.x + (rect.width - width) // 2
        start_y = rect.y + (rect.height - height) // 2

        for row, col in cells:
            draw_x = start_x + (col - min_col) * size
            draw_y = start_y + (row - min_row) * size
            cell_rect = pygame.Rect(draw_x, draw_y, size - 1, size - 1)
            pygame.draw.rect(screen, COLORS[self.next_piece.kind_id], cell_rect, border_radius=6)
