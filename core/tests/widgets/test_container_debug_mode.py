from os import environ

from travertino.colors import rgb

import toga


# test that a non-container-like widget in layout debug mode has a default background
def test_button_debug_background():
    """A Button in layout debug mode has a default background."""
    # Enable layout debug mode
    environ["TOGA_DEBUG_LAYOUT"] = "1"

    button = toga.Button()

    # assert that the bg is default
    assert hasattr(button.style, "background_color")
    assert not button.style.background_color


# test that a container-like widget in layout debug mode has a non-default background
def test_box_debug_background():
    """A Box in layout debug mode has a non-default background."""
    # Enable layout debug mode
    environ["TOGA_DEBUG_LAYOUT"] = "1"

    # need enough for coverage of palette array index rollover
    box = toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()
    toga.Box()

    # assert that the bg is not default/white
    assert hasattr(box.style, "background_color")
    assert not box.style.background_color == rgb(0, 0, 0)


# test that a container-like widget in normal mode has a default background
def test_box_normal_background():
    """A Box has no default background."""
    # Disable layout debug mode
    environ["TOGA_DEBUG_LAYOUT"] = "0"

    box = toga.Box()

    # assert that the bg is default
    assert hasattr(box.style, "background_color")
    assert not box.style.background_color
