mk = open("mankee.txt",'w')
mk.write("sample text\n")
mk.write('i like eating chicken')
mk.close()

km = open('mankee.txt', 'r')
text = km.read()
print(text)
km.close()

