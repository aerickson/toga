from __future__ import annotations

import random
import os

from collections.abc import Iterable

from .base import StyleT, Widget


# based on colors from https://davidmathlogic.com/colorblind
pastel_palette = [
    "#d0e2ed",  # very light blue
    "#b8d2e9",  # light blue
    "#f8ccb0",  # light orange
    "#f6d3be",  # soft orange
    "#c7e7b2",  # light green
    "#f0b2d6",  # light pink
    "#e5dab0",  # light yellow
    "#d5c2ea",  # light lavender
    "#b2e4e5",  # light teal
    "#e5e4af",  # light cream
    "#bde2dc",   # soft turquoise
]
random.shuffle(pastel_palette)

class Box(Widget):
    _MIN_WIDTH = 0
    _MIN_HEIGHT = 0

    def __init__(
        self,
        id: str | None = None,
        style: StyleT | None = None,
        children: Iterable[Widget] | None = None,
    ):
        """Create a new Box container widget.

        :param id: The ID for the widget.
        :param style: A style object. If no style is provided, a default style
            will be applied to the widget.
        :param children: An optional list of children for to add to the Box.
        """
        # if layout debug mode, change bg color
        if 'TOGA_DEBUG_LAYOUT' in os.environ and os.environ['TOGA_DEBUG_LAYOUT'] == '1':
            # globals are gross, but ok when we're debugging
            global color_index
            try:
                if color_index == len(pastel_palette) - 1:
                    color_index = 0
                else:
                    color_index += 1
            except NameError:
                color_index = 0
            style.background_color = pastel_palette[color_index]

        super().__init__(id=id, style=style)

        # Create a platform specific implementation of a Box
        self._impl = self.factory.Box(interface=self)

        # Children need to be added *after* the impl has been created.
        self._children: list[Widget] = []
        if children is not None:
            self.add(*children)

    @property
    def enabled(self) -> bool:
        """Is the widget currently enabled? i.e., can the user interact with the widget?

        Box widgets cannot be disabled; this property will always return True; any
        attempt to modify it will be ignored.
        """
        return True

    @enabled.setter
    def enabled(self, value: bool) -> None:
        pass

    def focus(self) -> None:
        """No-op; Box cannot accept input focus."""
        pass
