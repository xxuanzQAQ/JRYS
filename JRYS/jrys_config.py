from typing import Dict

from gsuid_core.utils.plugins_config.models import GSC, GsStrConfig
from gsuid_core.utils.plugins_config.gs_config import StringConfig

from .utils.resource.RESOURCE_PATH import CONFIG_PATH

CONFIG_DEFAULT: Dict[str, GSC] = {
    "BotName": GsStrConfig(
        "机器人名称",
        "显示在运势建议框左侧的机器人名称，例如「小岸」",
        "小岸",
    ),
    "BgImagePath": GsStrConfig(
        "自定义背景图目录",
        "自定义背景图片所在目录的绝对路径，留空则使用默认目录（支持子目录递归搜索）",
        "",
    ),
}

JRYSConfig = StringConfig(
    "JRYS",
    CONFIG_PATH,
    CONFIG_DEFAULT,
)
