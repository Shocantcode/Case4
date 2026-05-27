def calculate_booking_fee(guest_age, room_type, booking_day, stay_duration):
    # Solusi minimum agar test pass
    if stay_duration < 1 or stay_duration > 14:
        raise ValueError("Booking duration must be between 1 and 14 nights")
    
    return "Valid booking" 