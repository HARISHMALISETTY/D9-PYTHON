"""
strings: group of characters enclosed in b/w "" or ''
to define multiline string---> """"""


"""

str1="something is fishy"
        #  -10.....-5-4-3-2-1

# print(str1[3])
# print(str1[5:15]) #starts at 5 and ends at 14
# print(str1[:12]) #starts at 0 and ends at 11
# print(str1[:]) #starts at 0 and ends at end of the string
# print(str1[3:15:2]) #starts at 3 and ends at 14 by taking 2 steps at a time, skips every single character
# print(str1[-10:-3])
# print(str1[-3:-10:-1])

# print(str1[::-1])
# print(str1[::-2])
# print(str1[::2])

"""
operations on strings
+(concationation),*(repetetion)
"""
# str1='hello'
# # str2='world'
# str2='3'
# print(str1+str2)

# str1='python'
# x='3'
# x='ok'
# print(str1*x)

"""
removing space from the string
starting space(leading space) and ending space(trailing space) can be removed
to remove leading space-->lstrip()
to remove trailing space--->rstrip()
to remove both--->strip()

this method doesn't modify the existing string.
it will returns the new string by removing spaces
"""

# username="harish  123   "
# print(len(username))
# x=username.strip()
# print(len(x))

# print(username)
# print(len(username))

# username="   Ilove My India   "
# print(username)

# username1="###**harish***##  "
# print(username1)
# x=username1.strip('#')
# print(x)
# op=username.lstrip()
# print(username.strip())


"""
finding substrings from the given string:
find()--->str.find(substring) or str.find(substring,start,end)
returns the index num of first occurance of substring, if not then returns -1

index()--->str.index(substring) or str.index(substring,start,end)
returns the index num of first occurance of substring, if not then returns valueerror


rfind()-->str.rfind(substring) or str.rfind(substring,start,end)
returns the index num of last occurance of substring by searching from right to left.
if not then returns -1

rindex()-->str.rindex(substring) or str.rindex(substring,start,end)
returns the index num of last occurance of substring by searching from right to left, 
if not then returns valueerror.
"""

# str1="PYTHON IS EASY Easy"
# str1="AOKDNCDUECWDERTYSXCVESWDF"

# # op=str1.find('Eat')
# # print(op)

# op=str1.find('D',7,10)
# print(op)

str1="PYTHON IS EASY Easy"

# op=str1.index('x')
# print(op)

# op=str1.rfind('x')
# print(op)


# op=str1.rindex('x')
# print(op)


"""
counting substrings in given string
count()-->used to count the substrings from given string
str.count(substring)
    OR
str.count(substring,start,end)
"""

# str1="PYTHON PYTHON JAVA JS PYTHON"

# op=str1.count('ON',2)
# print(op)

"""
splitting the string
to split the string into multiple partitions we can use split().
this will returns in the form of list.
splitting can be happened with help of seperator which should be avaialble in given string
by default it will consider space as a seperator if any space available in given string
first arg-->act as a seperator
second arg-->number of substrings to be splitted

"""

str1="DO*SOMETHING*GREAT*FROM*NOW"
op=str1.split('*',3)
print(op)
