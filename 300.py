def si_o_no(pregunta):
    respuestas_afirmativas = {'si', 's', 'Si', 'SI'}
    respuestas_negativas = {'no', 'n', 'No', 'NO'}

    while True:
        respuesta = input(f'{pregunta} (si/no): ').lower()

        if respuesta in respuestas_afirmativas:
            return True
        elif respuesta in respuestas_negativas:
            return False
        else:
            print('Respuesta no válida. Por favor, responda con "si" o "no".')

# Ejemplo de uso
pregunta_usuario = "¿Quieres continuar?"
respuesta_usuario = si_o_no(pregunta_usuario)
print(f'El usuario respondió: {respuesta_usuario}')
