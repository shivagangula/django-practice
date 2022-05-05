from .models import Department, Empolyee
from rest_framework import serializers
from .message import MessageValidations





class DepartmentSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Department
        fields = [
            'name',
            'uuid',
            'updated_at',
            'created_at'
        ]


class EmployeeSerializer(serializers.ModelSerializer, MessageValidations):
    department = DepartmentSerializer(required=False)   
    
    def validate(self, data):
        employee =  self.instance
        if employee.name  == data.get('name'):
            raise serializers.ValidationError(MessageValidations.duplicate_name)
        return data

    def update(self, instance, validated_data):
        departments_instance = instance.department
        department_data = validated_data.get('department')
        if department_data:
            departments_instance.name = department_data.get('name', departments_instance.name)
            departments_instance.save()

        instance.name = validated_data.get('name')
        instance.save()
        return instance

    class Meta:
        model = Empolyee
        fields = [
            'uuid',
            'name',
            'department',
            'created_at',
            'updated_at'
        ]


class CreateListEmployeeSerializer(serializers.ModelSerializer, MessageValidations):
    department = DepartmentSerializer(required=False)
    department_uuid = serializers.UUIDField(required=False, write_only=True)   
    
    def create(self, validated_data):
        department_uuid = validated_data.get('department_uuid')
        
        try:
            department = Department.objects.get(uuid=department_uuid)
        except Department.DoesNotExist :
            raise serializers.ValidationError(MessageValidations.no_department)

        del validated_data['department_uuid']
        return Empolyee.objects.create(department=department, **validated_data)


    class Meta:
        model = Empolyee
        fields = [
            'uuid',
            'name',
            'department',
            'created_at',
            'updated_at',
            'department_uuid'
        ]