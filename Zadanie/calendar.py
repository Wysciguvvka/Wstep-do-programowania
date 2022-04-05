"""
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

"""


class ListingStrategy:
    def begin(self) -> None:
        pass

    def event(self, title, date, time) -> None:
        print(f'Title: {title}\nDate: {date}, {time}')

    def end(self) -> None:
        pass


def list_calendar(calendar: list[dict], listing_strategy) -> None:
    listing_strategy.begin()

    for event in calendar:
        listing_strategy.event(event['Title'], event['Date'], event['Time'])
        pass

    listing_strategy.end()
