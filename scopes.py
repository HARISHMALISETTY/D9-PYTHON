# x=10 #global x

# def func1():
    
#     print(x)
# func1()

# print(x)



# def outer():
#     x=10
#     def inner():
#         x=5
#         print(x+2,'from inner function')
#     inner()
#     print(x*3,'from outer function')
# outer()


# 1.if i try to access x variable
# a.function first will check inside the function 


"""
scope modifiers:
these are the keywords which will change scope of the variables.
1.global--->change local to global
2.nonlocal-->it will change enlosed to local.

"""

# def func1():
#     global x
#     x='hello'
#     print(x)
# func1()
# print(x)

# ip1='data'
# def func1():
#     global ip1
#     ip1='science'
#     print(ip1,'from the fun')
# func1()
# print(ip1,'out of the fun')

"""
to access local variable from outside
to update global variable from inside of the function..
global keyword will be useful

"""

# def outer():
#     x=125
#     def inner():
#         nonlocal x
#         x='hello'
#     inner()
#     print(x)
# outer()

"""
to update outer function variable from inner function which is
having enclosed scope we can use nonlocal scope-modifier
# """
# x=12
# def func1():
#     global x #accessing global x
#     x=5 #updating global x from 12 to 5
#     print(x,'from func1')
#     def func2():
#         x=6
#         print(x,'from func2')
#     func2()
# func1()
# print(x)








