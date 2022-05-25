

from rest_framework import serializers
from modules.DrfSerializers.models.model_serializer import Forest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .model import ForestSerializer

from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from modules.DrfRenders.renders import SerializerDataRender

class ForestSerializerHyper(serializers.ModelSerializer):
    forest_name = serializers.CharField(max_length=25, required=False, source='name')
    tree_count = serializers.IntegerField(required= False)
    location = serializers.CharField(max_length=25, required=False)
    url = serializers.HyperlinkedIdentityField(view_name='seri:forest-detail', lookup_field='id')
    

    #Override this to support serialization, for read operations
    #custom fields are not support
    """ def to_representation(self, instance):
        return {
            'name': instance.name,
        } """
    
    class Meta:
        model = Forest
        fields = ['id','url', 'forest_name', 'tree_count', 'location']

from rest_framework import viewsets

class HyperLinkedSerializerAPI(generics.GenericAPIView):

    #renderer_classes = [CamelCaseJSONRenderer, SerializerDataRender]

    def get(self, request, *args, **kwargs):
        query_data = Forest.objects.all()
        #Serializing multiple objects
        ser_data = ForestSerializerHyper(query_data, many=True, context={'request': request})
        return Response(
                {'status': 'succuss', 'data': ser_data.data},
                status=status.HTTP_200_OK)


class HyperlinkedModelSerializerRecordViewAPI(generics.RetrieveAPIView):
    queryset = Forest.objects.all()
    serializer_class = ForestSerializer
    lookup_field = "id"