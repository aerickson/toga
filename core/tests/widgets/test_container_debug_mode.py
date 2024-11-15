from os import environ

import toga
from toga_dummy.utils import (
    assert_action_not_performed,
    assert_action_performed,
)

# Enable debug mode
environ["TOGA_DEBUG_LAYOUT"] = "1"


# clone of a test in test_box.py
def test_create_box():
    """A Box can be created."""
    box = toga.Box()
    # Round trip the impl/interface
    assert box._impl.interface == box

    assert_action_performed(box, "create Box")
    assert_action_not_performed(box, "add child")
