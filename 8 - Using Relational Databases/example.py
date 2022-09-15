# Connecting to database and search request
import sys
import mysql.connector


def getEmployeesByLastName(surname):
    sql = "SELECT Number, Last_name, First_name, Salary FROM Employee"
    sql += " WHERE Last_name='" + surname + "'"
#    print(sql)
    cursor = connection.cursor()    # cursor is used to forward the SQL statement to the database server for result set
    cursor.execute(sql)     # to execute the SQL statement in the string variable
    result = cursor.fetchall()  # result set is requested from server; can be .fetchmany or .fetchone
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return


# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='user',
         password='pAs5w_0rD',
         autocommit=True
         )

last_name = input("Enter last name: ")
getEmployeesByLastName(last_name)

sys.exit(0)

# Update, insert, delete


def updateSalary(num, add):
    sql = "UPDATE Employee SET Salary=" + str(add) + " WHERE Number=" + str(num)
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print("Salary updated")


number = int(input("Enter number: "))
newSalary = float(input("Enter new salary: "))
updateSalary(number, newSalary)
