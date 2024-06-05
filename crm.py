import psycopg2
connection = psycopg2.connect(database="crm")
cursor = connection.cursor()

# CRUD for companies table
def create_company():
    comp_name = input('Please enter name of the company: ')

    cursor.execute('INSERT INTO companies (name) VALUES (%s)', [comp_name])
    connection.commit()
    print('Successfully added ' + str(comp_name) + ' to the database!')

def get_companies():
    cursor.execute('SELECT * FROM companies')
    print(cursor.fetchall())

def update_company():
    comp_id = input('Please enter the ID of the company to update: ')
    new_comp_name = input('Type the NEW name for the company: ')

    cursor.execute('UPDATE companies SET name = %s WHERE id = %s', [new_comp_name, comp_id])
    connection.commit()
    print('Successfully updated to ' + str(new_comp_name) + ' in the database!')

def delete_company():
    comp_id = input('Type the id of the company to delete: ')

    cursor.execute('DELETE FROM companies WHERE id = %s', [comp_id])
    connection.commit()
    print('Seccessfully delete from database')


# CRUD for employees table
def create_employee():
    emp_name = input('Please enter name of the employee: ')
    emp_position = input('Please enter the position of the employee: ')
    employer_id = input('Please enter the ID of the employer: ')
    while not employer_id:
        employer_id = input('Please enter the ID of the employer: ')

    cursor.execute('INSERT INTO employees (name, position, company_id) VALUES (%s, %s, %s)', [emp_name, emp_position, employer_id])
    connection.commit()
    print('Successfully added ' + str(emp_name) + ' ' + str(emp_position) + ' to the database!')

def get_employees():
    cursor.execute('SELECT * FROM employees JOIN companies ON employees.company_id = companies.id')
    print(cursor.fetchall())


def update_employee():
    emp_id = input('Please enter the ID of the employee to update: ')
    new_emp_name = input('Type the NEW name for the employee: ')
    new_emp_position = input('Type the NEW position for the employee: ')

    cursor.execute('UPDATE employees SET name = %s, position = %s WHERE id = %s', [new_emp_name, new_emp_position, emp_id])
    connection.commit()
    print('Successfully updated to ' + str(new_emp_name) + ' ' + str(new_emp_position) + ' in the database!')

def delete_employee():
    emp_id = input('Type the id of the employee to delete: ')

    cursor.execute('DELETE FROM employees WHERE id = %s', [emp_id])
    connection.commit()
    print('Successfully deleted from database')


# CRM Terminal Menu
def init():

    while True:
        print('Welcome to the CRM')
        print('1. Create Company')
        print('2. View Companies')
        print('3. Update Company')
        print('4. Delete Company')
        print('5. Create Employee')
        print('6. View Employees')
        print('7. Update Employee')
        print('8. Delete Employee')
        print('9. Exit')

        user_input = input('Enter your choice: ')

        if user_input == '1':
            create_company()
        elif user_input == '2':
            get_companies()
        elif user_input == '3':
            update_company()
        elif user_input == '4':
            delete_company()
        elif user_input == '5':
            create_employee()
        elif user_input == '6':
            get_employees()
        elif user_input == '7':
            update_employee()
        elif user_input == '8':
            delete_employee()
        elif user_input == '9':
            break
        else:
            print('Invalid input.')

init()

connection.close()
cursor.close()