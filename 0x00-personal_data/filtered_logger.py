#!/usr/bin/env python3
"""Module that defines a function: filter_datum for Task_0"""
import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Returns a log message

    Args:
        fields (list): all fields to obfuscate
        redaction (str): a string representing by what the field will
                         be obfuscated
        message (str): log line
        separator (str): character separating all fields in the log line
    Returns:
        Log message as string
    """
    final_message: str = message
    for field in fields:
        pattern: str = r"({}=)([^{}]+)".format(field, separator)
        final_message = re.sub(pattern, r"\1" + redaction, final_message)

    return final_message
