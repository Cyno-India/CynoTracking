from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Tracker
        fields = ['id','status','api_call_time','tracking_number','updated_time','booked','arrival','outbound','delivered','tracking_info']


class TrackDetailsSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Tracker
        fields = ['tracking_number','updated_time','booked','arrival','outbound','delivered',]
    
    def to_representation(self, instance):
        data = super(TrackDetailsSerializer, self).to_representation(instance)
        # manipulate data here 
        return data