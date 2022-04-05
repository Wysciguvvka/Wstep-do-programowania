from menu import *


# from calendar import


#
# w tym miejscu możesz napisać kod odpowiedzialny za menu (polecenia)
# i strategie wyświetlania wydarzeń z kalendarza
#

def main():
    # wydarzenia przechowuj w liście
    calendar = []

    # zakładamy, że wydarzenie to słownik z kluczami title, date, time
    # jeśli chcesz przechowywać wydarzenie w innej strukturze danych
    # to pamiętaj o zmianie jej obsługi w funkcji list_calendar
    # event = {
    #    'title': 'Programowanie obiektowe w jezyku PYTHON - Cwiczenia',
    #    'date': '27.03.2022',
    #    'time': '9:00',
    # }
    #
    # dodaj wydarzenie event do kalendarza calendar

    menu = Menu()

    # tutaj możesz dodać kolejne polecenia do menu
    menu.add_command(NewEvent(menu))
    menu.add_command(ListCalendar(menu))
    menu.add_command(ExportCalendar(menu))
    menu.add_command(ExitCommand(menu))
    menu.run()


main()
