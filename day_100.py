# # # # # # # # # # # # # # # # # # # # # # # # # # # # a=int(input("enter the number\n"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # b=int(input("enter the number second\n"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # c=a+b
# # # # # # # # # # # # # # # # # # # # # # # # # # # # print("add to number:",c)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # task1 complete
# # # # # # # # # # # # # # # # # # # # # # # # # # # # next task runnning
# # # # # # # # # # # # # # # # # # # # # # # # # # # a=int(input("enter the square roots\n"))
# # # # # # # # # # # # # # # # # # # # # # # # # # # c=a*a
# # # # # # # # # # # # # # # # # # # # # # # # # # # print("square root number:",c)
# # # # # # # # # # # # # # # # # # # # # # # # # # b=12
# # # # # # # # # # # # # # # # # # # # # # # # # # h=12
# # # # # # # # # # # # # # # # # # # # # # # # # # c=0.5*b*h
# # # # # # # # # # # # # # # # # # # # # # # # # # print("calculate triangle area:",c)
# # # # # # # # # # # # # # # # # # # # # # # # # a=12
# # # # # # # # # # # # # # # # # # # # # # # # # b=13
# # # # # # # # # # # # # # # # # # # # # # # # # a=b
# # # # # # # # # # # # # # # # # # # # # # # # # b=12
# # # # # # # # # # # # # # # # # # # # # # # # # c=b
# # # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # # print(c)
# # # # # # # # # # # # # # # # # # # # # # # # a=12
# # # # # # # # # # # # # # # # # # # # # # # # b=13
# # # # # # # # # # # # # # # # # # # # # # # # temp=a
# # # # # # # # # # # # # # # # # # # # # # # # a=b
# # # # # # # # # # # # # # # # # # # # # # # # b=temp
# # # # # # # # # # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # # # # # # # # a=12
# # # # # # # # # # # # # # # # # # # # # # # b=13
# # # # # # # # # # # # # # # # # # # # # # # a,b=b,a
# # # # # # # # # # # # # # # # # # # # # # # print(a,b)
# # # # # # # # # # # # # # # # # # # # # # a=int(input("enter the check positive or negative\n"))
# # # # # # # # # # # # # # # # # # # # # # if a>0:
# # # # # # # # # # # # # # # # # # # # # #     print("positive number")
# # # # # # # # # # # # # # # # # # # # # # elif a<0:
# # # # # # # # # # # # # # # # # # # # # #     print("negative number")
# # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # #     print("number is zero")        
# # # # # # # # # # # # # # # # # # # # # number=int(input("enter the check odd or even\n"))
# # # # # # # # # # # # # # # # # # # # # if number<0:
# # # # # # # # # # # # # # # # # # # # #     print("please enter the positive number")
# # # # # # # # # # # # # # # # # # # # # elif number%2==0:
# # # # # # # # # # # # # # # # # # # # #     print("number is even")
# # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # #     print("odd number")        
# # # # # # # # # # # # # # # # # # # # num=int(input("enter the year check the leap year \n"))
# # # # # # # # # # # # # # # # # # # # if num%400==0 and num%100==0:
# # # # # # # # # # # # # # # # # # # #     print("leap year")
# # # # # # # # # # # # # # # # # # # # elif num%4==0 and num%100!=0:
# # # # # # # # # # # # # # # # # # # #     print("leap year")
# # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # #     print("not leap year")        
# # # # # # # # # # # # # # # # # # # a=int(input("first number\n"))
# # # # # # # # # # # # # # # # # # # b=int(input("second number\n"))
# # # # # # # # # # # # # # # # # # # c=int(input("third number\n"))
# # # # # # # # # # # # # # # # # # # if a>b:
# # # # # # # # # # # # # # # # # # #     if a>c:
# # # # # # # # # # # # # # # # # # #         print("a is big")
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         print("c is big")    
# # # # # # # # # # # # # # # # # # # elif b>c:
# # # # # # # # # # # # # # # # # # #     print("b is big")
# # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # #     print("c is big")
# # # # # # # # # # # # # # # # # # # num=int(input("enter the number check prime or not"))
# # # # # # # # # # # # # # # # # # # count=0
# # # # # # # # # # # # # # # # # # # i=1
# # # # # # # # # # # # # # # # # # # while i<=num:
# # # # # # # # # # # # # # # # # # #     if num%i==0:
# # # # # # # # # # # # # # # # # # #         count+=1
# # # # # # # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # # # # # # # if count==2:
# # # # # # # # # # # # # # # # # # #     print(" prime")
# # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # #     print("not prime")    
# # # # # # # # # # # # # # # # num=int(input("enter the check prime or not number\n"))
# # # # # # # # # # # # # # # # i=2
# # # # # # # # # # # # # # # # while i<num-1:
# # # # # # # # # # # # # # # #     if num%i==0:
# # # # # # # # # # # # # # # #         print(" not prime",num)
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print("prime",num)
# # # # # # # # # # # # # # # # # import random
# # # # # # # # # # # # # # # # # num=random.randint(1,10)
# # # # # # # # # # # # # # # # # print(num)    
# # # # # # # # # # # # # # # lower=int(input("enter the first range number"))
# # # # # # # # # # # # # # # upper=int(input("enter the second range number"))
# # # # # # # # # # # # # # # for num in range(lower,upper+1):
# # # # # # # # # # # # # # #     if num>1:
# # # # # # # # # # # # # # #         for i in range(2,num):
# # # # # # # # # # # # # # #             if num%i==0:
# # # # # # # # # # # # # # #                 break
# # # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # # #             print(num)    
# # # # # # # # # # # # # # n=4
# # # # # # # # # # # # # # count=1
# # # # # # # # # # # # # # i=1
# # # # # # # # # # # # # # while i<=4:
# # # # # # # # # # # # # #     count=count*i
# # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # #     # print(count)
# # # # # # # # # # # # # # print(count)
# # # # # # # # # # # # # n=12
# # # # # # # # # # # # # for i in range(1,11):
# # # # # # # # # # # # #     print(f"{n}*{i} =",n*i)
# # # # # # # # # # # # n=10
# # # # # # # # # # # # a=0
# # # # # # # # # # # # b=1
# # # # # # # # # # # # i=0
# # # # # # # # # # # # print(a)
# # # # # # # # # # # # print(b)
# # # # # # # # # # # # while i<=n:
# # # # # # # # # # # #     c=a+b
# # # # # # # # # # # #     a=b
# # # # # # # # # # # #     b=c
# # # # # # # # # # # #     i+=1
# # # # # # # # # # # #     print(c)
# # # # # # # # # # # user=int(input("check the armstrong number\n"))
# # # # # # # # # # # sum=0
# # # # # # # # # # # temp=user
# # # # # # # # # # # # cube=
# # # # # # # # # # # while temp>0:
# # # # # # # # # # #     digit=temp%10
# # # # # # # # # # #     cube=digit**3
# # # # # # # # # # #     sum=sum+cube
# # # # # # # # # # #     temp=temp//10
# # # # # # # # # # # if user==sum:
# # # # # # # # # # #     print("yes armstrong number")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("no armstrong number")        
# # # # # # # # # # user=int(input("check armstrong number")) #153
# # # # # # # # # # # sum=0
# # # # # # # # # # # temp=user #153
# # # # # # # # # # # while temp>0:
# # # # # # # # # # #     digit=temp%10
# # # # # # # # # # #     cube=digit**3
# # # # # # # # # # #     sum=sum+cube
# # # # # # # # # # #     temp=temp//10
# # # # # # # # # # # if user==sum:
# # # # # # # # # # #     print("yes")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("no")        
# # # # # # # # # # lower=int(input("first  number\n"))
# # # # # # # # # # upper=int(input("second number\n"))
# # # # # # # # # # for num in range(lower,upper+1):
# # # # # # # # # #     order=len(str(num))
# # # # # # # # # #     sum=0
# # # # # # # # # #     temp=num
# # # # # # # # # #     while temp>0:
# # # # # # # # # #         digit=temp%10
# # # # # # # # # #         cube=digit**order
# # # # # # # # # #         sum=sum+cube
# # # # # # # # # #         temp=temp//10
# # # # # # # # # #     if num==sum:
# # # # # # # # # #         print(num)
# # # # # # # # # n=4
# # # # # # # # # sum=0
# # # # # # # # # i=1
# # # # # # # # # while i<=n:
# # # # # # # # #     sum=sum+i
# # # # # # # # #     # print(sum)
# # # # # # # # #     i+=1
# # # # # # # # # print(sum)    
# # # # # # # # # n=12
# # # # # # # # # i=1
# # # # # # # # # while n>=i:
# # # # # # # # #     if i%4==0:
# # # # # # # # #         print(i)

# # # # # # # # #     # print(divided)
# # # # # # # # #     i+=1
# # # # # # # # #         # print(i)
# # # # # # # # decimal=12
# # # # # # # # print(bin(decimal),"in binary")
# # # # # # # # print(oct(decimal),"in octal")
# # # # # # # # print(hex(decimal),"in hexadecimal")
# # # # # # # a="a"
# # # # # # # print(ord(a))
# # # # # # # print(chr(112))

# # # # # # # i=int(input("value of palindrome"))
# # # # # # # rev=0
# # # # # # # temp=i
# # # # # # # while i>0:
# # # # # # #     rev=(rev*10)+i%10
# # # # # # #     i=i//10
# # # # # # # if temp==rev:
# # # # # # #     print("palindrome yes")
# # # # # # # else:
# # # # # # #     print("not palindrome ")    
# # # # # # # a=input("enter the number")
# # # # # # # match a:
# # # # # # #     case "1":
# # # # # # #         print("yes")
# # # # # # #     case "2":
# # # # # # #         print("no")
# # # # # # #     case _:
# # # # # # #         print("default")        
# # # # # # # str=input("string\n")
# # # # # # # temp=str
# # # # # # # a=str[::-1]
# # # # # # # if temp==a:
# # # # # # #     print("palindrome str yes")
# # # # # # # else:
# # # # # # #     print("not palindrome str")    
# # # # # # # print(a)
# # # # # # num=int(input("enter the number find factor"))
# # # # # # for i in range(1,num+1):
# # # # # #     if num%i==0:
# # # # # #         print(i)
# # # # # n=4
# # # # # sum=0
# # # # # for i in range(1,n+1):
# # # # #     sum=sum+i
# # # # #     # print(sum)
# # # # # print(sum)    

# # # # def sum(num):
# # # #     if num<=1:
# # # #         return num
# # # #     else:
# # # #         return (num)+sum(num-1)     
# # # # print(sum(4))    
# # # def fibo(n):
# # #     if n<=1:
# # #         return n
# # #     else:
# # #         return fibo(n-1)+fibo(n-2)
# # # n=12
# # # for i in range(n):
# # #     print(i)    


# # def fac(n):
# #     if n<=1 or n==0:
# #         return n
# #     else:
# #         return n*fac(n-1)
# # print(fac(4))    
    

# a=input("enter the str")
# str=a[::-1]
# if str==a:
#     print("yes palindrome")
# else:
#     print("not palidrome")    





  