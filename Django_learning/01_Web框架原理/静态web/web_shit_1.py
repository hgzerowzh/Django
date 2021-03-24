import socket


def f1(request):
    # request中包含了用户请求的所有内容：请求头+请求体
    # 从一个html文件中读取内容，再将内容返回给客户端
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data

def f2(request):
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    return data

routers = [
    ('/f1', f1),
    ('/f2', f2),
]

def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        # 等待客户端来连接
        conn, addr = sock.accept()
        # 获取用户发送的数据，收到的数据是Bytes，(二进制格式)
        data = conn.recv(8096)


        """对用户发来的信息进行提取"""

        # 将内容转化成字符串类型
        data = str(data, encoding='utf-8')
        # data = bytes('shit', encoding='utf-8')

        # 将内容分割成请求头和请求体
        headers, bodys = data.split('\r\n\r\n')
        # 得到请求头中的每一行数据
        temp_list = headers.split('\r\n')
        # 对请求头中的第一行数据进行提取，取得请求方法、请求URL、请求方法
        method, url, protocol = temp_list[0].split(' ')

        """根据用户请求的URL来返回不同的内容"""
        """思路：
            遍历routers中的每个元组的第一个值和请求头中的url进行比较，
            若匹配成功，则将对应的函数名赋值给func_name，进而去执行该URL对应的函数
        """
        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break
        if func_name:
            response = func_name(data)  # 把data中的内容传进去
        else:
            response = b"404 not found"

        conn.send(response)
        conn.close()


if __name__ == '__main__':
        run()
