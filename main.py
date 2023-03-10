from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from aqt.qt import QAction
from aqt.utils import qconnect
from aqt import mw
from .src import my_logger, my_constants, my_user_interactive_GUI

my_logger.add_log("all stuff imported")


def show_custom_dialog() -> dict:
    dialog = my_user_interactive_GUI.MyCustomDialog(mw)
    dialog.exec_()
    return dialog.get_files_info()


def create_multiple_decks() -> None:
    # TODO while logging the info the dict of info is printing two times. Perhaps something is running multiple times fit it
    my_logger.add_log(show_custom_dialog())


def __create_decks(decks: list) -> bool:
    """Create decks from the list provide with 
    Returns True if decks are successfully created
    Returns False if decks are not created successfully"""
    return True


def __get_decks(deliminator: str, file_paths: list) -> list:
    """Create list of the decks from the files path and deliminator provided
    Returns list of the decks"""
    return [None, None]

action = QAction("Create Multiple Decks", mw)
qconnect(action.triggered, create_multiple_decks)
mw.form.menuTools.addAction(action)
