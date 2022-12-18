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
    cursor.execute(sql)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def updatePassword(uid, origin_pwd, new_pwd):
    conn, cursor = getConnect()
    res = {
        "code": 1,
        "msg": "修改密码失败！"
    }
    if not getUserByIdAndPwd(uid, origin_pwd).get("data"):
        res = {
            "code": 1,
            "msg": "原密码不正确！"
        }
    else:
        sql = f"update user set upwd = '{new_pwd}' where uid = '{uid}'"
        try:
            cursor.execute(sql)
            conn.commit()
            res = {
                "code": 0,
                "msg": "修改成功！"
            }
        except Exception as e:
            conn.rollback()
            print(e)
    return res


def getScoreByUid(uid, nature='', department='', exam_method=''):
    """
    通过学号获取成绩
    :param uid:
    :param nature:
    :param department:
    :param exam_method:
    :return:
    """
    conn, cursor = getConnect()
    sql = f"select ROW_NUMBER() over () as id, uc.cname, c.cnature, c.cdepartment, c.cexammethod, c.ccredit, score " \
          f"from user_course uc inner join user u on uc.uid = u.uid inner join course c on uc.cname = c.cname " \
          f"where u.uid = '{uid}' and c.cnature like '%{nature}%' and " \
          f"c.cdepartment like '%{department}%' and c.cexammethod like '%{exam_method}%'"
    print(sql)
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
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
    sql = "select row_number() over () as id, uid, uname, ugender, uidentify, uclid, uemail from user where urole = 1"
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
    sql = f"update user set uname = '{uname}', ugender = '{ugender}', uidentify = '{uidentify}', uclid = '{uclid}'" \
          f", uemail ='{uemail}' where uid = '{uid}'"
    print(sql)
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


def getScoreBandByCName(course_name):
    """
    获取课程名为course_name的各个分段的学生人数
    :param course_name:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select SUM(IF(score <= 100 and score >= 90, 1, 0)) as A, SUM(IF(score < 90 and score >= 80, 1, 0)) as B, " \
          f"SUM(IF(score < 80 and score >= 70, 1, 0)) as C, SUM(IF(score < 70 and score >= 60, 1, 0)) as D, " \
          f"SUM(IF(score < 60, 1, 0)) as E from user_course where cname = '{course_name}'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getMaxAndMinAndAvgScoreByCLid(class_id):
    """
    获取班级号为class_id的班级的各科最高分、最低分以及平均分
    :param class_id:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select uc.cname, MAX(score) as max_score, MIN(score) as min_score, AVG(score) as avg_score " \
          f"from user_course uc inner join user u on uc.uid = u.uid where u.uclid = '{class_id}' group by uc.cname"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getOverallGradeLevelByCLid(class_id):
    """
    获取班级号为class_id的班级综合成绩等级各分段人数
    :param class_id:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select SUM(IF(avg_score >= 85 and avg_score <= 100, 1, 0)) as A, " \
          f"SUM(IF(avg_score >= 70 and avg_score < 85, 1, 0)) as B, " \
          f"SUM(IF(avg_score >= 60 and avg_score < 70, 1, 0)) as C, " \
          f"SUM(IF(avg_score < 60, 1, 0)) as D from (" \
          f"select AVG(score) as avg_score from user_course uc " \
          f"inner join user u on uc.uid = u.uid where u.uclid = '{class_id}' group by u.uid" \
          f") s"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllClasses():
    """
    获取用户表中已存在的班级号
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select distinct uclid from user where urole = 1"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getAllCourseAvgScore(uid):
    """
    获取所有课程的平均分
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select cname, AVG(score) as avg_score from user_course where cname in " \
          f"(select cname from user_course where uid = '{uid}') group by cname"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def searchStudentScore(course_name='', course_nature='', course_department=''):
    """
    搜索学生成绩
    :param course_name:
    :param course_nature:
    :param course_department:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select ROW_NUMBER() over () as id, u.uid, u.uname, uc.cname, c.cnature, c.cdepartment, c.cexammethod, " \
          f"c.ccredit, score from user_course uc inner join user u on uc.uid = u.uid inner join course c " \
          f"on uc.cname = c.cname where c.cname like '%{course_name}%' and " \
          f"c.cnature like '%{course_nature}%' and c.cdepartment like '%{course_department}%'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def getScoreByUidAndCName(uid, course_name):
    """
    查找学号为uid课程为course_name的学生成绩
    :param uid:
    :param course_name:
    :return:
    """
    connection, cursor = getConnect()
    sql = f"select uid, cname, score from user_course where uid = '{uid}' and cname = '{course_name}'"
    cursor.execute(sql)
    res = {
        "code": 0,
        "msg": "success",
        "data": cursor.fetchall()
    }
    cursor.close()
    connection.close()
    return res


def addStudentScore(uid, course_name, score):
    connection, cursor = getConnect()
    if not cursor.execute(f"select uid from user where uid = '{uid}'"):
        return {
            "code": 1,
            "msg": "学号不存在！"
        }
    if cursor.execute(f"select 1 from user_course where uid = '{uid}' and cname = '{course_name}' limit 1"):
        return {
            "code": 1,
            "msg": f"该学生的{course_name}课程成绩已经存在！"
        }
    sql = f"insert into user_course(uid, cname, score) VALUES ('{uid}', '{course_name}', '{score}')"
    res = {
        "code": 0,
        "msg": "添加成绩成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "添加成绩失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def deleteStudentScore(uid, course_name):
    connection, cursor = getConnect()
    if not cursor.execute(f"select uid from user where uid = '{uid}'"):
        return {
            "code": 1,
            "msg": "学号不存在！"
        }
    sql = f"delete from user_course where uid = '{uid}' and cname = '{course_name}'"
    res = {
        "code": 0,
        "msg": "删除成绩成功！"
    }
    try:
        code = cursor.execute(sql)
        connection.commit()
        if code == 0:
            res = {
                "code": 0,
                "msg": f"该学生的{course_name}课程成绩不存在！"
            }
    except Exception as e:
        res = {
            "code": 1,
            "msg": "删除成绩失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res


def updateStudentScore(uid, course_name, score):
    connection, cursor = getConnect()
    sql = f"update user_course set score = '{score}' where uid = '{uid}' and cname = '{course_name}'"
    res = {
        "code": 0,
        "msg": "修改成绩成功！"
    }
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "修改成绩失败！"
        }
        connection.rollback()
        print(e)
    cursor.close()
    connection.close()
    return res
