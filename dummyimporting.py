# Austin Hasten
# Initial Commit - February 28th, 2018

from aqt.importing import ImportDialog
from anki.importing.csvfile import TextImporter

class DummyImporter(TextImporter):
    def __init__(self, col, flds, delimiter, data):
        super().__init__(col, None)
        self.flds = flds
        self.data = data
        self.delimiter = delimiter
        self.numFields = len(self.flds)
        self.fileobj = open('dummy', 'w+')

class ImportDialog(ImportDialog):
    def __init__(self, mw, flds, data, delimiter=';', importMode=2, allowHTML=True):
        self.importMode = importMode
        self.allowHTML = allowHTML
        super().__init__(mw, DummyImporter(mw.col, flds, delimiter, data))

    def exec_(self):
        self.frm.importMode.setCurrentIndex(self.importMode)
        self.frm.allowHTML.setCheckState(self.allowHTML)
        self.frm.allowHTML.close()
        self.frm.autoDetect.close()
        super().exec_()

    def showMapping(self, keepMapping=False, hook=None):
        super().showMapping(keepMapping, hook)
        for num in range(len(self.mapping)):
            text = f"<b>{self.importer.flds[num]}</b> is:"
            self.grid.itemAtPosition(num, 0).widget().setText(text)
