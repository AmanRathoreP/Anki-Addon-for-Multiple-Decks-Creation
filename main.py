from aqt.qt import QAction
from aqt.utils import qconnect
from aqt import mw
from .src import my_logger, my_user_interactive_GUI

my_logger.add_log("all stuff imported")


def show_custom_dialog() -> dict:
    dialog = my_user_interactive_GUI.MyCustomDialog(mw)
    
    if my_logger.my_constants.qt_version == 5:
        dialog.exec_()
    else:
        dialog.exec()

    return dialog.get_files_info()


def create_multiple_decks() -> None:
    # TODO while logging the info the dict of info is printing two times. Perhaps something is running multiple times fix it
    info = show_custom_dialog()
    mw.showWarning("One or multiple decks were not created") if (__create_decks(__get_decks(
        info["deliminator"], info["files"])) == False) else print('')



def __create_decks(decks: list) -> bool:
    """Create decks from the list provide with 
    Returns True if decks are successfully created
    Returns False if decks are not created successfully"""
    for deck_name in decks:
        mw.col.decks.id(deck_name)
    return True


def __get_decks(deliminator: str, file_paths: list) -> list:
    """Create list of the decks from the files path and deliminator provided
    Returns list of the decks"""
    decks = set()
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                decks.update(f.read().split(deliminator))
        except Exception as e:
            my_logger.add_log(
                "Probably the file is non readable", my_logger.logging.ERROR)
            my_logger.add_log(e, my_logger.logging.ERROR)
    return [item for item in list(decks) if item.strip()]

action = QAction("Create Multiple Decks", mw)
qconnect(action.triggered, create_multiple_decks)
mw.form.menuTools.addAction(action)
