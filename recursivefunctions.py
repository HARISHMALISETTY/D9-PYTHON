"""
a function being called by itself on a particular condition is called recursion process.
and that function can be called as recursive function
maximum limit for recursion is 1000 approximately
"""

# def recu():
#     print('hello')
#     return recu()
# recu()
#printing numbers from 10 to 0
def recu(n):
    if n>=0:
        print(n)
        return recu(n-1)
# recu(10)

#print numbers from 1 to 10
# def rec1(n):
#     if n<=10:
#         print(n)
#         return rec1(n+1)
# rec1(1)
#10 9 8 7 6 5 4 3 2 1

#due to recursion--->more memory will be wasted because of more times of calling same function
#so we went to loops instead of recursion

#sum of the n numbers using recursion.

#ip=5 op=15
#ip=10 op=??

#write a program to print n number of fibonocci series without recursion
# def rec1(n,sum):
#     if n<=10:
#         sum+=n
#         return rec1(n+1,sum)
#     else:
#         print(sum)
# rec1(1,0)

# n=5
# 01123

# n=6
# 011235
# 0112358 13 21
# n=int(input('enter num of fibonocci series : '))
# a=0
# b=1 
# if n<=0:
#     print('enter positive numbers ')
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for x in range(3,n+1):
#         c=a+b 
#         print(c)
#         a=b
#         b=c

"""
count of characters in given string
str1=hello world

"""

# def count_of_chars(str1):
#     dict1={}
#     for char in str1:
#         if char in dict1:
#             dict1[char]+=1
#         else:
#             dict1[char]=1
#     print(dict1)

# count_of_chars('helloworld')
# count_of_chars('something')
# count_of_chars('awesome')
# {'h':1,'e':1,'l':3..}



# def count1(str1):
#     checked=""
#     for i in str1:
#         if i in checked:
#             continue
#         count=0        
#         for j in str1:
#             if i==j:
#                 count+=1
#         print(i,count)
#         checked+=i

# count1('BANANA')

"""
compare two strings and print common characters from both
1.hello,hi---->h
2.chill,check-->ch
3.pooja,apoorva--poa>

"""

# def comparee(str1,str2):
#     checked=''
#     for char1 in str1: #p o o
#         if char1 in checked:
#             continue
#         for char2 in str2: #a p o o r v a
#             if char1==char2:
#                 print(char1)
#                 break
#             checked+=char1
# comparee('pooja','apoorva')


"abc"-->it should print all pairs of chars 
op-->
"""
aa
ab
ac
ba
bb
bc
ca
cb
cc
"""

list1=['apple','banana','orange','mango','grapes']
op=['elppa','ananab','egnaro','ognam','separg']