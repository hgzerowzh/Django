from django.shortcuts import render, redirect, HttpResponse
import pymysql
import json

def classes(request):
    tk = request.COOKIES.get('ticket')
    # tk = request.get_signed_cookie('ticket', salt='xxxooo')
    if not tk:
        return redirect('/login/')

    # 获取所有的class信息，然后渲染到模板中
    conn = pymysql.connect(host='10.0.0.204', user='hgzero', port=3306, password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute("select id,title from class")
    class_list = conn_cursor.fetchall()
    conn_cursor.close()
    conn.close()
    return render(request, "classes.html", {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, "add_class.html")
    else:
        print(request.POST)
        v = request.POST.get("title")
        if len(v) > 0:
            conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test', charset='utf8')
            conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            conn_cursor.execute('insert into class(title) values(%s)', v)
            conn.commit()
            conn_cursor.close()
            conn.close()
            return redirect('/classes/')
        else:
            return render(request, 'add_class.html', {'msg': "班级名称不能为空！"})

def del_class(request):
    nid = request.GET.get('nid')

    conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute('delete from class where id=(%s)', nid)
    conn.commit()
    conn_cursor.close()
    conn.close()
    return redirect('/classes/')


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')

        conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test', charset='utf8')
        conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn_cursor.execute('select id,title from class where id=(%s)', nid)
        result = conn_cursor.fetchone()
        conn_cursor.close()
        conn.close()
        return render(request, 'edit_class.html', {'result': result})
    else:
        class_id = request.GET.get('nid')
        class_name = request.POST.get('title')

        conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test', charset='utf8')
        conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn_cursor.execute('update class set title=(%s) where id=(%s)', [class_name, class_id])
        conn.commit()
        conn_cursor.close()
        conn.close()
        return redirect('/classes/')


def students(request):
    conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test',charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute('select students.id, students.name, class.title, class.id as class_id from students left join class on students.class=class.id')
    result = conn_cursor.fetchall()
    conn_cursor.close()
    conn.close()

    class_list = sqlhelper.get_list('select id,title from class', [])
    return render(request, 'students.html', {"students_info": result, "class_list": class_list})

def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test',charset='utf8')
        conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn_cursor.execute('select id,title from class')
        result = conn_cursor.fetchall()
        conn_cursor.close()
        conn.close()
        return render(request, 'add_student.html', {'class_info': result})
    else:
        stu_name = request.POST.get('stu_name')
        stu_class = request.POST.get('class_id')

        conn = pymysql.connect(host="10.0.0.204", port=3306, user='hgzero', password='woshiniba', db='my_test',charset='utf8')
        conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn_cursor.execute('insert into students(name, class) values((%s),(%s))', [stu_name, stu_class, ])
        conn.commit()
        conn_cursor.close()
        conn.close()
        return redirect("/students/")

def del_students(request):
    stu_id = request.GET.get("stu_id")

    conn = pymysql.connect(host='10.0.0.204', port=3306, user='hgzero', password='woshiniba', db='my_test', charset='utf8')
    conn_cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn_cursor.execute('delete from students where id=%s', [stu_id, ])
    conn.commit()
    conn_cursor.close()
    conn.close()
    return redirect('/students/')


from utils import sqlhelper
def edit_students(request):
    if request.method == "GET":
        stu_id = request.GET.get('stu_id')

        class_list = sqlhelper.get_list('select id,title from class', [])
        stu_info = sqlhelper.get_one('select id,name,class from students where id=%s', [stu_id, ])
        return render(request, 'edit_students.html', {'class_list': class_list, 'stu_info': stu_info})
    else:
        stu_id = request.GET.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_class = request.POST.get('class_id')

        sqlhelper.modify('update students set name=(%s),class=(%s) where id=(%s)', [stu_name, stu_class, stu_id])
        return redirect('/students/')

######对话框######

def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlhelper.modify('insert into class(title) values(%s)', [title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级不能为空!')

def ajax_del_class(request):
    nid = request.POST.get('nid')
    sqlhelper.modify('delete from class where id=%s', [nid, ])
    return HttpResponse('ok')

def ajax_edit_class(request):
    ret = {'status': True, 'message': None}
    # try:
    #     class_id = request.POST.get('Edit_id')
    #     class_title = request.POST.get('Edit_title')
    #     sqlhelper.modify('update class set title=%s where id=%s', [class_title, class_id, ])
    # except Exception as e:
    #     ret['status'] = False
    #     ret['message'] = "shit! 出错了！"
    # return HttpResponse(json.dumps(ret))

    class_id = request.POST.get('Edit_id')
    class_title = request.POST.get('Edit_title')
    if len(class_title) > 0:
        sqlhelper.modify('update class set title=%s where id=%s', [class_title, class_id, ])
    else:
        ret['status'] = False
        ret['message'] = "处理异常"
    return HttpResponse(json.dumps(ret))


def ajax_add_student(request):
    ret = {'status': True, 'mesg': False}
    try:
        stu_name = request.POST.get('stu_name')
        class_id = request.POST.get('stu_class')
        sqlhelper.modify('insert into students(name, class) values(%s,%s)', [stu_name, class_id, ])
    except Exception as e:
        ret['status'] = False
        ret['mesg'] = "shit！出错了！"
    return HttpResponse(json.dumps(ret))

def ajax_edit_student(request):
    ret = {'status': True, 'message': None}
    try:
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_class_id = request.POST.get('stu_class_id')
        sqlhelper.modify('update students set name=%s,class=%s where id=%s', [stu_name, stu_class_id, stu_id])
    except Exception as e:
        ret['status'] = False
        ret['message'] = "Shit! 出错了！"
    return HttpResponse(json.dumps(ret))


def teachers(request):
    ret = sqlhelper.get_list("""
        select teacher.id as t_id,teacher.name as t_name,class.id as c_id,class.title as t_title
        from teacher 
        left join teacher_class on teacher.id=teacher_class.teacher_id
        left join class on class.id=teacher_class.class_id;
    """, [])
    result = {}
    for row in ret:
        tid = row['t_id']
        if tid in result:
            result[tid]['t_title'].append(row['t_title'])
        else:
            result[tid] = {'t_id': row['t_id'], 't_name': row['t_name'], 't_title': [row['t_title']], }
    return render(request, 'teachers.html', {'teacher_info': result.values()})


def add_teacher(request):
    if request.method == 'GET':
        ret = sqlhelper.get_list('select id,title from class', [])
        return render(request, 'add_teacher.html', {'class_list': ret})
    else:
        name = request.POST.get('teacher_name')
        class_id = request.POST.getlist('teacher_class')

        obj = sqlhelper.SqlHelper()
        teacher_id = obj.create('insert into teacher(name) value(%s)', [name, ])

        data_list = []
        for cls_id in class_id:
            temp = (teacher_id, cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher_class(teacher_id, class_id) values(%s, %s)', data_list)
        obj.close()
        return redirect('/teachers/')


def edit_teacher(request):
    if request.method == 'GET':
        t_id = request.GET.get('teacher_id')
        obj = sqlhelper.SqlHelper()
        teacher_name = obj.get_one('select id,name from teacher where id=%s', [t_id, ])
        teacher_class = obj.get_list('select class_id from teacher_class where teacher_id=%s', [t_id, ])
        class_list = obj.get_list('select id,title from class', [])
        obj.close()

        teacher_class_list = []
        for i in teacher_class:
            teacher_class_list.append(i['class_id'])

        return render(request, 'edit_teacher.html', {
            "t_name": teacher_name,
            "t_class": teacher_class_list,
            "class_list": class_list,
        })
    else:
        t_id = request.GET.get('t_id')
        t_name = request.POST.get('teacher_name')
        t_class = request.POST.getlist('teacher_class')

        obj = sqlhelper.SqlHelper()
        obj.modify('update teacher set name=%s where id=%s', [t_name, t_id])

        obj.modify('delete from teacher_class where teacher_id=%s', [t_id, ])

        data_list = []
        for cls_id in t_class:
            temp = (t_id, cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher_class(teacher_id, class_id) values(%s, %s)', data_list)
        obj.close()
        return redirect('/teachers/')


def get_all_class(request):
    if request.method == 'GET':
        obj = sqlhelper.SqlHelper()
        all_class = obj.get_list('select id,title from class', [])
        obj.close()
        return HttpResponse(json.dumps(all_class))
    else:
        status_info = {'status': True, 'message': None}
        try:
            teacher_name = request.POST.get('teacher_name')
            teacher_class = request.POST.getlist('teacher_class')

            obj = sqlhelper.SqlHelper()
            teacher_id = obj.create('insert into teacher(name) values(%s)', [teacher_name, ])

            ret = []
            for i in teacher_class:
                i_ret = (teacher_id, i)
                ret.append(i_ret)
            obj.multiple_modify('insert into teacher_class(teacher_id, class_id) values(%s,%s)', ret)
            obj.close()
        except Exception as e:
            status_info['status'] = False
            status_info['message'] = "出错了！"
        return HttpResponse(json.dumps(status_info))


def layout(request):
    return render(request, 'layout.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        if user == 'hgzero' and pwd == 'woshiniba':
            obj = redirect('/classes/')
            obj.set_cookie('ticket', 'shitshitshit')
            # obj.set_signed_cookie('ticket', 'shitshitshit', salt='xxxooo')
            return obj
        else:
            return render(request, 'login.html')
