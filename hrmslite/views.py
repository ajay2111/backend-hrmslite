from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

class EmployeeListCreate(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        return Response(EmployeeSerializer(employees, many=True).data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmployeeDelete(APIView):
    def delete(self, request, pk):
        try:
            emp = Employee.objects.get(id=pk)
            emp.delete()
            return Response(status=204)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=404)


class AttendanceCreate(APIView):
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AttendanceList(APIView):
    def get(self, request, employee_id):
        records = Attendance.objects.filter(employee__employee_id=employee_id)
        data = [{
            "date": r.date,
            "status": r.status
        } for r in records]
        return Response(data)
