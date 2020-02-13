#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import datetime
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from feedback_Category import config

# 声明一个跳出循环类，遇到就跳出循环
class BreakFor(Exception):
    pass


# 声明一些变量
# 脚本开始执行时间
now_tiem = time.time()

# 反馈页数
feedback_pages = 0

# 反馈总数
feedback_count = 0

# 分类反馈数量
category_feedback_count = 0

# 获取 webdriver 对象
driver = webdriver.Chrome(config.CHROME_PATH)

# 最大化浏览器
driver.maximize_window()

# 加载网址
driver.get(config.FEEDBACK_URL)

# 隐式等待 10 秒
driver.implicitly_wait(10)

# 获取反馈总数
feedback_count = re.findall(r'[0-9]\d*', driver.find_element_by_id("feedTable_info").text)

# 找到开始/结束日期控件
start_date_element = driver.find_element_by_id("start_date")
end_date_element = driver.find_element_by_id("end_date")

# 因为控件有 readonly 属性，虽然引用了 jquery 库，但是为了保险，使用 js 去掉 readonly 属性
start_date_element_remove_readonly_attribute = "document.getElementById('start_date').removeAttribute('readonly')"
end_date_element_remove_readonly_attribute = "document.getElementById('end_date').removeAttribute('readonly')"

# 执行 js 语句
driver.execute_script(start_date_element_remove_readonly_attribute)
driver.execute_script(end_date_element_remove_readonly_attribute)

# 给时间控件输入日期
# 判断今天是否为星期一，如果是星期一，start_date_element 就是上星期五，否则就是昨天
# weekday() 返回的是int，星期一是0，星期天是6
today_week = datetime.datetime.now().weekday()   

# 如果是星期一，那么减3天
if today_week == 0:
    delta_three = datetime.timedelta(days=3)
    temp = datetime.datetime.now() - delta_three
    start_date = "00" + str(temp.date())
else:
    delta_one = datetime.timedelta(days=1)
    temp = datetime.datetime.now() - delta_one
    start_date = "00" + str(temp.date())

end_date = "00" + str(datetime.datetime.now().date())

# 如果想指定分类某端时间，可以覆盖 start_date, end_start，默认注释
# start_date = "00YYYY-mm-dd"   # "002020-02-13"
# end_date = "00YYYY-mm-dd"     # "002020-02-13"

# 填入时间
start_date_element.send_keys(start_date)
end_date_element.send_keys(end_date)



# 点击提交过滤按钮
driver.find_element_by_id("filter_feeds_button").click()

# 选择100条记录
driver.find_element_by_name("feedTable_length").send_keys("100")

"""
1.通过 xpath 找到页数，用页数控制循环次数
2.每页循环100次，使用 xpath 找到每条反馈的内容，和 config 的 list 对比
3.如果最后一页提示找不到 element 表示结束了，应该跳出循环
"""
feedback_pages = len(driver.find_elements_by_xpath('//*[@id="feedTable_paginate"]/span/a'))

for page in range(1, feedback_count + 1):
    print("当前 %d 页开始分类" %(page))

    # 循环 100 次。最后一页可能不够100条，所以要try except 兼容
    # 循环要从1开始，到100结束
    try:
        for y in range(1, 101):
            feedback_content = driver.find_element_by_xpath('//*[@id="feedTable"]/tbody/tr[' + str(y) + ']/td[6]').text
            edit_or_save = driver.find_element_by_xpath('//*[@id="feedTable"]/tbody/tr[' +str(y)+ ']/td[8]/div/button')

            try:
                for query in config.PRIVACY:
                    # 判断 query 是否在反馈内容中
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("担心泄露隐私")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.CLOSE_LOOK_ON_LOOK:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("关闭看一看")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.SEXY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("色情低俗")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.TITLE:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("标题党")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.PYRAMID_SALES_SWINDLE:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("传销诈骗")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.RELIGION:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("宗教反馈")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.RECOMMEND_STOCK:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("推股荐股")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.VIDEO_CANNOT_PLAY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("视频无法播放")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.VIDEO_CATON:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("视频卡顿")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.NOT_FOUND_ENTRY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        osCon = driver.find_element_by_xpath('//*[@id="feedTable"]/tbody/tr[' +str(y)+ ']/td[3]')

                        if osCon.text[0] == "a":
                            os = osCon.text.split("-")

                            if int(os[1]) >= 27:
                                # 点击“编辑”按钮
                                edit_or_save.click()
                                driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                # 点击“保存”按钮
                                edit_or_save.click()
                            else:
                                edit_or_save.click()
                                driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                edit_or_save.click()
                            raise BreakFor
                        elif osCon.text[0] == "i":
                            if osCon.text[1] == "O":
                                os = osCon.text.split(" ")
                                try:
                                    osVersion = os[1].split(".")[0]
                                except IndexError:
                                    continue
                                if int(osVersion) >= 12:
                                    edit_or_save.click()
                                    driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                    edit_or_save.click()
                                else:
                                    edit_or_save.click()
                                    driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                    edit_or_save.click()
                            elif osCon.text[1] == "P":
                                os = osCon.text.split(" ")

                                try:
                                    osVersion = os[2].split(".")[0]
                                except IndexError:
                                    raise KeyError

                                if int(osVersion) >= 12:
                                    edit_or_save.click()
                                    driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                    edit_or_save.click()
                                else:
                                    edit_or_save.click()
                                    driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                    edit_or_save.click()
                            raise BreakFor

                for query in config.MANAGE_DISCOVER:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.LOOK_ONE_LOOK_WHITE_SCREEN:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("看一看白屏")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.LOOK_ONE_LOOK_CANNOT_OPEN:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("看一看打不开")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.ADD_NEW_FUNCTIO:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("新增功能反馈")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.LOOK_ONE_LOOK_CRASH:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("看一看闪退")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.LOOK_ONE_LOOK_BLACK_SCREEN:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("看一看黑屏")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.PICTUERS_CANNOT_LOAD:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("图片加载不出")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.POOR_CONTENT_QUALITY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("内容质量差")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.RED_DOT_CANNOT_CANCEL:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("红点消不了")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.FONT_FEEDBACK:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("字体反馈")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.OCCUPY_MEMORY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("认为看一看占内存")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.ARTICLES_CANNOT_OPEN:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("文章打不开")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.FALSE_INFORMATION:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("虚假信息")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.VIDEO_BLACK_SCREEN:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("视频黑屏")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

                for query in config.SEXY:
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("色情低俗")

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor
            except BreakFor as e:
                continue
        print("当前 %d 页结束分类" % (page))
    except NoSuchElementException as e:
        print("当前 %d 页结束分类" % (page))
        # 表示分完了
        print("分类完毕")

    # 点击下一页
    driver.find_element_by_id("feedTable_next").click()

print("共有 %d 条反馈，已分类 %d 条反馈，未分类 %d 条反馈" %(feedback_count, category_feedback_count, feedback_count -
                                          category_feedback_count))
print("执行时间： %s 秒" %(int(time.time() - now_tiem)))
driver.close()