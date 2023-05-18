from rest_framework import serializers
from .models import StudDetails, Cricketers



class serialization(serializers.ModelSerializer):
    class Meta:
        model = StudDetails
        exclude = ['id']
        #fields = '__all__'

class Cricketer_list(serializers.ModelSerializer):
    class Meta:
        model = Cricketers
        exclude = ['id']
        #fields = '__all__'

    def create(self, validated_data):
        return Cricketers(**validated_data)
    
    def update(self, instance, validated_data):
        instance.cricket_id = validated_data.get('cricket_id', 'instance.cricket_id')
        instance.name = validated_data.get('name', 'instance.name')
        instance.role = validated_data.get('role', 'instance.role')
        instance.nation = validated_data.get('nation', 'instance.nation')
        instance.save()
        return instance
