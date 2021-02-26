# UI 设计

## Web 端

- 简单
- 简洁

## 客户端 GUI

- 可以使用 Qt Designer 设计
  - 但是要注意: 改变窗口大小时, 控件的布局变化是否合理 (不要全部绝对定位布局导致拉宽/拉长窗口出现大片空白,控件全在最左边!)

- 设计简单且简洁
- 用 Qt Designer 设计完成后, 将用 pyuic 生成的 python 文件放入 src/app/base_ui
- 在 src/app/ui 下新建名称一致(不是相同)的 python 文件, 创建一个继承自 base_ui 里自动生成的窗体类的子类
  - 在子类中做修改, 不要修改 base_ui 下的源文件
  - 这样子可以再去修改 Qt Designer 的设计而自己在 python 源码上做的修改不丢失
  - (可以仿照 setupUi 函数来创建一个 setupAdditionalUi 函数, 在初始化窗口时调用)
- 没有用 Qt Designer 设计, 直接用 python 编写的窗口代码放在 src/app/ui 下

