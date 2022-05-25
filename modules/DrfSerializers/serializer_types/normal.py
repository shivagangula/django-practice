# Basic class
# which is needed for creating objects
from rest_framework.parsers import JSONParser
import io
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers


class Forest:
    def __init__(self, forest_name, number_of_trees, forest_location):
        self.forest_name = forest_name
        self.number_of_trees = number_of_trees
        self.forest_location = forest_location

    def __str__(self):
        return f"{self.forest_name}"


# Declearing serializer for forest objects
class ForestSerializer(serializers.Serializer):
    forest_name = serializers.CharField(max_length=25)
    number_of_trees = serializers.CharField(max_length=25)
    forest_location = serializers.CharField(max_length=25)


# Create forest object
forest_amazon = Forest(forest_name="Amazon Forest",
                number_of_trees="24000", forest_location="India")
forest_nallamala = Forest(forest_name="Nallamala Forest",
                number_of_trees="4040", forest_location="Andrapradesh")


# pass single object
serializer_data = ForestSerializer(forest_amazon).data # data type <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

# pass multiple objects
forest_list = [forest_amazon, forest_nallamala]
serializer_data = ForestSerializer(forest_list, many= True).data #<class 'rest_framework.utils.serializer_helpers.ReturnList'>


"""
At this point we've translated the model instance into Python native datatypes. 
To finalise the serialization process we render the data into json.
"""

# serialiizing python objects to json
forest_json = JSONRenderer().render(serializer_data) # forest_json - byte data type

# de-serializering json to python
stream = io.BytesIO(forest_json)
forest_data = JSONParser().parse(stream) # forest_data - dict data type
#----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#playing with Instances :
class ForestSerializer2(serializers.Serializer):
    forest_name = serializers.CharField(max_length=25, required=False)
    number_of_trees = serializers.CharField(max_length=25, required=False)
    forest_location = serializers.CharField(max_length=25, required=False)

    def create(self, validated_data):
        return Forest(**validated_data)

    def update(self, instance, validated_data):
        instance.forest_name = validated_data.get('forest_name', instance.forest_name)
        instance.number_of_trees = validated_data.get('number_of_trees', instance.number_of_trees)
        instance.forest_location = validated_data.get('forest_location', instance.forest_location)
        return instance



forest_nilagiri  = {
    "forest_name":"Nilagiri Forest", 
    "number_of_trees":"2545", 
    "forest_location":"Telangana"}
serializer_data = ForestSerializer2(data=forest_nilagiri)
if serializer_data.is_valid():
      serializer_data.save()
      print(serializer_data.data)
else:
    print(serializer_data.errors)


#update object
forest_tirumala = Forest(
    forest_name="Tirumala Forest",
     number_of_trees = "25465",
    forest_location="Tirupathi")
serializer_data = ForestSerializer2(forest_tirumala, data={"number_of_trees":"3000"})
if serializer_data.is_valid():
      serializer_data.save()
      print(serializer_data.data)
else:
    print(serializer_data.errors)
