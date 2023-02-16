from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        # fields=['id','name','roll','city']
        exclude=[]
        read_only = ['name']
        # We cannot update read only field 

    def validate_name(self,value):
        if value.islower():
            raise serializers.ValidationError('Name should be start with capital letters')
        return value

        
    def validate_city(self,value):
        if value.islower():
            raise serializers.ValidationError('City name should be start with capital letters')
        return value
    
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

