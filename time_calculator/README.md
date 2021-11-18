# Time Calculator

Pseudo código:

--- 

Variáveis

- Início
- Período
- Contador = 0

---

Enquanto contador < periodo:

Inicio++

Se inicio >= 12:
inicio = 0
troca_turno(inicio.split()[1])

---

troca_turno(inicio(am/pm)):

se turno 'am':</br>
    turno = pm </br>
se turno 'pm':</br>
    turno = am </br>

--- 

Se dia da semana:
    se inicio troca_turno pm > am:
        return dia_seguinte

---

dias = Período/24h

Domingo: 0
Segunda: 1
Terça: 2
Quarta: 3
Quinta: 4
Sexta: 5
Sábado: 6

contador = 0

Enquando contador < dias: </br>
    para dia_semana: numero: </br>
        se chave: valor == dia_semana: numero: </br>
            numero ++ </br>
        se numero > 6 </br>
            numero = 0 </br>
    return dia_semana: numero(final) </br>

retorna a união dos valores gerados pelas funções. </br>