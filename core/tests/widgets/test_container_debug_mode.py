from os import environ

from travertino.colors import rgb

import toga


def test_box_debug_background():
    """A Box in layout debug mode has a non-default background."""
    # Enable layout debug mode
    environ["TOGA_DEBUG_LAYOUT"] = "1"

    box = toga.Box()

    # assert that the bg is not default/white
    assert hasattr(box.style, "background_color")
    assert not box.style.background_color == rgb(0, 0, 0)


def test_box_normal_background():
    """A Box has no default background."""
    # Disable layout debug mode
    environ["TOGA_DEBUG_LAYOUT"] = "0"

    box = toga.Box()

    # assert that the bg is not default/white
    assert hasattr(box.style, "background_color")
    assert not box.style.background_color
