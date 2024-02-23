# # # # # # # # # # # operator symbol and cammand number of operation perform
# # # # # # # # # # # 1 arithmetic operator (+,-,*,/)
# # # # # # # # # # # 2 logical operator (and ,not ,or)
# # # # # # # # # # # 3 comparision operator (==,=>,=< etc)
# # # # # # # # # # # 4 bitwise operator
# # # # # # # # # # # 5 membership  operator
# # # # # # # # # # # 6 identify operator
# # # # # # # # # # # 7 assignment  operator
# # # # # # # # # # i=3
# # # # # # # # # # j=30
# # # # # # # # # # print(i is j)
# # # # # # # # # # print(i is not j)
# # # # # # # # # ### flow control
# # # # # # # # #      # conditional flow control
# # # # # # # # #          # if block
# # # # # # # # #          # if else block 
# # # # # # # # #          # if elif block
# # # # # # # # #          # nested if block
# # # # # # # # #      # looping flow control
# # # # # # # # #          # while loop block
# # # # # # # # #          # while else block
# # # # # # # # #          # nested while 
# # # # # # # # #          # for block     
# # # # # # # # #          # for else block
# # # # # # # # #          # nested for block
# # # # # # # # # per =int(input("enter the percentage marks\n"))
# # # # # # # # # if per>=60:
# # # # # # # # #     print("first division")
# # # # # # # # # elif per>=45 and per<60:
# # # # # # # # #     print("second division")
# # # # # # # # # elif per>=33 and per<45:
# # # # # # # # #     print("third division")
# # # # # # # # # else:
# # # # # # # # #     print("fail")            coaching
# # # # # # # # n=int(input("enter the number\n"))
# # # # # # # # if n>=0:
# # # # # # # #     if n%2==0:
# # # # # # # #         print("even")
# # # # # # # #     else:
# # # # # # # #         print("odd")    
# # # # # # # ###### loops - block use to repeat the statement execution
# # # # # # # # print("hello")
# # # # # # # # for i in range(100):
# # # # # # # #     print("hello") multiple time print to the program
# # # # # # # # (1) while loop
# # # # # # # # i=1
# # # # # # # # while(i<=10):
# # # # # # # #     print("hello world")
# # # # # # # #     i+=1
# # # # # # # # (2) for loop
# # # # # # # n=int(input("enter value"))
# # # # # # # i=1
# # # # # # # while(i<=n):
# # # # # # #     if n%i==0:
# # # # # # #         print(i,"factor",end=" ")
# # # # # # #     i+=1    
n=int(input("enter value"))
count=0
i=1
while(i<=n):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not prime")           
# # # # # wap sum natural number
# # # # s=0
# # # # i=1
# # # # while i<=10:
# # # #     s=s+i
# # # #     i+=1
# # # # print("sum",s)
# # # # factorial wap 
# # # f=1
# # # n=int(input("enter the value factorial number\n"))
# # # while(n>=1):
# # #     f=f*n
# # #     n-=1
# # # print("factorial value",f)  
# # # s=0  
# # # n=1
# # # while n<=5:
# # #     u=int(input("enter the value"))

# # #     s=u+s
# # #     n+=1
# # # print(s)    
# # # break statement
# # # i=1
# # # while i<=10:
# # #     print(i)
# # #     if i==5:
# # #         break
# # #     i+=1
# # # #  continue statement
# # # i=1
# # # while i<=10:
# # #     i+=1
# # #     if i==3 or i==5 or i==7:
# # #         continue
# # #     print(i)
# # # s=0
# # # n=1
# # # while n<=5:
# # #     n+=1
# # #     u=float(input("enter"))
# # #     if u<0:
# # #         continue
# # #     s=s+u
# # # print(s)
# # n=10
# # i=2
# # while i<n:
# #     if n%i==0:
# #         print(n,"m is prime")
# #         break
# #     i+=1
# # else:
# #     print(" not prime number",n)      
# # nested loop
# n=1
# while n<=100:
#     i=2
#     while i<n:
#         if n%i==0:
#             break
#         i+=1
#     else:
#         print(n)
#     n+=1
# n=17
# i=2
# while i<n:
#     if n%i==0:
#         print(" not prime")
#         break
#     i+=1
# else:
#     print(" prime")
            





    
