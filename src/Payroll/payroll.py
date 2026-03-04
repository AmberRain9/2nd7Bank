def main():
    tax_rate = 0.20

    employees = [
        ("John Doe", 40, 15.50),
        ("Jane Smith", 35, 18.25),
        ("Bob Johnson", 45, 12.75),
        ("Alice Williams", 38, 16.00),
        ("Charlie Brown", 42, 14.50),
        ("Diana Prince", 37, 19.75),
        ("Edward Norton", 40, 13.25),
        ("Fiona Green", 33, 17.50),
        ("George Harris", 44, 15.75),
        ("Helen Clark", 39, 16.50),
        ("Ian Mitchell", 41, 14.00),
        ("Julia Roberts", 36, 18.50),
        ("Kevin Lee", 43, 13.65),
        ("Linda Davis", 38, 17.25),
        ("Michael Scott", 40, 15.25),
        ("Nancy White", 35, 19.00),
        ("Oliver King", 42, 14.75),
        ("Patricia Moore", 37, 16.75),
        ("Quinn Taylor", 39, 15.00),
        ("Rachel Green", 34, 18.75)
    ]

    print("Name, Gross-pay, Taxes, Net-pay")

    for name, hours, rate in employees:
        gross_pay = hours * rate
        taxes = gross_pay * tax_rate
        net_pay = gross_pay - taxes

        print(f"{name}, {gross_pay:.2f}, {taxes:.2f}, {net_pay:.2f}")


if __name__ == "__main__":
    main()