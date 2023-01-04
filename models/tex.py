class how:
    name=''
l = [str(k) for k in dir(how) if not k.startswith('__')]
print(l)