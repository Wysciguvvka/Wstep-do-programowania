from __future__ import annotations
import re

"""
W tym pliku znajdziesz obsługę menu.
Aby utworzyć własny wpis w menu musisz:
1. Stworzyć nową klasę dziedziczącą po MenuCommand.
   * funkcja description() powinna zwracać napis, który zostanie wyświetlony użytkownikowi
   * funkcja execute() powinna zawierać kod, który zostanie wykonany w przypadku wywołania danej opcji w menu
2. Za pomocą funkcji add_command() dodać utworzony obiekt stworzonej przez siebie klasy do menu.
3. Polecenia menu wskazane jest przechowywać na liście np. _commands
"""


class MenuCommand:
    def description(self):
        """Zwróć nazwę z pozycji menu"""
        raise NotImplementedError

    def execute(self):
        """Wykonanie kodu dla danej pozycji menu"""
        raise NotImplementedError


class ExitCommand(MenuCommand):
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self.menu.stop()


class NewEvent(MenuCommand):
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def description(self) -> str:
        return "New event"

    def execute(self) -> None:
        title = input('Title: ')
        if not re.match(r'^[a-zA-Z0-9 ,.-]+$', title):
            print('Invalid input')
            return
        date = input('Date: ')
        if not re.match(r'^(\d{1,2}).(\d{1,2}).(\d{4})$', date):
            print('Invalid input')
            return
        time = input('Time: ')
        if not re.match(r'^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', time):
            print('Invalid input')
            return
        self.menu.calendar.append(
            {'Title': title,
             'Date': date,
             'Time': time, }
        )


class ListCalendar(MenuCommand):
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def description(self) -> str:
        return "List calendar"

    def execute(self) -> None:
        from calendar import list_calendar, ListingStrategy
        strategy = ListingStrategy()
        list_calendar(self.menu.calendar, strategy)


class ExportCalendar(MenuCommand):
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def description(self) -> str:
        return "Export calendar to iCalendar"

    def execute(self) -> None:
        _events = []
        for event in self.menu.calendar:
            _event = event.copy()
            _date = _event['Date'].split('.')
            _time = _event['Time'].replace(':', '')
            _format = f'{_date[2]}{_date[1]}{_date[0]}T{_time}00'
            _event_txt = f'BEGIN:VEVENT\n' \
                         f'DTSTART:{_format}\n' \
                         f'DTEND:{_format}\n' \
                         f'SUMMARY:{_event["Title"]}\n' \
                         f'END:VEVENT\n'
            _events.append(_event_txt)
        events = ''.join(_events)
        _text = f'BEGIN:VCALENDAR\n' \
                f'VERSION:2.0\n' \
                f'BEGIN:VTIMEZONE\n' \
                f'TZID:Europe/Warsaw\n' \
                f'X-LIC-LOCATION:Europe/Warsaw\n' \
                f'END:VTIMEZONE\n' \
                f'{events or ""}' \
                f'END:VCALENDAR'
        print(_text)
        with open('calendar.ics', 'w+', encoding='utf8') as _ics:
            _ics.write(_text)


class Menu:
    def __init__(self) -> None:
        self._commands = []
        self._stop = False
        self.calendar = []

    def add_command(self, cmd: MenuCommand) -> None:
        self._commands.append(cmd)

    def run(self) -> None:
        self._display_menu()
        self._execute_selected_command()
        self.stop()

    def stop(self) -> None:
        self._stop = True

    def _display_menu(self) -> None:
        for cmd in self._commands:
            print(f'{self._commands.index(cmd) + 1}. {cmd.description()}')

    def _execute_selected_command(self) -> None:
        while not self._stop:
            try:
                cmd_num = int(input('Select menu item (1-4): '))
                cmd = self._commands[cmd_num - 1]
                cmd.execute()
            except (IndexError, ValueError):
                print('Invalid command')
            except EOFError:
                pass
