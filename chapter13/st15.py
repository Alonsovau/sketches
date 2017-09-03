# 启动一个web浏览器
import webbrowser


webbrowser.open('http://www.python.org')
webbrowser.open_new_tab('http://www.python.org')


c = webbrowser.get('safari')
c.open('http://docs.python.org')
