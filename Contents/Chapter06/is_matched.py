# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:21:46 2017

@author: Jihoon_Kim
"""

import ArrayStack

#  An Algorithm for Matching Delimiters


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()

    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find("<")

    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1 : k]
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return S.is_empty()
