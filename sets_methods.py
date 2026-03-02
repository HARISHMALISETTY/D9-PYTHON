# set1={'hello','python','sql','red','orange'}

# """
# add()-->add the value into the set
# update()-->add values from one set to another set and its modifies the original set itself.
# remove()-->it will removes the specific element from the set if it available otherwise throws an error.
# discard()-->it will also removes the specific element from the set if it is available otherwise nothing will do.
# pop()-->to removes random element from the set
# union()-->used to join multiple sets.
# |-->to apply union operation b/w multiple sets.

# intersection()--->gives the common values or duplicates from given sets, we can use for sets with list/tuple also
# &--->used for intersection with same type of objects 
# in union method we can join set with either list or tuple also and returns set only finally
# but if we use | , we can join only sets but not any other type object

# difference()-->shows the different value from set1 by comparing with set2.
# it will returns the different value only from first set
# works for different types of objects also

# - -->used to perform difference operation b/w sets.
# works only for sets.

# """
# set1={'python','java','sql','excel'}
# set2={'python','sql','js'}
# set3={'python','html','css','java'}

# # op=set1.difference(set2,set3)
# op=set1-set2-set3
# print(op)





# # set1={1,2,3,4,'hi'}
# # set2={4,5,6,2,'hi'}
# # set3=[7,8,9,'hi']

# # op=set1.intersection(set2,set3)
# # op=set1&set2&set3
# # print(op)



# # op=set1.union(set2,set3)
# # op=set1|set2|set3
# # list1=('op','lp','qp')
# # op=set1.union(set2,set3,list1)
# # op=set1|set2|set3|list1
# # print(op)

# # set1.remove('sql')
# # print(set1)

# # set1.discard('sql-lite')
# # set1.pop()
# # print(set1)
# # set1.add('biryani')
# # print(set1)

# # set2={'pineapple','mango','grapes'}

# # set1.update(set2)
# # print(set1)


# # set11=frozenset({1,2,3})
# # print(type(set11))
# # set11.pop()

# #frozenset is completely immutable,frozen set can be built using method frozenset()

# # set11.add('hi')
# # set11.upate({'hi','hello'})

"""
sets- methods

1.intersection_update()-->updates the set1 with common elements by comparing with set2.
2.difference_update()-->updates the set1 with different elements by comparing with set2.
3.symmetric_difference()-->returns the new set with uncommon values from
                            2 sets
4.^ performs the symmetric difference operation
5.issubset()-->check if one set is completely inside of anotherset.
6.<=check the issubset or not
7.issuperset()-->check if set contains all elements of another set
8.>= checks superset or not
9.isdisjoint()-->check if two sets have no common elements
10.clear()-->removes all the elements from the set

"""

# set1={'kumar','vijay','ajay'}
# set2={'kumari','krishna','sushma','vijay','meghana'}

# op=set1.intersection(set2)
# print(op)
# print(set1)

# set1.intersection_update(set2)
# print(set1)

# lalith_skills={'html','css','python','sql'}
# pavitra_skills={'python','excel','powerbi','java'}

# required_skilss={'python','sql','excel'}

# lalith_skills.intersection_update(required_skilss)
# pavitra_skills.intersection_update(required_skilss)

# print(lalith_skills)
# print(pavitra_skills)

#it will modify the original set with common elements from the given set


# set1={1,2,3}
# set2={4,5,3}

# # op=set1.difference(set2)
# # print(op)

# set1.difference_update(set2)
# print(set1)

#it will modifies the original set with values which are different by comparing
#with second set

#symmetric_difference()

# set1={'apple','banana','orange'}
# set2=['grapes','banana','orange','kiwi']

# op=set1.symmetric_difference(set2)
# print(op)

# op=set1^set2
# print(op)

#symmetric_difference_update()

# set1.symmetric_difference_update(set2)
# print(set1)

# intersection
# difference
# symmetric_difference

# op=
# op=
# op=

# intersection_update
# difference_update
# symmetric_difference_update


# x={'read','write','edit','share'}

# y={'read','write'}

# op=y.issubset(x)
# op=y<=x
# print(op)

# x1={1,2,3,4,5,6}
# x2={4,5,2,3,'hello'}

# op=x1.issuperset(x2)
# op1=x2.issubset(x1)
# print(op)
# print(op1)


#isdisjoint()

xx1={1,2,3}
xx2={5,6,4}

op=xx1.isdisjoint(xx2)
print(op)

xx2.clear()
print(xx2)