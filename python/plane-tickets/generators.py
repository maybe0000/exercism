"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    # a = []
    # for i in range(number):
    #     a.append(chr(i%4+ord('A')))
    # return a

    for index in range(number):
        yield chr(index%4 + ord('A'))


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    def seat_numbers():
        i = 1
        while True:
            if i == 13:
                i += 1
            yield i
            yield i
            yield i
            yield i
            i += 1
    
    for seat_number, el in zip(seat_numbers(), generate_seat_letters(number)):
        yield f"{seat_number}{el}"
    
    # for i,l in enumerate(generate_seat_letters(number)):
    #     seat_number = i//4+1
    #     if seat_number != 13:
    #         yield f"{seat_number}{l}"

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return dict(zip(passengers, generate_seats(len(passengers))))

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for element in seat_numbers:
        yield f"{element}{flight_id}{'0'*(12 - len(element) - len(flight_id))}"
