from sys import argv

script,filename=argv

txt=open(filename)

print(f"here's your file {filename}:")
print(txt.read())

print("type the filename again:")
file_again=input("> ")

txt_again=open(file_again)

print(txt_again.read())
