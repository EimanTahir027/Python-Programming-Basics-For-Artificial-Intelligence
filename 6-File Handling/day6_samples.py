

try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File Not Found!")