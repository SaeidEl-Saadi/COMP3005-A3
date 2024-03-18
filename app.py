import psycopg

conn = None

#list records
def getAllStudents():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()

#add record
def addStudent(first_name, last_name, email, enrollment_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    print("record added")

#update record
def updateStudentEmail(student_id, new_email):
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    print("record updated")

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

    #ARE BELOW FOR FUNCTION TESTING
    getAllStudents()
    addStudent("Saeid", "El-Saadi", "t2", "2021-03-01")
    getAllStudents()
    #FUNCTION TESTING ENDS HERE

    conn.close()
main()