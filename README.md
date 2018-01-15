# answerHelper
百万英雄、冲顶大会答题帮手

原理：adb 截取手机界面，获取题目文字，搜索指定的搜索引擎获取答案，展现 

## IOS/Android 上 WebDriverAgent的安装

参考 ：https://www.leon0204.com/article/95.html

- 本机环境 Mac 10.13.2 | Python 3.6.4 

-  整个程序运行完大概2-3 s 左右 


-  pip3 模块： baidu-aip  lxml  Pillow  requests bs4 wda

# 使用方法：
1 ADB连接 ios 真机之后，开启 iproxy 监听，执行 python 程序 。 2 需要去配置百度的api ，注册，获取 APP_ID，API_KEY，SECRET_KEY ，填写在 answer.py 的 配置代码中。

 ```python3  answer.py  1 ```
 
 
 运行效果
 
 
 ![运行效果](https://www.leon0204.com/img/github/answerHelper1.png)

 截图
 
 
 ![运行效果](https://www.leon0204.com/img/github/answerHelper2.png)
 
 题目文字部分图片
 
 
 ![运行效果](https://www.leon0204.com/img/github/answerHelper3.png)
 
 
 实际运行效果感受：
 50% 成功率吧，受查询题目限制，比如数学类题目就基本查不到答案，时间上比较紧张 ，参考了其他的插件和辅助程序，比如搜狗推出的答题插件，实际使用中发现还不如自己的用的舒服。答题还是靠运气，多喊上几个好朋友一起，成功率更大。


欢迎 PR 交流讨论

   
