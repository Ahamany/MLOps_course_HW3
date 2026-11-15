"""Вычислить количество, среднее, минимум и максимум значений из CSV."""

import csv
import json
from pathlib import Path


def main() -> None:
    with Path("data/numbers.csv").open(encoding="utf-8", newline="") as stream:
        values = [int(row["value"]) for row in csv.DictReader(stream)]
    metrics = {
        "count": len(values),
        "mean": round(sum(values) / len(values), 2),
        "min": min(values),
        "max": max(values),
    }
    path = Path("output/metrics.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(metrics)


if __name__ == "__main__":
    main()
