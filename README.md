# stockreport
通过触发抓取东方财富最新研报并发送到指定邮箱。

## 配置
配置DailyReport.py内21，22，23行发送邮箱信息；
配置25行指定的receivers邮箱；
直接执行py文件。

## 使用场景
配置stock.bat内的路径和run.vbs的指向，将run.vbs放置于Windows的自启动文件夹路径：
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp；
脚本将会自动在开启时执行。
