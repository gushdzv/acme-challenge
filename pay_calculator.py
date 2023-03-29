from datetime import datetime


class PayCalculator:
    def __init__(self, rates):
        self.rates = rates

    # Method to calculate_pay that takes in a name and a schedule string and returns the name and total pay
    def calculate_pay(self, name, schedule):
        shifts = schedule.split(",")
        total_pay = 0
        for shift in shifts:
            day, time_range = shift[:2], shift[2:]
            start_time, end_time = self.parse_time_range(time_range)
            shift_hours = self.calculate_shift_hours(start_time, end_time)
            rate = self.get_rate(day, start_time, end_time)
            total_pay += shift_hours * rate
        return name, total_pay

    # Takes in a time range string and returns the start and end times as datetime.time objects
    def parse_time_range(self, time_range):
        start_time_str, end_time_str = time_range.split("-")
        start_time = datetime.strptime(start_time_str.strip(), "%H:%M").time()
        end_time = datetime.strptime(end_time_str.strip(), "%H:%M").time()
        return start_time, end_time

    # Takes in a start time and an end time and returns the number of hours worked in the shift
    def calculate_shift_hours(self, start_time, end_time):
        hours = end_time.hour - start_time.hour
        minutes = end_time.minute - start_time.minute
        shift_hours = hours + minutes / 60
        return shift_hours

    # Checks the time window for each shift to fix the rate price
    def get_rate(self, day, start_time, end_time):
        rate = None
        for time_window, time_rate in self.rates[day].items():
            window_start, window_end = self.parse_time_range(time_window)
            if window_start <= start_time <= window_end and window_start <= end_time <= window_end:
                rate = time_rate
                break
            else:
                rate = self.rates[day]["18:01-00:00"]
        return rate
