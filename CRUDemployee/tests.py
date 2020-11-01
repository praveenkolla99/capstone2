from django.test import TestCase
from CRUDemployee.models import Employee

from django.core.files import File

class EmployeeTestCase(TestCase):
	def setUp(self):
		Employee.objects.create(id=101, name="Rock", age=18)

	def test_employee_retrieve(self):
		obj = Employee.objects.get(id=101)
		self.assertEqual(obj.name, "Rock")

	def test_employee_update(self):
		obj = Employee.objects.get(id=101)
		obj.name = "Sam"
		obj.save()
		print("\nObject updated!")
		newObj = Employee.objects.get(id=101)
		self.assertEqual(newObj.name, 'Sam')

	def test_employee_delete(self):
		count = Employee.objects.count()
		obj = Employee.objects.get(id=101)
		obj.delete()
		newCount = Employee.objects.count()
		print(count, newCount)
		self.assertEqual(count-1, newCount)


