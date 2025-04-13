# Sistema de Rutas Transmilenio
# Creado: 11 de abril de 2025

class SistemaTransmilenio:
    def __init__(self):
        # Diccionario de rutas: clave = código de ruta, valor = lista de estaciones
        self.rutas = {
            'B74': ['Portal El Dorado', 'Av. Rojas', 'Salitre El Greco', 'CAN', 'Quinta Paredes', 'CAD', 'Paloquemao', 'San Façon', 'Av. Jiménez'],
            'H20': ['Portal Norte', 'Toberín', 'Cardio Infantil', 'Mazurén', 'Calle 146', 'Calle 142', 'Alcalá', 'Prado', 'Calle 127', 'Pepe Sierra'],
            'K43': ['Portal Suba', 'Av. Boyacá', 'Niza', 'Shaio', 'Colina Campestre', 'Calle 127', 'Calle 106', 'Calle 100', 'Virrey', 'Calle 85'],
            'F23': ['Portal 20 de Julio', 'Country Sur', 'Olaya', 'Restrepo', 'Fucha', 'Ciudad Jardín', 'Policarpa', 'Av. Jiménez', 'Museo Nacional'],
            'G12': ['Portal Américas', 'Biblioteca Tintal', 'Patio Bonito', 'Banderas', 'Mandalay', 'Mundo Aventura', 'Marsella', 'Pradera', 'Communeros']
        }
        
        # Troncales del sistema
        self.troncales = {
            'Troncal Caracas': ['Portal Usme', 'Portal Tunal', 'Calle 40 Sur', 'Av. Jiménez', 'Héroes'],
            'Troncal Calle 80': ['Portal 80', 'Granja', 'Polo', 'Escuela Militar', 'Virrey'],
            'Troncal NQS': ['Portal Sur', 'Soacha', 'Ricaurte', 'CAD', 'Av. Chile'],
            'Troncal Américas': ['Portal Américas', 'Banderas', 'Kennedy', 'CAD'],
            'Troncal Suba': ['Portal Suba', 'Niza', 'Shaio', 'Pepe Sierra', 'Héroes'],
            'Troncal Eldorado': ['Portal Eldorado', 'Aeropuerto', 'CAD', 'Centro Memoria']
        }
    
    def consultar_ruta(self, codigo_ruta):
        """Consulta las estaciones de una ruta específica."""
        if codigo_ruta in self.rutas:
            return f"Ruta {codigo_ruta}: {' → '.join(self.rutas[codigo_ruta])}"
        else:
            return f"La ruta {codigo_ruta} no existe en el sistema."
    
    def buscar_rutas_por_estacion(self, estacion):
        """Busca todas las rutas que pasan por una estación específica."""
        rutas_encontradas = []
        
        for codigo, estaciones in self.rutas.items():
            if estacion in estaciones:
                rutas_encontradas.append(codigo)
        
        if rutas_encontradas:
            return f"Rutas que pasan por {estacion}: {', '.join(rutas_encontradas)}"
        else:
            return f"No se encontraron rutas que pasen por {estacion}."
    
    def consultar_troncal(self, nombre_troncal):
        """Consulta las estaciones principales de una troncal."""
        if nombre_troncal in self.troncales:
            return f"Troncal {nombre_troncal}: {' → '.join(self.troncales[nombre_troncal])}"
        else:
            return f"La troncal {nombre_troncal} no existe en el sistema."
    
    def listar_rutas(self):
        """Lista todas las rutas disponibles."""
        return "Rutas disponibles: " + ", ".join(self.rutas.keys())
    
    def listar_troncales(self):
        """Lista todas las troncales disponibles."""
        return "Troncales disponibles: " + ", ".join(self.troncales.keys())

def menu_principal():
    """Función para mostrar el menú principal del sistema."""
    print("\n===== SISTEMA DE RUTAS TRANSMILENIO =====")
    print("1. Consultar ruta")
    print("2. Buscar rutas por estación")
    print("3. Consultar troncal")
    print("4. Listar todas las rutas")
    print("5. Listar todas las troncales")
    print("0. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Error: Debe ingresar un número.")
        return -1

def main():
    sistema = SistemaTransmilenio()
    
    while True:
        opcion = menu_principal()
        
        if opcion == 0:
            print("Gracias por utilizar el Sistema de Rutas Transmilenio. ¡Hasta pronto!")
            break
            
        elif opcion == 1:
            codigo = input("Ingrese el código de la ruta (ejemplo: B74): ")
            print(sistema.consultar_ruta(codigo))
            
        elif opcion == 2:
            estacion = input("Ingrese el nombre de la estación: ")
            print(sistema.buscar_rutas_por_estacion(estacion))
            
        elif opcion == 3:
            print("Troncales disponibles:", ", ".join(sistema.troncales.keys()))
            troncal = input("Ingrese el nombre de la troncal: ")
            print(sistema.consultar_troncal(troncal))
            
        elif opcion == 4:
            print(sistema.listar_rutas())
            
        elif opcion == 5:
            print(sistema.listar_troncales())
            
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
    