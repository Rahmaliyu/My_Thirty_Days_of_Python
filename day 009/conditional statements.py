age = int(input('Enter your Age:  '))
if age >= 18 :
    print('You are old enough to drive.')
else:
    remaiing_age = 18 - age
    print('you are not  18. wait for  {} years  for you to start driving'.format(remaiing_age))

my_age = 25
your_age = int(input('Enter your age : '))
age_difference = your_age - my_age
if your_age > my_age :
        if age_difference == 1 :
            print('you are one year older than me')
        else :
            print('you are {} older than me.'.format(age_difference))
elif  my_age == your_age:
        print('we are the same age ')
else :
     print('i am older than you')        


A = int(input('Enter number one'))
B =int(input('Enter number two'))

if A > B :
     print(f'{A}  is grater than {B}')
elif A < B:
     print(f'{A} is smaller than {B} ')
else :
     print(f'{A} is equal to {B} ')     


score = int(input ('Enter Studnts score : (from 0 - 100)  '))
if score >= 80 and score <= 100:
     print('Studen\'ts grade is A ')
elif score >= 70 and score <= 89:
     print('Studen\'ts grade is B')
elif score >= 60 and score <= 69:
     print('Studen\'ts grade is C') 
elif score >= 50 and score <= 59:
     print('Studen\'ts grade is D')
elif score >= 0 and score <= 49:
     print('Studen\'ts grade is F') 
else :
     print('invalid score')


Month = input('please enter month if the year to know its season :  ')   
Months = [ 'September','October', 'November',' December', 'January ','February', 
         'March', 'April', 'May', 'June', 'July' ,'August' ]  


if Month in  Months[:3] :
     print('the season is Autumn')
elif Month in Months[3:6] :
    print('the season is winter') 
elif Month in Months[6:9] :
    print('season is Spring')
else:
      print('the season is summer')               

          
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter the name of a fruit  ')
if fruit in fruits:
     print('That fruit already exist in the list')
else:
     fruits.append(fruit)
     print('The fruit you entered does not exist in the list, and it has been added in the list', fruits)
     


     person={
    'first_name': 'Asabe',
    'last_name': 'Danladi',
    'age': 250,
    'country': 'Nigeria',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 
               'Python'],
    'address': {
        'street': 'Layin Malamai',
        'zipcode': '02210'
    }
    }
if 'skills' in person :
     median = len( person['skills'])
middle_item = median // 2
print(person['skills'][middle_item])

if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person have python skills')
    else:
        print('this person has no python skills')
else:
    print('this person dont have any skill')

    
if person['skills'] == ['JavaScript', 'React'] :
     print('He is a front end developer')
elif ['Node', 'Python', 'MongoDB'] in person['skills']:
     print('He is a backend developer')     
elif ['React', 'Node', 'MongoDB'] in person['skills']  :
     print ('He is a fullstack developer')
else:
     print ('unknown title')

     
if person['is_marred'] == True and person['country'] == 'Nigeria':
     print(person['first_name'], person['last_name'], 'Lives in', person['country'], 'He is Married')

