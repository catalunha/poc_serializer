from rest_framework import serializers
from .objects import Comment


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
