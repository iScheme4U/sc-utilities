#  The MIT License (MIT)
#
#  Copyright (c) 2025. Scott Lau
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

import yaml

from excel_utils import calculate_column_index


def chain_get(src: dict, path: str, default=None):
    keys = path.split(".")
    value = src
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
        else:
            return default
    return value if value is not None else default


class Config:
    ENCODING = "utf-8"
    DEFAULT_CONFIG_PATH = "production.yml"

    def __init__(self, path=DEFAULT_CONFIG_PATH):
        self._config_path = path
        self._config: dict = dict()
        with open(self._config_path, "r", encoding=Config.ENCODING) as f:
            self._config.update(yaml.load(f, Loader=yaml.FullLoader))

    def get(self, path: str, default=None):
        return chain_get(self._config, path, default)

    def get_column_index(self, key: str) -> int:
        """
        从配置计算列索引
        """
        config = self._config.get(key)
        return calculate_column_index(config)

    def save(self):
        with open(self._config_path, "w", encoding=Config.ENCODING) as f:
            yaml.dump(self._config, f, allow_unicode=True, sort_keys=False)

    def __repr__(self):
        return str(self._config)
