from pytest import MonkeyPatch
from travertino.colors import color

import toga


# test that a non-container-like widget in layout debug mode has a default background
def test_button_debug_background():
    """A Button in layout debug mode has a default background."""
    # Enable layout debug mode
    with MonkeyPatch.context() as mp:
        mp.setenv("TOGA_DEBUG_LAYOUT", "1")
        button = toga.Button()
        # assert that the bg is default
        assert hasattr(button.style, "background_color")
        assert not button.style.background_color


# test that a container-like widget in layout debug mode has a non-default background
def test_box_debug_background():
    """A Box in layout debug mode has a non-default background."""
    # Enable layout debug mode
    with MonkeyPatch.context() as mp:
        mp.setenv("TOGA_DEBUG_LAYOUT", "1")

        boxes = []
        debug_bg_palette_length = len(toga.widgets.base.debug_background_palette)
        # need enough for coverage of debug_background_palette array index rollover
        for i in range(debug_bg_palette_length + 3):
            boxes.append(toga.Box())

        for counter, box in enumerate(boxes, start=1):
            index = counter % debug_bg_palette_length
            print(counter)
            assert hasattr(box.style, "background_color")
            assert box.style.background_color == color(
                toga.widgets.base.debug_background_palette[index]
            )


# test that a container-like widget in normal mode has a default background
def test_box_normal_background():
    """A Box has no default background."""
    # Disable layout debug mode
    with MonkeyPatch.context() as mp:
        mp.setenv("TOGA_DEBUG_LAYOUT", "0")
        box = toga.Box()
        # assert that the bg is default
        assert hasattr(box.style, "background_color")
        assert not box.style.background_color
