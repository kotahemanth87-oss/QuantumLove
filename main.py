from math import sin, cos, pi
from random import choice

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.clearcolor = (0, 0, 0, 1)


class HeartCanvas(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.colors = [
            (1, 0.2, 0.2, 1),
            (0.2, 0.4, 1, 1),
            (0.3, 1, 0.3, 1),
            (1, 1, 0.2, 1),
            (0.2, 1, 1, 1),
            (1, 0.2, 1, 1),
            (1, 0.6, 0.1, 1),
            (1, 0.5, 0.8, 1),
        ]
        self.t = 0
        Clock.schedule_interval(self.draw_frame, 1 / 30)

    def on_size(self, *args):
        self.canvas.clear()

    def on_pos(self, *args):
        self.canvas.clear()

    def draw_frame(self, dt):
        self.t += dt
        self.canvas.clear()

        w, h = self.width, self.height
        cx, cy = w / 2, h / 2
        scale = min(w, h) / 35.0

        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=self.pos, size=self.size)

            # soft glow behind heart
            for r, a in [(220, 0.06), (170, 0.08), (120, 0.12)]:
                Color(1, 0.2, 0.4, a)
                Ellipse(pos=(cx - r, cy - r), size=(2 * r, 2 * r))

            # animated heart points
            prev = None
            for i in range(121):
                angle = i * 2 * pi / 120
                x = 16 * (sin(angle) ** 3) * scale
                y = (13 * cos(angle) - 5 * cos(2 * angle) - 2 * cos(3 * angle) - cos(4 * angle)) * scale

                px = cx + x
                py = cy + y

                c = choice(self.colors)
                Color(*c)
                Ellipse(pos=(px - 4, py - 4), size=(8, 8))

                if prev is not None:
                    Color(*c)
                    Line(points=[prev[0], prev[1], px, py], width=1.3)

                # small sparkle trails similar to turtle zig-zags
                for _ in range(3):
                    dx = (choice([-1, 1]) * (2 + (i % 3)))
                    dy = (choice([-1, 1]) * (2 + (i % 2)))
                    Color(*choice(self.colors))
                    Line(points=[px, py, px + dx, py + dy], width=1)

                prev = (px, py)

            # title text placeholder using simple bars and shapes not labels
            # kept minimal to avoid extra dependencies.


class QuantumLoveApp(App):
    def build(self):
        return HeartCanvas()


if __name__ == '__main__':
    QuantumLoveApp().run()
