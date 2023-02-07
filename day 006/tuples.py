empty_tuple = ()

Brothers = ('Yaya',  'Dan Malam',  'Abdu')
Sisters = ('Ladi','Kande','Ikilima','Lantana')
siblings = Brothers + Sisters
print(siblings)

No_of_siblings =len(siblings)
print(f'I have {No_of_siblings} siblings')
Siblings = list(siblings)
Siblings.append('Abba')
Siblings.append('Umma')
family_members = tuple(Siblings)
print(f'My family members are : {family_members}')

Fam= list(family_members)

*scadic, Abba, Umma = Fam
print('siblings unpacked from family members', scadic)
idi, Dm, Auduwa, Ladidi, Kandala, iki, Lanto, *rest = Fam
print('Parents unpacked from family members',rest)

fruits = ('lemon', 'pear', 'apple', 'cashew')
vegetables = ('carrots', 'tomato', 'lettuce', 'potato')
animals_products = ('meat', 'eggs', 'hide','milk', 'cheese')
food_stuff_tp = fruits + vegetables + animals_products
print('Food stuff tuple is : ' , food_stuff_tp )
food_stuff_lt = list(food_stuff_tp)
print('Food stuff list is : ' , food_stuff_lt )
No_of_foodstuff = len(food_stuff_lt)
middle_item = No_of_foodstuff // 2
slicing_middle_item = food_stuff_lt[middle_item]

print('The middle item is ',slicing_middle_item)
first_3_items = food_stuff_lt[0:3]
print('the first three items are ', first_3_items)
last_3_items = food_stuff_lt[-4:-1]
print('the last three items are ', last_3_items)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('checking whether Estonia is a nordic country :', 'Estonia' in nordic_countries)
print('checking whether Iceland is a nordic country :', 'Iceland' in nordic_countries)