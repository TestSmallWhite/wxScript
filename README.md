# wxScript
# 注意事项
1. 该脚本只能在腾讯内网使用！
2. 需要在“config.py”文件中配置 URL、CHROME_PATH

# 默认会判断当天星期几
  * 如果是星期一，分类开始日期是上周五
  * 如果是非星期一，分类开始日期是昨天
  * 分类结束日期默认是当天

如果想指定日期，请在 run.py 下的 start() 输入日期
```python
if __name__ == '__main__':
    ca = Category()
    ca.start() # 默认为None
    ca.start("2020-02-15", "2020-02-16") # 第一个是开始日期，第二个是结束日期
```

# 增加关键词
1. 增加 query，需要在 config.py 上修改
1. 如果 query list 已存在，直接在原有的 list 上加上 query
2. 需要新增 query list，直接在末尾追加一个新 list 即可，新 list 第一位一定是二级分类的文本
  ```python
    # ......
    ["文章打不开", "文章打不开"],
    ["虚假信息", "虚假", "骗人"],
    ["视频黑屏", "视频黑屏"], # 注意要加上英文逗号“,”
    ["新增二级分类文本", "query 1", "query 2", "..."] # 新增 list
  ]
  ```
