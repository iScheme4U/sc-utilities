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
import re

ASCII_A = ord('A')
ASCII_Z = ord('Z')
# 代表是26进制
ORDINAL_VALUE = ASCII_Z - ASCII_A + 1

def calculate_column_index(column_letter: str) -> int:
    if column_letter is None or type(column_letter) != str or len(column_letter) == 0:
        raise ValueError(f"parameter {column_letter} is invalid")

    if re.match(r'^[a-zA-Z]+$', column_letter) is None:
        raise ValueError(f"parameter {column_letter} contains invalid characters")
    # 转换为大写
    column_name = column_letter.upper()
    column_letter_stack = list()
    # 将字母序列转换为栈式结构
    for letter in column_name:
        column_letter_stack.append(ord(letter) - ASCII_A + 1)

    # 最后结果
    result = 0
    # 当前是第几位，1是个位、2是十位、3是百位，依此类推
    level = 1
    while len(column_letter_stack) > 0:
        ascii_value = column_letter_stack.pop()
        result += ascii_value * level
        # 每进一次，乘以进制数字
        level = level * ORDINAL_VALUE
    return result - 1


def calculate_column_name_from_index(index: int) -> str:
    if index is None or type(index) != int or index < 0:
        raise ValueError(f"parameter {index} is invalid")
    value = index + 1
    result = list()
    div, mod = divmod(value, ORDINAL_VALUE)
    if mod == 0:
        div -= 1
        mod += ORDINAL_VALUE
    result.append(chr(ASCII_A + mod - 1))
    while div != 0:
        value = div
        div, mod = divmod(value, ORDINAL_VALUE)
        if mod == 0:
            div -= 1
            mod += ORDINAL_VALUE
        result.append(chr(ASCII_A + mod - 1))
    result.reverse()
    return "".join(result)
