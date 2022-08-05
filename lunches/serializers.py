from rest_framework import serializers
from .models import Menu, Restaurant, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    """серіалізація ресторанів"""
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    """серіалізація меню
    виводить назви ресторанів та кількість голосів за кожне меню"""
    rest = serializers.SlugRelatedField(read_only=True, slug_field='name_of_rest')
    class Meta:
        model = Menu
        fields = ('id','name_of_menu', 'first_course', 'second_course',
                  'snack', 'salad', 'side', 'dish', 'beverage',
                  'day', 'rest', 'votes',)
        read_only_fields = ('votes',)












def create(self, validated_data):
    return Comment(**validated_data)

def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.content = validated_data.get('content', instance.content)
    instance.created = validated_data.get('created', instance.created)
    instance.save()
    return instance