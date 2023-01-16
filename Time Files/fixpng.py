w = []
temp = []
image = open("flag.png", "rb")

while 1:
    cur = image.read(1)
    if not cur:
        break
    temp.append(cur)
    if len(temp) == 4:
        while len(temp):
            w.append(temp.pop())

image.close()

while len(temp):
    w.append(temp.pop())

image = open("fixed.png", "wb")
for i in w:
    image.write(i)
