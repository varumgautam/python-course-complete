# number=int(input("enter the check wheather prime or not prime\n"))
# num=1
# a=0
# while(num<=number):
#     if (number%num==0):
#         a=a+1
#     num+=1    
# if a==2:
#     print("prime")
# else:
#     print("not prime")  
# print(a)                  

# number=int(input("enter the check wheather prime or not prime\n"))
# for i in range(2,number):
#     if number%i==0:
#         print("not prime number")
#         break
# else:
#     print("prime number")        


# string=input("enter the string for the user type\n")
# a=string.split()
# i=0
# c=[]
# for x in a:
#     b=len(x)
#     d=str(b)+a[i]
#     c.append(d)
#     i+=1
# d=" ".join(c)    
# print(d)
# print(type(d)) # input - varun is good boy output-5varun 2is 4good 3boy

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i-j+1,end=" ")
#     print()    



# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         a=ord("A")
#         print(chr(a+n-i+j-1),end=" ")
#     print()    



# n=3
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         a=ord("A")
#         print(chr(a+i-1),end=" ")
#         j+=1
#     i+=1
#     print()


# n=3
# i=1
# ch=65
# while(i<=n):
#     j=1
#     while(j<=n):
#         a=ord("A")
#         print(chr(ch),end=" ")
#         ch+=1
#         j+=1
#     i+=1
#     print()


# n=3
# i=1
# while(i<=n):
#     j=1
#     while(j<=n):
#         a=ord("A")
#         print(chr(65+j+i-2),end=" ")
#         j+=1
#     i+=1
#     print()



# n=3
# i=1
# ch=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         a=ord("A")
#         print(chr(a+ch-1),end=" ")
#         ch+=1
#         j+=1
#     i+=1
#     print()





# n=4
# i=1
# # ch=1 
# while(i<=n):
#     j=1
#     while(j<=i):
#         a=ord("A")
#         print(chr(65+n-i+j-1),end=" ")
#         # ch+=1
#         j+=1
#     i+=1
#     print()


# n=3
# i=1
# ch=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         a=ord("A")
#         print(chr(a+n-i),end=" ")
#         ch+=1
#         j+=1
#     i+=1
#     print()    



# n=int(input("enter the value of number:\n"))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*(i),end=" ")
#     print()   


# n=5
# i=1
# while(i<=n):
#     print(" "*(n-i),"*"*(i),end=" ")
#     i+=1
#     print()




# n=5
# i=1
# while(i<=n):
#     print("*"*(n-i+1),end=" ")
#     i+=1
#     print()




# n=5
# i=1
# while(i<=n):
#     print(" "*(i-1),str(i)*(n-i+1),end=" ")
#     i+=1
#     print()




# n=4
# i=1
# while(i<=n):
#     print(" "*(n-i),str(i)*(i),end=" ")
#     i+=1
#     print()



# n=4
# i=1
# ch=1
# while(i<=n):
#     print(" "*(i-1),end="")
#     j=1
#     while(j<=n-i+1):
#         print((i+j-1),end="")
#         j+=1
#     i+=1
#     print()


# n=3
# i=1
# ch=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         a=ord("A")
#         print(chr(a+n-i),end=" ")
#         ch+=1
#         j+=1
#     i+=1
#     print()    




# n=4
# i=1
# ch=1
# while(i<=n):
#     print(" "*(n-i+1),end="")
#     j=1
#     while(j<=i):
#         print(ch,end="")
#         ch+=1
#         j+=1
#     i+=1
#     print()    




# n=4
# for i in range(1,n+1):
#     print(" "*(n-i+1),end="")
#     for j in range(1,i+1):
#         print((j),end="")
#     print()    



# # for i in range(1,n):
# #     # print(" "*(i-1),end="")   
# #     for j in range(1,i+1):
# #         print(j,end="") 
# #     print()    


# 1,2,3,4,5=15
# def issumnatural(num):
#     if num==0:
#         return 0
#     else:
#         return num+issumnatural(num-1)   # 5+sum(4) 4+sum(3) 3+sum(2) 2+sum(1) 1+0
    
# print(issumnatural(5))    

#0,1,1,2,3,5,8,13,21

# def fact(num):
#     if num==0 :
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fact(num-1)+fact(num-2)   #0,1,1,2
# a=int(input("enter the number\n"))
# for i in range(a):
#     print(fact(i))    #1+0 ,1+1











