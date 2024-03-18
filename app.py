#Name: Saeid El-Saadi
#ID: 101231225
import psycopg

conn = None

#list records
def getAllStudents():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    print("\n")
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

#delete record
def deleteStudent(student_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    print("record deleted")

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

    #getAllStudents()
    #addStudent("Saeid", "El-Saadi", "saeidelsaadi@cmail.carleton.ca", "2024-03-18")
    #getAllStudents()

    #getAllStudents()
    #updateStudentEmail(13, "test1@gmail.com")
    #getAllStudents()

    #getAllStudents()
    #deleteStudent(13)
    #getAllStudents()
    #FUNCTION TESTING ENDS HERE

    conn.close()
main()