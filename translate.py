# Library Imports
from __future__ import annotations
from typing import TYPE_CHECKING
from PyQt6.QtWidgets import QDialogButtonBox

# Relative Imports
from Data.translations import translationVar, Key
from Data.enums import Languages, MainTab, MenuTab, Settings
from Widgets.color_picker import ColorPicker

if TYPE_CHECKING:
    from main import Main


class Translate:
    @staticmethod
    def findLanguageFromInt(inputLangauge: int) -> Languages:
        for language in Languages:
            if language.value == inputLangauge:
                return language
        return Languages.Default

    @staticmethod
    def translate(window: Main, language: Languages) -> None:
        translationVar.setLanguage(language)
        _translate = translationVar.translateFrom

        window.title.setText(_translate(Key.TranslucentFlyoutsConfig))

        # Apply Button
        window.applyButton1.setText(_translate(Key.apply))
        window.applyButton2.setText(_translate(Key.apply))
        window.applyButton3_1.setText(_translate(Key.apply))
        window.applyButton3_2.setText(_translate(Key.apply))
        window.applyButton3_3.setText(_translate(Key.apply))
        window.applyButton3_4.setText(_translate(Key.apply))
        window.applyButton3_5.setText(_translate(Key.apply))
        window.applyButton3_6.setText(_translate(Key.apply))
        window.applyButton4.setText(_translate(Key.apply))

        ######### Paramaters #########

        # Main Tab Widget- Tabs
        window.mainTabWidget.setTabText(MainTab.Global, _translate(Key.Tab._global))
        window.mainTabWidget.setTabText(MainTab.DropDown, _translate(Key.Tab.dropDown))
        window.mainTabWidget.setTabText(MainTab.Menu, _translate(Key.Tab.menu))
        window.mainTabWidget.setTabText(MainTab.Tooltip, _translate(Key.Tab.tooltip))

        # Menu Tab Widget- Tabs
        window.menuTabWidget.setTabText(MenuTab.General, _translate(Key.Tab.Menu.general))
        window.menuTabWidget.setTabText(MenuTab.Animation, _translate(Key.Tab.Menu.animation))
        window.menuTabWidget.setTabText(MenuTab.Hot, _translate(Key.Tab.Menu.hot))
        window.menuTabWidget.setTabText(MenuTab.DisabledHot, _translate(Key.Tab.Menu.disabledHot))
        window.menuTabWidget.setTabText(MenuTab.Focusing, _translate(Key.Tab.Menu.focusing))
        window.menuTabWidget.setTabText(MenuTab.Separator, _translate(Key.Tab.Menu.separator))

        # Tab-Descriptions
        window.description1.setText(_translate(Key.TabDescription._global))
        window.note1.setText(_translate(Key.TabDescription.globalNote))
        window.description2.setText(_translate(Key.TabDescription.dropDown))
        window.description3.setText(_translate(Key.TabDescription.menu))
        window.description4.setText(_translate(Key.TabDescription.tooltip))

        # Effect Type
        window.lbl_effectType1.setText(_translate(Key.Parameter.effectType))
        window.lbl_effectType2.setText(_translate(Key.Parameter.effectType))
        window.lbl_effectType3.setText(_translate(Key.Parameter.effectType))
        window.lbl_effectType4.setText(_translate(Key.Parameter.effectType))

        # Corner Type
        window.lbl_cornerType1.setText(_translate(Key.Parameter.cornerType))
        window.lbl_cornerType2.setText(_translate(Key.Parameter.cornerType))
        window.lbl_cornerType3.setText(_translate(Key.Parameter.cornerType))
        window.lbl_cornerType4.setText(_translate(Key.Parameter.cornerType))

        # Enable Drop Shadow
        window.lbl_enableDropShadow1.setText(_translate(Key.Parameter.enableDropShadow))
        window.lbl_enableDropShadow2.setText(_translate(Key.Parameter.enableDropShadow))
        window.lbl_enableDropShadow3.setText(_translate(Key.Parameter.enableDropShadow))
        window.lbl_enableDropShadow4.setText(_translate(Key.Parameter.enableDropShadow))

        # No Border Color
        window.lbl_noBorderColor1.setText(_translate(Key.Parameter.noBorderColor))
        window.lbl_noBorderColor2.setText(_translate(Key.Parameter.noBorderColor))
        window.lbl_noBorderColor3.setText(_translate(Key.Parameter.noBorderColor))
        window.lbl_noBorderColor4.setText(_translate(Key.Parameter.noBorderColor))

        # Enable Theme Colorization
        window.lbl_enableThemeColorization1.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization2.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization3_1.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization3_2.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization3_3.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization3_4.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization3_5.setText(_translate(Key.Parameter.enableThemeColorization))
        window.lbl_enableThemeColorization4.setText(_translate(Key.Parameter.enableThemeColorization))

        # Dark Mode Border Color
        window.lbl_darkModeBorderColor1.setText(_translate(Key.Parameter.darkModeBorderColor))
        window.lbl_darkModeBorderColor2.setText(_translate(Key.Parameter.darkModeBorderColor))
        window.lbl_darkModeBorderColor3.setText(_translate(Key.Parameter.darkModeBorderColor))
        window.lbl_darkModeBorderColor4.setText(_translate(Key.Parameter.darkModeBorderColor))

        # Light Mode Border Color
        window.lbl_lightModeBorderColor1.setText(_translate(Key.Parameter.lightModeBorderColor))
        window.lbl_lightModeBorderColor2.setText(_translate(Key.Parameter.lightModeBorderColor))
        window.lbl_lightModeBorderColor3.setText(_translate(Key.Parameter.lightModeBorderColor))
        window.lbl_lightModeBorderColor4.setText(_translate(Key.Parameter.lightModeBorderColor))

        # Dark Mode Gradient Color
        window.lbl_darkModeGradientColor1.setText(_translate(Key.Parameter.darkModeGradientColor))
        window.lbl_darkModeGradientColor2.setText(_translate(Key.Parameter.darkModeGradientColor))
        window.lbl_darkModeGradientColor3.setText(_translate(Key.Parameter.darkModeGradientColor))
        window.lbl_darkModeGradientColor4.setText(_translate(Key.Parameter.darkModeGradientColor))

        # Light Mode Gradient Color
        window.lbl_lightModeGradientColor1.setText(_translate(Key.Parameter.lightModeGradientColor))
        window.lbl_lightModeGradientColor2.setText(_translate(Key.Parameter.lightModeGradientColor))
        window.lbl_lightModeGradientColor3.setText(_translate(Key.Parameter.lightModeGradientColor))
        window.lbl_lightModeGradientColor4.setText(_translate(Key.Parameter.lightModeGradientColor))

        # Disabled
        window.lbl_disabledEffect1.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect2.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect3_1.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect3_2.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect3_3.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect3_4.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect3_5.setText(_translate(Key.Parameter.disabled))
        window.lbl_disabledEffect4.setText(_translate(Key.Parameter.disabled))

        # Menu-General Exclusive
        window.lbl_noSystemDropShadow.setText(_translate(Key.Parameter.noSystemDropShadow))
        window.lbl_enableImmersiveStyle.setText(_translate(Key.Parameter.enableImmersiveStyle))
        window.lbl_enableCustomRendering.setText(_translate(Key.Parameter.enableCustomRendering))
        window.lbl_enableFluentAnimation.setText(_translate(Key.Parameter.enableFluentAnimation))
        window.lbl_noModernAppBackgroundColor.setText(_translate(Key.Parameter.noModernAppBackgroundColor))
        window.lbl_colorTreatAsTransparent.setText(_translate(Key.Parameter.colorTreatAsTransparent))
        window.lbl_colorTreatAsTransparentThreshold.setText(_translate(Key.Parameter.colorTreatAsTransparentThreshold))

        # Menu-Animation Exclusive
        window.lbl_fadeOutTime.setText(_translate(Key.Parameter.fadeOutTime))
        window.lbl_fadeInTime.setText(_translate(Key.Parameter.fadeInTime))
        window.lbl_popInTime.setText(_translate(Key.Parameter.popInTime))
        window.lbl_popInStyle.setText(_translate(Key.Parameter.popInStyle))
        window.lbl_startRatio.setText(_translate(Key.Parameter.startRatio))
        window.lbl_enableImmediateInterupting.setText(_translate(Key.Parameter.enableImmediateInterupting))

        # Dark Mode Color
        window.lbl_darkModeColor1_1.setText(_translate(Key.Parameter.darkModeColor))
        window.lbl_darkModeColor1_2.setText(_translate(Key.Parameter.darkModeColor))
        window.lbl_darkModeColor1_3.setText(_translate(Key.Parameter.darkModeColor))
        window.lbl_darkModeColor1_4.setText(_translate(Key.Parameter.darkModeColor))

        # Light Mode Color
        window.lbl_lightModeColor1_1.setText(_translate(Key.Parameter.lightModeColor))
        window.lbl_lightModeColor1_2.setText(_translate(Key.Parameter.lightModeColor))
        window.lbl_lightModeColor1_3.setText(_translate(Key.Parameter.lightModeColor))
        window.lbl_lightModeColor1_4.setText(_translate(Key.Parameter.lightModeColor))

        # Corner Radius
        window.lbl_cornerRadius1_1.setText(_translate(Key.Parameter.cornerRadius))
        window.lbl_cornerRadius1_2.setText(_translate(Key.Parameter.cornerRadius))
        window.lbl_cornerRadius1_3.setText(_translate(Key.Parameter.cornerRadius))
        window.lbl_cornerRadius1_4.setText(_translate(Key.Parameter.cornerRadius))

        # Width
        window.lbl_width1_1.setText(_translate(Key.Parameter.width))
        window.lbl_width1_2.setText(_translate(Key.Parameter.width))

        ######### Values #########

        # Effect Type
        window.effectType1.setItemText(Settings.EffectType.Disabled, _translate(Key.Value.EffectType.disabled))
        window.effectType1.setItemText(Settings.EffectType.FullyTransparent, _translate(Key.Value.EffectType.transparent))
        window.effectType1.setItemText(Settings.EffectType.SolidColor, _translate(Key.Value.EffectType.solid))
        window.effectType1.setItemText(Settings.EffectType.Blurred, _translate(Key.Value.EffectType.blur))
        window.effectType1.setItemText(Settings.EffectType.Acrylic, _translate(Key.Value.EffectType.classicAcrylicBlur))
        window.effectType1.setItemText(Settings.EffectType.ModernAcrylic, _translate(Key.Value.EffectType.modernAcrylicBlur))
        window.effectType1.setItemText(Settings.EffectType.AcrylicBackgroundLayer, _translate(Key.Value.EffectType.acrylic))
        window.effectType1.setItemText(Settings.EffectType.MicaBackgroundLayer, _translate(Key.Value.EffectType.mica))
        window.effectType1.setItemText(Settings.EffectType.MicaVariantBackgroundLayer, _translate(Key.Value.EffectType.micaAlt))

        window.effectType2.setItemText(Settings.EffectType.Disabled, _translate(Key.Value.EffectType.disabled))
        window.effectType2.setItemText(Settings.EffectType.FullyTransparent, _translate(Key.Value.EffectType.transparent))
        window.effectType2.setItemText(Settings.EffectType.SolidColor, _translate(Key.Value.EffectType.solid))
        window.effectType2.setItemText(Settings.EffectType.Blurred, _translate(Key.Value.EffectType.blur))
        window.effectType2.setItemText(Settings.EffectType.Acrylic, _translate(Key.Value.EffectType.classicAcrylicBlur))
        window.effectType2.setItemText(Settings.EffectType.ModernAcrylic, _translate(Key.Value.EffectType.modernAcrylicBlur))
        window.effectType2.setItemText(Settings.EffectType.AcrylicBackgroundLayer, _translate(Key.Value.EffectType.acrylic))
        window.effectType2.setItemText(Settings.EffectType.MicaBackgroundLayer, _translate(Key.Value.EffectType.mica))
        window.effectType2.setItemText(Settings.EffectType.MicaVariantBackgroundLayer, _translate(Key.Value.EffectType.micaAlt))
        window.effectType2.setItemText(Settings.EffectType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.effectType3.setItemText(Settings.EffectType.Disabled, _translate(Key.Value.EffectType.disabled))
        window.effectType3.setItemText(Settings.EffectType.FullyTransparent, _translate(Key.Value.EffectType.transparent))
        window.effectType3.setItemText(Settings.EffectType.SolidColor, _translate(Key.Value.EffectType.solid))
        window.effectType3.setItemText(Settings.EffectType.Blurred, _translate(Key.Value.EffectType.blur))
        window.effectType3.setItemText(Settings.EffectType.Acrylic, _translate(Key.Value.EffectType.classicAcrylicBlur))
        window.effectType3.setItemText(Settings.EffectType.ModernAcrylic, _translate(Key.Value.EffectType.modernAcrylicBlur))
        window.effectType3.setItemText(Settings.EffectType.AcrylicBackgroundLayer, _translate(Key.Value.EffectType.acrylic))
        window.effectType3.setItemText(Settings.EffectType.MicaBackgroundLayer, _translate(Key.Value.EffectType.mica))
        window.effectType3.setItemText(Settings.EffectType.MicaVariantBackgroundLayer, _translate(Key.Value.EffectType.micaAlt))
        window.effectType3.setItemText(Settings.EffectType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.effectType4.setItemText(Settings.EffectType.Disabled, _translate(Key.Value.EffectType.disabled))
        window.effectType4.setItemText(Settings.EffectType.FullyTransparent, _translate(Key.Value.EffectType.transparent))
        window.effectType4.setItemText(Settings.EffectType.SolidColor, _translate(Key.Value.EffectType.solid))
        window.effectType4.setItemText(Settings.EffectType.Blurred, _translate(Key.Value.EffectType.blur))
        window.effectType4.setItemText(Settings.EffectType.Acrylic, _translate(Key.Value.EffectType.classicAcrylicBlur))
        window.effectType4.setItemText(Settings.EffectType.ModernAcrylic, _translate(Key.Value.EffectType.modernAcrylicBlur))
        window.effectType4.setItemText(Settings.EffectType.AcrylicBackgroundLayer, _translate(Key.Value.EffectType.acrylic))
        window.effectType4.setItemText(Settings.EffectType.MicaBackgroundLayer, _translate(Key.Value.EffectType.mica))
        window.effectType4.setItemText(Settings.EffectType.MicaVariantBackgroundLayer, _translate(Key.Value.EffectType.micaAlt))
        window.effectType4.setItemText(Settings.EffectType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # Corner Type
        window.cornerType1.setItemText(Settings.CornerType.DontChange, _translate(Key.Value.CornerType.dontChange))
        window.cornerType1.setItemText(Settings.CornerType.Square, _translate(Key.Value.CornerType.squareCorners))
        window.cornerType1.setItemText(Settings.CornerType.LargeRound, _translate(Key.Value.CornerType.largeCorners))
        window.cornerType1.setItemText(Settings.CornerType.SmallRound, _translate(Key.Value.CornerType.smallCorners))

        window.cornerType2.setItemText(Settings.CornerType.DontChange, _translate(Key.Value.CornerType.dontChange))
        window.cornerType2.setItemText(Settings.CornerType.Square, _translate(Key.Value.CornerType.squareCorners))
        window.cornerType2.setItemText(Settings.CornerType.LargeRound, _translate(Key.Value.CornerType.largeCorners))
        window.cornerType2.setItemText(Settings.CornerType.SmallRound, _translate(Key.Value.CornerType.smallCorners))
        window.cornerType2.setItemText(Settings.CornerType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.cornerType3.setItemText(Settings.CornerType.DontChange, _translate(Key.Value.CornerType.dontChange))
        window.cornerType3.setItemText(Settings.CornerType.Square, _translate(Key.Value.CornerType.squareCorners))
        window.cornerType3.setItemText(Settings.CornerType.LargeRound, _translate(Key.Value.CornerType.largeCorners))
        window.cornerType3.setItemText(Settings.CornerType.SmallRound, _translate(Key.Value.CornerType.smallCorners))
        window.cornerType3.setItemText(Settings.CornerType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.cornerType4.setItemText(Settings.CornerType.DontChange, _translate(Key.Value.CornerType.dontChange))
        window.cornerType4.setItemText(Settings.CornerType.Square, _translate(Key.Value.CornerType.squareCorners))
        window.cornerType4.setItemText(Settings.CornerType.LargeRound, _translate(Key.Value.CornerType.largeCorners))
        window.cornerType4.setItemText(Settings.CornerType.SmallRound, _translate(Key.Value.CornerType.smallCorners))
        window.cornerType4.setItemText(Settings.CornerType.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # Enable Drop Shadow
        window.enableDropShadow1.setItemText(Settings.EnableDropShadow.No, _translate(Key.Value.Bool.no))
        window.enableDropShadow1.setItemText(Settings.EnableDropShadow.Yes, _translate(Key.Value.Bool.yes))

        window.enableDropShadow2.setItemText(Settings.EnableDropShadow.No, _translate(Key.Value.Bool.no))
        window.enableDropShadow2.setItemText(Settings.EnableDropShadow.Yes, _translate(Key.Value.Bool.yes))
        window.enableDropShadow2.setItemText(Settings.EnableDropShadow.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.enableDropShadow3.setItemText(Settings.EnableDropShadow.No, _translate(Key.Value.Bool.no))
        window.enableDropShadow3.setItemText(Settings.EnableDropShadow.Yes, _translate(Key.Value.Bool.yes))
        window.enableDropShadow3.setItemText(Settings.EnableDropShadow.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.enableDropShadow4.setItemText(Settings.EnableDropShadow.No, _translate(Key.Value.Bool.no))
        window.enableDropShadow4.setItemText(Settings.EnableDropShadow.Yes, _translate(Key.Value.Bool.yes))
        window.enableDropShadow4.setItemText(Settings.EnableDropShadow.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # No Border Color
        window.noBorderColor1.setItemText(Settings.NoBorderColor.No, _translate(Key.Value.Bool.no))
        window.noBorderColor1.setItemText(Settings.NoBorderColor.Yes, _translate(Key.Value.Bool.yes))

        window.noBorderColor2.setItemText(Settings.NoBorderColor.No, _translate(Key.Value.Bool.no))
        window.noBorderColor2.setItemText(Settings.NoBorderColor.Yes, _translate(Key.Value.Bool.yes))
        window.noBorderColor2.setItemText(Settings.NoBorderColor.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.noBorderColor3.setItemText(Settings.NoBorderColor.No, _translate(Key.Value.Bool.no))
        window.noBorderColor3.setItemText(Settings.NoBorderColor.Yes, _translate(Key.Value.Bool.yes))
        window.noBorderColor3.setItemText(Settings.NoBorderColor.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.noBorderColor4.setItemText(Settings.NoBorderColor.No, _translate(Key.Value.Bool.no))
        window.noBorderColor4.setItemText(Settings.NoBorderColor.Yes, _translate(Key.Value.Bool.yes))
        window.noBorderColor4.setItemText(Settings.NoBorderColor.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # Enable Theme Colorization
        window.enableThemeColorization1.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization1.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))

        window.enableThemeColorization2.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization2.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))
        window.enableThemeColorization2.setItemText(Settings.EnableThemeColorization.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.enableThemeColorization3_1.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization3_1.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))
        window.enableThemeColorization3_1.setItemText(Settings.EnableThemeColorization.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.enableThemeColorization3_2.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization3_2.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))

        window.enableThemeColorization3_3.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization3_3.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))

        window.enableThemeColorization3_4.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization3_4.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))

        window.enableThemeColorization3_5.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization3_5.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))

        window.enableThemeColorization4.setItemText(Settings.EnableThemeColorization.No, _translate(Key.Value.Bool.no))
        window.enableThemeColorization4.setItemText(Settings.EnableThemeColorization.Yes, _translate(Key.Value.Bool.yes))
        window.enableThemeColorization4.setItemText(Settings.EnableThemeColorization.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # Disabled
        window.disabledEffect1.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect1.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))

        window.disabledEffect2.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect2.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))
        window.disabledEffect2.setItemText(Settings.Disabled.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.disabledEffect3_1.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect3_1.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))
        window.disabledEffect3_1.setItemText(Settings.Disabled.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        window.disabledEffect3_2.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect3_2.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))

        window.disabledEffect3_3.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect3_3.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))

        window.disabledEffect3_4.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect3_4.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))

        window.disabledEffect3_5.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect3_5.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))

        window.disabledEffect4.setItemText(Settings.Disabled.No, _translate(Key.Value.Bool.no))
        window.disabledEffect4.setItemText(Settings.Disabled.Yes, _translate(Key.Value.Bool.yes))
        window.disabledEffect4.setItemText(Settings.Disabled.UseGlobalSetting, _translate(Key.Value.useGlobalSetting))

        # Menu Exclusive
        window.noSystemDropShadow.setItemText(Settings.NoSystemDropShadow.No, _translate(Key.Value.Bool.no))
        window.noSystemDropShadow.setItemText(Settings.NoSystemDropShadow.Yes, _translate(Key.Value.Bool.yes))

        window.enableImmersiveStyle.setItemText(Settings.EnableImmersiveStyle.No, _translate(Key.Value.Bool.no))
        window.enableImmersiveStyle.setItemText(Settings.EnableImmersiveStyle.Yes, _translate(Key.Value.Bool.yes))

        window.enableCustomRendering.setItemText(Settings.EnableCustomRendering.No, _translate(Key.Value.Bool.no))
        window.enableCustomRendering.setItemText(Settings.EnableCustomRendering.Yes, _translate(Key.Value.Bool.yes))

        window.enableFluentAnimation.setItemText(Settings.EnableFluentAnimation.No, _translate(Key.Value.Bool.no))
        window.enableFluentAnimation.setItemText(Settings.EnableFluentAnimation.Yes, _translate(Key.Value.Bool.yes))

        window.noModernAppBackgroundColor.setItemText(Settings.NoModernAppBackgroundColor.No, _translate(Key.Value.Bool.no))
        window.noModernAppBackgroundColor.setItemText(Settings.NoModernAppBackgroundColor.Yes, _translate(Key.Value.Bool.yes))

        window.popInStyle.setItemText(Settings.PopInStyle.SlideDown, _translate(Key.Value.PopInStyle.slideDown))
        window.popInStyle.setItemText(Settings.PopInStyle.Ripple, _translate(Key.Value.PopInStyle.ripple))
        window.popInStyle.setItemText(Settings.PopInStyle.SmoothScroll, _translate(Key.Value.PopInStyle.smoothScroll))
        window.popInStyle.setItemText(Settings.PopInStyle.SmoothZoom, _translate(Key.Value.PopInStyle.smoothZoom))

        window.enableImmediateInterupting.setItemText(Settings.EnableImmediateInterupting.No, _translate(Key.Value.Bool.no))
        window.enableImmediateInterupting.setItemText(Settings.EnableImmediateInterupting.Yes, _translate(Key.Value.Bool.yes))

        # Others
        # Connectors.connectMouseEvent(window)
        window.appliedWidget.applied_text.setText(_translate(Key.changesApplied))
        window.appliedWidget.ok_button.setText(_translate(Key.ok))
        ColorPicker.vColorPicker.ui.window_title.setText(_translate("Color Picker"))
        ColorPicker.vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).setText(_translate("OK"))
        ColorPicker.vColorPicker.ui.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).setText(_translate("Cancel"))

        # Settings
        window.settingsHeading.setText(_translate(Key.Settings.settingsHeading))
        window.toolBox.setItemText(0, _translate(Key.Settings.ToolBox.general))
        window.toolBox.setItemText(1, _translate(Key.Settings.ToolBox.appearance))
        window.toolBox.setItemText(2, _translate(Key.Settings.ToolBox.internalFunctions))
        window.toolBox.setItemText(3, _translate(Key.Settings.ToolBox.externalFunctions))
        window.lbl_general_1.setText(_translate(Key.Settings.General.chooseLangauge))
        window.lbl_general_2.setText(_translate(Key.Settings.General.installationLocation))
        window.location_error_text.setText(_translate(Key.Settings.locationError))
        window.chooseButton.setText(_translate(Key.Settings.General.chooseFolders))
        window.saveButton.setText(_translate(Key.save))
        window.lbl_appearance_1.setText(_translate(Key.Settings.Appearance.manual))
        window.lbl_appearance_2.setText(_translate(Key.Settings.Appearance.presets))
        window.lbl_background_color.setText(_translate(Key.Settings.Appearance.backgroundColor))
        window.lbl_secondary_background_color.setText(_translate(Key.Settings.Appearance.secondaryBackgroundColor))
        window.lbl_label_color.setText(_translate(Key.Settings.Appearance.labelColor))
        window.lbl_text_color.setText(_translate(Key.Settings.Appearance.textColor))
        window.lbl_icon_color_mode.setText(_translate(Key.Settings.Appearance.iconColorMode))
        window.iconColorMode.setItemText(0, _translate(Key.Settings.Appearance.IconColorMode.lightMode))
        window.iconColorMode.setItemText(1, _translate(Key.Settings.Appearance.IconColorMode.darkMode))
        window.lbl_preset.setText(_translate(Key.Settings.Appearance.selectPreset))
        window.saveButton_2.setText(_translate(Key.save))
        window.installButton.setText(_translate(Key.Settings.InternalFunctions.install))
        window.uninstallButton.setText(_translate(Key.Settings.InternalFunctions.uninstall))
        window.runButton.setText(_translate(Key.Settings.InternalFunctions.run))
        window.stopButton.setText(_translate(Key.Settings.InternalFunctions.stop))
        window.location_note.setText(_translate(Key.Settings.InternalFunctions.locationNote))
        window.download_note.setText(_translate(Key.Settings.ExternalFunctions.downloadNote))
        window.downloadButton.setText(_translate(Key.Settings.ExternalFunctions.downloadAndInstall))
