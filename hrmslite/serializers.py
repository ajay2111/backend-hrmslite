from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(write_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee_id', 'date', 'status']

    def create(self, validated_data):
        emp_id = validated_data.pop('employee_id')
        employee = Employee.objects.get(employee_id=emp_id)
        return Attendance.objects.create(employee=employee, **validated_data)
