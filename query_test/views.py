from django.db.models import Value as V
from django.db.models.functions import StrIndex , Replace, Upper, Substr, Trim, Concat
from django.shortcuts import render
from .models import Worker, Bonus, Title
from django.db.models import F, Count, Q

def test(): ...


# Q-1. Write an SQL query to fetch “FIRST_NAME” from Worker table using the alias name as <WORKER_NAME>.
q = Worker.objects.annotate(worker_name=F('first_name'))
# print(q.values())


# Q-2. Write an SQL query to fetch “FIRST_NAME” from Worker table in upper case.
q = Worker.objects.annotate(
    first_name_cap=Upper(F('first_name')))
# print(q.values())

# Q-3. Write an SQL query to fetch unique values of DEPARTMENT from Worker table.
# Support only postgresql
#q = Worker.objects.all().distinct('department')
# print(q.values())


# Q-4. Write an SQL query to print the first three characters of  FIRST_NAME from Worker table.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#substr
q = Worker.objects.annotate(first_name_letter=Substr('first_name', 1, 3))
# upper q = Worker.objects.annotate(first_name_letter = Upper ( Substr('first_name', 1,3)))
# print(q.values())


# Q-5. Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#strindex
q = Worker.objects.filter(first_name='Amitabh').annotate(
    amitabh_index=StrIndex('first_name',  V('a'))).get().amitabh_index
# print(q)

# Q-6. Write an SQL query to print the FIRST_NAME from Worker table after removing white spaces from the right side.
# Q-7. Write an SQL query to print the DEPARTMENT from Worker table after removing white spaces from the left side.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#trim


# Q-8. Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length.
q = Worker.objects.values('department').annotate(Count(F('department'))).values('department', 'department__count')
#print(q)

#Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#replace
q = Worker.objects.annotate(replaced_name = Replace('first_name', V('a'), V('A')))
#print(q.values())

#Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#concat
q = Worker.objects.annotate(complete_name = Concat('first_name', V(' '), 'last_name'))
#print(q.values('complete_name'))


# Q-11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.
q = Worker.objects.all().order_by('first_name')
#print(q.values('first_name'))

#Q-13. Write an SQL query to print details for Workers with the first name as 'Vishal and 'Monika from Worker table.
q = Worker.objects.filter(
    Q(first_name='Vishal') | Q(first_name = 'Monika'))

q = Worker.objects.filter(first_name__in = ['Vishal','Monika'])
#print(q.values('first_name'))


