# # # # # # # # # # # # ht=float(input("enter height of person\n"))
# # # # # # # # # # # # if ht<140:
# # # # # # # # # # # #     print("dwarf")
# # # # # # # # # # # # elif  ht>=140 and ht<=170:
# # # # # # # # # # # #     print("average") 
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("tall")    
# # # # # # # # # # # # 2 second question    
# # x=int(input("enter first value x \n"))
# # y=int(input("enter second value y \n"))
# # z=int(input("enter third value z \n"))
# # if (x>y):
# #     if x>z:
# #         print("x greater")
# #     else:
# #         print("z greater")    
# # elif y>z:
# #     print("y greater")
# # else:
# #     print("z greater")            
# # # # # # # # # # n=int(input("enter value horizontal\n"))
# # # # # # # # # # m=int(input("enter value vertical\n"))
# # # # # # # # # # if (n>0 and m>0):
# # # # # # # # # #     print("first quadrant")
# # # # # # # # # # elif(n<0 and m>0):
# # # # # # # # # #     print("second quadrant")
# # # # # # # # # # elif(n<0 and m<0):
# # # # # # # # # #     print("third quadrant")
# # # # # # # # # # elif(n>0 and m<0):
# # # # # # # # # #     print("fourth quadrant")
# # # # # # # # # # else:
# # # # # # # # # #     print("orgin point")    
# # # # # # # # # roll_no=int(input("enter roll no\n"))
# # # # # # # # # name=input("enter name \n")
# # # # # # # # # marks1=int(input("enter first physics marks\n"))
# # # # # # # # # marks2=int(input("enter seocnd chemistry marks\n"))
# # # # # # # # # marks3=int(input("enter third math marks\n"))
# # # # # # # # # total_marks=marks1+marks2+marks3
# # # # # # # # # percentage=((marks1+marks2+marks3)/300)*100
# # # # # # # # # print("roll no\n",roll_no)
# # # # # # # # # print("name\n",name)
# # # # # # # # # print("three marks subjects physics,chemistry,math\n",marks1,marks2,marks3)
# # # # # # # # # print("total marks\n",total_marks)
# # # # # # # # # print("percentage",percentage)
# # # # # # # # # if percentage>=60:
# # # # # # # # #     print("first division")
# # # # # # # # # elif percentage>45 and percentage<60:
# # # # # # # # #     print("second division")
# # # # # # # # # else:
# # # # # # # # #     print("third division")    
# # # # # # # # side1=int(input("enter side 1\n"))
# # # # # # # # side2=int(input("enter side 2\n"))
# # # # # # # # side3=int(input("enter side 3\n"))
# # # # # # # # if side1==side2 and side2==side3:
# # # # # # # #     print("equilateral")
# # # # # # # # elif side1==side2 and side1!=side3 and side2!=side3:
# # # # # # # #     print("isosceles")
# # # # # # # # else:
# # # # # # # #     print("scalene")      
# # # # # # # triangle1=int(input("enter 1 value of triangle\n"))
# # # # # # # triangle2=int(input("enter 2 value of triangle\n"))
# # # # # # # triangle3=int(input("enter 3 value of triangle\n"))
# # # # # # # if triangle1==triangle2 and triangle1==triangle3:
# # # # # # #     print("it is valid triangle")
# # # # # # # else:
# # # # # # #     print("not valid triangle")    
# # # # # # char=input("enter the value \n")
# # # # # # if (char.isaplpha()):
# # # # # #     print("alphabet")
# # # # # # elif (char.isdigit()):
# # # # # #     print("digit")
# # # # # # else:
# # # # # #     print("spacial character")        
# # # # # char = input('enter your character : ')
# # # # # if((char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')):
# # # # #     print("The Given Character ", char, "is an Alphabet")
# # # # # elif(char >= '0' and char <= '9'):
# # # # #     print("The Given Character ", char, "is a Digit")
# # # # # else:
# # # # #     print("The Given Character ", char, "is a Special Character")
# # # # x=input("value")
# # # # if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'): 
# # # #     print("Vowel") 
# # # # else: 
# # # #     print("Consonant") 
# # # customer_id=int(input("enter customer id \n"))
# # # name=input("enter name of user\n")
# # # unit_user_consume=int(input("enter total unit \n"))
# # # if unit_user_consume<199:
# # #     print("paid amount of bill",unit_user_consume*(1.20),"no need paid surcharge")
# # #     print("total net bill payment amount",unit_user_consume*(1.20))
# # # elif unit_user_consume>200 and unit_user_consume<400:
# # #     print("total paid amount bill",unit_user_consume*(1.50),"no need surcharge amount paid") 
# # #     print("total net bill payment amount",unit_user_consume*(1.50))   
# # # elif unit_user_consume>400 and unit_user_consume<600:
# # #     print("total paid amount bill",unit_user_consume*(1.80),"surcharge amount paid ",(unit_user_consume*(1.80))*(0.15))
# # #     print("total net payment amount bill",unit_user_consume+(unit_user_consume)*(0.15))    
# # # else:
# # #     print("total amount bill  ",unit_user_consume*(2.0),"surcharge amount paid",(unit_user_consume*(2.0))*(0.15))  
# # #     print(" total net amount paid",(unit_user_consume*(2.0))+(unit_user_consume*(2.0))*(0.15))  
# # n=int(input("enter the num of month\n"))
# # if n==0 or n==2  or n==7 or n==8 or n==10 or n==12:
# #     print("month have 31 days")
# # elif n==3  or n==6 or n==9 or n==11 or n==5:
# #     print("month have 30 days")
# # else:
# #     print("month have 28 days")        
# n1=int(input("enter the value input number\n"))
# n2=int(input("enter the value input number\n"))
# user=input(" 1 addition\n 2 subtraction \n 3 multiplication\n 4 division\n")
#     if user=="1":
#         print("addition",n1+n2)
#     elif user=="2":
#         print("subtraction",n1-n2)
#     elif user=="3":
#         print("multiply",n1*n2)
#     elif user=="4":
#         print("division",n1/n2)         
#     else:
#         print("default value")



