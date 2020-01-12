import unittest
from context import hotel_system
from hotel_system.file_handler import parse_line, parse_date


class TestFileHandlerMethods(unittest.TestCase):
    def test_parse_line_one_date(self):
        line = 'Regular: 16Mar2009(mon)'
        parsed_line = parse_line(line)

        self.assertEqual(len(parsed_line), 2)
        self.assertEqual(parsed_line[0], 'Regular')
        self.assertEqual(parsed_line[1], ' 16Mar2009(mon)')

    def test_parse_line_multiple_dates(self):
        line = 'Regular: 16Mar2009(mon), 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'
        parsed_line = parse_line(line)

        self.assertEqual(len(parsed_line), 2)
        self.assertEqual(parsed_line[0], 'Regular')
        self.assertEqual(parsed_line[1], ' 16Mar2009(mon), 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')

    def test_parse_date(self):
        date = '16Mar2009(mon)'
        parsed_date = parse_date(date)

        self.assertEqual(parsed_date.day, 16)
        self.assertEqual(parsed_date.month, 3)
        self.assertEqual(parsed_date.year, 2009)


if __name__ == "__main__":
    unittest.main()
