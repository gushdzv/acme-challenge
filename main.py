from pay_calculator import PayCalculator

rates = {
    "MO": { "00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20 },
    "TU": { "00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20 },
    "WE": { "00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20 },
    "TH": { "00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20 },
    "FR": { "00:01-09:00": 25, "09:01-18:00": 15, "18:01-00:00": 20 },
    "SA": { "00:01-09:00": 30, "09:01-18:00": 20, "18:01-00:00": 25 },
    "SU": { "00:01-09:00": 30, "09:01-18:00": 20, "18:01-00:00": 25 },
}


def main():
    pay_calculator = PayCalculator(rates)
    try:
        with open("employee_schedule.txt", "r") as f:
            data = f.readlines()
        for line in data:
            name, schedule = line.strip().split("=")
            name, total_pay = pay_calculator.calculate_pay(name, schedule)
            print(f"The amount to pay {name} is: {total_pay} USD")
    except Exception as err:
        print(f"Unexpected Error {err=}")


if __name__ == "__main__":
    main()

