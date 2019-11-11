from PyQt5.QtCore import QObject

class ControllerTelaSistema(QObject):
    def __init__(self, model):
        self.model = model