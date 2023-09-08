from django.db import models


class PersonModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class AlbumModel(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class TrackModel(models.Model):
    album = models.ForeignKey(
        AlbumModel,
        related_name="tracks",
        on_delete=models.CASCADE,
    )
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    # class Meta:
    #     unique_together = ["album", "order"]
    #     ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.order}: {self.title}"
