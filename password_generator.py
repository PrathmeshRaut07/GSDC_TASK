import random
def password_generator():
    small_characters=[chr(x) for x in range(ord('a'),ord('z')+1)]
    capital_characters=[chr(x) for x in range(ord('A'),ord('Z')+1)]
    special_characters=['!','@','#','$','%','^','*','(',')','+','-','[',']','{','}','|',';',':','.','<','>']
    numbers=[str(i) for i in range(0,10)]
    List=small_characters+capital_characters+special_characters+numbers
    random.shuffle(List)
    a=random.choices(List,k=10)
    random.shuffle(a)
    return ''.join(a)
print('Do you what to generate password?')
response=input()
if response=='Yes'or 'yes':
    print(password_generator())
else:
    print('not logged in')    
