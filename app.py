import psycopg

conn = None

def getAllStudents():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    global conn
    try:    #connect to the database
        conn = psycopg.connect (
            dbname="Assignment 3 Q1",
            user="postgres",
            password="pass",
            host="localhost",
            port="5432"
        )
    except psycopg.operationalError as e:   #if the connection fails
        print (f"Error:{e}")
        exit(1)
    print("Database connected")


    getAllStudents()

    print("Database connected")
    conn.close()
main()