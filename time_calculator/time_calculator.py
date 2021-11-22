def add_time(start, duration):

    contador = 0
    while contador < duration:
        start += 1

        if start.split(":")[1] >= 12:
            start = 0
            turno = start.split(" ")[1]
            troca_turno(turno)

    return new_time


def troca_turno(turno):
    if "AM" in turno:
        return "PM"
    elif "PM" in turno:
        return "AM"


def tem_optional():
    return len(list(add_time)) > 2


def trocou_turno(turno):
    return bool(troca_turno(turno))


def dia_seguinte(start):
    if "PM" in start and trocou_turno:
        return "dia seguinte"


def semana(duration):
    dias = duration / 24

    dias_semana = []
    domingo = {"domingo", 0}
    segunda = {"segunda", 1}
    terca = {"terça", 2}
    quarta = {"quarta", 3}
    quinta = {"quinta", 4}
    sexta = {"sexta", 5}
    sabado = {"sabado", 6}
