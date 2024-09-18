# AGPL-3.0 License
# Copyright (C) Arthur Milchior  2018 - 2023  <https://github.com/Arthur-Milchior>
# Copyright (C) Shigeyuki 2024 <http://patreon.com/Shigeyuki>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from anki.lang import _
from aqt.deckbrowser import DeckBrowser
from aqt.qt import *
from aqt.utils import askUser

from .config import getUserOption, writeConfig

lastHandler = DeckBrowser._linkHandler


def _linkHandler(self, url):
    if ":" in url:
        (cmd, arg) = url.split(":")
        if cmd == "dragColumn":
            return columnHandler(self, arg)
        elif cmd == "optsColumn":
            # return columnOptions(self, arg)
            return  QTimer.singleShot(10, lambda: custom_column(self, arg))
    return lastHandler(self, url)


def columnHandler(self, arg):
    draggedDeckId, ontoDeckId = arg.split(",")
    draggedDeckId = int(draggedDeckId)
    ontoDeckId = int(ontoDeckId)
    columns = getUserOption("columns")
    columns.insert(draggedDeckId, columns.pop(ontoDeckId))
    writeConfig()
    self.show()


# def custom_column(self, colpos):
#     # from aqt.utils import tooltip
#     from .custom_by_shige.custom_column import CustomColumnDialog
#     colpos = int(colpos)
#     columns = getUserOption("columns")
#     column = columns[colpos]
#     # tooltip(f"Custom Column :  {colpos}<br>{column}")
#     dialog = CustomColumnDialog(column, self.mw, self)
#     dialog.exec()

def custom_column(self, colpos):
    # from aqt.utils import tooltip
    from .custom_by_shige.custom_column import CustomColumnDialog
    print(f"Received colpos: {colpos}")
    colpos = int(colpos)
    print(f"Converted colpos to int: {colpos}")
    columns = getUserOption("columns")
    print(f"Retrieved columns: {columns}")
    column = columns[colpos]
    print(f"Selected column: {column}")
    # tooltip(f"Custom Column :  {colpos}<br>{column}")
    dialog = CustomColumnDialog(column, self.mw, self)
    print("Initialized CustomColumnDialog")
    dialog.exec()
    print("Executed dialog")


def deleteColumn(self, colpos):
    if not askUser(_("""Are you sure you wish to delete this column ?""")):
        return
    colpos = int(colpos)
    print("They are sure.")
    columns = getUserOption("columns")
    column = columns[colpos]
    column["present"] = False
    writeConfig()
    self.show()



# def columnOptions(self, colpos):
#     m = QMenu(self.mw)
#     a = m.addAction(_("Delete"))
#     a.triggered.connect(lambda: deleteColumn(self, colpos))
#     if hasattr(m, 'exec_'): # added
#         m.exec_(QCursor.pos())
#     else:
#         m.exec(QCursor.pos())

# def columnOptions(self, colpos):
#     m = QMenu(self.mw)

#     b = m.addAction("⚙️Custom")
#     b.triggered.connect(lambda: QTimer.singleShot(0, custom_column(self, colpos)))

#     a = m.addAction("🗑️Delete")
#     a.triggered.connect(lambda: deleteColumn(self, colpos))

#     if hasattr(m, 'exec_'): # added
#         m.exec_(QCursor.pos())
#     else:
#         m.exec(QCursor.pos())





