#  The MIT License (MIT)
#
#  Copyright (c) 2022. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import unittest
from sc_utilities import calculate_column_index, calculate_column_name_from_index


class ExcelTestCase(unittest.TestCase):
    def test_calculator_column_index(self):
        self.assertEqual(0, calculate_column_index('A'))
        self.assertEqual(25, calculate_column_index('Z'))
        self.assertEqual(26, calculate_column_index('AA'))
        self.assertEqual(28, calculate_column_index('AC'))
        self.assertEqual(701, calculate_column_index('ZZ'))
        self.assertEqual(702, calculate_column_index('AAA'))
        self.assertEqual(730, calculate_column_index('ABC'))

    def test_calculator_column_name(self):
        self.assertEqual("A", calculate_column_name_from_index(0))
        self.assertEqual('Z', calculate_column_name_from_index(25))
        self.assertEqual('AA', calculate_column_name_from_index(26))
        self.assertEqual('AC', calculate_column_name_from_index(28))
        self.assertEqual('ZZ', calculate_column_name_from_index(701))
        self.assertEqual('AAA', calculate_column_name_from_index(702))
        self.assertEqual('ABC', calculate_column_name_from_index(730))


if __name__ == '__main__':
    unittest.main()
