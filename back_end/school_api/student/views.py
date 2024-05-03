from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student2
from . serializer import StudentSerializer
from django.http import JsonResponse



# Create your views here.



@api_view(['GET'])
def load_student(request):
    students = Student2.objects.all()
    serialized_data = StudentSerializer(students, many = True)
    return JsonResponse(serialized_data.data,safe=False)

@api_view(['POST'])
def add_student(request):
    serialized_data = StudentSerializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'message':'data inserted successfully','status':200})
    else:
        print('form not valid')
        return JsonResponse({'message':'error','status':201})

@api_view(['DELETE'])
def del_student(request,s_id):
    student = Student2.objects.get(id = s_id)
    student.delete()
    return JsonResponse({'message':"deleted successfully"})

@api_view(['PUT'])
def update_student(request,s_id):
    student = Student2.objects.get(id=s_id)
    serialized_data = StudentSerializer(student,data = request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'message':'updated successfully'})
    else:
        return JsonResponse({'message':'error'})





 




    
