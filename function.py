## functions ##
# definition of a process
   # to avoid repeatation of code 
   # to arrange the program
   # 
#  type of function
      # build in function  - which are already defined ex-print,max,min,len,etc
      # user defined function  - itself defined function (itself example type)
## step to br followed while using function:
  

  ## in built function:
          ## call the function
  ## user defined function:
          ## write the definition block
          ## call the function
# syntax #

# def display():
#     print("hello")
# display()    

# def display(a,b): - a,b is a parameter
#     print(a+b)
# display(5,3)    - argument 5,3 

# def evenodd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# evenodd(8)            
# evenodd(5)

# def multiply(a,b):
    # print(a*b)
# multiply(b=5,a=3) - # a,b is keyword argument    

# def multiply(a=1,b=1):
#     print(a*b)
# multiply()
# multiply(7)
# multiply(13,4)    

# def add(a,b):
#     print("add",a+b)
# add(a,b)     # local variable 


# def add(a,b):
#     global c
#     global d
#     c=a
#     d=b
#     print("addition",a+b)
# add(6,5)
# add(2,3)
# add(c,d)    # global variable

## prime number ##

# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     else:
#         return True
# print(prime(9))

## complete program ##


# arbitrary argument
# def getval(*val):
#     print(val)
# getval(1,2,3,3,3,4,4,5,5,5,)     #tuple format data strored


# keyword arbitrary argument

# def getval(**val):
#     print(val)
# getval(a=1,b=2,c=3)     #key :value pair data stored is dictionary format.


# def  getval(a,b,c):
#     print(a+b+c)
# l=[3,4,5]
# getval(*l)    #list *



# def  getval(a,b,c):
#     print(a+b+c)
# d={"a":2,"b":4,"c":3}    
# getval(**d)    #dictionary **


# def ismax(num1,num2,num3):
#     if num1>num2: 
#         if num1>num3:
#             return num1
#         else:
#             return num3  
#     elif num2>num3:
#         if num2>num1:
#             return num2
#         else:
#             return num1
#     else:
#         return  num3    
# print(ismax(2,1,3))                



# add list number 

# def valget(a,b,c,d,e):
#     return a+b+c+d+e
# l=[8,2,3,0,7]
# print(valget(*l))

# multiply of the 

# def valget(a,b,c,d,e):
#     return a*b*c*d*e
# l=[8,2,3,-1,7]
# print(valget(*l))


# reversed string questions

# def isstring(string):
#     s=string[::-1]
#     return s
# print(isstring("1234abcd")) # reverse the string program


# def factorial(num):
#     if num==1:
#         return num
#     else:
#         return (num)*factorial(num-1)
# print(factorial(4))    


# def isalphas(string):
#     d ={"upper":0,"lower":0}
#     for i in string:
#         if i.isupper():
#               d["upper"]+=1
#         elif i.islower():
#               d["lower"]+=1
#         else:
#              pass
#     print("upper",d["upper"])    
#     print("lower",d["lower"])
# isalphas("Varun is a Good Boy")  # upper and lower charracter count the string program






# def islist(l):
#     a=[]
#     for i in l:
#         if i not in a:
#             a.append(i)
#         else:
#             pass    
#     return a     
# #     print(a)        
# print(islist([1,2,3,3,3,4,5]))  # duplicate value remove the lists
                




# def isprime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     else:
#         return True    
# print(isprime(9))    # prime or not prime check program
        


# def iseven(number):
#     l=[]
#     for i in number:
#         if i%2==0:
#             l.append(i)
#         else:
#             pass    
#     return l
# print(iseven([1,2,3,4,5,6,7,8,9])) # accepted output -[2,4,6,8]
        











