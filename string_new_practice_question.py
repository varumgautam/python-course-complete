# # # # str=input("enter str\n") ### sorted string with function
# # # # out="".join(sorted(str))
# # # # print(out)

# # # # user=input("enter str\n") ###
# # # # s="".join(sorted(user))
# # # # print(s)

# # # # user=input("enter str\n") #without function loop reversed string
# # # # s=user[::-1]
# # # # for i in s:
# # # #     print(i)

# # # # user=input("enter str\n") #reversed loop string
# # # # s=reversed(user)
# # # # for i in s:
# # # #     print(i)

# # # # logic string reversed loop
# # # # user="varun"
# # # # string=""
# # # # i=len(user)-1
# # # # while i>=0:
# # # #     string=string+user[i]
# # # #     i-=1
# # # # print(string)    


# # # # str=input("enter the str\n") ## reversed words string
# # # # s=str.split()
# # # # # print(s)
# # # # s1=s[::-1]
# # # # # print(s1)
# # # # output=" ".join(s1)
# # # # print(output)



# # # # user=input("enter the str\n")
# # # # s=user.split()
# # # # # print(s)
# # # # s1=s[::-1]
# # # # # print(s1)
# # # # output=" ".join(s1)
# # # # print(output)



# # # # user=input("enter the str\n")
# # # # out=" "
# # # # s=user.split()
# # # # print(s)
# # # # for i in s:
# # # #     st=len(i)
# # # #     # out=" "join(str)
# # # #     # print(st)
# # # #     output=" ".join(s)    
# # # #     out=out + (str(st)+output)
# # # # print(out)


# # # # user="varun gautam" ## internal reversed words ##
# # # # s=user.split()
# # # # s1=[]
# # # # print(s)
# # # # for i in s:
# # # #     s1.append(i[::-1])
# # # # output=" ".join(s1)    
# # # # print(output)    
# # # # print(s1)


# # s="one two three four five six"
# # l=s.split()
# # i=0
# # l1=[]
# # while i>len(l):
# #     if i%2==0:
# #         l1.append(l[i])
# #     else:
# #         l1.append(l[i][::-1]) 
# #     i=i+1
# # print(l1)        

# # # s="one two three four five six"
# # # l=s.split()
# # # i=0
# # # l1=[]
# # # while i>len(l):
# # #     if i%2==0:
# # #         l1.append(l[i])
# # #     else:
# # #         l1.append(l[i][::-1]) 
# # # #     i=i+1
# # # # print(l1)        
# # # # print(l)

# # # user="varungautam"
# # # i=0
# # # while i<len(user):
# # #     print(user[i])
# # #     i=i+2
# # # # print(s1)    
# # # print("\n")
# # # i=1
# # # while i<len(user):
# # #     print(user[i])
# #     # i=i+2

# # user="varungautam"
# # s=user[0::2]
# # print(s)


# # s1="varun"
# # s2="jatin"
# # print(s1+s2)



# # merge string altenative ## WAP 

# # str1="varun"
# # str2="jatin"
# # i,j=0,0
# # output=" "
# # while i<len(str1) or j<len(str2):
# #     if i<len(str1):
# #         output=output+str1[i]
# #         i+=1
# #     if j<len(str2):
# #         output=output+str2[j]
# #         j+=1
# #     i+=1
# #     j+=1
# # print(output)    


# # string count in first numeric with string print#


# # str1="varun jatina"
# # s=str1.split()
# # print(s)
# # # l=len(s[1])
# # output=[]
# # l=""
# # i=0
# # while i<len(s):
# #     l=len(s[1])
# #     l.append(s[i])
# #     i+=1
# # print(str(l)+output)
# # print(l) not solved error this questions#

# # lenth=len(str1)
# # print(str(lenth)+str1)


    
# # user="v5ar2u1n"
# # alpha=[]
# # digit=[]
# # for ch in user:
# #     if ch.isalpha():
# #         alpha.append(ch)
# #     else:
# #         digit.append(ch)
# # output="".join(sorted(alpha)+sorted(digit))
# # print(output)

# # user="1vzy23vs"
# # output=sorted(user)
# # print(output)



# # a4b3c2 accepted input aaaabbbcc #

# str=str(input("enter str\n"))
# output=""
# for ch in str:
#     if ch.isalpha():
#         x=ch
#     else:
#         d=int(ch)
#         output=output+(x*4)
# print(output)        


