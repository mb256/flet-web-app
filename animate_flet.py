import os
import random
import time
from math import pi

import flet
from flet import Container, ElevatedButton, Page, Stack, colors


def main(page: Page):

    size = 40
    gap = 6
    duration = 3000

    c1 = colors.PINK_500
    c2 = colors.AMBER_500
    c3 = colors.LIGHT_GREEN_500
    c4 = colors.DEEP_PURPLE_500
    c5 = colors.LIGHT_BLUE_500
    c6 = colors.TEAL_ACCENT_200

    all_colors = [
        colors.AMBER_400,
        colors.AMBER_ACCENT_400,
        colors.BLUE_400,
        colors.BROWN_400,
        colors.CYAN_700,
        colors.DEEP_ORANGE_500,
        colors.CYAN_500,
        colors.INDIGO_600,
        colors.ORANGE_ACCENT_100,
        colors.PINK,
        colors.RED_600,
        colors.GREEN_400,
        colors.GREEN_ACCENT_200,
        colors.TEAL_ACCENT_200,
        colors.LIGHT_BLUE_500,
    ]

    parts = [
        # T
        (0, 0, c4),
        (1, 0, c4),
        (2, 0, c4),
        (1, 1, c4),
        (1, 2, c4),
        (1, 3, c4),
        (1, 4, c4),
        # M
        (4, 0, c3),
        (5, 1, c3),
        (6, 2, c3),
        (7, 1, c3),
        (8, 0, c3),
        (4, 1, c3),
        (4, 2, c3),
        (4, 3, c3),
        (4, 4, c3),
        (8, 1, c3),
        (8, 2, c3),
        (8, 3, c3),
        (8, 4, c3),

        # "  "
        # + 2 to the left
        (10, 2, c6),
        (11, 2, c6),

        # M
        (13, 0, c2),
        (14, 1, c2),
        (15, 2, c2),
        (16, 1, c2),
        (17, 0, c2),
        (13, 1, c2),
        (13, 2, c2),
        (13, 3, c2),
        (13, 4, c2),
        (17, 1, c2),
        (17, 2, c2),
        (17, 3, c2),
        (17, 4, c2),
        # F
        (19, 0, c1),
        (19, 1, c1),
        (19, 2, c1),
        (19, 3, c1),
        (19, 4, c1),
        (20, 0, c1),
        (21, 0, c1),
        (20, 2, c1),
        # P
        (23, 0, c5),
        (24, 0, c5),
        (25, 0, c5),
        (25, 1, c5),
        (23, 1, c5),
        (23, 2, c5),
        (24, 2, c5),
        (25, 2, c5),
        (23, 3, c5),
        (23, 4, c5),
    ]

    width = 27 * (size + gap)
    height = 5 * (size + gap)

    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    # spread parts randomly
    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        #go_button.visible = True
        #again_button.visible = False
        page.update()

    def assemble(e):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        #go_button.visible = False
        #again_button.visible = True
        page.update()


    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.spacing = 30
    page.add(canvas)

    while True:
        randomize(None)
        time.sleep(3.2)
        assemble(None)
        time.sleep(4)


flet.app(target=main)
