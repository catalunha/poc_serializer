from api.models import AlbumModel
from api.serializers import AlbumSerializer

# +++ exemplo 1
# a4 = AlbumModel.objects.get(pk=4)
# print(a4)
# aList = AlbumModel.objects.all()
# print(aList)
# for item in aList:
#     print(item)

# s4 = AlbumSerializer(a4)
# print(s4)
# print(s4.data)
# --- exemplo 1

# +++ exemplo 2
# data1 = {
#     "name": "album name 1",
#     "artist": "album artist 1",
#     "tracks": [
#         {"order": 1, "title": "track title 1", "duration": 10},
#         {"order": 2, "title": "track title 2", "duration": 20},
#     ],
# }
# s1 = AlbumSerializer(data=data1)
# print(s1.is_valid())
# # print(s1.data)
# a1 = s1.save()
# print(a1)
# --- exemplo 2
# +++ exemplo 3
a6 = AlbumModel.objects.get(pk=6)
print(a6)
s6 = AlbumSerializer(a6)
# print(s6)
print(s6.data)
# --- exemplo 3
