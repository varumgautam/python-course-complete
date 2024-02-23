##  first question of star pattern ##
# n=4
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i>=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()            

## second question of star pattern ##

# n=6
# for i in range(1,n):
#     for j in range(1,n):
#         if i<=j:
#             print(n-j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()


## third question of star pattern ##

# l1=[1]
# l2=[]
# for row in range(1,1+int(input("enter the number of rows/n"))):
#     l2.append(l1[-1])
#     for e in l1:
#         l2.append(e+l2[-1])
#     print(l1)
#     l1=list(l2)
    # l2.clear()


## common string find to two characters ##

# str1="VARUNVARUN"
# s={}
# for i in str1:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(str(s))     



str1="naina"
str2="jataj"
s={}
for i in str1:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(str(s))            


