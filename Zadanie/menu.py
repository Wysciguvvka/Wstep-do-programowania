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
        from calendar import list_calendar, PrintStrategy
        strategy = PrintStrategy()
        list_calendar(self.menu.calendar, strategy)


class ExportCalendar(MenuCommand):
    def __init__(self, menu: Menu) -> None:
        self.menu = menu

    def description(self) -> str:
        return "Export calendar to iCalendar"

    def execute(self) -> None:
        from calendar import list_calendar, ExportStrategy
        strategy = ExportStrategy()
        calendar = self.menu.calendar
        list_calendar(calendar, strategy)


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
