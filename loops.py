# #whenever we need to implement as per the dataset-->we can consider size of the data

# # list=["tank1","tank2","tank3","tank4"]

# # for x in list:
# #     print(f"filling the water in {x}")


# # students=["pooja","harigopal","aishwarya","sohail","dhakshayani","umamahesh"]
# # count=0
# # for student in students:
# #     count+=1
# #     print(f"{student} index is {count-1}")

# # list=[1,2,3,4,5,6,7,8,9,10]
# # for num in list:
# #     print(f"2 x {num}={num*2}")


# # student_info=[
# #     {"name":"pooja","rollno":"16g34a0456"},
# #     {"name":"harigopal","rollno":"16b12a0678"},
# #     {"name":"aishwarya","rollno":"16g34a0457"}
# #     ]
# # for student in student_info:
# #     print(student["name"])



# #dataset of 10 students with marks with 3 toppers, 3 average student,4 below average

# students = [
#      {"id": 1, "name": "Sneha", "score": 72},
#     {"id": 2, "name": "Vikas", "score": 65 },
#     {"id": 3, "name": "Amit", "score": 92 },
#     {"id": 4, "name": "Priya", "score": 88},
#     {"id": 5, "name": "Rahul", "score": 81 },
#    {"id": 6, "name": "Ravi", "score": 28},
#     {"id": 7, "name": "Suman", "score": 15},
#     {"id": 8, "name": "Neha", "score": 58},
#     {"id": 9, "name": "Kiran", "score": 45},
#     {"id": 10, "name": "Pooja", "score": 39},
    
# ]
# for student in students:
#     if student["score"]>=90:
#         # print(student,"high level")
#         student["status"]="hihg-level"
#     elif student["score"]>=75:
#         # print(student,"medium-level")
#         student["status"]="medium level"
#     else:
#         # print(student,"low-level")
#         student["status"]="low-level"
# print(students)

#take list of reels information based on few categories
#movies,travel,tech,food,cringe with reelid,likescount,category,
#need to add new property status with super-viral/viral/general as per the below
# #conditions
# 1.likes >=20k then super-viral 
# 2.likes>=10k then viral 
# 3.likes<=10k then general 

#i want to iterate or perform some task based on my requirement then i can use range
# for x in range(start,end,step):

#print numbers from 1 to 10 by skipping every 3 values

# for x in range(0,10):
#     print(x+1)

# for x in range(0,10,3):
#     print(x)

# num=int(input("enter a num :"))
# for x in range(1,11):
#     print(f"{num} x {x} = {num *x}")

#print numbers from 1 to 30

#if num is divisible by 2 then print num-fizz
#if num is divisible by 5 then print num-buzz
#if num is divisible by 2 and 5 then print num fizz-buzz

# for x in range(2,5,2):
#     print(x)

# #1.to print numbers from 10 to 40
# for x in range(10,41):
#     print(x)

#step value is considering +1 by default.


#to print from 40 to 10
# for x in range(40,9,-1):
#     print(x)

#sum of all numbers from 1 to 10
# sum=0
# for x in range(1,11):
#     sum=sum+x
#     # print(x)
# print(sum)

#sum of squares of all numbers from 1 to 10
# sum=0
# for x in range(1,11):
#     sum=sum+x**2
#     # print(x)
# print(sum)

#print squares of all numbers in given range

# 5-->10

# square of 5 is 25
# square of 6 is 36
# square of 7 is 49
# square of 10 is 100


# starting_value=int(input("enter the start value : "))
# ending_value=int(input("enter the end value : "))

# for i in range(starting_value,ending_value+1):
#     print(f"square of {i} is {i**2}")

#print only vowels in given string
# str1="data science"
# seq='aeiouAEIOU'
# count=0
# for char in str1:
#     if char in seq:
#         count+=1
#         print(char)
# print(f"{count} vowels are available in the given string")

# str='madam'

# str1='seven-hours'
#print characters in reverse 

# for char in range(len(str1)-1,-1,-1):
#     print(str1[char])


#reverse a string and print it
# rev=""
# for char in range(len(str1)-1,-1,-1):
#     print(char)
#     rev+=str1[char]
# print(rev)
# if(str1==rev):
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")


# set1={4,5,6,'hello','hii',12,13}
# for x in set1:
#     print(x)

# for x in range(len(set1)-1,-1,-1):
#     # print(set1[x])
#     print(x)

#we can't access values in the set using indexes

#while loop:
"""
when we need to execute statements in a loop until condition becomes true, then we can go for while loop.
when count of iteration is not known then we can go for while loop.
syntax:

while condition:
    set of statements


this will executes the statement in a loop or infinite loop until condition becomes fail.
"""

# for num in range(1,11):
#     print(num)


#with in the syntax of for loop we have where we start and where we stop.
#if in while loop--->starting and updating rules we need to write seperately.which are not part of the syntax
# num=1
# while(num<=10):
#     print(num)
#     num+=1

# num=1
# while True:
#     print(num)

str1="welcome"
# x=0
# while x<=len(str1)-1:
#     print(str1[x])
#     x+=1


# x=len(str1)-1
# while x>=0:
#     print(str1[x])
#     x-=1

# rev=""
# x=len(str1)-1
# while x>=0:
#     # print(str1[x])
#     rev+=str1[x]
#     x-=1

# x=6--->x>=0-->rev='e'--->x=5
# x=5--->x>=0-->rev='em'-->x=4
# x=4--->x>=0--->rev='emo'-->x=3
# x=3-->x>=0-->rev='emoc'-->x=2
# x=2--->x>=0--->rev='emocl'-->x=1
# x=1--->x>=0-->rev='emocle'-->x=0
# x=0-->x>=0--->rev='emoclew'--->x=-1
# x=-1--->x>=0-->ends

# num=1254

num=1254
ld1=num%10
print("ld1 :",ld1)
rn1=num//10
print("rn1:",rn1)

ld2=rn1%10
print("ld2 :",ld2)
rn2=rn1//10
print("rn2 :",rn2)


#implement this using while loop