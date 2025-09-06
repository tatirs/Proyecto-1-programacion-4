def obtener_datos_usuario():
    departamento = input("Ingrese el departamento: ").strip().upper()
    municipio = input("Ingrese el municipio: ").strip().upper()
    cultivo = input("Ingrese el cultivo: ").strip().lower().capitalize()

    try:
        limit = int(input("Ingrese el número de registros a consultar: "))
    except ValueError:
        print("El límite debe ser un número entero.")
        return None

    return departamento, municipio, cultivo, limit
