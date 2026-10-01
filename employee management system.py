

employees = {}

while True:
    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("enter your choice::::"))
    match choice:
        # add emp
        case 1:

            empId = int(input("enter a emp id ::"))

            if empId in employees:
                print("employee id allredy exist")
            else:
                name = input("enter a emp name ::")
                age = int(input("enter a emp age ::"))
                desg = input("enter a emp desg  ::")
                sal = float(input("enter a emp sal :: "))

                employees[empId] = {
                    "Name": name,
                    "Age": age,
                    "Desg": desg,
                    "Salary": sal,
                }
            print("Employee Added Successfully.")

        case 2:
            if len(employees) == 0:
                print("No Employee Found.")
            else:

                print("\nEmployee Details")
                print("-" * 50)

            for empId, details in employees.items():
                print("Employee ID :", empId)
                print("Name        :", details["Name"])
                print("Age         :", details["Age"])
                print("Designation :", details["Desg"])
                print("Salary      :", details["Salary"])
                print("-" * 50)

        case 3:
            # ===================search employee============================

            empId = int(input("enter a employee ID::which emp wantto search"))

            if empId in employees:
                print("employee found...")

                print("Employee ID :", empId)
                print("Name        :", employees[empId]["Name"])
                print("Age         :", employees[empId]["Age"])
                print("Designation :", employees[empId]["Desg"])
                print("Salary      :", employees[empId]["Salary"])

            else:
                print("emp not found")

        case 4:
            print("++++++++++++++++++++++Employee update++++++++++++++++++++++")

            empId = int(input("enter a emp ID to update the emp details"))

            if empId in employees:
                employees[empId]["Name"] = input("Enter a updated name of employee")
                employees[empId]["Age"] = input("Enter a updated age of employee")

                print("Employee Updated Successfully.")

            else:
                print("Employee not found")

        case 5:
            print(
                "+++++++++++++++++Employee Delete operation+++++++++++++++++++++++++++"
            )

            empId = int(input("enter a employee ID to delete a emp"))

            if empId in employees:
                del employees[empId]
                print("Employee Deleted Successfully.")

            else:
                print("Employee Not Found.")

        case 6:
            print("Thank you...............")
            break

        case _:

            print("Invalid Choice! Please Try Again.")
