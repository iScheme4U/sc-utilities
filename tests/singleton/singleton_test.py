#  The MIT License (MIT)
#
#  Copyright (c) 2025  Scott Lau
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

import logging
import unittest

from sc_utilities import log_init, log_wrapper
from sc_utilities.singleton import Singleton


class Test(metaclass=Singleton):
    def __init__(self):
        logging.getLogger(__name__).info("Test __init__ called")


class SingletonTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        logger = log_init()
        logging.getLogger(__name__).info("logger %s", logger)

    @log_wrapper
    def test_singleton(self):
        test_a = Test()
        test_b = Test()
        logging.getLogger(__name__).info("test_a %s", test_a)
        logging.getLogger(__name__).info("test_b %s", test_b)
        self.assertEqual(test_a, test_b)


if __name__ == '__main__':
    unittest.main()
