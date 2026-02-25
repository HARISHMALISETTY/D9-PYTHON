# #if we use a block multiple times--->block using
# #if we use a block multiple times with different inputs--->reuasble block

# #block means set of tasks/instructions.

# #to reduce the length of the code

# """
# A function is a reusable block of code/statements that performs specific task.
# it helps organize code and avoid repetetions unnecessarily.

# by default function will returns None if it is not returning anything specifically.

# """

# #static function:function which gives always same output without taking any inputs.
# def Sample():
#     print("hello iam sample function")

# Sample()
# Sample()
# Sample()

# #dynamic functions:functions which gives different outputs based on given inputs.
# """
# while building dynamic functions, we should take inputs.
# inputs should take in the form of parameters/arguments while using function

# eg: def sample(name,city):  name and city--->parameters
#     print(name,city)

#     sample('kiran','hyd') kiran and hyd are arguements
#     sample('harish','nlr')
# count of parameters and arguments should be equal always
# always positions of params and args should be match 

# #interpreter will go to function call intially, then enter inside the function body with the arguements

# in dynamic functions we have few types based on how we are passing arguements
# 1.positional arguements
# 2.default parameters--->whenever we have defualt values which shouldnot be changed inside the function
# then we can use these default parameters.
# always default param should be end of the params
# default param can be overwrite if we pass a value through arguments
# 3.arbitrary arguements(*args)-->
# whenever we dont know the count of arguments to be pass then we should use this arbitrary arguements
# all the arguements can be assign to single param in the tuple format
# we should add * before the param name
# 4.keyword arbitrary arguements()--->
# whenever we dont the specific order of arguements to be follow, then we will pass arguements with variable names 
# then those arguements can be assign to single param in the form of a dictionary.

# """

# # print(x)
# # x=5

# # def Greetings(name,city):
# #     print(f"{name} is from {city}")

# # Greetings('harish','nlr')
# # Greetings('harish','nlr')
# # Greetings('kiran','guntur')
# # Greetings('hyd','Akhil')


# #default parameters

# # def function2(y,z,x=25):
# #     print(x,y,z)

# # function2(4,5,20)

# # def student_info(name,city,institute="10000coders"):
# #     print(f"{name} is from {city} and joined in {institute}")
# # student_info('lalith','bnglr')
# # student_info('kiran','gnt')

# # def billing(item,price,quantity,gst=0.05):
# #     total_bill=price*quantity+gst*(price*quantity)
# #     print(f"total bill for {item} is {total_bill}")
# # billing('dosa',25,2)
# # billing('poori',30,4)

# # def students(*p):
# #     print(p)
# # students('hari','krishna','lalith','madhav')
# # students('harish')
# # students('kiran','akhil')

# #1-ram 2-lakshman 3-bharath

# def ramayana(**children):
#     print(f"first one is {children['first']},second one is {children['second']},third one is {children['third']}")
#     # print(children)

# ramayana(third='bharath',first='ram',second='lakshman')

# #whenever we dont know count of args--->*params/args
# #whenever we dont know count/order--->**args/params
#a function can return another function is called higher order function

# def demo():
#     print("hello")
#     # return 'function ends'
# print(demo())

#by default function will returns None value

# def sample():
#     print('hello')
#     return 'something'
#     print('welcome') #ignored

# print(sample())


# def sample1():
#     return 'hello'

# x=sample1() assigning function call to x
# print(x)


# def sample2():
#     return 'iam sample2'

# x=sample2 #iam assigning function name/definition to x
# print(x())

# def sample3():
#     print('hello sample3')
#     return 'byeee'
#     print('hhhhhhhhhhhhh')
# y=sample3

# print(y)
# y()
# print(y())

#we can assign a function to a variable
#a function definition can be take as values inside the datastructures like list/tuple
#a function which can pass as a argument into another function, then that can be called as callbackfunction
#a function which will take another function as a argument or returns another function then it can be called as higher order function


# because of above 4 points--->functions in python can be considered as a firstclass functions 

# def func1():
# #     print('iam function 1')
# def func2():
#     print("iam function 2")

# list1=[func1,func2]
# list1[0]()
# list1[1]()

# def func3():
#     print("iam a function 3")
#     return func2()
# func3()


# def fun4():
#     return 'iam function 4'


# def fun5(cbf):
#     print(cbf())
#     return 'iam function 5'

# print(fun5(fun4))

#here func4 is going as arguement into the func5
#func5 is taking func4 as a argument

# we can also define a function without name
# a function without name can be called as anonymous function
#to define anonymous function in python we have to use lambda keyword
#for short logical problems/single line of codes, we can use lambda function
#by default it will return values without using return keyword

# syntax:
# -------
# fun1=lambda param:logic 

# def sample():
#     return "hello"
# print(sample())

# #lamda function without params
# fun2=lambda : 'hello'
# print(fun2())

# #lamda function with single param
# fun3=lambda x:x
# print(fun3(10))

# #lambda function with multiple params
# fun4=lambda x,y:x+y
# print(fun4(4,5))

# fun5=lambda x,y=4:x+y
# print(fun5(8,2))

# fun6=lambda *x:x[0]+x[1]+x[2]
# print(fun6(1,2,3))

# fun7=lambda **x:x
# print(fun7(first=4,second=5,third=6))

#recursive function:
"""
a function being called by itself on a particular condition is called recursion process.
and that function can be called as recursive function
1.default params
2.positional args
3.arbitrary args
4.keyword-arbitrary
5.keyword args
6.higher order
7.callback
8.anonymous using lambda
9.recursive function
"""






def reverse(num):
    rev=0
    if num<0:
        num=num*-1
        num1=num
    while num!=0:
        ld=num%10
        rev=rev*10+ld
        num=num//10
    print(rev)

reverse(123)
reverse(456)


#write a function to add 3 numbers


def addition(a,b,c):
    return a+b+c 
print(addition(1,2,3))
print(addition(4,8,10))

#write a function to print multiplication table of given input

def m_table(num):
    for x in range(1,11):
        print(f"{num} * {x} = {num*x}")
    return f'{num} table printed'
# print(m_table(4))

#write a function to print numbers for given range
def numbers(x1,x2):
    for i in range(x1,x2):
        print(i)
numbers(20,31)
numbers(1,11)
numbers(235,256)