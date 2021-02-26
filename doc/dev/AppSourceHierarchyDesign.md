# 应用程序源码层次结构设计

## App

顶层包, 包含主程式`__main__.py`

### auth

认证模块, 用于处理用户登录

### base_ui & ui

UI  模块, 处理 UI 界面逻辑 , 更多UI界面设计内容参见[UIDesign.md](UIDesign.md)

### ipc

进程间通信模块, 其中 commander 用于向 worker 发送消息, data_bridge 用于接收 worker 的消息

### logic

程序功能逻辑

### settings

程序设置管理模块

### utils

杂项工具模块, 包含的工具例如: 

- singleton : 实现单例类
- gen_token :  生成32位 hex token

### constants

包含很多程序常量, 会被 `__init__.py` import

### pcsapp (Piculator Client Software Application)

全局单例APP类, 可以用来挂载一部分全局变量

这个类被实例化为 myapp, 可以从app 模块引入

### QRunner

主窗体启动函数