import pulp

def planificar_produccion(productos, recursos):
    # Crear un problema de programación lineal
    prob = pulp.LpProblem("PlanificacionProduccion", pulp.LpMaximize)

    # Variables de decisión (cantidad de cada producto a producir)
    cantidad_productos = pulp.LpVariable.dicts("Cantidad", productos, lowBound=0, cat='Integer')

    # Función objetivo (maximizar la ganancia total)
    prob += pulp.lpSum([productos[producto]["ganancia"] * cantidad_productos[producto] for producto in productos])

    # Restricciones de recursos
    for recurso in recursos:
        prob += pulp.lpSum([productos[producto]["requerimientos"][recurso] * cantidad_productos[producto] for producto in productos]) <= recursos[recurso]

    # Resolver el problema
    prob.solve()

    # Mostrar resultados
    print("\nPlan de Producción:")
    for producto in productos:
        print(f"{producto}: {pulp.value(cantidad_productos[producto])} unidades")

if __name__ == "__main__":
    # Definir productos y sus características
    productos = {
        "ProductoA": {"ganancia": 10, "requerimientos": {"recurso1": 2, "recurso2": 1}},
        "ProductoB": {"ganancia": 8, "requerimientos": {"recurso1": 1, "recurso2": 3}},
    }

    # Definir recursos disponibles
    recursos_disponibles = {"recurso1": 20, "recurso2": 15}

    # Ejecutar la planificación de producción
    planificar_produccion(productos, recursos_disponibles)
