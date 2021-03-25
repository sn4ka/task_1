text = str(input("Введите текст на англ.языке: "))
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"
Y = "Y"
y = "y"
acount = 0
ecount = 0
icount = 0
ocount = 0
ucount = 0
ycount = 0
for letter in text:
    if letter in A or letter in a:
        acount += 1

    if letter in E or letter in e:
        ecount += 1

    if letter in I or letter in i:
        icount += 1

    if letter in O or letter in o:
        ocount += 1

    if letter in U or letter in u:
        ucount += 1

    if letter in Y or letter in y:
        ycount += 1

print("a",acount,"\ne", ecount,"\ni", icount,"\no", ocount,"\nu", ucount,"\ny", ycount)
