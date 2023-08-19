class StyleSheet:
    @staticmethod
    def main() -> str:
        return """
        QMainWindow{
        background-color:black;
        }
        QWidget#tab_1,QWidget#tab_2,QWidget#tab_4{
        background-color:black;
        }
        QLabel{
        color:white;
        }
        """

    @staticmethod
    def frame():
        return "QWidget#scrollAreaWidgetContents{background-color:white;}"

    @staticmethod
    def buttonColorStylesheet(rgba: tuple | str) -> str:
        if type(rgba) == str:
            return "QPushButton{background-color:" + rgba + ";width:20px}"
        elif type(rgba) == tuple:
            colorString: str = f"rgb({rgba[0]},{rgba[1]},{rgba[2]})"
            return "QPushButton{background-color:" + colorString + ";width:20px}"
        else:
            return ""

    @staticmethod
    def buttoResetStyleSheet() -> str:
        return "QPushButton{background-color: none;width:20px;}"
