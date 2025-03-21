data={}
data2={}
skills=[]
qulification_information={}
list_data=[]

data['id']=int(input('please enter your id: '))
data['name']=input('please enter your name: ')
data['exprinece']=input('please enter your exprience: ')
print('please enter your skills! ')
skills.append(input('please enter your first skills: '))
skills.append(input('please enter your seonds skills: '))
skills.append(input('please enter your thirds skills: '))
data['skills']=skills
print('please enter your qulification information! ')
qulification_information['qulificationname']=input('please enter your qulification name: ')
qulification_information['passingyear']=input('please enter your passing year: ')
list_data.append(qulification_information)
data['qulification']=list_data
qulification_information={}
qulification_information['qulificationname']=input('please enter your qulification name: ')
qulification_information['passingyear']=input('please enter your passingyear: ')

list_data.append(qulification_information)
data['qulification']=list_data
print('please seconds student information input! ')
data2['id']=int(input('please enter your id:'))
data2['name']=input('please enter your name: ')
data2['exprience']=input('please enter your exprience: ')
data['']=data2

skills=[]
print('please enter your skills!')
skills.append(input('please enter your first skills: '))
skills.append(input('please enter your seonds skills: '))
skills.append(input('please enter your thirds skills: '))

data['skill']=skills

qulification_information={}
list_data=[]
print('please enter your qulification!')
qulification_information['qulification name']=input('please enter your qulification name: ')
qulification_information['passingyear']=input('please enter your passing year: ')
list_data.append(qulification_information)
data['qulification2']=list_data

print(data)