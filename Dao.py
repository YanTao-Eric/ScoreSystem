import pymysql


def getConnect():
    """
    获取数据库连接
    :return:
    """
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='521027',
        db='stu_sc_sys',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    return conn, cursor


def getUserByIdAndPwd(username, password):
    conn, cursor = getConnect()
    sql = f"select uid, uname, ugender, uidentify, uclid, uemail, urole from user where uid='{username}' " \
          f"and upwd='{password}'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchone()
    }
    cursor.close()
    conn.close()
    return res


def getUserInfoById(uid):
    conn, cursor = getConnect()
    sql = f"select uid, uname, ugender, uidentify, uclid, uemail, urole from user where uid='{uid}'"
    cursor.execute(sql, uid)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def getScoreByUserId(uid):
    conn, cursor = getConnect()
    sql = f"select ROW_NUMBER() over () as id, uc.cname, c.ccredit, c.cnature, c.cdepartment, c.cexammethod, score " \
          f"from user_course uc inner join course c on uc.cname = c.cname where uc.uid = '{uid}'"
    cursor.execute(sql, ())
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def getAllUsers():
    connection, cursor = getConnect()
    sql = 'select uid, uname, ugender, uidentify, uclid, uemail, upwd, urole from user'
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllStudents():
    connection, cursor = getConnect()
    sql = 'select row_number() over () as id, uid, uname, ugender, uidentify, uclid, uemail, upwd, urole ' \
          'from user where urole = 1'
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def searchStudents(uname, ugender):
    """
    学生信息搜索
    :param uname:
    :param ugender:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select row_number() over () as id, uid, uname, ugender, uidentify, uclid, uemail, upwd, urole from user " \
          f"where urole = 1 and uname like '%{uname}%' and ugender like '%{ugender}%'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def addStudent(uid, uname, ugender, uidentify, uclid, uemail):
    """
    添加一个学生信息，密码默认为123456
    :param uid:
    :param uname:
    :param ugender:
    :param uidentify:
    :param uclid:
    :param uemail:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"insert into user(uid, uname, ugender, uidentify, uclid, uemail, upwd) values ('{uid}', '{uname}'" \
          f", '{ugender}', '{uidentify}', '{uclid}', '{uemail}', '123456') "
    res = {
        "code": 0,
        "msg": "添加成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "添加失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def deleteUser(uid):
    """
    通过uid删除用户
    :param uid:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"delete from user where uid = '{uid}'"
    res = {
        "code": 0,
        "msg": "删除成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "删除失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def updateUser(uid, uname, ugender, uidentify, uclid, uemail):
    """
    通过uid更新用户信息
    :param uid:
    :param uname:
    :param ugender:
    :param uidentify:
    :param uclid:
    :param uemail:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"update user set uname = '{uid}', ugender = '{uname}', uidentify = '{uidentify}', uclid = '{ugender}'" \
          f", uemail ='{uemail}' where uid = '{uid}'"
    res = {
        "code": 0,
        "msg": "修改成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "修改失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def getAllCourses():
    """
    获取所有的课程信息
    :return:
    """
    connection, cursor = getConnect()
    sql = "select cid, cname, ccredit, cnature, cdepartment, cexammethod from course"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getCourseByCid(cid):
    """
    获取cid的课程
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select cid, cname, cnature, ccredit, cdepartment, cexammethod from course where cid = '{cid}'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getDataDictByType(dtype):
    """
    获取dtype类型的数据字典
    :param:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select d.ddtkey as k, d.ddtvalue as v from dictionary d where d.ddtype = '{dtype}'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllDepartments():
    """
    获取所有的学院
    :return:
    """
    connection, cursor = getConnect()
    sql = "select did as k, dname as v from department"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getMaxStuNumber(s_num_prefix):
    """
    获取以s_num_prefix开头的最大学号
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select MAX(uid) as max_id from user where uid like '{s_num_prefix}%'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def addCourse(cname, nature, credit, department, exam_method):
    """
    添加课程
    :return:
    """
    connection, cursor = getConnect()
    sql = f"insert into course(cname, cnature, ccredit, cdepartment, cexammethod) VALUES ('{cname}', '{nature}'" \
          f", '{credit}', '{department}', '{exam_method}')"
    res = {
        "code": 0,
        "msg": "添加课程成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "添加课程失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def deleteCourse(cid):
    """
    删除课程
    :return:
    """
    connection, cursor = getConnect()
    sql = f"delete from course where cid = {cid}"
    res = {
        "code": 0,
        "msg": "删除课程成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "删除课程失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def searchCourses(department, exammethod):
    """
    搜索课程信息
    :param department:
    :param exammethod:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select cid, cname, ccredit, cnature, cdepartment, cexammethod from course " \
          f"where cdepartment like '%{department}%' and cexammethod like '%{exammethod}%'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def updateCourseInfo(cid, cname, nature, credit, department, exammethod):
    """
    修改课程信息
    :param cid:
    :param cname:
    :param nature:
    :param credit:
    :param department:
    :param exammethod:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"update course set cname = '{cname}', cnature = '{nature}', ccredit = '{credit}'" \
          f", cdepartment = '{department}', cexammethod = '{exammethod}' where cid = '{cid}'"
    res = {
        "code": 0,
        "msg": "修改课程成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "更新课程失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res
