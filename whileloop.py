# #strong number
# #perfect number
# #perfect square
# #neon
# #sunny
# #buzz

# # #1.sum of digits in a given number
# # num=1254

# # 1254%10--->4
# # 125--->1254//10--->125

# # 125-->125%10--->5

# # 125//10--->12


# # 1.remove last digit 
# # 2.reduce the num


# num=1254895
# #print digits in reverse from given num
# # while num>0:
# # while num>=0:
# # while num>=1:
# #     ld=num%10
# #     print(ld)
# #     num=num//10

# # 1.1254>0---->1254%10--->4 prints 4--->1254-->1254//10--->125
# # 2.125>0---->125%10--->5--->prints 5---->125--->125//10--->12
# # 3.12>0--->12%10--->2--->prints 2--->12-->12//10--->1
# # 4.1>0--->1%10--->1--->prints 1--->1--->1//10--->0

# #count the digits in given num
# # count=0
# # while num>=1:
# #     ld=num%10
# #     # print(ld)
# #     count+=1
# #     num=num//10
# # print(count)


# #sum of digits in given num
# #125--->8
# #246--->12
# # sum=0
# # while num>=1:
# #     ld=num%10
# #     sum+=ld
# #     num=num//10
# # print(sum)

# #sum of squares of digits in num
# #123-->
# # num=125
# # sum=0
# # while num>=1:
# #     ld=num%10
# #     sum+=ld**2
# #     num=num//10
# # print(sum)

# #strong number--->sum of factorials of each digits is equal to number itself

# # num1=5
# # fact=1
# # while num1>=1:
# #     fact=fact*num1
# #     num1-=1
# # print(fact)


# # 125--->1fact+2fact+5fact--->1+2+120-->123
# #145--->1+24+120--->145

# num=199
# num1=num
# sum=0
# while num>=1: 
#     ld=num%10
#     fact=1
#     while ld>=1:
#         fact=fact*ld 
#         ld-=1
#     sum+=fact
#     num=num//10 #this logic is reducing num to 0
# if(sum==num1):
#     print("it is a strong number")
# else:
#     print("it is not a strong number")

# # 125>=1---->ld=5--->
# #                     5>=1--->fact=5--->ld=4
# #                     4>=1--->fact=20-->ld=3
# #                     3>=1--->fact=60-->ld=2
# #                     2>=1--->fact=120-->ld=1
# #                     1>=1--->fact=120-->0
# #             sum=120
# # 12>=1---->ld=2--->
# #                 2>=1--->fact=2--->ld=1
# #                 1>=1--->fact=2--->ld=0
# #                 0>=1-->end 
# #             sum=122
# # 1>=1--->ld=1---->
# #                 1>=1--->fact=1--->ld=0
# #                 0>=1--->Ends 
# #             sum=123          


# #palindrome num
# # 1221
# # 145541
# # 121
# # 181
# # 999
# # 1001

# num=121
# rev=0
# ld=1
# rev=revx10+ld--->1

# ld=2
# rev=revx10+2-->1x10+2--->12

# ld=1
# rev=revx10+1--->12x10+1-->121

# 3,4--->34=3x10+4--->34
# 34,5--->345--->34x10+5-->345
# 345,6--->345x10+6--->3456

#build a logic to reverse given num
num=-125521
rev=0
if num<0:
    num=num*-1
num1=num
while num!=0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if num1==rev:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#to check whether given num is armstrong or not


# 1.-125!=0-->ld=-5-->rev=-5--->-12
# 2.-12!=0-->ld=-2--->-5x10-2---->-52-->-1
# 3.-1!=0--->ld=-1--->-52x10-1---->-521


# # print(-125!=0)
# print(-125/10)

"""
task:
-----
level1--->practise all types of functions with syntaxes and examples on a paper and also execute them

level2--->implement all the previous problems using functions
"""

"""
1.userdefined
2.predefined
"""
