word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of'
word_4 = 'Python'
space =  ' '
sentence_1 = word_1 + space + word_2 + space + word_3 + space + word_4

word_5 = 'Coding'
word_6 = 'For'
word_7 = 'All'
company = word_5 + space + word_6 + space + word_7
print(company)

print(len(company))

print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.strip('Coding'))
string_to_be_found = 'Coding'
print(company.index(string_to_be_found))
print(company.find('Coding'))
print(company.replace( 'Coding' , 'Python'))
print(company.replace( 'Coding' , 'Python'))
sentence_2 = 'Python for Everyone'
print(sentence_2.replace( 'Everyone' , 'All'))
print(company.split())
social_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_media.split(','))
print(company[0])
print(company[-1])
print(company[10])
PFE = sentence_2[0:3]
print(PFE)
CFO =  company[0:7:11]
print(CFO)
print(company.find('C'))
print(company.find('F'))
company_2 ='Coding for All People'
print(company_2.rfind('l'))
sentence_3 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_3.find('because'))
print(sentence_3.rfind('because'))
because = sentence_3[31:54]
print(because)
print(company.startswith('Coding'))
print(company.endswith('Coding'))
company_3 = '   Coding For All      ' 
print(company_3.strip(' '))
Argument_1='30DaysOfPython'
Argument_2 ='thirty_days_of_python'
print(Argument_1.isidentifier())
print(Argument_2.isidentifier)
python_lib =['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_words = '# '.join(python_lib)
print(joined_words)
print("I am enjoying this challenge.\n I just wonder what is next.")
print('Name\t Age\tCountry\tCity \nAsabeneh  250\tFinland\tHelsinki')  

radius = 10
pi = 3.14
area = pi * radius ** 2
print(f'The area of a circle with a radius {radius} is {area}' )


a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')