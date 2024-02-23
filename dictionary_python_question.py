# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka"}
# d={}
# for x in sorted(dict):
#     d[x]=dict[x]
# print(d)    

# d={"one":1,"three":3,"four":4,"two":2}
# d1={}
# val=list(d.values())
# val_sort=sorted(d.values())
# key=list(d.keys())
# for x in val_sort:
#     ind=val.index(x)
#     key_s=key[ind]
#     print(key_s)
#     d1[key_s]=x
# print(d1)


# dict={0:10,1:20}
# dict[2]=30
# print(dict)
# dict.update({4:300})
# print(dict)


# dict1={0:10,1:20}

# dict2={2:34,3:45}

# dict3={4:101,5:220}
# # d={}
# # d.update({0:10,1:20,2:34,3:45,4:101,5:220})
# # print(d)
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)


# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}
# for i in dict:
#     print(i)



# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}
# for i in dict:
#     print(i,dict[i])


# dict1={0:10,1:20}
# dict2={2:34,3:45}
# dict1.update(dict2)
# print(dict1)


# dict={}
# n=int(input("enter the value:"))
# for i in range(1,n+1):
#     dict[i]=i**2
# print(dict)    


# dict2={2:34,3:45}
# print(sum(dict2))
# print(max(dict2))
# print(min(dict2))
# for i in dict2:
#     print(dict2[i]*i)




# dict2={2:34,3:45}
# a=dict2.values()
# print(sum(a))




# dict2={2:34,3:45}
# a=dict2.values()
# print(a)




# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#008000', '#0000FF']
# d=dict(zip(a,b))   #### zip format d=dict(zip(keys,values))
# print(d)  


# list=[(1,2),(3,4)]
# for i,j in list:
#     print(i,j)   #####  zip used this concepts



# dict2={2:34,3:45}
# print(dict2)
# if 2 in dict2:
#     del dict2[2]
# print(dict2)    





# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}
# print(dict.keys())
# print(dict.values())
# print(dict.items())




# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}
# # print(dict.pop(1))
# # print(dict.popitem())

# for i in dict.items():
#     print(i)


# dict={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}

# del(dict[1])
# print(dict)


# keys=[1,2,3,4,5]
# values=["varun","jatin","priyanka","mom","dad"]
# d=dict(zip(keys,values))
# print(d)

# keys=[1,2,3,4,5]
# values=["varun","jatin","priyanka","mom","dad"]
# d={}
# for x in range(len(keys)):
#     d[keys[x]]=values[x]
# print(d)




# dict={1:20,2:23,3:30,4:45}
# d={key:val for (key,val) in dict.items() if val%2==0}
# print(d)


# dict={1:20,2:23,3:30,4:45}
# dict["jatin"]=dict.pop(1)   ### dict[1]="varun" value only change
# print(dict)                 ### dict["varun"]=dict.pop(1) key remove change it this location

# dict={1:

# dict={1:{1:2,2:4}}
# dict[1][2]="varun"
# print(dict)


# dict={1:20,2:23,3:30,4:45}
# m=max(dict)



# dict1={9:90}
# dict2={1:"varun",4:"jatin",3:"mom",2:"priyanka",2:"priyanka"}
# dict3={"var":"u"}
# d={}
# for i in (dict1,dict2,dict3):
#     d.update(i)
# print(d)    
# # dict1.update(dict2)
# # dict1.update(dict3)
# # print(dict1)



# dict2={2:3,3:10}
# mul=1
# for i in dict2:
#     mul=mul*dict2[i]
# print(mul)    



# dict2={2:34,3:45}
# for i in sorted(dict2):
#     print(i,dict2[i])


# str1=input("enter the str \n")
# s1=str1.split()
# # print(s1)
# s2=s1[::-1]
# # print(s2)
# print(" ".join(s2))



# list1=[1,2,2,3,3,4,5,5,5,6,6]
# # a=list1.count(1)
# list2=[]
# # print(a)
# for i in list1:
#     if list1.count(i)==1:
#         list2.append(i)
# print(list2)   
# str1="i love you"
# str2=["varun","jatin"]
# print(" , ".join(str2))





# mystr="a,a,a,b,b,c,c,c"
# a="".join(mystr.replace(",",""))
# list1=list(a)
# d={}
# print(a)
# print(list1)
# for i in list1:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)         
# s3=" ".join(d)   
# print(s3)
# print("".join())    



# num=int(input("enter the number\n"))
# temp=num
# reverse=0
# while(temp>0):
#     reminder=temp%10
#     reverse=(reverse*10)+reminder
#     temp=temp//10
# print(reverse)    
# if num==reverse:
#     print("palin")
# else:
#     print("not")        




# n=10
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)    




# n=4
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
# print(sum)    



######### list,set and dictionary comprehension   #######
# list=[1,1,2,32,4]
# list1=[]
# for i in list:
#     list1.append(i**2)


# second method comprehension
# list1=[i**2 for i in list if i<=4]
# list=[x**2 if x<=3 else x**3 for x in l]
# print(list1)    

# l1=[y**2 for x in l for y in x]

# l=[[y**2 for y in x] for x in l]

## l=[[["*"for z in range(6)]for y in range(4)] for x in range(3)]

