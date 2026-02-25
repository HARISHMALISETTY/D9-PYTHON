# """
# operator:
# An operator is a symbol which tells python to perform the operation on or b/w
# values.
# 1.ARITHMETIC OPERATOR:
# +,-,*,/,//,%,**
# 2.ASSIGNMENT OPERATOR:
# =,+=,-=,*=,/=,//=,%=,**=
# 3.comparision (relational) operators-->output will be always boolean
# ==,<,>,<=,>=,!=
# 4.logical operators:
# when we want to compare/check multiple conditions. always returns boolen values
# and,or,not
# 5.membership operator
# in, not in --->returns boolen values. used to check presense of value in 
# string,list,tuple,dictionary.
# 6.identity operator--->is is not--->to compare two values based on value and their memory address
# python uses same memory object for numbers within range of -5 to 256.

# 7.bitwise operator-->and,or,not,xor,leftshift,rightshift

# and ---> &--->0 and 1s--->

# or--->|
# not-->~
# xor--->^
# leftshift--> <<
# rightshift---> >>

# 8.Ternary operator
# """
# # print(2+2) #4
# # print(2.5+3.6) #6.1
# # print((4+5j)+(3+8j)) #7+13j
# # print("hello"+"world") #helloworld
# # print(3+"hi") #unsupported operand- typeerror

# # print([1,2,3]+[4,5,7]) #[1,2,3,4,5,7]
# # print((1,4,7)+(2,5,8)) #(1,4,7,2,5,8)
# # print({1,4}+{2,6}) #unsupported
# # print({"name":"harish"}+{"city":"hyd"}) #unsupported

# # print(True+12) #13
# # print(False+2) #2

# # print(True+True) #2
# # print(True+False) #1
# # print(False+False) #0

# # print(None+None) #unsupported
# # print(True+"hello") #unsupported

# # print("hello"-"world") #unsupported
# # print([1,5,7]-[2,6,8]) #unsupported

# # print((2+5j)*(3+2j)) #-4+19j

# # print("hello"*"hello") #unsupported

# # print("hello"*3) #hellohellohello
# # print("hello"*3.5) #unsupported

# # print([1,2,3]*[3,5,6]) #unsupport
# # print([1,2,3]*4) #[1,2,3,1,2,3,1,2,3,1,2,3]
# # print((1,2)*2) #(1,2,1,2)
# # print({1,3}*2) #unsupported
# # print((4+5j)/2) #2+2.5j
# # print((4+6j)/(4+8j))
# # print([1,4,8]/[1,2,4]) #unsupported
# # print([1,2,3]/3) #unsupported

# # print(10//3) #gives 3 by ignoring decimal values
# # print(10%4) #2 gives reminder

# # print(3**3)
# # print("hello"**3) #unsupported
# # print([1,2,3]**2) #unsupported
 

# # x=5
# # print(x)

# # x**=2
# # print(x)

# # str1="hello"
# # str1+="hi"
# # print(str1)

# # list1=[1,2,3]
# # list1+=[3,4]
# # print(list1)
# # set1={4,5,6}
# # set1|={4,6}
# # print(set1)
# # print({1,9,3}<={1,4,6,10})

# #1.if any value except zero can treat as a truth value
# #2.zero,"",[],None,{} can be treat as a falsy value.

# # print(True and True)
# # print(False and True)
# # print(True or True)
# # print(False or False)
# # print(False and "") # False 
# # print("" and True) #""
# # print(True and "") #""
# # print(True and 2) #2
# # print(True and -2) #-2
# # print(False and 0)
# # print(False and [])
# # print([] or [1,2,3])
# # print([1,5,6] and [1,6,8])

# # ip=2
# # list1=[1,5,8,9]
# # print(ip in list1)
# # student_name='prabhas'
# # students={'mineesh','madhu','omkar','divya','mani','pavitra'}
# # print(student_name not in students)


# # dict1={"name":"mineesh","city":"hyd","age":20,"gender":"male"}

# # print("mineesh" not in dict1)

# # str="something"
# # char="e"
# # print(char not in str)

# # optimization..??


# # x=5
# # y=6
# # z=7
# # a=7
# # b=6
# # c=5

# # x=int(458) 
# # y=int(458)

# # print( x is y)

# # 1 0001
# # 2 0010
# # 3 0011 
# # 4 0100
# # 5 101
# # 6 0110
# # 7 0111 
# # 8 1000
# # 9 1001
# # 10 1010

# # print(bin(50))
# #bitwise and &
# # 1.2&2-->?

# # print(7|5)

# # print(5^6)
# #&-->if both are one then only one otherwise zero
# # |--->if anyone is one then gives one otherwise zero
# # ^-->if both are different then gives one otherwise gives zero
# # ~-->this will inverts the given binary value by following 2's complement
# #here python will understand and writes the formula like -(x+1)
# # print(~10)
# #left shift--->4<<2
# #right shift

# # print(10<<2)
# # print(bin(40))
# # print(10>>2)

# #ternary-->assign value based on the condition
# #Truth-value if True else Falsy-value

# # x=5 if True else 6

# # print(x)


# # is_login=False 
# # login_status="loggedin" if is_login else "logged out"
# # #login_status="loggedin" if True else "logged out"
# # print(login_status)

# #give the feedback for the company based on the rating either excellent or good

# # rating=6
# # company_feedback="Excellent" if rating>4.5 else "good"
# # print(company_feedback)

# #whenever to execute condtional statements in simple and shorter way then we can use this ternary operator


# #check given num is even or odd


# # num=52102
# # op="even" if num%2==0 else "odd"
# # print(op)
# # op="even" if num&1==0 else "odd"
# # print(op)
# # str=str(num)
# # ld=str[-1]
# # seq=['0','2','4','6','8']
# # op="even" if ld in seq else "odd"
# # print(op)

# # rating=5
# # op="excellent" if rating>=4.5 else ("good" if rating >= 3.75 else "average") 
# # print(op)

# #extend this code to print below average and poor

# #nested ternary operator

# # print(~7)
# # print(4<<3)
# # print(5>>4)



# # #1.as per the salary need to categorize the employee.
# # 1.salry is greaterthan or equal to 1lkh-->senior level
# # 2.slry is lessthan 1lkh and greater than 60k-->medium level
# # 3.slry is lessthan 60k and greater than 25k--->beginner level 


# salary=int(input("enter the salary amount :"))
# # category="SENIOR" if salary>=100000 else "MEDIUM" if salary>=60000 else "BEGINNER" if salary >=25000 else "no job"
# # print(category)

# # print("SENIOR") if salary>=100000 else print("MEDIUM") if salary>=60000 else print("BEGINNER") if salary >=25000 else "no job"

# x=7
# print(~x)
print(bin(3))