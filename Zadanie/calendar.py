"""
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

"""


class ListingStrategy:
    def begin(self) -> None:
        pass

    def event(self, title, date, time) -> None:
        pass

    def end(self) -> None:
        pass


class PrintStrategy(ListingStrategy):

    def event(self, title, date, time) -> None:
        print(f'Title: {title}\nDate: {date}, {time}')


class ExportStrategy(ListingStrategy):
    def __init__(self):
        self.text = ''

    def begin(self) -> None:
        self.text = f'BEGIN:VCALENDAR\n' \
                    f'VERSION:2.0\n' \
                    f'BEGIN:VTIMEZONE\n' \
                    f'TZID:Europe/Warsaw\n' \
                    f'X-LIC-LOCATION:Europe/Warsaw\n' \
                    f'END:VTIMEZONE'
        print(f'BEGIN:VCALENDAR\n'
              f'VERSION:2.0\n'
              f'BEGIN:VTIMEZONE\n'
              f'TZID:Europe/Warsaw\n'
              f'X-LIC-LOCATION:Europe/Warsaw\n'
              f'END:VTIMEZONE')

    def event(self, title, date, time) -> None:
        _date = date.split('.')
        _time = time.replace(':', '')
        _format = f'{_date[2]}{_date[1]}{_date[0]}T{_time}00'
        _text = f'BEGIN:VEVENT\n' \
                f'DTSTART:{_format}\n' \
                f'DTEND:{_format}\n' \
                f'SUMMARY:{title}\n' \
                f'END:VEVENT'
        self.text = f'{self.text}\n{_text}'
        print(_text)

    def end(self) -> None:
        self.text = f'{self.text}\nEND:VCALENDAR'
        print(f'END:VCALENDAR')
        with open('calendar.ics', 'w+', encoding='utf8') as _ics:
            _ics.write(self.text)


def list_calendar(calendar: list[dict], listing_strategy) -> None:
    listing_strategy.begin()

    for event in calendar:
        listing_strategy.event(event['Title'], event['Date'], event['Time'])

    listing_strategy.end()
