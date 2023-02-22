#bday={'kalu':'apr 1', 'kate':'sep 23','nate':'dec 12'}

#while True:
#    a=input('enter the name: ')
#    if a in bday:
#        print(bday[a])
#        break
#    elif a not in bday:
#        print("key doesn't exist")
#        print('what is the bday of '+a)
#        s=input()
#        bday[a]=s
#   else:
#        print('invalid')
# ----------------------------------------------------------------------------
a = ['sane','kade','sid','oda','sane','oda','said','sid','sid']
s = input()
d = {}
for s in a:
   if s in d:
       d[s] += 1
   else:
       d[s] = 1
print(d)


