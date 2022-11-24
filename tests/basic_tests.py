import unittest
from tests.csv_test import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    # def test_read(self):
    #     printer = CSVPrinter("tests/test.csv")
    #     l = printer.read()
    #     self.assertEqual(3, len(l))

    def test_read1(self):
        printer = CSVPrinter("tests/test.csv")
        line = printer.read()
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("tests/test.csv")
        line = printer.read()
        self.assertEqual("value2B", line[1][1])

    def test_read3(self):
        try:
            printer = CSVPrinter("tests/test.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileExistsError as e:
            print(e)


a = TestCSVPrinter()
a.test_read1()
a.test_read2()
a.test_read3()

