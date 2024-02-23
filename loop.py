# # # # # # # # # # # # # # # n=int(input("enter the number user\n"))
# # # # # # # # # # # # # # # # i=2
# # # # # # # # # # # # # # # # while i<n:
# # # # # # # # # # # # # # # #     if n%i==0:
# # # # # # # # # # # # # # # #         print(" not prime",n)
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print("  prime",n)                                        
# # # # # # # # # # # # # # # # sum=0
# # # # # # # # # # # # # # # # n=int(input("enter the number"))
# # # # # # # # # # # # # # # # i=0
# # # # # # # # # # # # # # # # while i<=n:
# # # # # # # # # # # # # # # #     sum=sum+i
# # # # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # # # # print("sum natural number=",sum)    
# # # # # # # # # # # # # # sum=0
# # # # # # # # # # # # # # n=int(input("enter the value\n"))
# # # # # # # # # # # # # # i=0
# # # # # # # # # # # # # # while i<=n:
# # # # # # # # # # # # # #     sum=sum+i
# # # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # # # print("natural all number=",sum)      
# # # # # # # # # # # # # divisible by 5 
# # # # # # # # # # # # # n=550
# # # # # # # # # # # # # i=1
# # # # # # # # # # # # # while i<=n:
# # # # # # # # # # # # #     if i%5==0 and i<=150:
# # # # # # # # # # # # #         print("divisible by 5 =",i)
# # # # # # # # # # # # #     i+=1
# # # # # # # # # # # # n=5
# # # # # # # # # # # # digit=0
# # # # # # # # # # # # i=1
# # # # # # # # # # # # while i<=n:
# # # # # # # # # # # #     digit=i
# # # # # # # # # # # #     i+=1
# # # # # # # # # # # # print("total number of digit=",digit)    
# # # # # # # # # # # # calculate the sum of natural number
# # # # # # # # # # # fac=1
# # # # # # # # # # # i=1
# # # # # # # # # # # n=int(input("enter the number input\n"))
# # # # # # # # # # # while i<=n:
# # # # # # # # # # #     fac=fac*i
# # # # # # # # # # #     i+=1
# # # # # # # # # # # print("factorial number=",fac)    
# # # # # # # # # # table=5
# # # # # # # # # # i=1
# # # # # # # # # # while i<=10:
# # # # # # # # # #     result=table*i
# # # # # # # # # #     print("table ",table,"*",i,"=",result)
# # # # # # # # # #     i+=1
# # # # # # # # # n=55
# # # # # # # # # a=0
# # # # # # # # # b=1
# # # # # # # # # i=0
# # # # # # # # # print(a)
# # # # # # # # # print(b)
# # # # # # # # # while i<=n:
# # # # # # # # #     c=a+b
# # # # # # # # #     a=b
# # # # # # # # #     b=c
# # # # # # # # #     print(c)
# # # # # # # # #     i+=1
# # # # # # # # # # print(a)
# # # # # # # # # # print(c)    
# # # # # n=5
# # # # # for i in range(6):
# # # # #     print("* "*(i))
# # # # #     # for j in range(5):
# # # # # for i in range(5):
# # # # #     print("* "*(n-i-1))    
# # # # # # n=6
# # # # # # # i=0
# # # # # # # while i<n:
# # # # # # #     i+=1
# # # # # # #     if i==3 or i==6:
# # # # # # #         continue
# # # # # # #     print(i)
# # # # # # a=0
# # # # # # b=1
# # # # # # print(a,b,end=" ")
# # # # # # while True:
# # # # # #     c=a+b
# # # # # #     if c>=50:
# # # # # #         break
# # # # # #     print(c, end=" ")
# # # # # #     a=b
# # # # # #     b=c
# # # # n=4
# # # # while True:
# # # #     i=int(input("enter the value of guess \n"))
# # # #     if n==i:
# # # #         print("right value guess")
# # # #     else:
# # # #         print("try again")    

# # # row=1
# # # while row<=5:
# # #     col=1
# # #     while col<=5:
# # #        print("*",end=" ")
# # #        col+=1
# # #     print()   
# # #     row+=1
    
# # # row=1
# # # while row<=5:
# # #     col=1
# # #     while col<=row:
# # #        print("*",end=" ")
# # #        col+=1
# # #     print()   
# # #     row+=1
# # row=1
# # while row<=5:
# #     col=1
# #     while col<=6-row:
# #        print("*",end=" ")
# #        col+=1
# #     print()   
# #     row+=1
# row=1
# while row<=5:
#     sp=1
#     while sp<=5-row:
#         print("",end=" ")
#         sp+=1
#     sp=1
#     while sp<=2*row-1:
#         print("*",end="")
#         sp+=1
#     print()      
#     row+=1
 
 

# div=5
# div=div//2 - 2
# div=div/2 - 2.5
# div=div%2 - 1
# print(div)


n=-5
# # div=n
# # # rem=n
# # i=0
# # a=""
# # while(i<3):
# #     div=div//2
# #     rem=div%2
# #     # print(div)
# #     print(rem)
# #     i+=1
# # print(a)    
# # b=" ".join(a)
# # print(b)
print(bin(n))






