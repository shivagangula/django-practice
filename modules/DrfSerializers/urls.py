from django.urls import path
#from modules.DrfSerializers.serializer_types.normal import *
from modules.DrfSerializers.serializer_types.model import ModelSerializerAPI

urlpatterns = [
    path('model-ser/', ModelSerializerAPI.as_view()),
]