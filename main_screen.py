from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import sys
from server import flask_app
import database


if __name__ == "__main__":
    
    database.create_database_if_not_exists()
    database.create_user_table_if_not_exists()

    gui = QApplication(sys.argv)
    window = MainWindow(gui, flask_app)
    window.show()
    gui.exec()