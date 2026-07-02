import os
import sys

# Setup PyMySQL before importing Django
try:
    import pymysql  # type: ignore[import-untyped]
    pymysql.version_info = (2, 2, 1, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from student.models import Student
from employee.models import Employee
from django.db import connections
from django.db.utils import OperationalError

def test_database_connections():
    print("=" * 60)
    print("[*] DJANGO MULTI-DATABASE CONNECTION DEMO")
    print("=" * 60)

    # 1. Test SQLite (default) Connection
    print("\n[1] Testing SQLite Database ('default')...")
    try:
        conn_sqlite = connections['default']
        conn_sqlite.ensure_connection()
        print("[+] SQLite connection successful!")
        
        # Count records in SQLite
        student_count_sqlite = Student.objects.using('default').count()
        employee_count_sqlite = Employee.objects.using('default').count()
        print(f"    -> SQLite Records: {student_count_sqlite} Students | {employee_count_sqlite} Employees")

        # Create a demo student in SQLite
        demo_student_sqlite, created = Student.objects.using('default').get_or_create(
            rollnumber="SQLITE01",
            defaults={"name": "Alice (SQLite User)", "age": 20, "course": "Django & SQLite"}
        )
        if created:
            print(f"    -> Added demo student to SQLite: {demo_student_sqlite}")
        else:
            print(f"    -> Demo student already exists in SQLite: {demo_student_sqlite}")

    except Exception as e:
        print(f"[-] SQLite connection failed: {e}")

    # 2. Test MySQL (mysql_db) Connection
    print("\n[2] Testing MySQL Database ('mysql_db')...")
    try:
        conn_mysql = connections['mysql_db']
        conn_mysql.ensure_connection()
        print("[+] MySQL connection successful!")
        
        # Try counting records in MySQL
        try:
            student_count_mysql = Student.objects.using('mysql_db').count()
            employee_count_mysql = Employee.objects.using('mysql_db').count()
            print(f"    -> MySQL Records: {student_count_mysql} Students | {employee_count_mysql} Employees")

            # Create a demo student in MySQL
            demo_student_mysql, created = Student.objects.using('mysql_db').get_or_create(
                rollnumber="MYSQL01",
                defaults={"name": "Bob (MySQL User)", "age": 22, "course": "Django & MySQL"}
            )
            if created:
                print(f"    -> Added demo student to MySQL: {demo_student_mysql}")
            else:
                print(f"    -> Demo student already exists in MySQL: {demo_student_mysql}")

        except OperationalError as oe:
            print(f"    [!] Connected to MySQL server, but table query failed: {oe}")
            print("    [!] TIP: Have you created the tables in MySQL yet?")
            print("        Run this command in your terminal to create Django tables in MySQL:")
            print("        -> python manage.py migrate --database=mysql_db")

    except Exception as e:
        print(f"[-] MySQL connection failed: {e}")
        print("    [!] Make sure your MySQL server is running and credentials are correct!")

    print("\n" + "=" * 60)
    print("[*] Demo complete! See how `.using('db_name')` directs queries to specific databases.")
    print("=" * 60)

if __name__ == "__main__":
    test_database_connections()
