from math import cos,radians,sin,sqrt

v0 = float(input("Digite o valor do v0 em m/s²: "))
ang = radians(float(input("Digite o valor do angulo em graus (se não houver digite 0): ")))
y0 = float(input("Digite o valor de y0 em metros (se não houver digite 0): "))
t = float(input("Digite um instante: "))
g = 9.8

print(" ")
print(" ")

v0x = v0 * cos(ang)
print("V0X: {:.10f}".format(v0x))
v0y = v0 * sin(ang)
print("V0Y: {:.10f}".format(v0y))
print("")

def baskara(a,b,c):
    return -(-b - sqrt(b**2 - 4*a*c))/(2*a)

def t_alcance(t_sub,v0y,y0):
    return 2*t_sub + baskara(4.9,-v0y,-y0)
tsub = v0y/g
tar = t_alcance(tsub,v0y,y0)
print("Tempo em que o objeto permanece no ar: {:.10f}".format(tar))
print("")

x = v0x*t
print("Posição X no instante {:.2f} é: {:.10f}".format(t,x))
y = y0+(v0y*t)-(g*t**2)/2
print("Posição Y no instante {:.2f} é: {:.10f}".format(t,y))
print("")

print("A Vx no tempo {:.2f} é: {:.10f}".format(t,v0x))
vy = v0y - g*t
print("A Vy no tempo {:.2f} é: {:.10f}".format(t,vy))
modv = sqrt((v0x**2)+(vy**2))
print("O |V| no tempo {:.2f} é: {:.10f}".format(t,modv))
print(" ")


Hmax = (((v0y**2)/g)/2)+y0
print("Altura máxima: {:.10f}".format(Hmax))
print(" ")

alcance = (v0x*tar)
print("Alcançe horizontal: {:.10f}".format(alcance))
print(" ")

print("Velocidade X imdediatamente antes do solo: {:.10f}".format(v0x))
vy1 = v0y - 9.8*tar
print("Velocidade Y imediatamente antes do solo: {:.10f}".format(vy1))
modv1 = sqrt((vy1**2)+(v0x**2))
print("O |V| imediatamente antes do solo: {:.10f}".format(modv1))
print("")

print("Velocidade X na altura maxima: {:.10f}".format(v0x))
print("Velocidade Y na altura maxima: 0")
print("O |V| na altura maxima: {:.10f}".format(v0x))
print("")

alti = v0/t
print("Altura inicial em centímetros: {:.10f}".format(alti))
