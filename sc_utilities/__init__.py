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

__all__ = {
    "ensure_dir",
    "log_init",
    "log_wrapper",
    "Singleton",
    "calculate_column_index",
    "calculate_column_name_from_index",
    "SCException",
    "Config",
    "chain_get",
}

from .config_utils import Config, chain_get
from .file_utils import ensure_dir
from .log_utils import log_init, log_wrapper
from .singleton import Singleton
from .excel_utils import calculate_column_index, calculate_column_name_from_index
from .exceptions import *

__version__ = "0.0.15"
