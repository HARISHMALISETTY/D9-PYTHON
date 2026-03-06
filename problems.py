# """
# *
# *
# *
# *
# *
# """
# # for x in range(1,6):
# #     print('*')


# """ ***** """




# # for x in range(1,6):
# #     print('*',end=' ')


# """
# *****
# *****
# *****
# *****
# *****
# """
# # for i in range(1,6):
# #     for x in range(1,6):
# #         print('*',end=' ')
# #     print()
# """
# 11111
# 11111
# 11111
# 11111
# 11111

# """
# # for i in range(1,6):
# #     for x in range(1,6):
# #         print(1,end=' ')
# #     print()


# """
# 12345

# """
# # for x in range(1,6):
# #     print(x,end=' ')

# """
# 12345
# 12345
# 12345
# 12345
# 12345

# """
# for y in range(1,6):
#     for x in range(1,6):
#         print(x,end=' ')
#     print()
# """
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 

# """
# for y in range(1,6):
#     for x in range(1,6):
#         print(y,end=' ')
#     print()


# print(chr(97))

"""
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE

"""
# for y in range(1,6):
#     for x in range(65,70):
#         print(chr(x),end=' ')
#     print()
"""
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""

# for y in range(65,70):
#     for x in range(65,70):
#         print(chr(y),end=' ')
#     print()


"""
A B C
D E F
G H I

"""
# alphabet=65
# for y in range(5):
#     for x in range(5):
#         print(chr(alphabet),end=' ')
#         alphabet+=1
#     print()

"""

1 2 3
4 5 6
7 8 9

"""

# num=1
# for y in range(3):
#     for x in range(3):
#         print(num,end=' ')
#         num+=1
#     print()

# y=0-->x=0,1,2
# y=1-->x=0,1,2
# y=2-->x=0,1,2

"""

0 1 0
1 0 1
0 1 0

"""

# for x in range(3):
#     for y in range(3):
#         print((x+y)%2,end=' ')
#     print()

# x=0-->y=0,1,2
# x=1--->y=0,1,2
# x=2-->y=0,1,2

# print((0+0)%2)
# print((0+1)%2)
# print((0+2)%2)

# print((1+0)%2)
# print((1+1)%2)
# print((1+2)%2)

# print((2+0)%2)
# print((2+1)%2)
# print((2+2)%2)

"""
1 2 3
2 3 4
3 4 5


a b c
b c d
c d e


"""
# for y in range(3):
#     for x in range(1,4):
#         print(x+y,end=' ')
#     print()



# y->0-->x=1,2,3
# y-->1-->x=2,3,4
# y-->2-->x=1,2,3

# alphabet=96
# for y in range(3):
#     for x in range(1,4):
#         print(chr(x+y+alphabet),end=' ')
#     print()



# y-->0 x=1,2,3-->chr(1+0+96)=a chr(2+0+96)=b chr(3+0+96)=c 
# y-->1 x=1,2,3-->chr(1+1+96)=b chr(2+1+96)=c chr(3+1+96)=d
# y-->2 x=1,2,3--> chr(1+2+96)=c chr(2+2+96)=d chr(3+2+96)=e 


"""
1
12
123
1234
12345 

"""
# for y in range(1,6):
#     for x in range(1,y+1):
#         print(x,end='')
#     print()

# y=1-->x=0

# y=1--->x=1,2,3,4,5
# y=2-->x=1,2,3,4,5
# .
# .
# .
# y=5-->x=1,2,3,4,5

"""
1
22
333
4444
55555 

"""
# for y in range(1,6):
#     for x in range(1,y+1):
#         print(y,end='')
#     print()
# # y=1, x=1 print y -->1
# # y=2, x=1,2 print y--> 2 2
# # y=3, x=1,2,3 print y->3 3 3

"""
A
AB
ABC
ABCD
ABCDE
"""
# alphabet=64
# for y in range(1,6):
#     for x in range(1,y+1):
#         print(chr(x+alphabet),end='')
#     print()

"""
A
BB
CCC
DDDD
EEEEE

ip=['Hii','Hello','some','python','Java']

op=['iih','olleh','SOME','PYTHON','avaj']

without using predefined methods
"""

# 1.capitalize--->rev and lowercase 
# 2.lowercase--->uppercase
# ip=['Hii','Hello','some','python','Java']
# op=[]
# for char in ip:    
#     rev=''
#     if char[0]==char[0].upper():
#         for x in range(len(char)-1,-1,-1):            
#             rev+=char[x]        
#         op.append(rev.lower())
#     else:       
#         op.append(char.upper())
# print(op)

# ip=['some','happy','olive','theatre','show','zomato']
# op=['SOME','yppah','evilo','ertaeht','SHOW','ZOMATO']

# 4,5,5,7,4,6

str1=input('enter string 1 : ')
str2=input('enter string 2 : ')
count=0

# str1--->s 

# s covered 
# i covered 
# l covered 
# e covered



# if len(str1)!=len(str2):
#     print('Not anagram')
# else:
#     for i in range(len(str1)):
#         for j in range(len(str2)):
#             if str1[i]==str2[j]:
#                 str2=str2.replace(str2[j],'*')                
#                 count+=1 
#                 break   
#     if count==len(str2):
#         print('ANAGRAM')
#     else:
#         print('NOT ANAGRAM')

# s-->c=1 
# i-->c=2
# l--->c=3
# e-->c=3
# n-->c=4
# t-->c=6
# str1='happy'
# str2='hello'
# banana=b a n

# "abcd"--->print all the substrings of given string 
# a 
# ab 
# abc 
# abcd 
# b 
# bc 
# bcd 
# c 
# cd 
# d 
#count number of substrings can be done for given string
