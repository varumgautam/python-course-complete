# class Book:
#     title=["varun","jatin","priyanka","vinod","kavita"]
#     author=["army1","army2","army3","army4","army5"]
#     def __init__(self,title,author,price):
#         # self.title=title
#         self.author=author
#         self.price=price
#         if title in self.title:
#             self.title=title
#             print("yes this book avaliable")
#         else:
#             print("not boook avaliable")
#     def view(self):
#         print("title name :",self.title,"author name :",self.author,"price book :",self.price)
#     def __del__(self):
#         print("end of the process")    
# obj1=Book("varune","army1",3000)          
# obj1.view()  
          
# class bankaccount:
#     accountnumbers=["1213","1224","5234","8973","6373"]
#     name=["varun","jatin","priyanka","kavita","vinod"]
#     def __init__(self,accountnumber,name,balance):
#         self.accountnumber=accountnumber
#         self.name=name
#         self.balance=balance
#         if accountnumber in self.accountnumbers:
#             print("welcome to the bank")
#             print("total bank balance",self.balance)
#         else:
#             print("please enter the valid account number")   
#     def deposite(self,deposite_bal):
#         self.deposite_bal=deposite_bal
#         print("deposite amount",self.deposite_bal)
#         total=self.deposite_bal+self.balance
#         print("total amount is present after deposite",total)
#     def withdrawal(self,withdrawal_amount):
#         self.withdrawal_amount=withdrawal_amount
#         print("withdraw amount",self.withdrawal_amount)
#         print("after withdraw amount total ",(self.deposite_bal+self.balance)-self.withdrawal_amount)
#     def bank_fees(self):
#         self.bank_fees=self.withdrawal_amount
#         fees=(self.withdrawal_amount/100)*5
#         print("amount charges fees bank",fees)
# obj1=bankaccount("1213","varun",900)       
# obj1.deposite(400)     
# obj1.withdrawal(600)
# obj1.bank_fees()
    

# def fact(num):
#     if num==0 :
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fact(num-1)+fact(num-2)
# num=int(input("enter the value of number"))
# for i in range(0,num+1):    
#     print(fact(i))    



class computation:
    # listdiv=[]
    def factorial(self,number):
        self.number=number
        def fact(number):
                if number==0:
                    return 0
                elif number==1:
                    return 1
                else:
                    return fact(number-1)+fact(number-2)
        for i in range(0,number):        
            print(fact(i))
    def sum(self,num1,num2):
         self.num1=num1
         self.num2=num2
         print("sum of two number num1 and num2 result:",self.num1+self.num2) 
    def testprime(self,prime_num):
        self.prime_num=prime_num
        for i in range(2,self.prime_num):
              if self.prime_num%2==0:
                   print("this number is not prime number")
                   break
        else:
             print("this number is prime number")     
    def table_multiply(self,table_number):
         for i in range(1,10+1):
              print(f"table number {table_number} * {i} = {table_number*i}")    
    def alltable_multiply(self,alltable_number):
         for i in range(1,10+1):
                print(f"table number {alltable_number} * {i} = {alltable_number*i}") 
    def listdiv(self):
         listdiv=[1,2,3,4,5,6,7,8,9]
         list1=[]
         list_prime=[]
         for i in listdiv:
              if i%2==0:
                   list1.append(i)   
         print("listdiv",list1) 
         for i in listdiv:
              if int(i)%2==0:
                   pass
         else:
              list_prime.append(i)     
         print(list_prime)      

obj1=computation()
obj1.factorial(10)
obj1.sum(20,30)
obj1.testprime(8)
obj1.table_multiply(100000)
obj1.alltable_multiply(10)
obj1.listdiv()