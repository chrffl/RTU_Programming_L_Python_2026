"""
Lab 2.3 – Operator Frequency Counter
------------------------------------
Practice strings and dictionaries by counting characters.

Examples (these are also used to check your work):
>>> count_operators("3 + 5 * (2 - 1) + 7 / 2")
{'+': 2, '-': 1, '*': 1, '/': 1, '(': 1, ')': 1}
>>> count_operators("2 ** 3 - -4")
{'+': 0, '-': 2, '*': 2, '/': 0, '(': 0, ')': 0}
>>> count_operators("")
{'+': 0, '-': 0, '*': 0, '/': 0, '(': 0, ')': 0}
"""

OPERATORS = ["+", "-", "*", "/", "(", ")"]


def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    counts = {op: 0 for op in OPERATORS}
    for char in expression:
        if char in counts:
            counts[char] += 1
    return counts


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    expression = input("Enter an arithmetic expression: ")
    result = count_operators(expression)
    print(f"Operator counts: {result}")
