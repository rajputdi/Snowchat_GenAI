def seat_occupancy(total_seats: int, occupied_seats: int):
    seat_occupancy_percentage = (occupied_seats / total_seats) * 100 if total_seats != 0 else 0
    return seat_occupancy_percentage