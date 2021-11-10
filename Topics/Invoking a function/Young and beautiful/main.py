jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
if jack_age < alex_age:
    if jack_age < lana_age:
        print(jack_age)
    else:
        print(lana_age)
elif alex_age < lana_age:
    print(alex_age)
else:
    print(lana_age)
