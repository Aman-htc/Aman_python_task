



data=[]
student={}
qulification_list=[]
qulification={}
skills=[]

student2={}


student['id']=int(input('please enter your id: '))
student['name']=input('please enter your name: ')
student['experience']=input('please enter your experience: ')
print('please enter your skills!')
skills.append(input('please enter your first skills: '))
skills.append(input('plesae enter your seconds skills: '))
skills.append(input('please enter your thirds skills: '))
student['skills']=skills

print('please enter your qulification information!')

qulification['name']=input('please enter your qulification name: ')
qulification['passingyear']=int(input('please enter your passing year: '))
qulification_list.append(qulification)

student['qulification']=qulification_list

qulification={}

qulification['name']=input('please enter your qulification name: ')
qulification['passingyear']=int(input('please enter your passing year:'))

qulification_list.append(qulification)

student['qulification']=qulification_list
data.append(student)


print('please enter your second student input information! ')

student2['id']=int(input('please enter your id: '))
student2['name']=input('please enter your name: ')
student2['experience']=input('please enter your experience: ')


print('please enter your skills!')
skills=[]
skills.append(input('please enter your first skills: '))
skills.append(input('plesae enter your seconds skills: '))
skills.append(input('please enter your thirds skills: '))
student2['skills']=skills


print('please enter your qulification information!')
qulification_list=[]
qulification={}

qulification['name']=input('please enter your qulification name: ')
qulification['passingyear']=int(input('please enter your passing year: '))

qulification_list.append(qulification)

student2['qulification2']=qulification_list
data.append(student2)

print(data)