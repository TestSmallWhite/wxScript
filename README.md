# wxScript
# 注意事项
1. 该脚本只能在腾讯内网使用！
2. 需要将“demo_config.py”重命名为“config.py”

需要在“config.py”文件中配置 URL、CHROME_PATH

默认会判断当天星期几：
  如果是星期一，分类开始日期是上周五
  如果是非星期一，分类开始日期是昨天
分类结束日期默认是当天

如果想指定日期，请在这里取消注释
# start_date = "00YYYY-mm-dd"   # "002020-02-13"
# end_date = "00YYYY-mm-dd"     # "002020-02-13"

# 如果想增加关键词：
  1. 直接在原有的 list 上加上query
  2. 增加一个新的 list，如果新增 list，需要手动增加一个for循环，记住要对其代码
                    for query in config.PRIVACY:  # 这里需要修改 list 的名字，例如“PRIVACY”
                    # 判断 query 是否在反馈内容中
                    if query in feedback_content:
                        category_feedback_count = category_feedback_count + 1

                        # 点击“编辑”按钮
                        edit_or_save.click()

                        # 给选择框填入文本
                        driver.find_element_by_id("mySelect").send_keys("担心泄露隐私") # 这里需要修改二级分类，例如“担心泄露隐私”

                        # 点击“保存”按钮
                        edit_or_save.click()

                        # 跳出循环
                        raise BreakFor
