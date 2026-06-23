import csv
from pathlib import Path


def read_employees(file_path):
    employees = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if not row:
                continue

            name = row[0].strip()
            hours = float(row[1].strip())
            rate = float(row[2].strip())
            employees.append((name, hours, rate))

    return employees


def main():
    tax_rate = 0.20
    input_file = Path(__file__).with_name("input.data")
    employees = read_employees(input_file)

    print("Name, Gross-pay, Taxes, Net-pay")

    for name, hours, rate in employees:
        gross_pay = hours * rate
        taxes = gross_pay * tax_rate
        net_pay = gross_pay - taxes

        print(f"{name}, {gross_pay:.2f}, {taxes:.2f}, {net_pay:.2f}")


if __name__ == "__main__":
    main()