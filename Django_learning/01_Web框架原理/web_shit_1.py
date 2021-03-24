import socket
import pymysql

# 静态页面
def index(request):
    # request中包含了用户请求的所有内容：请求头+请求体
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data

# 静态页面
def article(request):
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    return data

# 动态页面，手动渲染
def user_info(request):

    # 连接数据库并取得数据
    mysql_conn = pymysql.connect(host='10.0.0.204', port=3306, user='hgzero', passwd='woshiniba', db='my_test')
    conn_cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
    ret = conn_cursor.execute("select name,age,gender from first_test")
    print("受影响的行数：%s" % ret)
    user_list = conn_cursor.fetchall()
    conn_cursor.close()
    mysql_conn.close()
    print("打印从数据库中拿到的内容: %s" % user_list)

    # 将从数据库中拿到的内容进行拼接
    content_list = []
    for row in user_list:
        tp = "<tr><th>%s</th><th>%s</th><th>%s</th></tr>" % (row["name"], row["age"], row["gender"])
        content_list.append(tp)
    user_content = "".join(content_list)

    # 将html文件中指定位置的内容替换成数据库中取得后拼接好的内容
    f = open("template_shit.html", "r", encoding='utf-8')
    html_template = f.read()
    f.close()

    # 替换为指定内容
    # 这里其实就是最简单的所谓的模板的渲染
    data = html_template.replace("@@content@@", user_content)

    return bytes(data, encoding="utf-8")

# 动态页面，用jinja2进行模板渲染
def template_shit(request):
    # 连接数据库并取得数据
    mysql_conn = pymysql.connect(host='10.0.0.204', port=3306, user='hgzero', passwd='woshiniba', db='my_test')
    conn_cursor = mysql_conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute("select name,age,gender from first_test")
    user_list = conn_cursor.fetchall()
    conn_cursor.close()
    mysql_conn.close()

    # 获取html模板的内容
    f = open("template_shit.html", "r", encoding='utf-8')
    html_data = f.read()
    f.close()

    # 用jinja2进行模板渲染
    from jinja2 import Template
    template = Template(html_data)
    # 用从数据库中拿到的user_list来替换模板中的user_list变量
    data = template.render(user_list=user_list)
    # 模板中定义的规则：
    """{% for rwo in user_list %}
                  <tr>
                      <td>{{row.name}}</td>
                      <td>{{row.age}}</td>
                      <td>{{row.gender}}</td>
                  </tr>
              {% endfor %}
    """
    print(data)  # 看看模板生成的内容
    return data.encode("utf-8")


routers = [
    ('/index.html', index),
    ('/article.html', article),
    ('/user_info.html', user_info),
    ('/template_shit.html', template_shit),
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
