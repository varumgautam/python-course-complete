class college:
    course=["B.tech","BCA","BBA","MBA","POLYTECHNIC","B.pharma","B.arch"]
    fees=["1lakh","50k","50k","60k","40k","1.20lakh","1.10lakh"]
    def addmission_cell(self,name,course):
        self.name=name
        self.course=course
        print(f"hellow {self.name} welcome to the addmission cell you are selected {self.course}course")
    def registrar_office(self):
        print(f"hello {self.name} welcome to ragistrar office")
    def management_system(self):
        print("welcome to management system","name",self.name,"course",self.course)
    def fees_deposit_cell(self):
        print("welcome to the fees department","name",self.name,"course",self.course)    
obj1=college()
print(obj1.fees)
print(obj1.course)
obj1.addmission_cell("varun","b.tech")
obj1.registrar_office()
# obj1.addmission_cell()
obj1.management_system()
obj1.fees_deposit_cell()


