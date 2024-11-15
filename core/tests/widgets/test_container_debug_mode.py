from os import environ

import toga

# Enable debug mode
environ["TOGA_DEBUG_LAYOUT"] = "1"


def test_box_debug_background():
    """A Box can be created."""
    box = toga.Box()

    # assert that the bg is not default/white
    assert hasattr(box.style, "background_color")
    assert not box.style.background_color == toga.colors.rgb(0, 0, 0)
