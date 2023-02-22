import re
x = input("Enter the name: ")
rex = re.compile(r'[A-Z](\w)*\sNakamoto')
find = rex.search(x)
print(find.group())

# accepted:
# 'Satoshi Nakamoto'
# 'Alice Nakamoto'
# 'RoboCop Nakamoto'

# Rejected:
#  'satoshi Nakamoto'
#  'Mr. Nakamoto'
#  'Nakamoto'
#  'Satoshi nakamoto'

