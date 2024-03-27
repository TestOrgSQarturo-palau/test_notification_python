print('this should have issues')

def noncompliant():
    ls = [1, 2, 3]
    foo(ls[3])  # Noncompliant


from mysql.connector import connection
connection.MySQLConnection(host='localhost', user='sonarsource', password='')  # Noncompliant
