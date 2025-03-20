student_data={}
student_data2={}
qulification_information={}
qulification_information2={}
list_data=[]

student_data['id']=int(input('please enter your id: '))
student_data['name']=input('please enter your name: ')
student_data['experience']=input('please enter your experience: ')
print('please enter your skills!')
student_data['first_skills']=input('please enter your first skills: ')
student_data['secod_skills']=input('please enter your second skills: ')
student_data['third_skills']=input('please enter your thirds skills: ')

print('please enter your qulification!')
qulification_information['name']=input('please enter your qulification name')
qulification_information['passingyear']=input('please enter your passing year: ')
list_data.append(qulification_information)
student_data['qulification']=list_data
qulification_information={}
qulification_information['name']=input('please enter your qulification name: ')
qulification_information['passingyear']=input('please enter your passing year: ')
list_data.append(qulification_information)
student_data['qulification']=list_data

print('enter your seconds student information!')

list_data=[]

student_data2['id']=int(input('please enter your id: '))
student_data2['name']=input('please enter your name: ')
student_data2['experience']=input('please enter your experience: ')

print('please enter your skills!')
student_data2['first_skills']=input('please enter your first skills: ')
student_data2['secod_skills']=input('please enter your second skills: ')
student_data2['third_skills']=input('please enter your thirds skills: ')

list_data.append(student_data2)
student_data['secondinformation']=list_data
print('please enter your qulification!')
list_data=[]

qulification_information['name']=input('please enter your qulification name: ')
qulification_information['passingyear']=input('please enter your passing year: ')
list_data.append(qulification_information)
student_data['qulification2']=list_data





#  print(json.dumps(student_data,indent=4))
print(student_data)









