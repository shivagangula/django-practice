from django.db.models import CharField
from django.db.models.functions import Cast
from django.db.models import Value as V
from django.db.models.functions import (
    StrIndex, Replace, Upper, Substr, Trim, Concat, Length)
from django.shortcuts import render
from .models import Worker, Bonus, Title
from django.db.models import F, Count, Q, Max, Sum
import time


#start = time.time()
#end = time.time()
#print("The time of execution of above program is :", end-start)

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
q = Worker.objects.values('department').annotate(
    Count(F('department'))).values('department', 'department__count')
# print(q)

# Q-9. Write an SQL query to print the FIRST_NAME from Worker table after replacing ‘a’ with ‘A’.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#replace
q = Worker.objects.annotate(
    replaced_name=Replace('first_name', V('a'), V('A')))
# print(q.values())

# Q-10. Write an SQL query to print the FIRST_NAME and LAST_NAME from Worker table into a single column COMPLETE_NAME. A space char should separate them.
# https://docs.djangoproject.com/en/4.0/ref/models/database-functions/#concat
q = Worker.objects.annotate(complete_name=Concat(
    'first_name', V(' '), 'last_name'))
# print(q.values('complete_name'))


# Q-11. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending.
q = Worker.objects.all().order_by('first_name')
# print(q.values('first_name'))

# Q-13. Write an SQL query to print details for Workers with the first name as 'Vishal and 'Monika' from Worker table.
q = Worker.objects.filter(
    Q(first_name='Vishal') | Q(first_name='Monika'))

q = Worker.objects.filter(first_name__in=['Vishal', 'Monika'])
# print(q.values('first_name'))


# Q-14. Write an SQL query to print details of workers excluding first names, 'Vishal and 'Monika' from Worker table.
q = Worker.objects.all().exclude(first_name__in=['Vishal', 'Monika'])
q = Worker.objects.filter(
    ~Q(first_name='Vishal') & ~Q(first_name='Monika')
)
# print(q.values('first_name'))

# Q-15. Write an SQL query to print details of Workers with DEPARTMENT name as “Admin”.
q = Worker.objects.filter(department="Admin")
#print(q.values('first_name', 'department'))

# Q-16. Write an SQL query to print details of the Workers whose FIRST_NAME contains ‘a’.
q = Worker.objects.filter(first_name__icontains="a")
# print(q.values('first_name'))

# Q-17. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘a’.
q = Worker.objects.filter(first_name__iendswith="a")  # Case-insensitive
# q = Worker.objects.filter(first_name__endswith="a") # Case-sensitive ( Exact Letter )
# print(q.values('first_name'))

# Q-18. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.
q = Worker.objects.annotate(
    a_letter_word=Length('first_name')).filter(
        first_name__iendswith='a').filter(a_letter_word=6)
# print(q.values('first_name'))


# Q-19. Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000
q = Worker.objects.filter(salary__range=[100000, 500000])
# print(q.values('first_name','salary'))

# Q-20. Write an SQL query to print details of the Workers who have joined in Feb’2014.
q = Worker.objects.filter(joining_date__year=2014, joining_date__month=2)
# print(q.values('first_name','joining_date'))

# Q-21. Write an SQL query to fetch the count of employees working in the department ‘Admin’.
q = Worker.objects.filter(department='Admin').aggregate(
    admin_count=Count('department'))
#q = Worker.objects.filter(department='Admin').count()
# print(q)

# Q-22. Write an SQL query to fetch worker names with salaries >= 50000 and <= 100000.

q = Worker.objects.filter(
    salary__gt=50000, salary__lt=100000
).annotate(worker_name=Concat('first_name', V(' '), 'last_name'))
#print(q.values('worker_name', 'salary'))

# Q-23 Write an SQL query to fetch the no. of workers for each department in the descending order
q = Worker.objects.values('department').annotate(
    emp_count=Count('department')).order_by('-department')
# print(q)

# Q-24. Write an SQL query to print details of the Workers who are also Managers.

q = Worker.objects.filter(title__worker_title='Manager')
# print(q.values('first_name','title__worker_title'))

# Q-25. Write an SQL query to fetch duplicate records having matching data in some fields of a table

q = Worker.objects.values('first_name').annotate(
    name_count=Count('first_name')).filter(name_count__gt=1)
#print(q.values('first_name', 'name_count'))


# Q-26. Write an SQL query to show only odd rows from a table
q = Worker.objects.annotate(
    is_odd_id=F('id') % 2).filter(is_odd_id=True)
# print(q.values('is_odd_id'))

q = Worker.objects.filter(id__iregex='^\d*[13579]$')
# print(q.values('id'))


# Q-28. Write an SQL query to clone a new table from another table.

# Q-29. Write an SQL query to fetch intersecting records of two tables.
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#intersection

# Q-32. Write an SQL query to show the top n (say 10) records of a table.
q = Worker.objects.all().order_by('-salary')[:3]
#print(q.values('first_name', 'salary'))

# Q-33. Write an SQL query to determine the nth (say n=5) highest salary from a table.
q = Worker.objects.all().order_by('-salary').first()
# print(q.salary)

# Q-35. Write an SQL query to fetch the list of employees with the same salary.

salary_list = Worker.objects.values('salary').annotate(
    salary_count=Count('salary')
).filter(salary_count__gt=1).values_list('salary', flat=True)

q = Worker.objects.filter(salary__in=salary_list)
#print(q.values('first_name', 'salary'))
#The time of execution of above program is : 0.0036687850952148438


#q = Worker.objects.filter(salary__in=Worker.objects.values('salary').annotate(
#    salary_count=Count('salary')
#).filter(salary_count__gt=1).values_list('salary', flat=True))
#The time of execution of above program is : 0.005208015441894531


# Q-39. Write an SQL query to fetch the first 50% records from a table.

no_workers = Worker.objects.all().count()
#The time of execution of above program is : 0.0007348060607910156 - Faster

#no_workers = Worker.objects.aggregate(Count('id'))
#The time of execution of above program is : 0.001260519027709961

q = Worker.objects.all()[:no_workers/2]
#print(q.count())

q = Worker.objects.all()[:Worker.objects.all().count()/2]
#print(q.count())
# The time of execution of above program is : 0.002501249313354492


#Q-40. Write an SQL query to fetch the departments that have less than five people in it.
q =  Worker.objects.values('department').annotate(dep_emp_count =  Count('department')).filter(
    dep_emp_count__lt = 3)
#print(q.query)

# Q-45. Write an SQL query to print the name of employees having the highest salary in each department.

max_salary = Worker.objects.values('department').annotate(
    Count(F('department'))
).annotate(
    salary_max = Max('salary')
).values_list('salary_max', flat=True)

q = Worker.objects.filter(salary__in = max_salary)

#print(q)

# Q-49. Write an SQL query to fetch departments along with the total salaries paid for each of them.

q = Worker.objects.values('department').annotate(
    department_salary_total =  Sum('salary')
)
print(q)