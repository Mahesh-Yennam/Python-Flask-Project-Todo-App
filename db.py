import pymysql as p

def connectdb():
    global con
    con = p.connect(host='localhost',
                    user='root',
                    port=3306,
                    password='',
                    database='tododb')
    return con.cursor()

def disconnectdb():
    con.commit()
    con.close()

def inserttodo(t):
    cur = connectdb()
    sqlquery="insert into todos(title,body) values(%s, %s)"
    # print(t)
    cur.execute(sqlquery, t)
    disconnectdb()

def selecttodo():
    cur = connectdb()
    sqlquery="select * from todos"
    cur.execute(sqlquery)
    todos=cur.fetchall()
    # print(todos)
    disconnectdb()
    return todos

def edittodo(id):
    cur = connectdb()
    sqlquery = "select * from todos where id=%s"
    cur.execute(sqlquery,id)
    todo=cur.fetchone()
    print(todo)
    disconnectdb()
    return todo

def updatetodo(id,title,body):
    cur = connectdb()
    sqlquery="update todos set title=%s, body=%s where id=%s"
    # print(t)
    cur.execute(sqlquery, (title,body,id))
    disconnectdb()

def deletetodo(id):
    cur=connectdb()
    sqlquery = "delete from todos where id=%s"
    cur.execute(sqlquery,id)
    disconnectdb()