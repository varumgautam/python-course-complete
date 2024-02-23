# # # # # # n=int(input("enter the number"))
# # # # # # i=1
# # # # # # count=0
# # # # # # while i<=n:
# # # # # #     if n%i==0:
# # # # # #         # print("no")
# # # # # #         count+=1
# # # # # #     i+=1    
# # # # # # if count==2:
# # # # # #     print("prime")
# # # # # # else:
# # # # # #     print("not prime")
# # # s="pythona12345"
# # # s1=0
# # # s2=0
# # # for x in s:
# # #     # print(x):
# # #     if 98=="a":
# # #         s1+=1
# # #     elif chr(48)=="1" and chr(57)>="9":
# # #         s2+=1      
# # # print("alphabet value",s1)         
# # # print("numerical value",s2)
# # # a=len(s)
# # # print(a)
# # # # n=6
# # # # i=0
# # # # while i<=6:
# # # #     i+=1
# # # #     if i==3 or i==5:
# # # #         continue
# # # #     print(i)
# # # s=input()
# # # for x in s[::-1]:
# # #     print(x,end=" ")
# # n=27
# # a=1
# # while a<=n:
# #     s=n%10  #5 a=5*10+d
# #     d=n//10 #1
# #     a=s*10+d
# # print(a)
# # display A to Z character
# for i in range(65,91):
#     print(chr(i))
user=input()
s1=0
s2=0
for i in user:
    while i<=2:    
        if str(i)>="a" and str(i)<="z":
            s1+=1
        elif str(i)>="0" and str(i)<="9":
            s2+=1
        else:
            print("not answer")   
print(s1,s2)             
