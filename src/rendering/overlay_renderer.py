import pygame
from OpenGL.GL import *

from src.config.settings import HUD_BACKGROUND, HUD_BORDER, HUD_MUTED, HUD_TEXT, WIN_OVERLAY


class OverlayRenderer:
    def __init__(self):
        pygame.font.init()
        self.small = pygame.font.SysFont("segoeui", 16)
        self.medium = pygame.font.SysFont("segoeuisemibold", 22)
        self.large = pygame.font.SysFont("segoeuisemibold", 44)

    def draw(self, width, height, state, level_name, level_subtitle):
        self._begin_2d(width, height)
        self._draw_hud_panel(width, height, state, level_name, level_subtitle)

        if state.won:
            self._draw_win_screen(width, height, state, level_name)

        self._end_2d()

    def _begin_2d(self, width, height):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def _end_2d(self):
        glDisable(GL_BLEND)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def _draw_hud_panel(self, width, height, state, level_name, level_subtitle):
        panel = (18, 18, min(520, width - 36), 124)
        self._draw_filled_rect(panel, HUD_BACKGROUND)
        self._draw_rect_outline(panel, HUD_BORDER, 2.0)

        self._draw_text(36, 30, f"Level {state.level_index + 1}: {level_name}", self.medium, HUD_TEXT)
        self._draw_wrapped_text(36, 58, level_subtitle, self.small, HUD_MUTED, max_width=panel[2] - 54, line_gap=4)
        self._draw_text(36, 92, f"Moves: {state.moves}", self.small, HUD_TEXT)
        self._draw_text(132, 92, f"Remaining: {state.remaining}", self.small, HUD_TEXT)
        self._draw_text(270, 92, "Drag to rotate", self.small, HUD_MUTED)
        self._draw_text(270, 110, "Click a free cube to send it away", self.small, HUD_MUTED)

    def _draw_win_screen(self, width, height, state, level_name):
        overlay = (0, 0, width, height)
        self._draw_filled_rect(overlay, WIN_OVERLAY)

        box_w = min(620, width - 80)
        box_h = 260
        box_x = (width - box_w) / 2
        box_y = (height - box_h) / 2
        panel = (box_x, box_y, box_w, box_h)

        self._draw_filled_rect(panel, (0.08, 0.10, 0.14, 0.96))
        self._draw_rect_outline(panel, (0.99, 0.84, 0.38, 0.95), 3.0)

        self._draw_text(box_x + 38, box_y + 52, "Level Cleared", self.large, (0.99, 0.90, 0.52))
        self._draw_wrapped_text(
            box_x + 40,
            box_y + 112,
            f"You finished {level_name} in {state.moves} moves.",
            self.medium,
            HUD_TEXT,
            max_width=box_w - 80,
            line_gap=6,
        )
        self._draw_wrapped_text(
            box_x + 40,
            box_y + 170,
            "Press N for the next level or R to replay this one.",
            self.small,
            HUD_MUTED,
            max_width=box_w - 80,
            line_gap=4,
        )

    def _draw_filled_rect(self, rect, color):
        x, y, w, h = rect
        glColor4f(*color)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + w, y)
        glVertex2f(x + w, y + h)
        glVertex2f(x, y + h)
        glEnd()

    def _draw_rect_outline(self, rect, color, line_width):
        x, y, w, h = rect
        glColor4f(*color)
        glLineWidth(line_width)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x, y)
        glVertex2f(x + w, y)
        glVertex2f(x + w, y + h)
        glVertex2f(x, y + h)
        glEnd()
        glLineWidth(1.0)

    def _draw_text(self, x, y, text, font, color):
        if not text:
            return

        surface = font.render(text, True, self._to_rgb255(color))
        pixels = pygame.image.tostring(surface, "RGBA", True)

        glRasterPos2i(int(x), int(y))
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glDrawPixels(surface.get_width(), surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, pixels)

    def _draw_wrapped_text(self, x, y, text, font, color, max_width, line_gap=4):
        words = text.split()
        if not words:
            return

        lines = []
        current = words[0]

        for word in words[1:]:
            candidate = f"{current} {word}"
            if font.size(candidate)[0] <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word

        lines.append(current)

        offset_y = y
        for line in lines:
            self._draw_text(x, offset_y, line, font, color)
            offset_y += font.get_linesize() + line_gap

    def _to_rgb255(self, color):
        if len(color) < 3:
            return (255, 255, 255)

        r, g, b = color[:3]
        if max(r, g, b) <= 1.0:
            return (int(r * 255), int(g * 255), int(b * 255))

        return (int(r), int(g), int(b))
