

from modules.DjangoFeatures.models.transaction_models import TableOne, TableTwo
from django.db import transaction, IntegrityError
from django.db.utils import DataError
from rest_framework import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


# Working
#tbo = TableOne.objects.create(data="Mindblow")
# TableTwo.objects.create(table_one_data=tbo)


# try:
#    tbo = TableOne.objects.create(data="Mindblow") # tbo data created
#    print(1/0)
#    TableTwo.objects.create(table_one_data=tbo) # data not created
# except:
#    print("Expection")


# handle transcations
# try:
#     with transaction.atomic():
#         tbo = TableOne.objects.create(data="Django")
#         print(tbo.data) # tbo data created
#         TableTwo.objects.create(table_one_data = tbo, data="shivashivashivashobabkdbdksjb") # issue with length constrain
# except IntegrityError:
#     print("IntegrityError")
# except DataError:
#     print("postgresql data errror")




#Nested serializer_class
class TableOneSerializer(serializers.ModelSerializer):
    data = serializers.CharField(required=False)

    class Meta:
        model = TableOne
        fields = "__all__"


class TabletwoSerializer(serializers.ModelSerializer):
    data = serializers.CharField(required=False,  max_length=10)
    table_one_data = TableOneSerializer(required=False, write_only=True)

    def create(self, validated_data):
        # creating dummy data without using post data and forcing faiulre
        try:
            with transaction.atomic():
                tbo = TableOne.objects.create(data="Django2")
                tbw = TableTwo.objects.create(
                    table_one_data=tbo, data="shivagangulashivagangul")
                return tbw
        except:
            raise serializers.ValidationError(
                {'db_error': "transaction failed"})

    class Meta:
        model = TableTwo
        fields = "__all__"




# views
class TranscationTestview(generics.GenericAPIView):
    serializer_class = TabletwoSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = TabletwoSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()  # if u not call then data will not save
            return Response({'status': 'succuss', 'data': serializer_data.data}, status=status.HTTP_200_OK)
        return Response({'status': 'failed', 'data': serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST)
