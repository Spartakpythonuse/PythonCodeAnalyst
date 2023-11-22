#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = 22 
name = 'Spartak'


# In[2]:


age


# In[4]:


print(name)


# In[9]:


user_ages = [10, 18, 21, 35, 42, 27, 12, 16]


# In[13]:


for i in user_ages:
    if i > 18:
        print(i)


# In[ ]:


#Напишите программу, проверяющую стаж работы сотрудника. 
#В переменной worker уже содержится список, содержащий значения как на 3-ем шаге (имя, фамилия, зарплата, стаж). 
#Поместите в переменную status следующую строку:


# In[62]:


worker = ['Olya', 'Silyutina', 350000, 3]


# In[63]:


status = '{user_name} {user_family} is {position}'


# In[64]:


status = '{user_name} {user_family} is {position}'
job = worker[-1]
if job < 2:
    position = 'junior'
elif job >= 2 and job <= 5:
    position = 'middle'
else:
    position = 'senior'

user_name = worker[0]
user_family = worker[1]

print(status.format(position = position, user_name = user_name , user_family = user_family))


# In[ ]:





# In[56]:


#В списке values содержатся числовые значения. 
#Создайте список tens и добавьте в него все числа из values, которые делятся на 10 нацело.


# In[1]:


values = [12, 134, 10, 47, 100, 20, 50, 160, 210]


# In[53]:


tens = []
for i in values:
    if i % 10 == 0:
        tens.append(i)
       


# In[ ]:





# In[4]:


workers = [['Ivan', 'Ivanov', 100000, 1], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 10]]


# In[ ]:





# In[5]:


for i in workers:
        if i[3] < 2:
            status = i[0] + ' ' + i[1] + ' ' + 'is Junior'
        elif i[3] >= 2 and  i[3] <= 5:
            status = i[0] + ' ' + i[1] + ' ' + 'is Middle'
        elif i[3] > 5:
            status = i[0] + ' ' + i[1] + ' ' + 'is Senior'
        print(status)


# In[ ]:





# In[ ]:





# In[189]:


#Поместите в список lst числа от 0 (n = 0) до 10 включительно (N = 10) c шагом 2 (dn = 2). 
#Для этого используйте условие while.
    


# In[15]:


dn = 2
n = 0
N = 10
lst = []
while n <= N:
    if n % dn == 0:
        lst.append(n)
        n = n + 1
    else:
        n = n + 1


# In[16]:


lst


# In[ ]:





# In[5]:


#Ключом будет логин пользователя (login)
#В качестве значения – словарь с характеристиками (как на предыдущем шаге) для этого пользователя


# In[13]:


users_dict = {
'mvolkova' : {'name' : 'Masha', 'surname' : 'Volkova', 'age' : 25, 'salary' : 60000, 'position' : 'junior' },
'pvoronov' : {'name' : 'Peter', 'surname' : 'Voronov', 'age' : 27, 'salary' : 100000, 'position' : 'junior' },
'pparker' : {'name' : 'Peter', 'surname' : 'Parker', 'age' : 35, 'salary' : 150000, 'position' : 'middle' },
'akarpov' : {'name' : 'Anatoly', 'surname' : 'Karpov', 'age' : 30, 'salary' : 250000, 'position' : 'senior' }
}


# In[ ]:




