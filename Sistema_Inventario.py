
# Nombres: Bryan Cevallos y Fareed Guzmán
def menu_principal():
    print("\n Sistema de Inventarios para Mascotas ")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Salir")
    return input("Seleccione una opción: ")

def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    inventario[nombre] = {'Cantidad': cantidad, 'Precio': precio}
    print(f"Producto '{nombre}' agregado con éxito.")

def editar_producto(inventario):
    nombre = input("Nombre del producto a editar: ")
    if nombre in inventario:
        cantidad = int(input(f"Nueva cantidad para '{nombre}': "))
        precio = float(input(f"Nuevo precio para '{nombre}': "))
        inventario[nombre] = {'Cantidad': cantidad, 'Precio': precio}
        print(f"Producto '{nombre}' actualizado con éxito.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado con éxito.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

def listar_productos(inventario):
    if inventario:
        print("\nInventario actual:")
        for nombre, detalles in inventario.items():
            print(f"- {nombre}: {detalles['Cantidad']} unidades, ${detalles['Precio']:.2f}")
    else:
        print("El inventario está vacío.")

def sistema_inventarios():
    inventario = {}
    while True:
        opcion = menu_principal()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            editar_producto(inventario)
        elif opcion == '3':
            eliminar_producto(inventario)
        elif opcion == '4':
            listar_productos(inventario)
        elif opcion == '5':
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    sistema_inventarios()

