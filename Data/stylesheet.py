class StyleSheet:
    @staticmethod
    def buttonColorStylesheet(rgba: tuple[int]) -> str:
        colorString: str = f"rgb({rgba[0]},{rgba[1]},{rgba[2]})"
        return (
            "QPushButton{background-color:" + colorString + ";height:20px;width:20px}"
        )
