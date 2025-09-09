
# Programa: Número invertido

# Solicita el número al usuario
numero = int(input("Ingresa un número entero: "))

# Conserva el signo si el número es negativo
signo = -1 if numero < 0 else 1
numero = abs(numero)

# Inicializa el número invertido
invertido = 0

# Ciclo para invertir los dígitos
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

# Aplica el signo original
invertido *= signo

# Muestra el resultado
print(f"El número invertido es: {invertido}")
