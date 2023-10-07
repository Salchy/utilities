# Script util para uso personal, donde me ayuda a contabilizar las asistencias y tickets que trabajé a lo largo de un mes.
# Originalmente cargo todo en un Excel, lo que hago acá, es sólo copiar la tipifacion del ticket, y corriendo el script me
# da la cantidad de tickets realizados, separados, por categoría, y dentro de esa categoría, los tipos de tickets dentro de esa categoría.
# Es algo muy util ya que me ayuda a realizar el informe mensual que piden en mi trabajo.

# Es una lista

# Ejemplo:
titlesTickets = [
    "Requerimiento/Redes",
    "Asistencia Técnica/Outlook",
    "Asistencia Técnica/Excel",
    "Requerimiento/Outlook"
]

def countsTickets():
    totalTickets = {} # Diccionario
    
    # Obtengo los datos y contabilizo
    for value in titlesTickets:
        splitted = value.split("/")
        ticketType, categoryTicket = splitted[0], splitted[1]
        if (not ticketType in totalTickets):
            totalTickets[ticketType] = {}
            totalTickets[ticketType]["total"] = 0 # Total por categoría
        if (not categoryTicket in totalTickets[ticketType]):
            totalTickets[ticketType][categoryTicket] = 0
        totalTickets[ticketType][categoryTicket] += 1
        totalTickets[ticketType]["total"] += 1
        
    # Ahora imprimir y dar formato
    count = 0
    for categories in totalTickets:
        print(f"{categories}: {totalTickets[categories]['total']}")
        print("")
        for tickets in totalTickets[categories]:
            if tickets != "total":
                print(f"{tickets}: {totalTickets[categories][tickets]}")
        count += totalTickets[categories]['total']
        print("-----------")

    print("")
    print(f"Total de tickets trabajados en el mes: {count}")
    print("")
    print("")
    print("")
    
countsTickets()