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
    info = show_custom_dialog()
    my_logger.add_log(info)
    info = __get_decks(info["deliminator"], info["files"])
    my_logger.add_log(info, my_logger.logging.DEBUG)

    if __create_decks(info):
        my_logger.add_log("Decks created successfully")
    else:
        my_logger.add_log("Error occurred in creating decks",
                          my_logger.logging.DEBUG)



def __create_decks(decks: list) -> bool:
    """Create decks from the list provide with 
    Returns True if decks are successfully created
    Returns False if decks are not created successfully"""
    return True


def __get_decks(deliminator: str, file_paths: list) -> list:
    """Create list of the decks from the files path and deliminator provided
    Returns list of the decks"""
    decks = set()
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            decks.update(f.read().split(deliminator))
    return [item for item in list(decks) if item.strip()]

action = QAction("Create Multiple Decks", mw)
qconnect(action.triggered, create_multiple_decks)
mw.form.menuTools.addAction(action)
