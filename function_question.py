# # def ismax(num1,num2,num3):
# #     if num1>num2:
# #         if num1>num3:
# #             return num1
# #         else:
# #             return num3
# #     elif num2>num1:
# #         if num2>num3:
# #             return num2
# #         else:
# #             return num3
# #     else:
# #         return num3        
# # print(ismax(7,9,3))    


# # def issum(a,b,c,d):
# #     return a+b+c+d
# # l=[2,3,4,5]
# # print(issum(*l))



# # def issum(a,b,c,d):
# #     return a*b*c*d
# # l=[2,3,4,5]
# # print(issum(*l))


# # def isfactorial(num):
# #     if num==1:
# #         return 1
# #     else:
# #         return num*isfactorial(num-1)
# # print(isfactorial(4))    



# # def isstring(string):
# #     a=string[::-1]
# #     return a
# # print(isstring("1234varun"))


# def isalphachar(string):
#     d={"lower":0,"upper":0}
#     l=[]
#     l2=[]
#     for i in string:
#         if i.isupper():
#             d["upper"]+=1
#             l.append(i)
#         elif i.islower():
#             d["lower"]+=1
#             l2.append(i)
#     print("lower",d["lower"])
#     print("upper",d["upper"])
#     print(l)
#     print(l2)
#     print(d)
# isalphachar("Varun is Good Boy")    


# # def isunique(l):
# #     list=[]
# #     for i in l:
# #         if i not in list:
# #             list.append(i)
# #         else:
# #             pass
# #     return list   
# # print(isunique([1,2,3,3,3,4,5]))         



# # def isprime(l):
# #     list=[]
# #     for i in l:
# #         if i%2==0:
# #             list.append(i)
# #         else:
# #             pass
# #     return list 
# # print(isprime([1,2,3,4,5,6,7,8,9]))       
            


    

### properties of functions

# display=print
# display(1,2,3,4,4)

## nested function

# def outer():
#     def inner():
#         print("Inner function")
#     print("Outer function")
#     return inner
# f=outer()
# f(5)
# f(9)    


