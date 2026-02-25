# """on order below 500rs-->starts charging 50rs as a delivery fee if distance is
# less than 3kms.

# if distance is more than 3kms, then for every one km they will charge 10rs.


# if we order more than 500rs then no delivery fee will be applicable.


# 1.we need to check order amount.
# 2.greaterthan or equal to 500 then no delivery fee.
# 3.if order is lessthan 500 then
# dfee will be applicable
# 4.if distance is less than or equal to 3 kms then add 50rs
# 4.if more than 3 then we need to find additional kms.

# 5kms--->2kms
# 7km--->4kms
# distance =8kms
# extradistance=distance-3=5kms
# total delivery fee we need to apply-->5x10=50

# 1.execute statements based on conditions
# 2.based on decisions
# """
# # #conditional statements--->
# # 1.if 
# # 2.if-else 
# # 3.if-elif-else 
# # 4.nested if \\

# # amount=float(input("enter the total amount :"))


# # print(type(amount),amount)
# # print(type(distance),distance)

# # if amount<500:
# #     distance=float(input("enter the distance :"))
# #     if distance<=3:
# #         print("delivery fee of 50rs is applicable")
# #     else:
# #         extra_distance=distance-3
# #         overall_deliveryfee=50+extra_distance*10
# #         print(f"delivery fee will be {overall_deliveryfee}")
# # else:
# #     print("no extra delivery fee will be applicable")


# """
# 1.spend the amount from cc
# 2.limit will be reduced, due amount will be increased
# 3.pay the amount 
# 4.limit will be increased and due will be reduced
# """


# print("""
# press 1 for spending cc,
# press 2 for paying cc
# """)

# choice=int(input("enter ur choice :"))
# print(choice)

# if choice==1:
#     print("u choose to spend the credit card")
#     due=0
#     limit=float(input("enter the cc limit :"))
#     amount_to_be_spend=float(input("enter amount to be spend : "))
#     limit=limit-amount_to_be_spend
#     due=due+amount_to_be_spend
#     print(f"""after spending of {amount_to_be_spend} rupees, 
#               ur limit is {limit} rupees 
#               and due is {due} rupees
#               """)
    
    
# elif choice==2:
#     print("u choose to pay the credit card bill")
#     due=float(input("enter due amount : "))
#     limit=float(input("enter limit amount : "))
#     payable_amount=float(input("enter amoiunt to be pay :"))
#     due=due-payable_amount
#     limit=limit+payable_amount
#     print(f"""
#             after paying of {payable_amount} rupees,
#             available limit is {limit} rupees
#             updated due amount is {due} rupees   
    
#     """)


# x=1225
# y=1225
# z=1225
# print(id(x))
# print(id(y))
# print(id(z))

x=125
X=256
print(x)

print(X)


x12h='hello'
x23='welcome'
y2j='something'

print(x12h,x23,y2j)















