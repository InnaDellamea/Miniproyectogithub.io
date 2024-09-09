num_uno = int(input("Ingrese el primer número: "))
num_dos = int(input("Ingrese el segundo número: "))
num_tres = int(input("Ingrese el tercer número: "))

if num_uno == num_dos == num_tres:
    print(f"Los tres números son iguales: {num_uno}")
else: 
    if num_uno > num_dos:
        temp = num_uno
        num_uno = num_dos
        num_dos = temp
    if num_uno > num_tres:
        temp = num_uno
        num_uno = num_tres
        num_tres = temp
    if num_dos > num_tres:
        temp = num_dos
        num_dos = num_tres
        num_tres = temp

    print(f"Los números ordenados de menor a mayor son: {num_uno}, {num_dos} y {num_tres}")
    