from rest_framework import serializers

from api.models import PersonalCard


class PersonalCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCard
        fields = [
            "id", "name", "last_name", "age",
            "middle_name", "gender", "vaccinated",
        ]

    def create(self, validated_data):
        """
        Create and return a new `PersonalCard` instance with given data
        """
        return PersonalCard.objects.create(**validated_data)

    @staticmethod
    def validate_age(age: int):
        if age < 0:
            raise serializers.ValidationError("Age should be non negative")
        return age

    def update(self, instance: PersonalCard, validated_data):
        """
        Update and return existing `PersonalCard` instance with given
        validated data
        """
        instance.name = validated_data.get("name", instance.name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.middle_name = validated_data.get("middle_name", instance.middle_name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance
