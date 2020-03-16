#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import datetime
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import config


# 声明一个跳出循环类，遇到就跳出循环
class BreakFor(Exception):
    pass


class Category(object):
    def __init__(self):
        # 声明一些变量
        # 脚本开始执行时间
        self.now_tiem = time.time()

        # 反馈页数
        self.feedback_pages = 0

        # 反馈总数
        self.feedback_count = 0

        # 分类反馈数量
        self.category_feedback_count = 0

    # 遍历 query，和反馈内容进行匹配
    def match_query(self, feedback_num, feedback_content):
        for query_list in config.QUERY_LIST:
            # 由于每个list的第一个是二级分类，所以要从索引 1 开始判断
            for num in range(1, len(query_list)):
                # 判断 query 是否在反馈内容中
                if query_list[num] in feedback_content:
                    # 如果是看一看找不到，需要判断是国内用户还是欧盟用户，这里优先处理入口找不到的反馈
                    if query_list[0] == "找不到入口":
                        self.category_feedback_count = self.category_feedback_count + 1

                        os_con = self.driver.find_element_by_xpath(
                            '//*[@id="feedTable"]/tbody/tr[' + str(feedback_num) + ']/td[3]')

                        if os_con.text[0] == "a":
                            os = os_con.text.split("-")

                            if int(os[1]) >= 27:
                                # 点击“编辑”按钮
                                self.edit_or_save.click()
                                self.driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                # 点击“保存”按钮
                                self.edit_or_save.click()
                            else:
                                self.edit_or_save.click()
                                self.driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                self.edit_or_save.click()
                            raise BreakFor
                        elif os_con.text[0] == "i":
                            if os_con.text[1] == "O":
                                os = os_con.text.split(" ")
                                try:
                                    os_version = os[1].split(".")[0]
                                except IndexError:
                                    continue
                                if int(os_version) >= 12:
                                    self.edit_or_save.click()
                                    self.driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                    self.edit_or_save.click()
                                else:
                                    self.edit_or_save.click()
                                    self.driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                    self.edit_or_save.click()
                            elif os_con.text[1] == "P":
                                os = os_con.text.split(" ")

                                try:
                                    os_version = os[2].split(".")[0]
                                except IndexError:
                                    raise KeyError

                                if int(os_version) >= 12:
                                    self.edit_or_save.click()
                                    self.driver.find_element_by_id("mySelect").send_keys("欧盟用户找不到入口")
                                    self.edit_or_save.click()
                                else:
                                    self.edit_or_save.click()
                                    self.driver.find_element_by_id("mySelect").send_keys("看一看入口找不到")
                                    self.edit_or_save.click()
                            raise BreakFor
                    else:
                        self.category_feedback_count = self.category_feedback_count + 1

                        # 点击“编辑”按钮
                        self.edit_or_save.click()

                        # 给选择框填入文本
                        self.driver.find_element_by_id("mySelect").send_keys(query_list[0])

                        # 点击“保存”按钮
                        self.edit_or_save.click()

                        # 跳出循环
                        raise BreakFor

    # 比较日期大小
    def comparing_date(self, time_a, time_b):
        test_start_date = datetime.datetime.strptime(time_a, "%Y-%m-%d")
        test_end_date = datetime.datetime.strptime(time_b, "%Y-%m-%d")

        return test_start_date > test_end_date

    # 脚本启动
    def start(self, start_date=None, end_date=None):
        # 先判断下时间
        if start_date and end_date:
            # 结束时间不能比开始时间小
            if self.comparing_date(start_date, end_date):
                raise Exception("结束时间不能比开始时间小")

            # 添加上00
            start_date = "00" + start_date
            end_date = "00" + end_date
        elif start_date and end_date == None:
            end_date = str(datetime.datetime.now().date())

            # 结束时间不能比开始时间小
            if self.comparing_date(start_date, end_date):
                raise Exception("结束时间不能比开始时间小")

            # 添加上00
            start_date = "00" + start_date
            end_date = "00" + end_date
        elif start_date == None and end_date:
            start_date = str(datetime.datetime.now().date())

            # 结束时间不能比开始时间小
            if self.comparing_date(start_date, end_date):
                raise Exception("结束时间不能比开始时间小")

            # 添加上00
            start_date = "00" + start_date
            end_date = "00" + end_date
        else:
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

        # 获取 webdriver 对象
        self.driver = webdriver.Chrome(config.CHROME_PATH)

        # 最大化浏览器
        self.driver.maximize_window()

        # 加载网址
        self.driver.get(config.FEEDBACK_URL)

        # 隐式等待 10 秒
        self.driver.implicitly_wait(10)

        # 找到开始/结束日期控件
        start_date_element = self.driver.find_element_by_id("start_date")
        end_date_element = self.driver.find_element_by_id("end_date")

        # 因为控件有 readonly 属性，虽然引用了 jquery 库，但是为了保险，使用 js 去掉 readonly 属性
        start_date_element_remove_readonly_attribute = "document.getElementById('start_date').removeAttribute('readonly')"
        end_date_element_remove_readonly_attribute = "document.getElementById('end_date').removeAttribute('readonly')"

        # 执行 js 语句
        self.driver.execute_script(start_date_element_remove_readonly_attribute)
        self.driver.execute_script(end_date_element_remove_readonly_attribute)

        # 填入时间
        start_date_element.send_keys(start_date)
        end_date_element.send_keys(end_date)

        # 选择100条记录
        self.driver.find_element_by_name("feedTable_length").send_keys("100")

        # 点击提交过滤按钮
        self.driver.find_element_by_id("filter_feeds_button").click()

        # 由于网络的问题，导致这里取到都是0，等三秒吧
        time.sleep(3)
        # 获取反馈总数
        self.feedback_count = re.findall(r'[0-9]\d*', self.driver.find_element_by_id("feedTable_info").text)[2]

        """
        1.通过 xpath 找到页数，用页数控制循环次数
        2.每页循环100次，使用 xpath 找到每条反馈的内容，和 config 的 list 对比
        3.如果最后一页提示找不到 element 表示结束了，应该跳出循环
        """
        self.feedback_pages = self.driver.find_elements_by_xpath('//*[@id="feedTable_paginate"]/span/a')[-1]

        for page in range(1, int(self.feedback_pages.text) + 1):
            print("第 %d 页开始分类" % (page))

            # 循环 100 次。最后一页可能不够100条，所以要try except 兼容
            # 循环要从1开始，到100结束
            try:
                # 当循环到101次，表示100次分完了，这时会报错indexerror，要记得处理
                for feedback_num in range(1, 102):
                    feedback_content = self.driver.find_element_by_xpath(
                        '//*[@id="feedTable"]/tbody/tr[' + str(feedback_num) + ']/td[6]').text
                    self.edit_or_save = self.driver.find_element_by_xpath(
                        '//*[@id="feedTable"]/tbody/tr[' + str(feedback_num) + ']/td[8]/div/button')

                    try:
                        self.match_query(feedback_num, feedback_content)
                    except BreakFor:
                        continue
            except NoSuchElementException:
                print("第 %d 页结束分类" % (page))

            # 点击下一页
            self.driver.find_element_by_id("feedTable_next").click()

        print("分类结束")

        print("共有 %s 条反馈，已分类 %d 条反馈，未分类 %d 条反馈" % (
            self.feedback_count, self.category_feedback_count, int(self.feedback_count) - self.category_feedback_count))
        print("执行时间： %s 秒" % (int(time.time() - self.now_tiem)))
        self.driver.close()


if __name__ == '__main__':
    ca = Category()
    ca.start()
