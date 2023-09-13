# 通用工具连接器

from . import utils
from .i18n import I18n
from .shortcut import ShortcutApi

from PySide2.QtCore import QObject, Slot, Signal


class UtilsConnector(QObject):
    def __init__(self):
        super().__init__()

    # 将文本写入剪贴板
    @Slot(str)
    def copyText(self, text):
        utils.copyText(text)

    # 创建快捷方式
    @Slot(str, result=bool)
    def createShortcut(self, position):
        return ShortcutApi.createShortcut(position)

    # 删除快捷方式
    @Slot(str, result=int)
    def deleteShortcut(self, position):
        return ShortcutApi.deleteShortcut(position)

    # 获取UI语言信息
    @Slot(result="QVariant")
    def i18nGetInfos(self):
        return I18n.getInfos()

    # 获取设置UI语言
    @Slot(str, result=bool)
    def i18nSetLanguage(self, lang):
        return I18n.setLanguage(lang)