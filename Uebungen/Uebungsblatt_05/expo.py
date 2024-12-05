def ez(n, z): #taylorreihe werden benutzt, um den Wert einer Funktion an einer Stelle näherungsweise zu berechnen (approximieren). So benutzen die meisten Taschenrechner beispielsweise Taylorreihen, um den Sinus und andere trigonometrische Funktionen zu berechnen, da eine genaue Berechnung zu rechenintensiv wäre.
        sum = 1  # first term 
        fact = 1

        for i in range(1, n+1):
            fact *= i  # Berechne die Fakultät in jedem Schritt
            sum += (z**i) / fact

        return sum


def main():
    
    result = ez(5, 2)
    print(result)
main()