import string
st = input("Please enter the string: ")
x = list(string.ascii_letters)
y = list(string.digits)
let, dig = 0, 0
for i in st:
    if i in x:
        let+=1
    elif i in y:
        dig+=1

print(let,dig)
        

