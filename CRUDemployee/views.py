from django.shortcuts import render, HttpResponse
from CRUDemployee.models import Employee


# Create your views here.
def home(request):
	if request.method=='POST':
		btn = request.POST['btn']
		if(btn=='insert'):
			id = request.POST['id']
			name = request.POST['name']
			age = request.POST['age']
			
			emp = Employee()
			emp.id = id
			emp.name = name
			emp.age = age
			
			try:
				emp.save()
			except:
				return render(request, 'CRUDemployee/result.html',{'result':"Error! Can't insert into Database"})
			return render(request, 'CRUDemployee/result.html',{'result': "Inserted successfully!"})
		elif(btn=='select'):
			id = request.POST['id']
			try:
				emp = Employee.objects.get(id=id)
			except:
				return render(request,'CRUDemployee/result.html',{'result':"Can't find data in the Database"})
			return render(request, 'CRUDemployee/index.html',{'emp':emp})
		elif(btn=='update'):
			id = request.POST['id']
			emp = Employee.objects.get(id=id)
			emp.name = request.POST['name']
			emp.age = request.POST['age']
			try:
				emp.save()
			except:
				return render(request, 'CRUDemployee/result.html',{"result":"Error! Can't update Database"})
			return render(request, 'CRUDemployee/result.html',{'result': "Successfully updated!"})
		elif(btn=='delete'):
			id = request.POST['id']
			try:
				emp = Employee.objects.get(id=id)
			except:
				return render(request, 'CRUDemployee/result.html',{'result':"User doesn't exist"})
			try:
				emp.delete()
			except:
				return render(request, 'CRUDemployee/result.html',{'result':"Couldn't delete record at this time!"})
			return render(request, 'CRUDemployee/result.html',{'result':"Record deleted successfully"})
		elif(btn=='selectAll'):
			emp = Employee.objects.all()
			return render(request, 'CRUDemployee/selectAll.html',{'emp':emp})
	return render(request, 'CRUDemployee/index.html')
