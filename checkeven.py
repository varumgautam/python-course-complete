# e=int(input("enter the check even number\n"))
# c=e%2==0
# print("check the result even number = ",c)


# c=int(input("check the number is leap year or not leap year"))
# if c%4==0 and c%100!=0:
#     print("it is leap year")
# elif c%400==0:
#     print("it is leap year")
# else:
#     print("not leap year") 


# class tv:
#     samsung="version.2.2"
#     model="FG35TV"
#     model_name="highfy"
#     def __init__(self,name_customer,phone_number):
#         # self.samsung=samsung
#         self.name_customer=name_customer
#         self.phone_number=phone_number
#         print("detalis customer :","name :",self.name_customer,"phone number :",self.phone_number)
#     def service_center(self,repair_items):
#         # print("name :",self.name_customer,"phone number :",self.phone_number)
#         print("which items is repair :",repair_items)
#     def bill(self,bill_amount):
#         # self.bill_amount=bill_amount    
#         print("amount of repair :",bill_amount)    

# obj1=tv("varun","7701962630")
# obj1.service_center("plate")   
# obj1.bill("2000k")
# print(obj1.samsung,obj1.model,obj1.model_name)

            

# string=input("enter the string\n")
# a=string.split()
# st=[]
# for x in a:
#     c=len(x)
#     d=str(c)+x
#     st.append(d)
# t=" ".join(st)    
# print(t)




# a=int(input("enter the first number\n"))
# b=int(input("enter the second number\n"))
# c=int(input("enter the third number\n"))
# if a>=b and a>=c:
#     print("a is greater")
# elif b>=a and b>=c:
#     print("b is greater")
# elif a==b and a==b and a==c:
#     print("all are equal ")    
# else:
#     print("c is greater")      




# num=int(input("enter the value of number\n"))
# # i=0
# a=1
# while(num>0):
#     a=a*(num)
#     # print(a)
#     num-=1
#     # i+=1
# print(a)


# def calculate(a,b):
#     try:
#         result=a/b
#         print("result ",result)
#     except ZeroDivisionError:
#         print("can't divide by zero number\n")   
# calculate(10,34)         


# def calculate(a,b):
#     try:
#         result=a/b
#         print("result ",result)
#     except ZeroDivisionError:
#         print("can't divide by zero number\n")  
#     except TypeError:
#         print("enter the number not str")     
#     except IndexError:    
#         print("v")
#     finally:
#         print("finaaaly eccepted")    
# calculate(10,"s")         



