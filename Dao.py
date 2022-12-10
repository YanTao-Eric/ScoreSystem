import pymysql


def getConnect():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='521027',
        db='stu_sc_sys',
        charset='utf8'
    )
    cursor = conn.cursor()
    return conn, cursor


def getUserByIdAndPwd(username, password):
    conn, cursor = getConnect()
    sql = 'select uid, urole from user where uid=%s and upwd=%s'
    cursor.execute(sql, (username, password))
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res


def getUserInfoById(uid):
    conn, cursor = getConnect()
    sql = 'select uid, uname, ugender, uidentify, uclid, utel, urole from user where uid=%s'
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
