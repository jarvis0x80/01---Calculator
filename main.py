from PySide6.QtGui import QIcon
from widget import Widget
from PySide6.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)
app.setApplicationName('Calculator')

app_icon = QIcon("icon.png")
app.setWindowIcon(app_icon)

mywidget = Widget()

mywidget.show()

app.exec()