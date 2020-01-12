import re
from datetime import datetime


def read_file(file):
    """Read the input file passed to the problem.

    Parameters:
    file (string): file name to be read

    Returns:
    List: A list with two elements: the customer category and
    a list with dates in the format:
    ['Rewards', [datetime(2019, 11, 01), datetime(2019, 11, 02)]]
    """

    data = []

    with open(file, 'r') as f:
        for line in f.readlines():
            customer_category, dates = parse_line(line)
            dates = dates.split(',')
            parsed_dates = []

            for date in dates:
                parsed_dates.append(parse_date(date))

            data.append(customer_category)
            data.append(parsed_dates)

    return data


def parse_line(line):
    """Returns a string splitted by ':' character

    Parameters:
    line (string): The string to be splitted in the format:
    'Something: to be splitted in two'

    Returns:
    List: A list with the string splitted in the format
    ['Something', ' to be splitted in two']
    """

    return line.split(':')


def parse_date(date):
    """Read a date in the format 16Mar2009(mon) and return a datetime
    date

    Parameters:
    date (string): A string with the date in the format '16Mar2009(mon)'

    Returns:
    datetime: A date in the format of a datetime type
    """

    date = re.split('([0-9]+)', date)  # '' '21' 'Mar' '2019' '(sat)'

    day = date[1]
    month = date[2]
    year = date[3]

    datetime_object = datetime.strptime('{0} {1} {2}'.format(month, day, year), '%b %d %Y')
    return datetime_object
