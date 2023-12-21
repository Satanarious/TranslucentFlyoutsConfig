<img src="../Screenshots/banner.png">
<p align=center>
<img src="https://img.shields.io/github/v/release/Satanarious/TransparentFlyoutsConfig?include_prereleases">
<img src="https://img.shields.io/github/downloads/Satanarious/TransparentFlyoutsConfig/total?color=pink">
<img src="https://img.shields.io/github/issues/Satanarious/TransparentFlyoutsConfig?color=green">
<img src="https://img.shields.io/github/issues-closed/Satanarious/TransparentFlyoutsConfig?color=purple">
<img src="https://img.shields.io/badge/Python-v3.10.11-yellow">
<img src="https://img.shields.io/badge/OS-Windows_10+-skyblue">
</p>
<img src="../Screenshots/language_and_description_spread.png" align="right" width=550>

> This translation is contributed by [zzqzzqzzq2002](https://www.github.com/zzqzzqzzq2002)

**半透明浮出控件配置(Translucent Flyouts Config) GUI** 是适用于 Windows 10/11 平台[半透明浮出控件](https://github.com/ALTaleX531/TranslucentFlyouts)(Translucent Flyouts, 一种用于对系统中 win32 样式上下文菜单等各种控件进行自定义的软件) 的配套 GUI 应用程序.

### 其他语言

- [English](../README.md)

目录:

- [安装方式](#安装方式)
- [使用说明](#使用说明)
- [贡献其他语言的翻译](#贡献其他语言的翻译)
- [计划实现的特性](#计划实现的特性)
- [依赖项](#依赖项)
- [声明](#声明)
- [许可证信息](#许可证信息)

## 安装方式

### 1. 一步到位的一键安装 (★ 推荐! )

> 提示：对于旧的 半透明浮出控件(Translucent Flyouts) 用户, 请卸载手动安装的 半透明浮出控件(Translucent Flyouts) 版本, 然后按照基本步骤操作.

<img src="../Screenshots/all_tabs_spread.png" align="right" width=500 alt="img1">

- 下载[最新发行版](https://github.com/Satanarious/TransparentFlyoutsConfigGUI/releases/latest).
- 解压所有文件到你想安装的文件夹.
- 运行 `TranslucentFlyoutsConfig.exe` 这个可执行文件.
- 点击进入右上角的设置.
- 移动到最下面的 外部功能 , 点击 `下载并安装` 按钮.

### 2. 手动安装

> 已经默认了你安装了最新版本的 [半透明浮出控件(Translucent Flyouts)](https://github.com/ALTaleX531/TranslucentFlyouts/releases/latest) Installed.

- 下载[最新发行版](https://github.com/Satanarious/TransparentFlyoutsConfigGUI/releases/latest).
- 解压所有文件到你想安装的文件夹.
- 运行 `TranslucentFlyoutsConfig.exe` 这个可执行文件.
- 点击进入右上角的设置. (到这一步位置都和上面一键安装一样)
- 在 总体配置 下方的 安装位置 中填入 半透明浮出控件(Translucent Flyouts) 的根目录路径, 然后点下面的 保存 .

## 使用说明

- 左键单击任何设置最右侧的 重置按钮 可将值重置为其默认值.
- 右键单击任何设置最右侧的 重置按钮 可将值还原回为上次保存的值.
- 颜色选择器 用于选择包括 alpha（不透明度）值的颜色.
- 单击任何参数的 标签 即可查看可用值及其描述.
- 按相应部分中的 "应用" 或 "保存" 按钮后, 任何更改都会立即生效.
- 在 "设置" 部分中:
  - 界面语言 用于选择本程序的语言.
  - 界面外观 可以通过选择相应配置项来更改应用程序主题, 也可以使用下方的预设来快速切换主题.
  - 内部功能 包括对功能的 激活、停止、安装和卸载等.
  - 外部功能 中的按钮用来一步到位地一键安装 半透明浮出控件(Translucent Flyouts).

## 贡献其他语言的翻译

如果您有信心为此项目做出贡献, 可以选择您熟练的语言.在此之前您可能想看看 [这个](Translations/hi-in.json)(印地语, hi-in.json) 或者 [这个](Translations/zh-cn.json)(简体中文, zh-cn.json)<font color=Grey size=1>(<-来自简体中文译者的广告)</font> 的翻译文件.

首次贡献者请使用以下步骤：

- 分支(fork) 本存储库.
- 按照约定的名称 "LanguageCode-CountryCode.json" 在 [Translations 目录](Translations/) 中创建一个文件, 全部小写.
- 复制 [hi-in.json](Translations/hi-in.json) 中的所有内容并将其粘贴到新文件中.
- 删除每个英语项的印地语翻译, 并替换为您将翻译的语言.

> 注意：有些翻译中一行以 `<code>` 结尾, 另一行以 `</code>`, 请特别注意并在翻译中保持这种形式, 否则会破坏代码.
> 这是一些示例:
>
> - `"Uses the corresponding value in the global tab as the <code>"`
> - `"</code> value."`

如果您想更进一步编辑 python 源文件以完成在程序中对语言文件的添加, 不妨遵循以下步骤：

- 打开 [Data/enum.py](Data/enums.py) 并在 ` Languages` 类中增加额外的值.
- 打开 [Data/paths.py](Data/paths.py) 并在 `Translations` 类的下方添加翻译文件的路径, 变量名要求与前面提到的语言完全相同.
- 打开 [Data/translations.py](Data/translations.py) 并在 `TranslationModel` 类的 `_fetch()` 方法中找到 字典 `translationPath` , 随后按照 `LanguageEnum:LanguageJSONPathVariable` 的格式添加一个键值对.
- 最后打开 [main.py](main.py) 并找到 `__init__` 方法, 在 `self.language` 这个字符串列表中按照顺序加入你所翻译的语言的名字, 这个名字是供用户选取语言时使用的.

> 注 1：如果你只想完成第一部分, 我也会接受推送请求(PR, Push request) 并自己完成第二部分. 但若你也完成了第二部分我(指原作者)将不胜感激.

> 注 2：我将保留当前字体不支持的语言的字体, 并将于未来添加更多字体.

## 计划实现的特性

查看 [跟踪器](https://github.com/users/Satanarious/projects/2/views/2) 以获取更多详细信息.

<img src="../Screenshots/theme_tease.png" align=right width=50%>

- [x] 多语言翻译支持.
- [x] 更好的参数说明.
- [x] 应用内主题支持.
- [x] 半透明浮出控件(Translucent Flyouts) 内部功能支持：
  - [x] 重启
  - [x] 停止
  - [x] 安装
  - [x] 卸载
- [x] 下载最新版本 半透明浮出控件(Translucent Flyouts) 的按钮.
- [ ] 更新到 半透明浮出控件(Translucent Flyouts) 最新版本的按钮.
- [ ] 添加支持语言的字体.
- [ ] 用户界面动画.
- [ ] 用于即时预览更改的预览窗格.
- [ ] 发布到 Microsoft Store 和或 Winget.

## 依赖项

### [半透明浮出控件(Translucent Flyouts)](https://github.com/ALTaleX531/TranslucentFlyouts)

该应用程序可以使 Windows 10/11 上的大多数 win32 弹出菜单于控件变得半透明/透明, 同时提供许多其他的选项用于细节调整以满足您的个性化需求.

### [PyQT6](https://www.riverbankcomputing.com/software/pyqt/)

PyQt 是 Qt 公司 Qt 应用程序框架的一套 Python 封装, 可在 Qt 支持的所有平台上运行, 包括 Windows、macOS、Linux、iOS 和 Android. 可以在 [此处](https://doc.qt.io/qtforpython-6/) 找到文档.

### [PyInstaller](https://pyinstaller.org/en/stable/)

PyInstaller 将 Python 应用程序及其所有依赖项捆绑到一个包中.用户无需安装 Python 解释器或任何模块即可运行打包的应用程序. PyInstaller 支持 Python 3.7 及更高版本, 并正确集成许多主要的 Python 包, 例如 numpy、matplotlib、PyQt、wxPython 等.

### [VColorPicker](https://github.com/nlfmt/pyqt-colorpicker)

VColorPicker 是一个简单的颜色选择器, 具有基于 Qt 创建的现代 UI, 可以轻松获取用户的颜色输入.

### Winrar

项目中使用的 Unrar.exe 取自 Winrar, 用于解压从 半透明浮出控件(Translucent Flyouts)下载 的文件.

### [由 Freepik - Flaticon 提供的勾号图标](https://www.flaticon.com/free-icons/tick)

应用程序中包含的在用户单击 "应用" 按钮时出现勾号图标, 该图标由 Freepik - Flaticon 设计.

## 声明

该应用程序包含有关配置上下文菜单与控件外观所需了解的所有内容, 从而使用户无需参考前面提到的配置文件.

> 注意：此应用程序仅用作 GUI, 以代替前面提到应用配置中所需的任何注册表编辑过程, 而不是一个独立的应用程序, 需要与 [半透明浮出控件(Translucent Flyouts)](https://github.com/ALTaleX531/TranslucentFlyouts) 一起使用.

[配置文件](https://github.com/ALTaleX531/TranslucentFlyouts/blob/master/CONFIG.md) 提供了配置 win32 样式上下文菜单与控件所需的各种描述和方法.由于 Windows 10 上缺少 云母材质(Mica)等, 因此某些功能仅适用于 Windows 11.

## 许可证信息

该软件使用 GNU GPL v3.0 许可证进行许可.

更多信息请查看 [许可证](https://github.com/Satanarious/TransparentFlyoutsConfig/blob/master/LICENSE) 文件.

> 中文译者注: 本翻译文件仅用于参考，请以英文原版 [说明文件](./README.md) 为准.
> 2023.12.18
