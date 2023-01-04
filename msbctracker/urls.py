import string
from django.contrib import admin
from django.urls import path , re_path
from .views import *
urlpatterns = [
    re_path('track',func.as_view()),
    re_path('PostTrack',PostingTrack.as_view()),
    re_path('TrackingDetails',GetTrackingDetails.as_view()),
    re_path('TrackDetails',GetTrackDetails.as_view()),
    re_path('details',GetDetails.as_view()),
    re_path('patch/<string:tracking_numbers>',PatchDetails.as_view()),
    # re_path(r'',PatchDetails.as_view()),
    re_path(r'^$', PatchDetails.as_view()),



]
