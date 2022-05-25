
from rest_framework import serializers
from modules.DrfSerializers.models.model_serializer import Forest
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# custom outside function validtor
def forest_name_validator(value):
    splited_value = value.split()
    if ('Forest' not in splited_value) :
        raise serializers.ValidationError('tress name must be contain forest name')
    

class ForestSerializer(serializers.ModelSerializer):


    name = serializers.CharField(max_length=25, required=False, validators=[forest_name_validator])
    tree_count = serializers.IntegerField(required= False)
    location = serializers.CharField(max_length=25, required=False)


    #field_level validation
    def validate_tree_count(self, value):
        if int(value) == 0:
            raise serializers.ValidationError({'input_error':'value must be greater then zero'})
        return value
    
    #object level validation:
    def validate(self, data):
        if data['location'] in ['Dubai']:
            raise serializers.ValidationError({'data_error':'this location were under ban'})
        return data
        
    #overide create method :
    def create(self, validated_data):
        try:
           Forest.objects.get(name=validated_data['name'])
           raise serializers.ValidationError({'data_error':'this forest alredy existed'})
        except Forest.DoesNotExist:
            return Forest.objects.create(**validated_data)
   
    #overide update method
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tree_count = validated_data.get(
            'tree_count', instance.tree_count)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

    class Meta:
        model = Forest
        fields = "__all__"


class ModelSerializerAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        ser_data = ForestSerializer(data = request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(
                {'status': 'succuss', 'data': ser_data.data},
                status=status.HTTP_200_OK)
        return Response(
            {'status': 'failed', 'errors': ser_data.errors},
            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        query_data = Forest.objects.all()
        #Serializing multiple objects
        ser_data = ForestSerializer(query_data, many=True)
        return Response(
                {'status': 'succuss', 'data': ser_data.data},
                status=status.HTTP_200_OK)
                
    def put(self, request, *args, **kwarg):
        ser_data = ForestSerializer(data = request.data, many=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(
                {'status': 'succuss', 'data': ser_data.data},
                status=status.HTTP_200_OK)
        return Response(
            {'status': 'failed', 'errors': ser_data.errors},
            status=status.HTTP_400_BAD_REQUEST)
        


#By default "unique together" validation enforces that all fields be required=True. 
# In some cases, you might want to explicit apply required=False to one of the fields, 
# in which case the desired behaviour of the validation is ambiguous.


#Deserializing multiple objects
#The default behavior for deserializing multiple objects is to support multiple object creation,
#  but not support multiple object updates. 
# For more information on how to support or customize either of these cases, 
# see the ListSerializer documentation  .