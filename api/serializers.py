from rest_framework import serializers
from .objects import Comment
from .models import AlbumModel, TrackModel


def validatorExample(value):
    if value == "abc@gmail.com":
        raise serializers.ValidationError("My validatorExample em content")


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validatorExample])
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        print("passou no CREATE")
        return Comment(**validated_data)

    def update(self, instance, validated_data, *args, **kwargs):
        print("passou no UPDATE")
        instance.email = validated_data.get("email", instance.email)
        instance.content = validated_data.get("content", instance.content)
        instance.created = validated_data.get("created", instance.created)
        return instance

    def validate_content(self, value: str):
        print("Passei no validate_content")
        if value.lower() == "aa":
            raise serializers.ValidationError("MyError em content", "001")
        return value

    def validate(self, data):
        print("Passando em validate")
        print(data)
        if "email" in data and "content" in data:
            if data["email"] == data["content"]:
                raise serializers.ValidationError(
                    "MyError email e content devem ser diferentes", "002"
                )
        return super().validate(data)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackModel
        fields = [
            "order",
            "title",
            "duration",
        ]


class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="track-model-detail",
    # nao funciona pois precisa do context
    # )
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field="pk",
    # )
    tracks = TrackSerializer(
        many=True,
        # read_only=True,
    )

    class Meta:
        model = AlbumModel
        fields = [
            "name",
            "artist",
            "tracks",
        ]

    def create(self, validated_data):
        print("create em AlbumSerializer 1")
        print(validated_data)
        print("create em AlbumSerializer 1a")
        tracks_data = validated_data.pop("tracks")
        print("create em AlbumSerializer 2")
        album = AlbumModel.objects.create(**validated_data)
        print("create em AlbumSerializer 3")
        for track_data in tracks_data:
            TrackModel.objects.create(album=album, **track_data)
        print("create em AlbumSerializer 4")
        return album
