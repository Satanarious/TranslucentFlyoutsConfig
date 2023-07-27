# Library Imports
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from Data.defaults import Defaults

# Relative Imports
from ui import Ui_MainWindow
from Dialogs.color_picker import ColorPickerButton


class Main(Ui_MainWindow):
    def __init__(self):
        self.mainWindow: QMainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.connectColorPickers()

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
        self.dark_mode_gradient_color_picker1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor1)
        )
        self.light_mode_gradient_color_picker1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor1)
        )
        self.dark_mode_opacity_picker1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity1)
        )
        self.light_mode_opacity_picker1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity1)
        )
        self.dark_mode_gradient_color_picker2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor2)
        )
        self.light_mode_gradient_color_picker2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor2)
        )
        self.dark_mode_opacity_picker2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity2)
        )
        self.light_mode_opacity_picker2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity2)
        )
        self.dark_mode_gradient_color_picker3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor3)
        )
        self.light_mode_gradient_color_picker3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor3)
        )
        self.dark_mode_opacity_picker3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity3)
        )
        self.light_mode_opacity_picker3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity3)
        )
        self.dark_mode_gradient_color_picker4_1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor4_1)
        )
        self.light_mode_gradient_color_picker4_1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor4_1)
        )
        self.dark_mode_opacity_picker4_1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity4_1)
        )
        self.light_mode_opacity_picker4_1.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity4_1)
        )
        self.dark_mode_gradient_color_picker4_2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor4_2)
        )
        self.light_mode_gradient_color_picker4_2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor4_2)
        )
        self.dark_mode_opacity_picker4_2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity4_2)
        )
        self.light_mode_opacity_picker4_2.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity4_2)
        )
        self.dark_mode_gradient_color_picker4_3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor4_3)
        )
        self.light_mode_gradient_color_picker4_3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor4_3)
        )
        self.dark_mode_opacity_picker4_3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity4_3)
        )
        self.light_mode_opacity_picker4_3.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity4_3)
        )
        self.dark_mode_gradient_color_picker4_4.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor4_4)
        )
        self.light_mode_gradient_color_picker4_4.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor4_4)
        )
        self.dark_mode_opacity_picker4_4.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity4_4)
        )
        self.light_mode_opacity_picker4_4.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity4_4)
        )
        self.dark_mode_gradient_color_picker4_5.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeGradientColor4_5)
        )
        self.light_mode_gradient_color_picker4_5.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeGradientColor4_5)
        )
        self.dark_mode_opacity_picker4_5.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.darkModeOpacity4_5)
        )
        self.light_mode_opacity_picker4_5.clicked.connect(
            lambda a: ColorPickerButton.openColorDialog(self.lightModeOpacity4_5)
        )


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    main: object = Main()
    main.mainWindow.show()
    app.exec()
