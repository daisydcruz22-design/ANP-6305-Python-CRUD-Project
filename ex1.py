
#list
no1=[10,20,30,40,55,66]
print(type(no1))

#tuple
no2=(2,3,4,5,5,)
print(type(no2))

#set-unique collection of elements
no3={3,4,5,6,7}
print(type(no3))

# dict -> store elem in key value pair format
stud_dtls = {
    "rollno" : 101,
    "studname" : "Raja",
    "course" : "DPBA"
} 

print(type(stud_dtls))
print(stud_dtls)

# emptydict
emp = {}


emp_dtls = {
    "emp1" : {
        "empID" : 101,
        "empName" : "Raja",
        "desg" : "Tester",
        "Sal" : 20000
    },
    "emp2" : {
            "empID" : 102,
            "empName" : "Raja",
            "desg" : "Tester",
            "Sal" : 20000
        },
    "emp3" : {
                "empID" : 101,
                "empName" : "Raja",
                "desg" : "Tester",
                "Sal" : 20000
            },
    "emp4" : {
                    "empID" : 101,
                    "empName" : "Raja",
                    "desg" : "Tester",
                    "Sal" : 20000
                }
}


print(emp_dtls)