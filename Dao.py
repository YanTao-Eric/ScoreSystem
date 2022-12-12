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
        "data": cursor.fetchall()
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


def addUser(uid, uname, ugender, uidentify, uclid, uemail, upwd, urole):
    connection, cursor = getConnect()
    sql = "insert into user(uid, uname, ugender, uidentify, uclid, uemail, upwd, urole) values (%d, %s, %d, %s, %d, " \
          "%s, %s, %d) "
    res = {
        "code": 0,
        "msg": "success"
    }
    try:
        cursor.execute(sql, (uid, uname, ugender, uidentify, uclid, uemail, upwd, urole))
        connection.commit()
    except Exception as e:
        res = {
            "code": 1,
            "msg": "error"
        }
        print(e)
    cursor.close()
    connection.close()
    return res
