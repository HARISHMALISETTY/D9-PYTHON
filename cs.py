# """
# normal statements-->statements which executes without depending on any condition are said to be
# normal statements
# conditional statements-->statements which executes based on condition/conditions are
# said to be conditional statements.

# 1.simple-if---> 
#                 if condtion :
#                     print()

# 2.if-else
# 3.if-elif-else
# 4.nested-if

# """

# # print("iam a normal statement1")
# # print("iam a normal statement2")
# # #making condition true directly
# # if True:
# #     print("iam a conditional statement1")
# # #decision is depends on expression(hardcoded)
# # if 2!=2:
# #     print("iam a conditional statement2") #executes when condtion is true
# # if ' ':
# #     print("hello world")
# # print("welcome everyone")

# # if not True:
# #     print("hello 1")
# # print("hello 2")

# # if True:
# #     print("true statement")
# # else:
# #     print("false statement")

# #if subscription is avaialable then watch ott otherwise please to subscribe

# # is_subsribed=False 
# # if is_subsribed:
# #     print("watch ott ")
# # else:
# #     print("please subscribe")


# #if profile is public then follow directly else make a request

# # is_profile_public=False 
# # if is_profile_public:
# #     print("follow directly")
# # else:
# #     print("make a request to follow")

# #whenever we need to check multiple conditions then we can use if-elif-else.

# #if candidate selected then send offerletter,
# #rejected send rejection mail if hold send mail that he is on hold

# # is_selected=True
# # is_rejected=False
# # is_on_hold=False 

# # if is_selected:
# #     print("send offer letter")
# # elif is_on_hold:
# #     print("wait for further updates")
# # elif is_rejected:
# #     print("send rejection mail")
# # else:
# #     print("go and try for jobs")

# # sql=False 
# # excel=False
# # powerbi=False
# # python=True

# # if sql and excel and powerbi and python:
# #     print("become a data analyst")
# # elif sql:
# #     print("become a sql developer")
# # elif excel:
# #     print("become a excel developer") 
# # elif python:
# #     print("become a python developer")
# # elif powerbi:
# #     print("become a powerbi developer")
# # else:
# #     print("go and join in 10000coders")

# #nested if---> if we want to add condition inside the other conditions(either if they are true or false).
# #we can use multiple ifs inside a if or else 

# """
# if condition1:
#     if condition T1.1:
#         print("statementT1")
# else:
#     if condition F1.1:
#         print("statementF1")

# -------------------------------------
# if condition1:
#     if condition T1.1:
#         print("statementT1")
#     else:
#         print("statementF1")
# elif condition2:
#     if condition T2.1:
#         print("statementT2")
#     else:
#         print("statementF2)
# else:
#     print("default statement")
# """ 

# # #instagram--->if account is private-->if both are frns-->u can send message
# # # if account is public--->send message directly 
# # if account is private--->both are not frns--->u can't send message 

# # is_account_private=False
# # are_friends=True 
# # allow_everyone=False

# # if is_account_private:
# #     if are_friends:
# #         print("can send message directly")
# #     else:
# #         print("can not send a message")
# # else:
# #     if allow_everyone:
# #         print("anyone can send message without following")   
# #     else:
# #         print("only frns can send message until he/she accept ur message request")

# #first we will check whether they r frns or not.
# #if they r frns--->directly send message
# #if they r not frns-->need to check account is private or public
# #if acnt is private--->cant send message directly without following
# #if acnt is public-->need to check allowing everyone or not
# #if allows everyone then send message
# #if not only frns can send message until they accept ur message request
# is_account_private=False
# are_friends=False 
# allow_everyone=False

# if are_friends:
#     print("send message directly")
# else:
#     if is_account_private:
#         print("they can not send message")
#     else:
#         if allow_everyone:
#             print("everyone can send message")
#         else:
#             print("only frns can send message until they accept ur message request")

# #if purchase amount is greater than or equal to 500 then delivery will be free
# #if not then delivery fee will be charges 50rs by default
# #purchase amount should be calculated based on the item price and quantity
# #if distance is more than 3kms then need to add 10rs extra

# price=int(input("enter item price : "))
# quantity=int(input("enter the quantity : "))
# purchase=quantity*price 
# distance=int(input("enter the distance : "))

# if purchase >=500:
#     print("no extra charge for delivery ")
# else:
#         if distance<=3:
#             print("extra 50rs will be added in the bill")
#         else:
#             print(f" amount of {(distance-3)*10+50} will be added to the bill ")
    

#creditcard bill payment
"""
limit _available
spending amount --> checks the limit and spend the amount
once u spend the amount --> then limit should br reduced and the due amount should be increses
pay the bill-->
limit should be increase and then due  should be reduce
"""



limit=int(input("enter the cc limit : "))
print("""
choose 1 for spending card,
choose 2 for paying the bill,
""")
choice=int(input("enter choice : "))
due=0

if choice == 1:
    spending_amount=int(input("enter the amount to be spend"))
    if spending_amount<=limit:
        limit-=spending_amount
        due+=spending_amount
        print(f"after spending of {spending_amount} rupees, avaiable limit is {limit} and due amount is {due}")
    else:
        print("insufficient limit ")

elif choice ==2:
    payable_amount=int(input("enter the amount to be pay : "))
    if payable_amount<=due:
        due-=payable_amount
        limit+=payable_amount
        print(f"after payment of {payable_amount} rupees, updated limit is {limit} and due is {due}")
    else:
        print("no dues for now, go and use ur card first")










