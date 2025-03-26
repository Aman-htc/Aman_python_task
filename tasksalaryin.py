list_data=[]

salary=input('please enter your salary 1: ')
if salary.isdigit():
    salary=int(salary)
    if salary >=10000 and salary<=100000:
        list_data.append(salary)
       
        salary=input('please enter your salary 2: ')
        if salary.isdigit():
            salary=int(salary)
            if salary >=10000 and salary<=100000:
                
                list_data.append(salary)
               
                salary=input('please enter your salary 3: ')
                if salary.isdigit():
                    
                    salary=int(salary)
                    if salary >=10000 and salary<=100000:
                       list_data.append(salary)
                       salary=input('please enter your salary 4: ')
                       if salary.isdigit():
                           salary=int(salary)
                           if salary >=10000 and salary <=100000:
                               list_data.append(salary)
                               print('Top two higher salary!') 

                               list_data.sort()
                               print(list_data[2:])

                               
                           else:
                               print('please enter you minimum 10000 and maximum 100000')    
                       else:
                           print('enter your money')    
                        
                    else:
                        print('please enter you minimum 10000 and maximum 100000')   
                else:
                    print('enter your money!')
    
            else:
                
                print('please enter you minimum 10000 and maximum 100000')   

        else:
           print('enter your money!')
    
    else:
        print('please enter you minimum 10000 and maximum 100000')   

else:
    print('enter your money!')
    
