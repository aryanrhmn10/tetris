from __future__ import annotations

import sys
import pygame

from game import TetrisGame
from scoreboard import ScoreBoard
from settings import (
    BACKGROUND,
    FALL_EVENT,
    FALL_INTERVAL_MS,
    FPS,
    GLOW,
    LEFT_MARGIN,
    PANEL_BG,
    PANEL_WIDTH,
    PANEL_X,
    PREVIEW_BOX,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SMALL_TEXT,
    TEXT,
    TITLE,
)


def draw_panel(
    screen: pygame.Surface,
    title_font: pygame.font.Font,
    body_font: pygame.font.Font,
    small_font: pygame.font.Font,
    game: TetrisGame,
    scoreboard: ScoreBoard,
) -> None:
    panel_rect = pygame.Rect(PANEL_X, 24, PANEL_WIDTH, SCREEN_HEIGHT - 48)
    pygame.draw.rect(screen, GLOW, panel_rect.inflate(8, 8), border_radius=18)
    pygame.draw.rect(screen, PANEL_BG, panel_rect, border_radius=16)

    screen.blit(title_font.render("Single Player", True, TEXT), (LEFT_MARGIN, 42))
    screen.blit(body_font.render(f"Score: {game.score}", True, TEXT), (LEFT_MARGIN, 96))

    preview_title_x = PANEL_X + 24
    preview_title_y = 112
    screen.blit(body_font.render("Next Piece", True, TEXT), (preview_title_x, preview_title_y))
    preview_rect = pygame.Rect(preview_title_x, preview_title_y + 42, PREVIEW_BOX[0], PREVIEW_BOX[1])
    pygame.draw.rect(screen, GLOW, preview_rect.inflate(6, 6), border_radius=14)
    pygame.draw.rect(screen, PREVIEW_BOX[2], preview_rect, border_radius=12)
    game.draw_next_piece(screen, preview_rect)

    controls_x = PANEL_X + 24
    controls_y = preview_rect.bottom + 28
    screen.blit(body_font.render("Controls", True, TEXT), (controls_x, controls_y))
    controls = [
        "←  Move Left",
        "→  Move Right",
        "↓  Move Down",
        "↑  Rotate",
        "R  Restart",
    ]
    y = controls_y + 38
    line_step = 34
    for line in controls:
        screen.blit(body_font.render(line, True, TEXT), (controls_x, y))
        y += line_step

    leaderboard_title_y = y + 10
    screen.blit(body_font.render("Leaderboard", True, TEXT), (controls_x, leaderboard_title_y))

    leaderboard_y = leaderboard_title_y + 40
    leaderboard_step = 28
    footer_reserved = 22
    available_lines = max(1, (panel_rect.bottom - footer_reserved - leaderboard_y - 10) // leaderboard_step)
    for line in scoreboard.top_lines(available_lines):
        screen.blit(body_font.render(line, True, TEXT), (controls_x, leaderboard_y))
        leaderboard_y += leaderboard_step

    footer = "GAME OVER: press any arrow key to restart"
    footer_surface = small_font.render(footer, True, SMALL_TEXT)
    screen.blit(footer_surface, (LEFT_MARGIN, SCREEN_HEIGHT - 32))


def draw_game_over_popup(screen: pygame.Surface, font: pygame.font.Font, small_font: pygame.font.Font) -> None:
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    popup = pygame.Rect(150, 250, 420, 150)
    pygame.draw.rect(screen, GLOW, popup.inflate(8, 8), border_radius=20)
    pygame.draw.rect(screen, PANEL_BG, popup, border_radius=18)

    title = font.render("GAME OVER", True, TEXT)
    subtitle = small_font.render("Press any arrow key to restart", True, SMALL_TEXT)
    screen.blit(title, title.get_rect(center=(popup.centerx, popup.centery - 18)))
    screen.blit(subtitle, subtitle.get_rect(center=(popup.centerx, popup.centery + 28)))


def main() -> None:
    pygame.init()
    pygame.display.set_caption(TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    title_font = pygame.font.Font(None, 62)
    body_font = pygame.font.Font(None, 38)
    small_font = pygame.font.Font(None, 24)

    game = TetrisGame()
    scoreboard = ScoreBoard()

    pygame.time.set_timer(FALL_EVENT, FALL_INTERVAL_MS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == FALL_EVENT and not game.game_over:
                game.tick_down()

            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                        scoreboard.add_score("Player", game.score)
                        game.reset()
                    elif event.key == pygame.K_r:
                        game.reset()
                    continue

                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_DOWN:
                    game.move_down(manual=True)
                elif event.key == pygame.K_UP:
                    game.rotate()
                elif event.key == pygame.K_r:
                    game.reset()

        screen.fill(BACKGROUND)
        game.draw(screen, title_font, body_font)
        draw_panel(screen, title_font, body_font, small_font, game, scoreboard)
        if game.game_over:
            draw_game_over_popup(screen, title_font, small_font)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
