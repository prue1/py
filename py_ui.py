# 需安裝 PyQt
# pip.exe install PyQt6

# 以下相容性問題, 無法安裝, 也非必要。
# pip.exe install PyQt6-tools

# 參考
# https://www.runoob.com/python3/python-pyqt.html

from PyQt6.QtWidgets import QApplication, QWidget

from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)  # Create the application instance
window = QWidget()          # Create a basic window widget
window.show()               # Make the window visible
sys.exit(app.exec())        # Start the event loop and exit when done
