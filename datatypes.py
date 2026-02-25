# non-primitive:
# 1.list
# 2.tuples.
# 3.sets
# 4.dictionaries.

"""
[] for list
() for tuple
{} for set and dictionaries.

crud
lists are mutable
stores the ordered indexed values
lists are dynamic
lists are slower than tuples
"""
# list1=[]
# # list1[0]=1 #re-assign
# # print(list1)
# list1=[1,2,3,4,5] #creating
# print(list1)
# print(list1[1])

# list1[2]='hello' #updating element in the list
# print(list1)

# del list1[2] #delete the value from the list
# print(list1)

# ip=list([1,2,3,4])
# print(ip)

#tuple-->
"""
immutable
to store the final data , we will use tuple
tuples executes faster than lists
tuples can accepts duplicates and  heterogeneous data.
we can access the values from tuple using indexing because it will store values 
in ordered collection.
tuples are only readable.
crud-->c and r only will applicable
crud--->
"""

# tuple1=(1,2,3,'hello','hi','welcome') #creation is done
# print(tuple1) #reading
# print(tuple1[-3])
# # tuple1[2]='hiiii' #trying to update, we can't update
# # print(tuple1)
# tuple2=([1,2],3,4) #now value inside the tuple can be updated

# print(tuple2[0][1])
# tuple2[0][1]='harish'

# print(tuple2)
# tuple3=('hello','welcome','python','sql')
# #i want to add 'excel' into this tuple3

# cnvrted_list=list(tuple3)
# print(cnvrted_list)

# cnvrted_list.append('excel')
# print(cnvrted_list)

# cnvrted_tuple3=tuple(cnvrted_list)
# print(cnvrted_tuple3)

# print(len(cnvrted_tuple3))
# del cnvrted_tuple3[2]
# print(cnvrted_tuple3)



"""
sets are used to store the unique values as a unordered collection.
whenever we try to execute the set or print the set values,it 
always gives random order
only especially for string values.
in set every value has the hashing values.for numbers-->number 
itself be the hashing value.
but for string hashing value will be generates randomly
we can't access elements in the set with indexing.so,we cant add values with indexing 
in sets like lists how we do.
so we will use union approach for adding two sets
we can use - for removing values from the set
"""

# set1={32,45,1,2,3,4,5,87,35}
# #i want to add 108

# # |
# op=set1|{108} #union
# print(op)

# op1=set1-{45}
# print(op1)
# # num1=1
# # value1='hello'
# # print(hash(num1))
# # print(hash(value1))

# print(set1)


# harish123--->harish123
# 83697eydfiuerhck028e038rfcuif--->


# 1.set to list 
set1={1,7,'apple',8,10}
list1=list(set1)
print(list1)

# 2.set to tuple 
tuple1=tuple(set1)
print(tuple1)

"""
lists/tuples/sets are used to store like
multiple persons,products,colors,books,students.

dictionary is used to store a full information of
a particualr person.,product,color,book,student.

dictionaries will store these information/data in 
the form of a key-value pair.

so, that key-value pair can be said to be as a property.
should not allows duplicate keys.

key always should be in a string only

 
"""

# dict1={"key":"value"}
stud_info={
            "name":"vaishnavi",
            "gender":"female",
            "age":21,
            "education":"b.tech",
            "mobile":9988744451,
            "skills":["python","sql","excel"]
            }
# print(stud_info)
stud_info["role"]="analyst" #to add new property
del stud_info["mobile"] #removes mobile property
# print(stud_info)

# print(stud_info["name"])
# print(stud_info.get("name"))

all_students_info=[{"name":"kishore","city":"hyd",
                    "address":{
                                "d.no":'15-45-85',
                                'streetname':'ambedkar-nagar',
                                'pincode':500072
                             }},
                    {"name":"manohar","city":"bnglr"},
                    {"name":"ram","city":"mumbai"}]

# print(all_students_info[1]["city"])

#the student manohar is from bnglr
print(f"the student {all_students_info[1]['name']} is from {all_students_info[1]['city']}")

print(all_students_info[0]['address']['streetname'])