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

# Ejecutar la sentencia a = 'cadena'
a = 'cadena'

# Crear un diccionario con las variables y sus valores
variables = {'a': a}

# Dibujar el diagrama y mostrarlo
image_filename = draw_memory_diagram(variables)
Image(filename=image_filename)
