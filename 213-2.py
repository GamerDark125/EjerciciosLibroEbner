import pygraphviz as pgv
from IPython.display import Image

def draw_memory_diagram(variables):
    graph = pgv.AGraph(directed=True)

    for var, value in variables.items():
        graph.add_node(var, label=f"{var}\n{value}")

    graph.layout(prog='dot')
    filename = "memory_diagram.png"
    graph.draw(filename)
    return filename

# Ejecutar la sentencia a = 'cadena' (asumiendo que ya se ejecutó previamente)
a = 'cadena'

# Ejecutar la sentencia b = a[2:3]
b = a[2:3]

# Crear un diccionario con las variables y sus valores
variables = {'a': a, 'b': b}

# Dibujar el diagrama y mostrarlo
image_filename = draw_memory_diagram(variables)
Image(filename=image_filename)
