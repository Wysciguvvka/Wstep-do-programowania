import codecs
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPlainTextEdit, QPushButton, QTabWidget, QVBoxLayout, QLabel, \
    QLineEdit, QCheckBox, QHBoxLayout
from PySide6.QtCore import QDate


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # self.setMinimumSize(QSize(440, 280))
        self.setWindowTitle("Program")
        # page 1
        self.page1 = QWidget()
        self.rot13area()
        # page 2
        self.page2 = QWidget()
        self.datetab()
        # page 3
        self.page3 = QWidget()
        self.backgroundcolor()
        tabs = self.createtabs()
        layout = QVBoxLayout(self)
        layout.addWidget(tabs)
        self.show()

    def rot13area(self):
        rot13text = QPlainTextEdit(self)
        rot13text.move(20, 30)
        rot13text.resize(400, 210)
        rot13text.setPlaceholderText("Placeholder")

        def _encrypt():
            text = rot13text.toPlainText()
            rot13text.setPlainText(codecs.encode(text, 'rot_13'))

        button = QPushButton(self)
        button.setText("Encrypt/Decrypt")
        button.clicked.connect(_encrypt)
        layout = QVBoxLayout()
        layout.addWidget(rot13text)
        layout.addWidget(button)
        self.page1.setLayout(layout)

    def datetab(self):
        label = QLabel()
        label.setText(f"Date duration calculator")
        label1 = QLabel()
        label1.setText(f"Date 1:")
        date1 = QtWidgets.QDateEdit()
        date1.setDate(QDate.currentDate())
        label2 = QLabel()
        label2.setText(f"Date 2:")
        date2 = QtWidgets.QDateEdit()
        # date2.setDate(QDate(2022, 1, 10))
        date2.setDate(QDate.currentDate())
        result = QLabel()
        # result.setText(f"Time difference:")
        result.setText(
            f"Time difference: "
            f"{int(abs((date1.date().toPython() - date2.date().toPython()).total_seconds() / 3600))} hours")

        def _deltatime():
            start = date1.date().toPython()
            end = date2.date().toPython()
            result.setText(f"Time difference: {int(abs((start - end).total_seconds() / 3600))} hours")

        # date1.dateTimeChanged.connect(_deltatime)
        # date2.dateTimeChanged.connect(_deltatime)
        button = QPushButton(self)
        button.setText("Calculate")
        button.clicked.connect(_deltatime)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(date1)
        layout.addWidget(label2)
        layout.addWidget(date2)
        layout.addWidget(result)
        layout.addWidget(button)
        self.page2.setLayout(layout)

    def backgroundcolor(self):
        label = QLabel()
        label.setText(f"Color Hex Code:")
        apply = QCheckBox("Apply")
        line = QLineEdit()
        line.setMaxLength(7)
        line.setPlaceholderText("#ffffff")
        line.textChanged.connect(lambda: self.setStyleSheet(
            f'QWidget {{background-color: {line.text()};}}') if apply.isChecked() else self.setStyleSheet(
            f'QWidget {{background-color: None;}}'))
        apply.stateChanged.connect(lambda: self.setStyleSheet(
            f'QWidget {{background-color: {line.text()};}}') if apply.isChecked() else self.setStyleSheet(
            f'QWidget {{background-color: None;}}'))

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line)
        layout.addWidget(apply)
        self.page3.setLayout(layout)

    def createtabs(self):
        tablist = QTabWidget(self)
        tablist.addTab(self.page1, "Rot13")
        tablist.addTab(self.page2, "Time")
        tablist.addTab(self.page3, "Background")
        return tablist


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())
