def _validate_inputs(guest_age: int, stay_duration: int) -> None:
    """Validate age and duration inputs."""
    if guest_age < 0:
        raise ValueError("Invalid age: age cannot be negative.")
    if stay_duration < 1 or stay_duration > 14:
        raise ValueError("Invalid duration: stay must be between 1 and 14 nights.")

def calculate_booking_fee(
    guest_age: int,
    room_type: str,
    booking_day: str,
    stay_duration: int,
) -> float:
    """
    Compute hotel booking price based on business rules.
    - Children under 5 stay free
    - Standard room: $100/night
    - Family room: $150/night
    - Weekend booking: +20%
    - Holiday season: +40%
    - Booking duration: 1-14 nights
    """
   
    _validate_inputs(guest_age, stay_duration)

  
    if guest_age < 5:
        return 0.0


    room_type_lower = room_type.lower()
    base_rate = 100.0 if room_type_lower == "standard" else 150.0
    subtotal = base_rate * stay_duration


    booking_day_lower = booking_day.lower()
    if booking_day_lower == "weekend":
        subtotal *= 1.20
    elif booking_day_lower == "holiday":
        subtotal *= 1.40
        
    return round(subtotal, 2)