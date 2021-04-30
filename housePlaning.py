objetivo = int(input("Inserte una cantidad objetivo:    "))
ahorro = int(input("Inserte una cantidad de ahorro mensual:    "))
roi = int(input("Inserte un ROI anual:    "))
dinero = 0
suma = 0
inversion = 0
conta = 1


while (objetivo > dinero):
    dinero = round(dinero + inversion,2)
    suma = round(dinero + (ahorro * 12),2)
    inversion = round(suma * (roi / 100),2)
    print (conta,"          ",dinero,"             ",suma,"            ",inversion)
    dinero =+ suma
    conta += 1