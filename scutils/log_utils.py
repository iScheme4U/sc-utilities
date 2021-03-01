#  The MIT License (MIT)
#
#  Copyright (c) 2021. Scott Lau
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
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from .file_utils import ensure_dir

# default log level: INFO
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
# default log file path: /tmp/logs/sc-sys.log
LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME', '/tmp/logs/sc-sys.log')
# default log format
LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s [%(levelname)s][%(name)s]: %(message)s')


def log_init():
    """Initialize logging configurations

    A new log file will be created everyday, log files will be saved for 32 days
    """
    ensure_dir(LOG_FILE_NAME)
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    file_handler = TimedRotatingFileHandler(LOG_FILE_NAME, when='D', interval=1, backupCount=32)
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
