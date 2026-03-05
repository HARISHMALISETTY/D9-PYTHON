# 1.if we copy one thing-->
# a.orignal
# b.copied piece

#shallow copy-->copies the objects with their referrence, so if we change
# nested object values in copied then it will reflects to orignal also.

#copy.copy()

#deep copy

# import copy
# orignal=[[1,2],[3,4]]

# copied=copy.copy(orignal)
# print('before changing')
# print(orignal)
# print(copied)

# copied[1][1]='helloo'
# print('after changing')
# print(copied)
# print(orignal)


# copied=copy.deepcopy(orignal)
# print('before changing')
# print(orignal)
# print(copied)

# copied[1][1]='helloo'
# print('after changing')
# print(copied)
# print(orignal)

