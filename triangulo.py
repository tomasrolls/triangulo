from tkinter import *
texto=""
def triangulo(ladoa,ladob,ladoc,delta):
    x0 = 400
    y0 = 400
    canvas = Canvas(width=800, height=800, bg='yellow')
    ladoa = ladoa*delta
    ladob = ladob*delta
    ladoc = ladoc*delta
    x1 = x0 - ladoa/2
    y1 = y0
    x2 = x0 + ladoa/2
    y2 = y0
    x3 = x2 -(ladob**2+ladoa**2-ladoc**2)/(2*ladoa)
    y3 = y0 - (ladob**2 - ((ladob**2+ladoa**2-ladoc**2)/(2*ladoa))**2)**.5
    if (ladoa==ladob) and (ladob==ladoc) :
        tipo = "Equilatero"
    elif (ladoa!=ladob) and (ladob!=ladoc) and (ladoc!=ladoa) :
        tipo = "Escaleno"
    else :
        tipo = "IsÃ³sceles"
    canvas.create_line(x1, y1, x2, y2, x3, y3, x1,y1)
    canvas.create_line(x0 -400, y0, x0 + 400, y0)
    canvas.create_line(x0, y0 - 400, x0, y0 + 400)
    canvas.pack(fill=BOTH, expand=1)
    return tipo
a = int(input("Lado a: "))
b = int(input("Lado b: "))
c = int(input("Lado c: "))
if (a+b)>c and (a+c)>b and (b+c)>a :
    p = a + b + c
    factor = 600/p
    texto = triangulo(a, b, c, factor)
    s = p/2
    a = (s * (s - a)*(s - b)*(s - c))**.5
    print("El triÃ¡ngulo formado por a, b, c es ",texto," de perÃ­metro ",p," y Ã¡rea ",a)
else :
    print("a, b, c no son lados de un triÃ¡ngulo")
