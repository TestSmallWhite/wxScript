# -*- coding:utf-8 -*-

"""
执行 run 之前需要在 config.py 配置 url、分类关键词
"""

# 分类网址
FEEDBACK_URL = ""

# webdrvier 存放位置
CHROME_PATH = r""

# query list
QUERY_LIST = [
    ["担心泄露隐私", "隐私", "私隐", "不想别人看到", "隱私", "稳私", "泄露信息", "瘾私", "不能让人看到",
     "不想被看到", "私密", "透露信息",  "给人知道信息", "暴露个人信息", "不想让别人看到", "不想让全部人员看到",
     "感觉被人监视", "别人看到我阅读", "不让别人看", "不想分享给", "不想被别人看", "不让朋友看到",
     "不想被任何人知道", "不想让我全部好友看", "不展示我在看", "不展示我的在看"],
    ["色情低俗", "色情", "低俗", "黄片", "淫秽", "涉黄", "黄色视频", "黄色文章"],
    ["标题党", "标题党", "文不对题", "张冠李戴", "标题与内容不符", "雷人标题"],
    ["传销诈骗", "传销", "古币", "钱币", "诈骗"],
    ["宗教反馈", "穆斯林", "基督"],
    ["推股荐股", "推荐股票"],
    ["视频无法播放", "视频打不开", "不能播放", "视频异常", "无法播放", "视频不能看", "视频播放异常"],
    ["视频卡顿", "视频无响应", "视频卡"],
    ["看一看入口找不到", "找不到入口", "没有看一看", "看一看找不到", "没有入口", "找不到看一看", "没有找到入口", "看一看没有", "没有“看一看”",
     "没有‘看一看’", "没有\"看一看\"", "没有\'看一看\'"],
    ["欧盟用户找不到入口", "发现页管理", "发现管理页"],
    ["看一看白屏", "看一看白屏", "白屏", "什么都不显示", "刷新后无内容", "不显示内容", "没有任何显示"],
    ["看一看打不开", "看一看打不开", "打不开"],
    ["新增功能反馈", "不要红点", "全选好友", "浏览历史", "瀏覽歷史", "一键屏蔽", "全部选择", "一键添加好友",
     "一键添加全部", "历史浏览记录", "全选按钮", "全选选项"],
    ["看一看闪退", "闪退", "重启"],
    ["看一看黑屏", "黑屏"],
    ["图片加载不出", "图片打不开", "图片加载不了"],
    ["内容质量差", "文章质量垃圾", "文理不通", "乱七八糟", "内容质量太差", "内容粗糙", "内容质量不", "内容太垃圾"
     ],
    ["红点消不了", "红点消不了"],
    ["认为看一看占内存", "占内存", "占空间", "占用空间"],
    ["文章打不开", "文章打不开"],
    ["虚假信息", "虚假", "骗人", "内容不真实", "假内容", "胡说八道", "瞎编乱造"],
    ["视频黑屏", "视频黑屏"],
    ["想关闭看一看", "关闭看一看", "关掉看一看", "不想要这个功能", "不想使用该功能", "不想用该功能", "想关闭这个",
     "取消看一看", "想关闭该功能", "不想要这功能"]
]