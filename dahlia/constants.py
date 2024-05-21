from __future__ import annotations

from os import environ
from re import compile

FORMATTERS = {
    "i": 7,
    "j": 2,
    "k": 8,
    "l": 1,
    "m": 9,
    "n": 4,
    "o": 3,
    "p": 5,
    "r": 0,
}

COLORS_3BIT = {
    "0": 30,
    "1": 34,
    "2": 32,
    "3": 36,
    "4": 31,
    "5": 35,
    "6": 33,
    "7": 37,
    "8": 30,
    "9": 34,
    "a": 32,
    "b": 34,
    "c": 31,
    "d": 35,
    "e": 33,
    "f": 37,
}

COLORS_4BIT = {
    **COLORS_3BIT,
    "8": 90,
    "9": 94,
    "a": 92,
    "b": 96,
    "c": 91,
    "d": 95,
    "e": 93,
    "f": 97,
}

COLORS_8BIT = {
    "0": 0,
    "1": 19,
    "2": 34,
    "3": 37,
    "4": 124,
    "5": 127,
    "6": 214,
    "7": 248,
    "8": 240,
    "9": 147,
    "a": 83,
    "b": 87,
    "c": 203,
    "d": 207,
    "e": 227,
    "f": 15,
}

COLORS_24BIT = {
    "0": [0, 0, 0],
    "1": [0, 0, 170],
    "2": [0, 170, 0],
    "3": [0, 170, 170],
    "4": [170, 0, 0],
    "5": [170, 0, 170],
    "6": [255, 170, 0],
    "7": [170, 170, 170],
    "8": [85, 85, 85],
    "9": [85, 85, 255],
    "a": [85, 255, 85],
    "b": [85, 255, 255],
    "c": [255, 85, 85],
    "d": [255, 85, 255],
    "e": [255, 255, 85],
    "f": [255, 255, 255],
}

COLOR_SETS: dict[int, dict[str, int]] = {
    3: COLORS_3BIT,
    4: COLORS_4BIT,
    8: COLORS_8BIT,
}

CODE_REGEXES = [r"(~?)([0-9a-fi-pr])", r"(~?)\[#([0-9a-fA-F]{6})\]"]

ANSI_REGEXES = [
    compile(r"\033\[(\d+)m"),
    compile(r"\033\[(?:3|4)8;5;(\d+)m"),
    compile(r"\033\[(?:3|4)8;2;(\d+);(\d+);(\d+)m"),
]

FORMAT_TEMPLATES = {
    3: "\033[{}m",
    4: "\033[{}m",
    8: "\033[38;5;{}m",
    24: "\033[38;2;{};{};{}m",
}

BG_FORMAT_TEMPLATES = {
    3: "\033[{}m",
    4: "\033[{}m",
    8: "\033[48;5;{}m",
    24: "\033[48;2;{};{};{}m",
}

NO_COLOR = environ.get("NO_COLOR", "").casefold() in ("1", "true")
