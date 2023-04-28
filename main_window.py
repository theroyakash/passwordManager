from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QMainWindow, QPushButton, QWidget
from server_button_group import ServerButtonGroup
from open_browser import open_browser_with_url


class MainWindow(QMainWindow):
    def __init__(self, app, flask_app):

        self.app = app

        super().__init__()
        self.setWindowTitle("Your Local Password Manager")

        serverButtonGroup = ServerButtonGroup(flask_app)
        self.setCentralWidget(serverButtonGroup)

        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.__quit_from_app)

        help = menubar.addMenu("&Help")
        help_action = help.addAction("About")
        help_action.triggered.connect(open_browser_with_url)


    def __quit_from_app(self):
        self.app.quit()