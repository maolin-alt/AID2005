"""
http 请求响应演示
"""

from socket import *

# 创建tcp套接字
s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Connect from", addr)  # 浏览器连接
    data = c.recv(4096)  # 接收的是http请求
    print(data.decode().split('\n')[0])

    # 响应格式
    f = open('index.html')
    info = f.read()
    html = "HTTP/1.1 200 OK\r\n"
    html += 'Content-Type:text/html\r\n'
    html += '\r\n'
    html += f.read()

    c.send(html.encode())  # 发送响应给客户端
    f.close()
    c.close()
s.close()
