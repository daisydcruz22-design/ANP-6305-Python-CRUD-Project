emp = {}

while True:
    print("\n======== Employee Management System =========")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter a choice: "))

    match choice:
        case 1:
            print("++++++++++++Add Employee+++++++++++++++++++")
            emp_id = int(input("Enter an employee Id: "))

            if emp_id in emp:
                print("Employee Id already exists")
            else:
                name = input("Enter emp name: ")
                desg = input("Enter emp desg: ")
                sal = int(input("Enter emp salary: "))

                emp[emp_id] = {
                    "Name": name,
                    "Desg": desg,
                    "Salary": sal,
                }

                print("Employee Added successfully=============")

        case 2:
            print("++++++++++++++++display all Employee++++++++++++++++++")
            print("employee details==============")

            if not emp:
                print("No employees found.")
            else:
                for emp_id, val in emp.items():
                    print("Emp Id ::", emp_id)
                    print("Emp name ::", val["Name"])
                    print("Emp desg ::", val["Desg"])
                    print("Emp sal ::", val["Salary"])

        case 3:
            print("++++++++++++++++Search Employee++++++++++++++++++")
            emp_id = int(input("Enter emp ID to search: "))

            if emp_id in emp:
                val = emp[emp_id]
                print("Emp Id ::", emp_id)
                print("Emp name ::", val["Name"])
                print("Emp desg ::", val["Desg"])
                print("Emp sal ::", val["Salary"])
            else:
                print("Employee not found")

        case 4:
            print("++++++++++++++++Update Employee++++++++++++++++++")
            emp_id = int(input("Enter emp ID to update: "))

            if emp_id in emp:
                emp[emp_id]["Name"] = input("Enter new emp name: ")
                emp[emp_id]["Desg"] = input("Enter new emp desg: ")
                emp[emp_id]["Salary"] = int(input("Enter new emp salary: "))
                print("Employee updated successfully")
            else:
                print("Employee not found")

        case 5:
            print("++++++++++++++++Delete Employee++++++++++++++++++")
            emp_id = int(input("Enter emp ID to delete: "))

            if emp_id in emp:
                del emp[emp_id]
                print("Employee deleted successfully")
            else:
                print("Employee not found")

        case 6:
            print("Thank you for using the application.........")
            break

        case _:
            print("Invalid choice")

# Employee ID
# Employee Name
# Department
# Salary