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
    sql = 'select uid, uname, ugender, uidentify, uclid, uemail, urole from user where uid=%s and upwd=%s'
    cursor.execute(sql, (username, password))
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
    sql = 'select uid, uname, ugender, uidentify, uclid, uemail, urole from user where uid=%s'
    cursor.execute(sql, uid)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def getScoreByUserId(username):
    conn, cursor = getConnect()
    sql = "select cid, cname, ccredit, dn.ddtvalue, d.dname, dm.ddtvalue, 100 as score from course c inner join dictionary dn on dn.ddtype='nature' and c.cnid = dn.ddtkey inner join department d on c.cdid = d.did inner join dictionary dm on dm.ddtype='exammethod' and c.cmid = dm.ddtkey order by cid"
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
    sql = 'select row_number() over () as id, uid, uname, ugender, uidentify, uclid, uemail, upwd, urole from user where urole = 1'
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
    sql = "insert into user(uid, uname, ugender, uidentify, uclid, uemail, upwd) values (%d, %s, %d, %s, %d, %s, %s) "
    res = {
        "code": 0,
        "msg": "添加成功！"
    }
    try:
        cursor.execute(sql, (uid, uname, ugender, uidentify, uclid, uemail, '123456'))
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
    sql = "delete from user where uid = %d"
    res = {
        "code": 0,
        "msg": "删除成功！"
    }
    try:
        cursor.execute(sql, uid)
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
    sql = "update user set uname = %s, ugender = %s, uidentify = %s, uclid = %s, uemail = %s where uid = %d"
    res = {
        "code": 0,
        "msg": "修改成功！"
    }
    try:
        cursor.execute(sql, (uname, ugender, uidentify, uclid, uemail, uid))
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
    sql = '''select row_number() over () as id, cname, ccredit, da.ddtvalue as nature, d.dname, db.ddtvalue
            from course c
            inner join dictionary da on c.cnid = da.ddtkey and da.ddtype = 'nature'
            inner join dictionary db on c.cmid = db.ddtkey and db.ddtype = 'exammethod'
            inner join department d on c.cdid = d.did'''
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllExamMethods():
    """
    获取所有的课程考核方式
    :return:
    """
    connection, cursor = getConnect()
    sql = "select d.ddtkey as k, d.ddtvalue as v from dictionary d where d.ddtype = 'exammethod'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllCourseNatures():
    """
    获取所有的课程性质
    :return:
    """
    connection, cursor = getConnect()
    sql = "select d.ddtkey as k, d.ddtvalue as v from dictionary d where d.ddtype = 'nature'"
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
