class ServerStatus:
    def __init__(self):
        self.__isRunning: bool = False

    def setServerOn(self) -> None:
        self.__isRunning = True

    def setServerOff(self) -> None:
        self.__isRunning = False

    def isRunning(self) -> bool:
        return self.__isRunning