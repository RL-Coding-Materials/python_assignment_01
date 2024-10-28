import pytest  # type: ignore
import subprocess

import random


def test_factorization_exec():
    data = (
        (1, ""),
        (2, "2"),
        (3, "3"),
        (4, "2^2"),
        (5, "5"),
        (6, "2*3"),
        (7, "7"),
        (8, "2^3"),
        (9, "3^2"),
        (10, "2*5"),
        (4407, "3*13*113"),
        (13041599400, "2^3*3^4*5^2*805037"),
    )

    for d in data:
        assert (
            subprocess.check_output(["python", "factorization.py", str(d[0])]).decode()
            == f"{d[0]} = {d[1]}\n"
        )
