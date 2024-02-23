#### oops-object oriented program structure.
    # class based programming.

###procedural oriented program structure.
   # c programming.

### class-collection of multiple function(method) and data(attributes).
   
###attributes--

      # class attribute  ---- created by class
      # instance attribute  --- created by instance

# ###instance/object ---- entity which access and modify the attributes and method of class.

# class Ducat:
#     courses=["python","data science","java","php"]
#     fees=[12000,15000,12990,7000,25000]
#     def councelling(self,name,course):
#         print("welcome councelling dept")
#         print("hello",name,"you have select",course)
#         self.name=name
#         if course in self.courses:
#             self.course=course


#             print("helllo ",name,)
#             self.f=self.fees[self.courses.index(course)]
#             print("your course fee is:",self.f)
#         else:
#             self.course=None
#             print("course not avaliable")    
#     def billing(self,course_fee):

#         print("welcome to billing ")    
#         if self.course is not None:
#             print("you have selected")
#             self.course_fee=course_fee
#             print("bal",self.f-self.course_fee)
#         else:
#             print("selected to valid course")
#         print("hellow",self.name)
#     def training(self):
#         print("hello welcome to training center",self.name)    

# obj1=Ducat()
# obj1.councelling("varun","python")
# obj1.billing(120)
# obj1.training()
# obj1=Ducat()
# print(obj1.courses)
# obj2=Ducat()
# print(obj2.fees)



# list1=[1,"a",3,4,"j"]
# list2=["varun","jarin","ajeet","sahil","shivam"]
# dic={}
# for i in range(0,len(list1)+1):
#     dic[list1[i-1]]=list2[i-1]
# print(dic)    
# # c=dict(zip(list1,list2))
# # print(c)



# class ducat():
#     def __init__(self,name,course):
#         print("welcome to ducat")
#         self.name=name
#         if course in self.course:
#             print("hello")
#             self.f=self.fees[self.courses.index(course)]
#             print("your course fees:",self.f)
#         else:
#             self.course=None
#             print("course not avalible")    
#     def __del__():
#         print("data erased")        




