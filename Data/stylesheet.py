class StyleSheet:
    @staticmethod
    def main(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QLabel{
        font-family: Nunito Sans 10pt Condensed;
        font-size: 13px;
        }
        QMainWindow,QWidget#centralwidget,QTabWidget,QTabWidget::tab{
            border:none;
            background-color: """
            + backgroundColor
            + """;
        }
        QFrame#titleFrame{
            background-color:"""
            + backgroundColor
            + """;
        }
        QFrame#mainFrame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QWidget#centralwidget{
            border-top-left-radius:8px;
            border-top-right-radius:8px;
            background-color:"""
            + backgroundColor
            + """;
        }
        QLabel{
            color:"""
            + labelColor
            + """;
        }
        QLabel#title{
            font-size:14px;
            font-weight:bold;
        }
        QWidget#tab1,
        QWidget#tab2,
        QWidget#tab3,
        QWidget#tab3_1,
        QWidget#tab3_2,
        QWidget#tab3_3,
        QWidget#tab3_4,
        QWidget#tab3_5,
        QWidget#tab3_6,
        QWidget#tab4,
        QScrollArea,
        QWidget#scrollAreaWidgetContents{
            background-color:"""
            + backgroundColor
            + """;
            border:1px solid """
            + secondaryBackgroundColor
            + """;
        }
        QComboBox{
            padding-left:10px;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QComboBox::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QComboBox::drop-down {
            border-left-width: 1px;
            border-left-color: """
            + textColor
            + """;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }
        QComboBox:on{
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 0px;
        }
        QComboBox::down-arrow {
            width: 20px;
            image: url("Assets/icons/down-arrow.png");
        }
        QComboBox QAbstractItemView{
            border: none;
            color:"""
            + textColor
            + """;
            border-left:1px solid """
            + labelColor
            + """;
            border-right:1px solid """
            + labelColor
            + """;
            border-bottom:1px solid """
            + labelColor
            + """;
            border-bottom-left-radius:8px;
            border-bottom-right-radius:8px;
            selection-background-color:"""
            + backgroundColor
            + """;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        
        }
        QComboBox QAbstractItemView::item:hover{
            background-color:"""
            + backgroundColor
            + """;
        }
        QLineEdit{
            padding-left:10px;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QSpinBox{
            padding-left:10px;
            selection-background-color:"""
            + secondaryBackgroundColor
            + """;
            selection-color:"""
            + labelColor
            + """;
            font-family: Andika;
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-radius:5px;
            color:"""
            + textColor
            + """;
        }
        QSpinBox::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QSpinBox::focus{
            border:1px solid """
            + labelColor
            + """;
        }
        QSpinBox::up-button, QSpinBox::down-button {
            border: none;
            background-color: none;
            margin-right:4px;
            width:10px;
        }
        QSpinBox::up-button{
            image: url("Assets/icons/up-arrow.png");
        }
        QSpinBox::down-button{
            image: url("Assets/icons/down-arrow.png");
        }
        QPushButton{
            border-radius:5px;
            width:25px;
            height:25px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        QToolButton#minimizeButton{
            padding:5px;
        }
        QToolButton#minimizeButton::hover{
            background-color:none;
            
        }
        QToolButton#closeButton::hover{
            background-color:red;
            border-top-right-radius:8px;
        }
        QScrollBar:vertical {
            border: 0px solid """
            + labelColor
            + """;
            background:"""
            + secondaryBackgroundColor
            + """;
            width: 8px;
            margin: 0px;
        }
        QScrollBar::handle:vertical{
            background-color: """
            + backgroundColor
            + """;
            border:0px solid """
            + secondaryBackgroundColor
            + """;
            border-radius:4px;
            min-height: 0px;
        }
         QScrollBar::add-line:vertical {       
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QTabWidget::pane{
            border:none;
        }
        QTabBar::pane {
            border: none;
        }
        QToolTip{
            color:"""
            + backgroundColor
            + """;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def appliedWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QFrame#applied_frame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border:1px solid """
            + labelColor
            + """;
            border-radius:8px;
        }
        QLabel#applied_text{
            font-family: Andika;
            font-size: 12;
            font-weight:bold;
        }
        QPushButton#ok_button{
            font-family: Nunito Sans 10pt Condensed;
            font-size:10;
            font-weight:bold;
            background-color:"""
            + textColor
            + """;
            color:"""
            + labelColor
            + """;
            width:50px;
        }
        QPushButton#ok_button::hover{
            color:"""
            + labelColor
            + """;
        }
        QPushButton#ok_button::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        """
        )

    @staticmethod
    def infoWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QFrame#titleFrame{
            background-color:"""
            + secondaryBackgroundColor
            + """;
            border-top-left-radius:8px;
            border-top-right-radius:8px;
            border-top:1px solid """
            + labelColor
            + """;
            border-left:1px solid """
            + labelColor
            + """;
            border-right:1px solid """
            + labelColor
            + """;
        }
        QLabel#title{
            font-family: Nunito Sans 10pt Condensed;
            font-size:14px;
            font-weight:bold;
        }
        QLabel#description{
            font-family: Andika;
        }
        QScrollArea{
            border:1px solid """
            + labelColor
            + """;
        }
        QToolButton#closeButton::hover{
            background-color:red;
            border-top-right-radius:8px;
        }
        """
        )

    @staticmethod
    def applyButton(
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QPushButton{
            border-radius:5px;
            color:"""
            + labelColor
            + """;
            width:70px;
            height:30px;
            background-color:"""
            + secondaryBackgroundColor
            + """;
        }
        QPushButton::hover{
            border:1px solid """
            + labelColor
            + """;
        }
        QPushButton::pressed{
            color:"""
            + labelColor
            + """;
            background-color:"""
            + textColor
            + """;
        }
        """
        )

    @staticmethod
    def mainTabBar(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:"""
            + textColor
            + """;
            padding-left:38px;
            padding-right:38px;
            padding-top:5px;
            padding-bottom:5px;
            margin-left:10px;
         }
        QTabBar::tab:hover{
            color:"""
            + labelColor
            + """;
        }
        QTabBar::tab:selected {
            color: """
            + labelColor
            + """;
            margin-top:3px;
            margin-bottom:3px;
            border:1px solid """
            + textColor
            + """;
            font-weight:bold;
            border-radius: 5px;
            background-color: """
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def menuTabBar(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
        QTabBar::tab { 
            background-color: """
            + secondaryBackgroundColor
            + """;
            color:"""
            + textColor
            + """;
            padding-left:17px;
            padding-right:17px;
            padding-top:5px;
            padding-bottom:5px;
         }
        QTabBar::tab:hover{
            color:"""
            + labelColor
            + """;
        }
        QTabBar::tab:selected {
            color: """
            + labelColor
            + """;
            font-weight:bold;
            background-color: """
            + backgroundColor
            + """;
        }
        """
        )

    @staticmethod
    def buttonColorStylesheet(rgba: tuple) -> str:
        colorString: str = f"rgb({rgba[0]},{rgba[1]},{rgba[2]})"
        return """QPushButton{background-color:""" + colorString + """;width:25px;height:25px;}"""

    @staticmethod
    def buttoResetStyleSheet(resetColor: str = "#313131") -> str:
        return """QPushButton{background-color:""" + resetColor + """;width:25px;height:25px;}"""

    class ColorPicker:
        @staticmethod
        def titleBar(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "white",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                    QFrame{
                    background-color:"""
                + secondaryBackgroundColor
                + """;
                    border-bottom-left-radius:0px;
                    border-bottom-right-radius:0px;
                    }

                    """
            )

        @staticmethod
        def windowTitle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "white",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                    QLabel{
                    font-size:13px;
                    color:"""
                + labelColor
                + """;
                    font-weight:bold;
                    }

                    """
            )

        @staticmethod
        def buttonTextStyle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "white",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                QDialogButtonBox QPushButton{
                font-size:12px;
                font-weight:normal;
                }
                QDialogButtonBox QPushButton::hover{
                    border:1px solid """
                + labelColor
                + """;
                }
                QDialogButtonBox QPushButton::pressed{
                    color:"""
                + labelColor
                + """;
                    background-color:"""
                + textColor
                + """;
                }
                """
            )

        @staticmethod
        def labelStyle(
            backgroundColor: str = "#202020",
            secondaryBackgroundColor: str = "#313131",
            labelColor: str = "white",
            textColor: str = "#7A7A7A",
        ) -> str:
            return (
                """
                QLabel{
                color:"""
                + labelColor
                + """;
                font-size:12px;
                font-weight:normal;
                }
                """
            )

    @staticmethod
    def settingsWidget(
        backgroundColor: str = "#202020",
        secondaryBackgroundColor: str = "#313131",
        labelColor: str = "white",
        textColor: str = "#7A7A7A",
    ) -> str:
        return (
            """
            QFrame{background-color:"""
            + backgroundColor
            + """; border-radius:8px;}
            QLabel{color:"""
            + labelColor
            + """;}
            QPushButton{color:"""
            + labelColor
            + """;background-color:"""
            + secondaryBackgroundColor
            + """;width:70px;}
            """
        )
