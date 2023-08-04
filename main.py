# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Relative Imports
from ui import Ui_MainWindow
from Dialogs.color_picker import ColorPicker


class Main(Ui_MainWindow):
    def __init__(self):
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.connectColorPickers()
        self.scope.currentIndexChanged.connect(
            lambda index: self.stackedWidget.setCurrentIndex(index)
        )

    def connectResetButtons(self):
        """
        Connect Reset Buttons to their respective methods
        """
        pass

    def connectColorPickers(self):
        """
        Connect Color Picker Buttons to:
        - Color Picker Dialog
        Connect Color Picker Dialog to:
        - Color Output lineEdit
        """
        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor1,
            pushButton=self.dark_mode_gradient_color_picker1,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor1,
            pushButton=self.light_mode_gradient_color_picker1,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor2,
            pushButton=self.dark_mode_gradient_color_picker2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor2,
            pushButton=self.light_mode_gradient_color_picker2,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor3,
            pushButton=self.dark_mode_gradient_color_picker3,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor3,
            pushButton=self.light_mode_gradient_color_picker3,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor4_1,
            pushButton=self.dark_mode_gradient_color_picker4_1,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor4_1,
            pushButton=self.light_mode_gradient_color_picker4_1,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor4_2,
            pushButton=self.dark_mode_gradient_color_picker4_2,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor4_2,
            pushButton=self.light_mode_gradient_color_picker4_2,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor4_3,
            pushButton=self.dark_mode_gradient_color_picker4_3,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor4_3,
            pushButton=self.light_mode_gradient_color_picker4_3,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor4_4,
            pushButton=self.dark_mode_gradient_color_picker4_4,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor4_4,
            pushButton=self.light_mode_gradient_color_picker4_4,
        )

        ColorPicker.connectColorDialog(
            lineEdit=self.darkModeGradientColor4_5,
            pushButton=self.dark_mode_gradient_color_picker4_5,
        )
        ColorPicker.connectColorDialog(
            lineEdit=self.lightModeGradientColor4_5,
            pushButton=self.light_mode_gradient_color_picker4_5,
        )


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main: object = Main()
    main.mainWindow.show()
    app.exec()
