import sys

def emissions_per_seat(avg_co2_emissions: float, avg_total_seats: float):
    # Custom logic to calculate average CO2 emissions per seat
    return avg_co2_emissions / avg_total_seats if avg_total_seats != 0 else 0