a = input().lower()
a = a.replace('a', '')
a = a.replace('o', '')
a = a.replace('i', '')
a = a.replace('e', '')
a = a.replace('y', '')
a = a.replace('u', '')
a = a.replace('', '.')
a = a.rstrip('.')
print(a)
