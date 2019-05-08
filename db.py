import sqlite3
from sqlite3 import Error
database = "gpa.db"
 
def connect (db_file = database):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None
 
def selectCourse ():
    cur = conn.cursor ()

    cur.execute ("""SELECT diff, marks, grade
        FROM userAgg, course_grade
        WHERE uname = Username
        AND cname = Course""")

    rows = cur.fetchall ()
    data = []
    grade = []
    for dif, agg, g in rows:
        data.append((dif, agg))
        grade.append(g)

    return data, grade

def selectPartialAgg (n):
    cur = conn.cursor()

    query = "SELECT marks, mymark, avg FROM guessAgg_" + str(n) + ", userAgg WHERE usName = uname AND cname = crName"
    cur.execute(query)
    rows = cur.fetchall()
 
    agg = []
    data = []
    for a, b, c in rows:
        agg.append(a)
        data.append ((b,c))

    return data, agg


def selectUserCourseMarks (user, crs, n):
    cur = conn.cursor()

    query = "SELECT mymark, avg FROM guessAgg_" + str(n) + " WHERE usName = ? AND crName = ?"
    cur.execute(query, (user, crs))
    data = cur.fetchone()
 
    return data[0], data[1]

conn = connect()