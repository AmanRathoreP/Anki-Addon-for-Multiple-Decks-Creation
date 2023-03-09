from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from aqt.qt import QAction
from aqt.utils import qconnect
from aqt import mw
from .src import my_logger, my_constants, my_user_interactive_GUI

my_logger.add_log("all stuff imported")


def show_custom_dialog() -> dict:
    dialog = my_user_interactive_GUI.MyCustomDialog(mw)
    stylesheet = my_user_interactive_GUI.QFile(r"src/my_style.css")
    stylesheet.open(my_user_interactive_GUI.QFile.ReadOnly |
                    my_user_interactive_GUI.QFile.Text)
    stream = my_user_interactive_GUI.QTextStream(stylesheet)
    dialog.setStyleSheet(stream.readAll())
    dialog.exec_()


action = QAction("Create Multiple Decks", mw)
qconnect(action.triggered, show_custom_dialog)
mw.form.menuTools.addAction(action)
