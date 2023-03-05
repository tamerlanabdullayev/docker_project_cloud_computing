from collections import Counter
import socket
from requests import get
import os

result = ""

current_dir = os.getcwd()
os.chdir(os.path.join(current_dir, "home", "data"))


print("List of the files in /home/data: " + ", ".join(os.listdir()), end="\n\n")
result += "List of the files in /home/data: " + ", ".join(os.listdir())

while True:
    try:
        file1_name = input("Enter the name of the first file: ")
        with open(file1_name, "r") as f:
            f1 = f.read()
        break
    except FileNotFoundError:
        print("File not found. Please try again.")

while True:
    try:
        file2_name = input("Enter the name of the second file: ")
        with open(file2_name, "r") as f:
            f2 = f.read()
        break
    except FileNotFoundError:
        print("File not found. Please try again.")


result += "\n\nNumber of words in IF.txt: " + str(len(f1.split()))
result += "\nNumber of words in Limerick.txt: " + str(len(f2.split()))
result += "\nTotal number of words in both files: " + str(len(f1.split()) + len(f2.split()))

result += "\n\nTop 3 words in IF.txt: "
for w in Counter(f1.split()).most_common(3):
    result += "\n    ‣" + str(w[0]) + ": " + str(w[1])

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
result += "\n\nThe local IP address of the computer is: " + IPAddr

ip = get('https://api.ipify.org').content.decode('utf8')
result += '\n\nThe public IP address of the computer is: {}'.format(ip)

print(result)

with open('result.txt', 'w', encoding='UTF-8') as f:
    f.write(result)
