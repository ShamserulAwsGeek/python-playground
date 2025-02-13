f = open("demofile.txt")
f = open("demofile.txt", "rt")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(10))

f = open("demofile.txt", "rt")
print(f.readline())


f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


f = open("demofile.txt", "r")
for x in f:
  print(x)


f = open("demofile.txt", "r")
print(f.readline())
f.close()