set1={'hello','python','sql','red','orange'}

"""
add()-->add the value into the set
update()-->add values from one set to another set and its modifies the original set itself.
remove()-->it will removes the specific element from the set if it available otherwise throws an error.
discard()-->it will also removes the specific element from the set if it is available otherwise nothing will do.
pop()-->to removes random element from the set
union()-->used to join multiple sets.
|-->to apply union operation b/w multiple sets.

intersection()--->gives the common values or duplicates from given sets, we can use for sets with list/tuple also
&--->used for intersection with same type of objects 
in union method we can join set with either list or tuple also and returns set only finally
but if we use | , we can join only sets but not any other type object

difference()-->shows the different value from set1 by comparing with set2.
it will returns the different value only from first set
works for different types of objects also

- -->used to perform difference operation b/w sets.
works only for sets.

"""
set1={'python','java','sql','excel'}
set2={'python','sql','js'}
set3={'python','html','css','java'}

# op=set1.difference(set2,set3)
op=set1-set2-set3
print(op)





# set1={1,2,3,4,'hi'}
# set2={4,5,6,2,'hi'}
# set3=[7,8,9,'hi']

# op=set1.intersection(set2,set3)
# op=set1&set2&set3
# print(op)



# op=set1.union(set2,set3)
# op=set1|set2|set3
# list1=('op','lp','qp')
# op=set1.union(set2,set3,list1)
# op=set1|set2|set3|list1
# print(op)

# set1.remove('sql')
# print(set1)

# set1.discard('sql-lite')
# set1.pop()
# print(set1)
# set1.add('biryani')
# print(set1)

# set2={'pineapple','mango','grapes'}

# set1.update(set2)
# print(set1)