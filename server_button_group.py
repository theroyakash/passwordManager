from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QMessageBox, QLabel
import multiprocessing

multiprocessing.set_start_method("fork")

class ServerButtonGroup(QWidget):
    def __init__(self, flask_app):

        self.server_is_running = False
        self.flask_app = flask_app

        super().__init__()

        mainLayout = QVBoxLayout()
        information_label = QLabel("once you start a server a new browser window will open with the URL. work your things there. to stop just press stop server.")

        start_server = QPushButton()
        stop_server = QPushButton()

        start_server.setText(f"Start the Server")
        stop_server.setText("Stop the Server")

        start_server.clicked.connect(self.start_server_clicked)
        stop_server.clicked.connect(self.stop_server_clicked)

        server_start_end_layout = QHBoxLayout()
        server_start_end_layout.addWidget(start_server)
        server_start_end_layout.addWidget(stop_server)

        mainLayout.addWidget(information_label)
        mainLayout.addLayout(server_start_end_layout)

        self.setLayout(mainLayout)

    def start_server_clicked(self):
        message = ""
        msgbx = QMessageBox()

        if self.server_is_running:
            msgbx.setIcon(QMessageBox.Critical)
            message = "server already running"
        else:
            self.server_is_running = True
            msgbx.setIcon(QMessageBox.Information)
            message = "server started on localhost:6969"
            self.webservice = multiprocessing.Process(target = self.flask_app.run, args=["0.0.0.0", 6969, False])
            self.webservice.start()
            # self.flask_app.run(debug=False, host="0.0.0.0", port=6969)
        
        msgbx.setText(message)
        msgbx.exec()

    def stop_server_clicked(self):
        message = ""
        msgbx = QMessageBox()

        if not self.server_is_running:
            msgbx.setIcon(QMessageBox.Critical)
            message = "nothing to stop"
        else:
            self.server_is_running = False
            msgbx.setIcon(QMessageBox.Information)
            message = "server stopped"
            self.webservice.terminate()
        
        msgbx.setText(message)
        msgbx.exec()