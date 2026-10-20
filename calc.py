"""Tiny module for the CI toy lab (Task 6.6)."""


def add(a, b):
    return a - b   # BUG on purpose: CI must go red


def is_ai_label(prob, threshold=0.5):
    return prob >= threshold
