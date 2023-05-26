from rest_framework import serializers
from .models import StudDetails, VoterId, CricketPlayers, Team


class serialization(serializers.ModelSerializer):
    class Meta:
        model = StudDetails
        exclude = ['id']
        #fields = '__all__'  
    
        

class Cricketer_list(serializers.ModelSerializer):    
    team_name = serializers.CharField(source = 'team.team_name', read_only = True)
    coach = serializers.SerializerMethodField()
    
    class Meta:
        model = CricketPlayers
        exclude = ['team']
    
    def validate(self, data):        
        if data['country'] == 'india':
            return data  
        else: 
            raise serializers.ValidationError("we allow only an indian players")
    
    def get_coach(self, obj):
        obj = 'rahul dravid'
        return obj

class VotingPerson(serializers.ModelSerializer):
    class Meta:
        model = VoterId
        # fields = '__all__'
        exclude = ['id']
        
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("You are not eligible for voting")
                
        elif data['name'] == 'aravindhan':
            raise serializers.ValidationError("already exist")      
          
        else:
            return data


    
