class StyleSheet:
    @staticmethod
    def main() -> str:
        return """
        QLabel#title{
        color:white;
        font-size:15px;
        }
        QFrame#mainFrame{
        border:1px solid white;
        border-radius:10px;
        }
        QWidget#scrollAreaWidgetContents{
            background-color:white;
        }
        """

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
