from api.models import AlbumModel, TrackModel

# AlbumModel.objects.all().delete()
# a1 = AlbumModel.objects.create(name="album1", artist="artist1")
# print(a1)
# a2 = AlbumModel.objects.create(name="album2", artist="artist2")
# print(a2)
a4 = AlbumModel.objects.get(pk=4)
t1 = TrackModel.objects.create(
    album=a4,
    order=1,
    title="track1",
    duration=10,
)
