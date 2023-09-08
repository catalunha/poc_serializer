from datetime import datetime

# from api.objects import Comment
from api.serializers import CommentSerializer

# +++ exemplo1

# c1 = Comment("a@gmail.com", "aa bb")

# s1 = CommentSerializer(c1)
# print("s1.data")
# print(s1.data)

# data2 = {"email": "b@gmail.com", "content": "cc dd", "created": datetime.now()}

# s2 = CommentSerializer(data=data2)
# print("s2")
# print(s2)

# print("s2.is_valid()")
# print(s2.is_valid())
# if not s2.is_valid():
#     print(s2.errors)

# print(s2.validated_data)

# c2 = s2.save()
# print(c2)
# print("update c1")
# print(c1)
# data1a = {"email": "b@gmail.com", "content": "cc dd ee", "created": datetime.now()}
# # data1a = {"content": "cc dd ee"}

# c1a = CommentSerializer(c1, data=data1a)
# if c1a.is_valid():
#     print("é valido")
#     c1ai = c1a.save()
# else:
#     print("nao é valido")
#     c1a.error_messages
# print(c1ai)
# print(c1a)
# --- exemplo1

# +++ exemplo2
# data1 = {"email": "a@gmail.com", "content": "bb", "created": datetime.now()}

# s1 = CommentSerializer(data=data1)
# if s1.is_valid():
#     print("data1 is valid. criar instancia")
#     print(s1.validated_data)
# else:
#     print("data1 is not valid. erros")
#     print(s1.errors)

# --- exemplo2

# +++ exemplo3
data1 = {"email": "a@gmail.com", "content": "bb", "created": datetime.now()}

s1 = CommentSerializer(data=data1)
print(repr(s1))
# if s1.is_valid():
#     print("=1=>", s1.data)
#     print("data1 is valid. criar instancia")
#     c1 = s1.save()
#     print(c1)
#     data1a = {"content": "cc"}
#     s1a = CommentSerializer(c1, data=data1a, partial=True)
#     if s1a.is_valid():
#         print(s1a.validated_data)
#         print(s1a.validated_data["content"])
#         c1a = s1a.save()
#         print(c1a)
#     else:
#         print("update invalid")

# else:
#     print("data1 is not valid. erros")
#     print(s1.errors)

# --- exemplo3

# +++ exemplo4

# --- exemplo4
