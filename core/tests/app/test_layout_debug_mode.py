from os import environ

import toga
from toga_dummy.utils import (
    assert_action_not_performed,
    assert_action_performed,
)

# a clone of core/tests/app/test_simpleapp.py, but sets the environment variable
# for the debug mode to be enabled

# Enable debug mode
environ["TOGA_DEBUG_LAYOUT"] = "1"


def test_layout_debug_mode(event_loop):
    """A simple app can be instantiated."""

    class SimpleApp(toga.App):
        def startup(self):
            self.main_window = toga.Window(title="My App")

            # At time startup is invoked, the default commands are installed
            assert len(self.commands) == 2

            # Add an extra user command
            self.commands.add(toga.Command(None, "User command"))

    app = SimpleApp(formal_name="Test App", app_id="org.example.test")

    # The app has a main window that is a Window, but *not* a MainWindow
    assert isinstance(app.main_window, toga.Window)
    assert not isinstance(app.main_window, toga.MainWindow)

    # The main window will exist, and will have the app's formal name.
    assert app.main_window.title == "My App"

    # The app commands exist, and menus have been created.
    assert_action_performed(app, "create App commands")
    assert_action_performed(app, "create App menus")

    # A simple app has no window menus
    assert_action_not_performed(app.main_window, "create Window menus")

    # 3 menu items have been created
    assert app._impl.n_menu_items == 3
