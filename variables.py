# # #a variable is a name of the container which stores a value/data/information
# # #why should we store the value into the variable?
# # #for reusing within the code itself.

# # x=25 #assigning 
# # x="hello" #re-assigning

# # print(x)

# # #variable name can startwith A-Z,a-z,_ but not with digits and any other special characters
# # #variable names are case sensitives
# # #should not contain any spaces
# # #should not use keywords as a varible names
# # #meaningfull variable names(name,gender,user_name) are preferrable 
# # #than normal names like x1,y1
# # #python will change the type of the variable automatically/dynamically as per the value we assigned.
# # #so python can be considered as a dynamically typed language 
# # #type()--->used to know the type of the value/data which is assigned to a variable.


# # student_name_1="akhil"
# # student_name_2="vijay"
# # student_name_3="rakesh"


# # student_1_roll_no=25
# # student_2_roll_no=26
# # student_3_roll_no=27
# # # print(type(student_3_roll_no))

# # student_3_roll_no="five"
# # # print(type(student_3_roll_no))


# # student_aggregate_1=9.5
# # student_aggregate_2=9.2
# # student_aggregate_3=9.1

# # #till now programmer was assigned value to the variable.but now i want to allow my user to give his value
# # #for that i can use input()
# # #value which we are taking through input method always considered as a string.


# # # first_name=input("enter firstname :")
# # # last_name=input("enter the lastname : ")
# # # print(first_name)
# # # print(last_name)

# # # print(first_name-last_name)


# # # value1=int(input("enter first value :"))
# # # value2=float(input("enter second value:"))

# # # print(value1)
# # # print(value2)
# # # print(value1+value2)


# # # a=5.7
# # # b=15
# # # c=a+b 
# # # print(c)
# # # print(type(c))

# # #c type is changing automatically as per the result.
# # #type conversion is happening internally, then this can be called implicit type conversion





# # #if we do type conversion manually then it can be called as explicit type conversion 

# # # int()--->converts string to integer
# # # x=25
# # # y=str(x)
# # # print(y,type(y))
# # # print(type(int(x)))
# # # float()--->converts string to float
# # # str()--->converts int/float to string 
# # # bool()--->generates boolean values

# # # x=" "
# # # y=bool(x)
# # # print(y)


# # # x=25--->bool(x) gives True
# # # x=-25--->bool(x) gives True
# # # x=0--->bool(x) gives False 
# # # x="hi"-->bool(x) gives True
# # # x=""--->bool(x) gives False 
# # # x=" "-->bool(x) gives True

# # x,y,z=2,3,4
# # print(x)
# # print(y)
# # print(z)

# # ip1="""Lorem Ipsum is simply dummy text 
# # of the printing and typesetting industry. 
# # Lorem Ipsum has been the industry's 
# # standard dummy text ever since the 1500s, 
# # when an unknown printer took a galley of type and scrambled it 
# # to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was 
# # popularised in the 1960s with the 
# # release of Letraset sheets containing 
# # Lorem Ipsum passages, and more recently
# #  with desktop publishing software like 
# #  \Aldus PageMaker including versions 
# #  of Lorem Ipsum"""
# # user_name="akhil"
# # role="manager"
# # location="hyd"
# # print(f"{user_name} is working as a {role} in {location}")


# # x="25"

# # #type conversion is happening internally-->implicit type conversion
# # #python is dynamically typed language

# # x=25
# # print(id(x))

# # x=35
# # print(id(x))

# # x=4
# # print(x)

# # print(id(x))
# # x=6
# # print(id(x))
# # print(x)



# # users=['harish','kiran']
# # print(id(users))
# # users.append('akhil')
# # print(id(users))

# # # id()--->it is a  method used to returns or show the identity or address or memory location of a value.

# # 1.int--->it is a pure numeric data which have whole numbers only.
# # eg:user mobile,user age,pincode,quantity(count),
# # eg:5,7,3923.

# # 2.float--->it is also a pure numeric value which contains decimal values
# # eg:quantity(weights),ratings,price.

# # 3.str-->group of characters which enclosed in b/w "".
# # eg:username,usergender,userpassword,labels,citynames,productnames...

# # 4.bool--->which contains truth values true/false.
# # eg:while checking conditions.
# # eg: is available?
# #     is active?
# #     like questioning.

# # 1.list--->[]
# # 2.tuple--->()
# # 3.sets --->{}
# # 4.dictionary-->{key:value}
# # 5.functions-->def 
# # 6.regex-->r""
# # 7.none-->None
# # 8.date time-->timezone


# """A list is a ordered collection of heterogeneous/homogenous data which is wrapped
#  b/w the [].
#  each value in the list can be called as element.
#  each element can be seperated with ,
#  list can be mutable.
#  allows duplicates.
#  every element in the list can be accessible with its respective index.
#  index will starts from always zero.
#  this will allow both positive indexing and negative indexing.
#  +ve-->starts from zero
#  -ve--->-1
#  stored in heap memory.

# """
# # for examples:
# #to store a multiple student names in single variable
# students=["umamahesh","harish","neelima","deva","divya","neelima","srinivas"]
# # print(len(students))
# # print(students[-4])
# # print(students[len(students)-4])
# # students[2]="devaraju"
# # print(students) #updating with positive indexing.
# #append
# # methodname(list_variable name) 
# #here we are passing entire list as a input
# # list_variable_name.method()
# #here we are passing a new values as a inputs to be apply for the list
# # students.append("nagarjuna")
# # print(students)

# # students.remove("neelima") #removes the first matched neelima
# # print(students)

# students.extend(["vijay","rashmika","samantha","nani"])
# print(students)

# #using extend method we can add more elements that should be pass as a list.
# students.pop() #this will removes last element by default.
# print(students)
# students.pop(-5)#this will removes the  indexed(+ve or -ve) value
# print(students)

topics:
-------
datatypes
classification of data types 
list introduction
few list methods
task
-----

cart=["shirt","facewash","bodyspray","shoes"]

1.change bodyspray to perfume
2.add watch to the cart
3.remove shirt from the cart 
4.find the cart size 





