


# Without loop only statement

data={}
data['id']=input('please enter your id: ')
if data['id'].isdigit():
    data['id']=int(data['id'])
    data['name']=input('please enter your name: ')
    if data['name'].isalpha():
        data['hindi']=input('please enter your hindi marks number: ')
        if data['hindi'].isdigit():
            data['hindi']=int(data['hindi'])
            data['english']=input('please enter your english marks number: ')
            if data['english'].isdigit():
                data['english']=int(data['english'])
                data['maths']=input('please enter your maths marks number: ')
                if data['maths'].isdigit():
                    data['maths']=int(data['maths'])
                    print('Marks details = ',data)
                    total_marks=data['hindi']+data['english']+data['maths']
                    print('Total marks = ',total_marks)
    
                    percentage= (total_marks / 300)*100
                    print('your percentage =',percentage)
                    if percentage >=60:
                        print('Student Division = First')
                    else:
                        
                        print('Student Division = Seconds')  
                    
                    
                else:
                    print('please enter marks number!')    
            else:
                print('please enter marks number!')    
        else:
            print('please marks number! ')    
    else:
        print('please enter your correct name! ')    
else:
    print('please enter  your id number! ')    
    
data2={}
data2['id']=input('please enter your id: ')
if data2['id'].isdigit():
    data2['id']=int(data2['id'])
    data2['name']=input('please enter your name: ')
    if data2['name'].isalpha():
        data2['hindi']=input('please enter your hindi marks number: ')
        if data2['hindi'].isdigit():
            data2['hindi']=int(data2['hindi'])
            data2['english']=input('please enter your english marks number: ')
            if data2['english'].isdigit():
                data2['english']=int(data2['english'])
                data2['maths']=input('please enter your maths marks number: ')
                if data2['maths'].isdigit():
                    data2['maths']=int(data2['maths'])
                    print('Marks details = ',data2)
                    total_marks2=data2['hindi']+data2['english']+data2['maths']
                    print('Total marks = ',total_marks2)
    
                    percentage2= (total_marks2 / 300)*100
                    print('your percentage =',percentage2)
                    if percentage2 >=60:
                        print('Student Division = First')
                    else:
                        
                        print('Student Division = Seconds') 
                    print('Topper student name!')     
                    if percentage >=percentage2:
                        print(data['name'],'is a topper')
                    else:
                        print(data2['name'],'is a topper')    
                    
                    
                else:
                    print('please enter marks number!')    
            else:
                print('please enter marks number!')    
        else:
            print('please marks number! ')    
    else:
        print('please enter your correct name! ')    
else:
    print('please enter  your id number! ')      