# Driver code
# lst = ["rohan", "amy", "sapna", "muhammad",
#        "aakash", "raunak", "chinmoy"]
# print(sorted(lst, key=len))

# print('C:\\Windows\\System32')
# from pathlib import Path, WindowsPath
#
# homeFolder = Path('C:/Users/Al')
# subFolder = Path('spam')
# a = homeFolder / subFolder
# # WindowsPath('C:/Users/Al/spam')
# print(str(homeFolder / subFolder))


# x = list(input("enter string: "))
# now = ''.join(x)
# ltr = ''.join(x[::-1])
# print("before reverse: " + now)
# print("after reverse: " + ltr)
# if now == ltr:
#     print("is palindrome")
# else:
#     print("not a palindrome")

# l = ["lol","ls","not"]
# l.append(4.1)
# l.insert(3,490)
# print(l)
# l.remove("ls")
# print(l)

# import requests, sys, webbrowser, bs4
#
# print('Googling...') # display text while downloading the Google page
# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
#
# res.raise_for_status()
#
# # Retrieve top search result Links.
# soup = bs4.BeautifulSoup(res.text)
#
# # Open a browser tab for each result.
# linkElems = soup.select('.r a')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     webbrowser.open('http://google.com' + linkElems[i].get('href'))
# str = (input("enter  a sentence: ").split())
# x = sorted(str, key=len)
# print("the longest string is ", x[-1], " of length", len(x[-1]))

a = ['kade','sade','made']
s = input()
d = {}
for i in a:
   if s in d:
       d[s] += 1
   else:
       d[s] = 1
print(d)

