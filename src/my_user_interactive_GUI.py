import sys
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout,  QLabel, QPushButton, QListWidget, QListWidgetItem, QFileDialog, QLineEdit
from PyQt5.QtGui import QPalette, QColor, QKeyEvent
from PyQt5.QtCore import Qt, pyqtProperty
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
from PyQt5.QtCore import QFile, QTextStream
import os
from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QDialog
from PyQt5.QtCore import Qt
from warnings import warn
try:
    from .my_constants import (style_sheets_dir, style_sheet_to_use)
except:
    warn("Running code outside anki")
    style_sheets_dir, style_sheet_to_use = r"C:\Users\amanr\AppData\Roaming\Anki2\addons21\myaddon2\user_files", "default.css"

input_info = {"deliminator": None, "files": [None, None]}


class FileWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.setMinimumSize(800, 500)
        self.setWindowTitle("Multiple decks creator")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.file_label = QLabel(self)
        self.file_label.setObjectName("file_label")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.file_label)

        self.file_list = QListWidget(self)
        self.file_list.setObjectName("file_list")
        self.file_list.setSelectionMode(QListWidget.ExtendedSelection)
        self.layout.addWidget(self.file_list)

        self.add_button = QPushButton("Add Files", self)
        self.add_button.setObjectName("add_button")
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Selected", self)
        self.delete_button.setObjectName("delete_button")
        self.layout.addWidget(self.delete_button)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setObjectName("submit_button")
        self.layout.addWidget(self.submit_button)

        self.add_button.clicked.connect(self.select_files)

        self.delete_button.clicked.connect(self.delete_selected_files)

        self.submit_button.clicked.connect(self.submit_files)

        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Data is delimited by")
        self.textbox.setObjectName("submit_button")
        self.textbox.returnPressed.connect(self.handle_return_pressed)
        self.layout.addWidget(self.textbox)

        self.update_selected_files_number()

    def select_files(self):
        """Opens a file dialog to allow the user to select files"""
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Files")

        for file_name in file_names:
            item = QListWidgetItem(file_name)
            self.file_list.addItem(item)

            self.update_selected_files_number()

    def update_selected_files_number(self):

        def __extract_file_names(file_paths):
            file_name_dict = {}
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                if file_name in file_name_dict:
                    file_name_dict[file_name].append(file_path)
                else:
                    file_name_dict[file_name] = [file_path]
            file_names = []
            for file_name, file_paths in file_name_dict.items():
                if len(file_paths) > 1:
                    for file_path in file_paths:
                        file_names.append(file_path)
                else:
                    file_names.append(os.path.basename(file_paths[0]))
            return file_names

        file_names = self.get_files()
        num_files = len(file_names)
        self.file_label.setText(
            f"{num_files} file{'s' if num_files > 1 else ''} selected")
        self.file_label.setToolTip("\n".join(__extract_file_names(file_names)))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            item = QListWidgetItem(file_path)
            if os.path.isdir(file_path) == False:
                self.file_list.addItem(item)
        self.update_selected_files_number()

    def delete_selected_files(self):
        """Remove the selected files from the list widget"""
        for item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(item))

        self.update_selected_files_number()

    def submit_files(self, text_box_data=None):
        """Remove the selected files from the list widget"""
        text_box_data = self.textbox.text()
        global input_info
        input_info = {"deliminator": str(
            text_box_data), "files": self.get_files()}
        if __name__ == "__main__":
            print(input_info)
        self.parent().close()

    def handle_return_pressed(self):
        self.submit_files()

    def get_files(self):
        """Return a list of the file names in the list widget"""
        file_names = []
        for i in range(self.file_list.count()):
            file_names.append(self.file_list.item(i).text())
        return file_names

    def set_files(self, file_names):
        """Add the specified files to the list widget"""
        for file_name in file_names:
            item = QListWidgetItem(file_name)
            self.file_list.addItem(item)

    def get_color(self):
        return self.file_label.palette().color(QPalette.WindowText)

    def set_color(self, color):
        palette = self.file_label.palette()
        palette.setColor(QPalette.WindowText, color)
        self.file_label.setPalette(palette)

    color = pyqtProperty(QColor, get_color, set_color)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Delete:
            # Delete the selected items from the QListWidget
            selected_items = self.file_list.selectedItems()
            for item in selected_items:
                self.file_list.takeItem(self.file_list.row(item))
        self.update_selected_files_number()

class MyCustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Multiple Decks Creator")
        layout = QVBoxLayout()
        file_widget = FileWidget()
        layout.addWidget(file_widget)
        self.setLayout(layout)
        with open(os.path.join(style_sheets_dir, style_sheet_to_use), 'r') as f:
            self.setStyleSheet(f.read())

    def get_files_info(self) -> dict:
        return input_info


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_dialog = MyCustomDialog()
    file_dialog.show()
    sys.exit(app.exec_())
