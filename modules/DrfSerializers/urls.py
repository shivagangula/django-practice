from django.urls import path
#from modules.DrfSerializers.serializer_types.normal import *
from modules.DrfSerializers.serializer_types.model import   ModelSerializerAPI
from modules.DrfSerializers.serializer_types.hyper_linked import HyperLinkedSerializerAPI, HyperlinkedModelSerializerRecordViewAPI
    
app_name = 'DrfSerializers'

urlpatterns = [
    path('model-ser/', ModelSerializerAPI.as_view()),
    path('hyper-ser/', HyperLinkedSerializerAPI.as_view()),
    path('hyper-ser/<int:id>/', HyperlinkedModelSerializerRecordViewAPI.as_view(), name="forest-detail"),
]