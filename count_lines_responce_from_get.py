import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.2/872.txt")
s = r.text.count("\n")
print(s)
