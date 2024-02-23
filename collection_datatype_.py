# # # # l=["varun",2,3,4,5,6,6,7,8]
# # # # # print[l[4::-1]]
# # # # # print(l[:3:-1]) 
# # # # # print(l[-2:])  
# # # # # print(l[4::-1])
# # # # # print(l[-1::1])
# # # # print(l[3:1:-1])#  [strt:end:step jump ]





# # # ###### 3D ARRAY PROGRAM DIMENESION  (3*4*6)
# # # l3=[]
# # # for z in range(3):
# # #     l2=[]
# # #     for y in range(4):
# # #         l1=[]
# # #         for x in range(6):
# # #             l1.append("*")
# # #         l2.append(l1)
# # #     l3.append(l2)
# # # print(l3) 



# # # multiply of list items program

# # l1=[1,2,3,4]
# # l2=len(l1)
# # i=1
# # sum=1
# # while i<=l2:
# #     sum=sum*i
# #     i+=1
# # print(sum) 


# ## largest numberof the list program smallest number of the list

# # l1=[1,2,3,4]
# # print(max(l1))


# # l1=[1,2,3,4]
# # print(min(l1))


# ## 
# # l1=[]
# # l2=len(l1)
# # if l2==0:
# #     print("list empty")
# # else:
# #     print("list not empty")    
# #  

# # duplicate element profram list remove 


# # l1=[1,1,323,323,34,1,34,1]
# # l2=[]
# # for x in l1:
# #     if x not in l2:
# #         l2.append(x)
# # print(l2)        

# #common 2 list items program
 
# # l1=[1,2,3,4,4,5,4]
# # l2=[1,7,2,7]
# # a=[]
# # for x in l1:
# #     if x in l2:
# #         a.append(x)
# # print(a)        


# # # if a>=1:
# #     print("common")
# # else:
# #     print("")    


# # l1=["red","green","white","black","pink","yellow"]
# # print(l1[1:4])

# #even number list itmen remove
# # l1=[1,2,3,4,5,6,34,52,55,65,43]
# # l2=[]
# # for x in l1:
# #     if x%2!=0:
# #         l2.append(x)
# # print(l2)            

# # import random
# # l1=[1,2,3,4,4,5,3,4,5]
# # random.shuffle(l1)
# # print(l1)

# l1=[1,1,2,2,3,4]
# l2=[1,2,34,4,5,6,7]
# # a=len(l1)
# # b=len(l2)
# # c=a-b
# # print(c)
    





# l1=["varun","jatin"]
# l2=""
# for x in l1:
#     l2=l2+x
# print(l2.replace(""," "))    


# l1=["varun","jatin"]
# for x in l1:
#     print(l1.index(x))

# l1=["varun","ngtxc"]
# l2=[]
# l2.append(l1)
# l2.append(l1)
# l2.append(l1)
# l3=[]
# l3.append(l2)

# print(l3)

# min max 2nd item big or small program of the list

# l1=[1,1,5,33,90,4,9,43,3,5,2,43,100]
# l2=max(l1)
# l1.remove(l2)
# l2=max(l1)
# print(l2)




# l1=[5,33,90,4,9,43,3,5,2,43,100]
# l2=min(l1)
# l1.remove(l2)
# l2=min(l1)
# print(l2)

## list unique item of the list



### frequency of the item is given list


# l1=[1,3,4,3,2,2,4,3,2,34,3]
# l2={}
# for x in l1:
#     if x in l2:
#         l2[x]+=1
#     else:
#         l2[x]=1    
# print(l2)





