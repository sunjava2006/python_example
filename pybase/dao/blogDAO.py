import pymysql


def getConnection():
    return pymysql.connect(host="localhost", user="blog", password="blog", charset='utf8', database="blog")


def addUser(regName, pwd, gender, birthday):
    sql = '''insert into reg_user (reg_name, pwd, gender, birthday)
             values (%s, %s, %s, %s)'''

    with getConnection() as cursor:
        cursor.execute(sql, (regName, pwd, gender, birthday))
    return cursor.rowcount


def listAll():
    sql = '''elect * from reg_user'''
    li = list()
    with getConnection() as cursor:
        cursor.execute(sql)
        for i in cursor:
            li.append(i)
    return li


li = listAll()
print(li)

#---------------------------------------
# count = addUser('王小光', '123456', '男', '1973-2-7')
# print(count)


