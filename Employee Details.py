class Employee:
    def __init__(self):
        self.name = ""
        self.empId = ""
        self.dept = ""
        self.salary = 0
        
    def getEmpDetails(self):
        self.name = input("Enter Employee name : ")
        self.empId = input("Enter Employee ID : ")
        self.dept = input("Enter Employee Dept : ")
        self.salary = int(input("Enter Employee Salary : "))
        
    def showEmpDetails(self):
        print("Employee Details")
        print("Name : ", self.name)
        print("ID : ", self.empId)
        print("Dept : ", self.dept)
        print("Salary : ", self.salary)
        
    def updtSalary(self, hike):
        self.salary += self.salary*hike/100
        print("Updated Salary for",self.name)
        
company = []
def main():
    for i in range(5):
        e1 = Employee()
        e1.getEmpDetails()
        company.append(e1)

    print("\nEMPLOYEE DETAILS\n")
    for emp in company:
        emp.showEmpDetails()
        
    dept = input("Enter Department for which you want to update salary")
    hike = eval(input("Enter hike in percentage : "))
    for emp in company:
        if emp.dept == dept:
            emp.updtSalary(hike)
            
    print("\nUPDATED EMPLOYEE DETAILS\n")
    for emp in company:
        emp.showEmpDetails()

main()
