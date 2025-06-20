#Implementar una calculadora que pida dos numero y una opeacion, vamos a usar la figyura de switch....case y luego con if...elif...else.

# num_1 = float(input("Dame tu primer numero: "))
# num_2 = float(input("Dame tu segundo numero: "))
# operador = input("Que operacion quieres hacer? (+,-,*,/): ")


# Como así que switch y case?

# Switch y case es una forma diferente de escribir condicionales, donde se evalua un parametro, booleano, y se va a direccionar inmediatamente segun los casos definidos 

# match operador:
#     case "+":
#         print("resultado", num_1 + num_2)
#     case "-":
#         print("resultado", num_1 - num_2)
#     case "*":
#         print("resultado", num_1 * num_2)
#     case "/":
#         if num_2 !=0:
#             print("Resultado", num_1 / num_2)
#         else:
#             print("Resultado no valido")
#     case _:
#         print("Resultado no valido")

num_1 = float(input("Dame tu primer numero: "))
num_2 = float(input("Dame tu segundo numero: "))
operador = input("Que operacion quieres hacer? (+,-,*,/): ")

if operador == "+":
    print("Resultado", num_1 + num_2)
elif operador == "-":
    print("Resulado", num_1 - num_2)
elif operador == "*":
    print("Resultado", num_1 * num_2)
elif operador == "/":
    if num_2 != 0:
        print("Resltado", num_1 / num_2)
    else:
        print("Er9r dividiendo por cero")
else:
    print("Operaciones no valida ")