# Marc Talabán 27-7-22
import re


def arithmetic_arranger(operaciones, solve=False):
    # Miramos que no tenga más de X operaciones
    if len(operaciones) > 5:
        return "Error: Too many problems."

    # Inicializamos las lineas del String final
    resTop = ""
    resBottom = ""
    resLines = ""
    resSumx = ""

    for problema in operaciones:

        # Miramos que solo se pueda sumar/restar y solo contener números
        if re.search("[^\s0-9.+-]", problema):
            if re.search("[/]", problema) or re.search("[*]", problema):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        # Cogemos números y que no puedan ser más grandes de 4 digitos
        primerNumero = problema.split(" ")[0]
        operador = problema.split(" ")[1]
        segundoNumero = problema.split(" ")[2]

        if len(primerNumero) >= 5 or len(segundoNumero) >= 5:
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        if operador == '+':
            sum = str(int(primerNumero) + int(segundoNumero))
        elif operador == '-':
            sum = str(int(primerNumero) - int(segundoNumero))

        # Hacemos el Output
        # Miramos la longitud máxima, le sumamos dos (el espacio y el tipo de operación)
        lengthMax = max(len(primerNumero), len(segundoNumero)) + 2
        primeraLinea = str(primerNumero).rjust(lengthMax)
        segundaLinea = operador + str(segundoNumero).rjust(lengthMax - 1)
        separador = ""
        for s in range(lengthMax):
            separador += "-"
        resultado = str(sum).rjust(lengthMax)

        if problema != operaciones[
            -1]:  # Sumamos espacios para diferenciar operaciones, si es la última no es necesario
            resTop += primeraLinea + '    '
            resBottom += segundaLinea + '    '
            resLines += separador + '    '
            resSumx += resultado + '    '
        else:
            resTop += primeraLinea
            resBottom += segundaLinea
            resLines += separador
            resSumx += resultado

        if solve:
            stringFinal = resTop + "\n" + resBottom + "\n" + resLines + "\n" + resSumx
        else:
            stringFinal = resTop + "\n" + resBottom + "\n" + resLines

    return stringFinal
