# cc98爬虫
## 功能

能够爬取cc98(2024年的cc98网站)的某一版面的全部帖子，保存到excel文档中。

## 使用

直接运行main.py即可运行。

命令行中输入```python main.py```。

## 一些常见问题

1. Authorization错误:常出现```json.decoder.JSONDecodeError```问题，说明大概是Authorization过期，可以打开浏览器F12，选择网络FETCH/XHR，打开任意帖子后查看topic包即可看到
  
   ![image](https://github.com/AKonjac0/spider_cc98/assets/110406952/7a7b5804-2869-4aeb-8c86-c12bad749dac)

~~一般而言不会出现这个问题，如果出现了就得改一下~~

~~或许以后会写一个自动获取Authorization的代码传上来~~

2.  版面编号为网址中的```board/```后的数字。常见版面编号：
```c
学习天地：68
心灵之约：182
缘分天空：152
```

## 其他

欢迎star,也欢迎在问题区提出其他改进/问题。

~~我应该会尽量改，虽然我很懒~~
