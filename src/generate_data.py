"""Создать 100 случайных целых чисел с фиксированным seed."""

import csv
import random
from pathlib import Path


def main() -> None:
    rng = random.Random(42)
    path = Path("data/numbers.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["value"])
        writer.writerows([rng.randint(0, 100)] for _ in range(100))
    print(f"Создан {path}: 100 чисел, seed=42")


if __name__ == "__main__":
    main()
