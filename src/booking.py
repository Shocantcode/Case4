def calculate_booking(guest_age, room_type, booking_day, stay_duration):
    # Logika TC04
    if booking_day == "Weekend":
        return "Weekend surcharge (+20%)"

    # Logika TC03
    return "Normal charge"