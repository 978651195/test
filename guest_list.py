#leon
#2019.3.1
#guest list
people=['tom','sophia','ken']
print(people)
message = " can't  go to an appointment"
print(people[2]+message)
people[2]='lucy'
print(people)
new_message=" I find a new table which can contain more people"
print(new_message)
people.insert(0,'jerry')
people.insert(2,'sunny')
people.append('atom')
print(people)
new_message=" sorry,I can only invite two people"
print(new_message)
person=people.pop()
new_message=" sorry,I can't invite you to my party"
print(person+new_message)
person=people.pop()
print(person+new_message)
person=people.pop(0)
print(person+new_message)
person=people.pop(2)
print(person+new_message)
new_message=" you are coming to my party!"
print(people[0]+new_message)
print(people[1]+new_message)
print(people)
del people[0]
del people[0]
print(people)
