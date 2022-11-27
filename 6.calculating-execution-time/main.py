from time import time
start = time()
#Python program to create acronyms
word = "Artifical Intelligence"
text = word.split()
a = ""
for i in text:
    a+=str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print(f"Execution Time : {execution_time}")