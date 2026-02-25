# # x=15 
# # y=25.5
# # z="hello world"

# # print(x)

# # print(type(z))

# # if i execute now here..python will understand the code the code till now.

# # 1.variable names should not starts with numbers or any spl characters except _ 
# # 2.variable names should not contain any empty spaces
# # 3.variable names are always case sensitives
# # 4.should not use keywords/reserved words as a variable names 

# name="10000 coders"
# #assigning    
# name="data science"
# #re assigning

# x=25
# x=15.5
# # print(type(x))
# #python can identify by default the type of the value which we assign.
# #pyhton can be called as a dynamically typed language.

# # firststudent="Harish"
# # first_student="akhil"
# # x,y,z=1,2,3
# # print(x,y,z)
# name=input("enter any name : ")
# print(f"hello {name}")


# mobile_name="samsung"
# price=68000
# rating=4.7
# color="white"
# is_available=False 


# print("i want to buy mobile_name which has rating of rating in color colour on price of price")

# if is_available:
#     print("how many mobiles u need")
# else:
#     print("sorry,out of stock")


# #when ever we want to print both values and variables at a time

# # print(f"i want to buy {mobile_name} which has rating of {rating} in {color} colour on price of {price}")

# # 1.comparing
# # 2.taking decisions
# # 3.filtering

# # is_fee_paid=True

# # if is_fee_paid:
# #     print("u have added in whatsapp group")
# # else:
# #     print("not yet added in wtsapp group")



# mobile_name=input("enter mobile name : ")
# budget=int(input("enter ur budget : "))
# color=input("enter ur desired color : ")
# budget_startsfrom=50000

# if budget>=budget_startsfrom:
#     print("mobiles are available")
# else:
#     print("no mobiles available")


#if we store single value into single variable-->primitive data type/simple
#if we store multiple values into single variable--->non-primitive/complex
# list,tuple,set,dictionaries



# revenue=int(input("enter the revenue: "))
# expenses=int(input("enter the expenses : "))
# company=input("enter company name : ")

# if revenue>expenses:
#     profit=revenue-expenses
#     print(f"{company} is in profits of {profit}")
# else:
#     loss=expenses-revenue
#     print(f"{company} is in losses of {loss}")

# expenses=[45000,25000,35000,"35k",None]
# revenue=[85000,65000,45000,None,"25k"]

# print(len(expenses))
# print(expenses[len(expenses)-3])



#append-->used to add value in list
#remove-->used to remove value from list
#???--->update existing value. we can use index of the element
#positive indexing always starts from zero
#negative indexing always starts from -1

# print(expenses)
# print(expenses[3])
# expenses[3]=35000
# print(expenses)

# expenses.remove(None)
# print(expenses)

# expenses.append(22500)
# print(expenses)
# print(expenses[-2])


# cart=["shirt","perfume","shoes","mobiles"]
# print(f"cart before new item adding : {cart}")
# item_tobe_add=input("enter the item :")
# cart.append(item_tobe_add)
# print(f"cart after adding new item : {cart}")

# company_names=["RGF-MADHAPUR","RGF-KPHB","RGF-JUBLIEEHILLS"]

# employees_count=[40,50,35]

# ratings=[4.2,4.65,3.9]

# activity_status=[True,True,False]

#1.add ameerpet branch
#2.add employees count for ameerpet branch

# new_branch="RGF-AMEERPET"

# company_names.append(new_branch)
# print(company_names)
# rating=4.35
# ratings.append(rating)
# print(ratings)
# emp_count=50
# employees_count.append(emp_count)
# print(employees_count)



# rgf_kphb_branch={
# 		         "company_name":"RGF_KPHB",
#                  "emp_count":45,
#                  "rating":4.25,
#                  "activity_status":True
#                 }
# # print(rgf_kphb_branch)


# print(rgf_kphb_branch["company_name"])
# print(rgf_kphb_branch["rating"])


rgf_all_branches=[ 
		{
		        "company_name":"RGF_KPHB",
                 "emp_count":45,
                 "rating":4.25,
                 "activity_status":True
                },
		{
		         "company_name":"RGF_MADHAPUR",
                 "emp_count":50,
                 "rating":4.55,
                 "activity_status":True
                },
                {
		         "company_name":"RGF_KPHB",
                 "emp_count":45,
                 "rating":4.25,
                 "activity_status":True
                }

]

print(rgf_all_branches[1]["rating"])





































