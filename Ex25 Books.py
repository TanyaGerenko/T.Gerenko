books=[
[34587,'Learning Python,Mark Lutz',4,40.95],
[98762,'Programming Python,Mark Lutz',5,56.80],
[77226,'Head First Python,Paul Barry',3,32.95],
[88112,'Einfuhrung in Python3,Bernd Klein',3,24.99]
    ]


def myfunc(*args):
    
    for arg in args:
        c=arg[2]*arg[3]
        if c<100:
            c=c+10
    return (arg[0],c)

books_zakaz = list(map(lambda x: myfunc(x),books))

print(books_zakaz)
