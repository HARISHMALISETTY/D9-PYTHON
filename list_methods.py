# list1=[4,6,7,8,12,14,16]

# op=list1[2:4] #starts at 2 and ends before 4
# op=list1[1:6:2] #starts at 1 and ends at 5 by taking 2 steps
# op=list1[::2] #starts from zero and ends at the end of the list by taking 2 steps
# op=list1[::-1]
# print(op)


"""
1.append()--->adds the single value at the end of the list
2.extend()-->adds multiple elements at a time to the given list through iterable objects(list/tuple/sets)
3.insert()-->add the value at specific index in the existing list
4.remove()--->removes the first occurance of argument if found.if not throws an error
5.pop()-->removes the last element from the list if not arg passes.
if arg passes then removes the indexed value as per the arg.
if index not found then throws an error
pop method will returns the value which is removed
6.clear()-->clears all the elements in the list
7.index()--->returns the index num of first occurance of arg value
8.sort()-->sort the list in ascending order by default
to sort in descending order we can use reverse=True inside sort method
9.reverse()-->will reverse the  given list
10.sorted()-->
11.join()--->it will joins all the elements in the given list with any string
"""
list1=['apple','banana','orange','grapes']
# op='-'.join(list1)
op=' and '.join(list1)
print(op)

# list1=[4,8,6,8,7,8,8,7]

# op=list1.sort()
# print(op)
# print(list1)


# list2=[9,7,2,19,23,4,10]
# op=sorted(list2)
# print(op)
# print(list2)

"""
sort method will change the original list
sorted method will not change the original list but returns
the new list by sorting it out.

"""







# # list1.sort()
# op=sorted(list1)
# print(list1)
# print(op)
# list1.sort() #sort in ascending order
# list1.sort(reverse=True) #sort in descending order
# list1.reverse()
# print(list1)

# op=list1.index(8,0,2)
# print(op)


# list1.clear()
# print(list1)
# op=list1.pop(4)
# print(op)
# print(list1)

# list1.remove(9)
# print(list1)




# list1=['hello','hi','12',15]
# op=list1.insert(2,[4,56])
# print(list1)

# list1.append(4)
# list1.append(4,5) #it wont allow more than one arg
# list1.append([4,6]) #can add as a nested list
# print(list1)
# print(list1[4][1])

# list1.extend([4,5,6])
# list1.extend((4,5,6))
# list1.extend({4,5,6})
# list1.extend({'apple','python','java'})
# print(list1)