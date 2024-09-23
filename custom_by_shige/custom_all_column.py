from aqt import QDialog, QScrollArea, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QLabel, QApplication, QWidget


WIDGET_WIDTH = 500
WIDGET_HEIGHT = 430

class ColumnDialog(QDialog):
    def __init__(self, parent=None, deckbrowser=None):
        super().__init__(parent)
        self.deckbrowser = deckbrowser

        self.initUI()

    def initUI(self):
        from ..config import getUserOption
        self.columns = getUserOption("columns")

        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        self.checkboxes = []
        for column in self.columns:
            if "name" in column and "present" in column:
                # checkbox = QCheckBox(column["name"])

                from ..strings import defaultHeader
                checkbox = QCheckBox(f'{defaultHeader[column["name"]]} | {column["description"]}')

                checkbox.setChecked(column["present"])
                self.checkboxes.append((checkbox, column))
                scroll_layout.addWidget(checkbox)

        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.save_and_close)
        button_layout.addWidget(ok_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.close)
        button_layout.addWidget(cancel_button)

        button_layout.addStretch()
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.setWindowTitle("Toggle on or off for all columns")

        self.resize(WIDGET_WIDTH, WIDGET_HEIGHT)

    def save_and_close(self):
        for checkbox, column in self.checkboxes:
            column["present"] = checkbox.isChecked()
        from ..config import writeConfig
        writeConfig()
        self.deckbrowser.show()
        self.close()


def open_all_column_dialog(self, deckbrowser):
    dialog = ColumnDialog(self, deckbrowser)
    dialog.exec()
