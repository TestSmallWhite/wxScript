# -*- coding:utf-8 -*-

"""
执行 run 之前需要在 config.py 配置 url、分类关键词
"""

# 分类网址
FEEDBACK_URL = ""

# webdrvier 存放位置
CHROME_PATH = r""

# 关键词list
# 担心泄露隐私
PRIVACY = ["隐私", "私隐", "不想别人看", "隱私", "稳私", "泄露", "瘾私" ]

# 关闭看一看
CLOSE_LOOK_ON_LOOK = ["关闭", "关掉", "不想要这个功能"]

# 色情低俗
SEXY = ["色情", "低俗"]

# 标题党
TITLE = ["标题党", "文不对题", "张冠李戴", "标题与内容不符", "雷人标题", "广告"]

# 传销诈骗
PYRAMID_SALES_SWINDLE = ["传销", "古币", "钱币", "诈骗"]

# 宗教反馈
RELIGION = ["穆斯林", "基督"]

# 推股荐股
RECOMMEND_STOCK = ["推荐股票"]

# 视频打不开
VIDEO_CANNOT_PLAY = ["视频打不开", "不能播放", "视频异常", "无法播放"]

# 视频卡顿
VIDEO_CATON = ["视频无响应", "视频卡"]

# 找不到入口，在 run 中会根据 os、os version 判断是海外用户或国内用户
NOT_FOUND_ENTRY = ["找不到入口", "没有看一看", "看一看找不到", "没有入口", "找不到看一看", "没有找到入口", "看一看没有", "没有“看一看”", "没有‘看一看’", "没有\"看一看\""
    , "没有\'看一看\'"]

# 发现页管理找不到看一看的入口，用户一般为欧盟的年轻用户
MANAGE_DISCOVER = ["发现页管理", "发现管理页"]

# 看一看白屏
LOOK_ONE_LOOK_WHITE_SCREEN = ["看一看白屏", "白屏", "什么都不显示", "刷新后无内容", "不显示内容"]

# 看一看打不开
LOOK_ONE_LOOK_CANNOT_OPEN = ["看一看打不开"]

# 新增功能反馈
ADD_NEW_FUNCTIO = ["红点", "全选", "浏览历史", "瀏覽歷史", "一键屏蔽", "建议", "希望"]

# 看一看闪退
LOOK_ONE_LOOK_CRASH = ["闪退", "重启"]

# 看一看黑屏
LOOK_ONE_LOOK_BLACK_SCREEN = ["黑屏"]

# 图片加载不出
PICTUERS_CANNOT_LOAD = ["图片打不开", "图片加载不了"]

# 内容质量差
POOR_CONTENT_QUALITY = ["质量", "垃圾", "文理不通", "乱七八糟"]

# 红点消不了
RED_DOT_CANNOT_CANCEL = ["红点消不了"]

# 字体反馈
FONT_FEEDBACK = ["文字", "字体"]

# 认为看一看占内存
OCCUPY_MEMORY = ["占内存", "占空间"]

# 文章打不开
ARTICLES_CANNOT_OPEN = ["文章打不开"]

# 虚假信息
FALSE_INFORMATION = ["虚假", "骗人"]

# 视频黑屏
VIDEO_BLACK_SCREEN = ["视频黑屏"]