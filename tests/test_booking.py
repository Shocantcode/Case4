import pytest

from src.booking import hotel_booking_price


# def test_TC01():
#     assert hotel_booking_price(30, "Standard", "Weekday", 3) == 300.0


# def test_TC02():
#     assert hotel_booking_price(4, "Standard", "Weekday", 2) == 0.0

# def test_TC03():
#     assert hotel_booking_price(5, "Standard", "Weekday", 2) == 200.0


# def test_TC04():
#     assert hotel_booking_price(35, "Family", "Weekend", 5) == 900.0




# Nicholas - TC09 — Invalid Duration (di atas 14 malam)
def test_invalid_duration_above_max():
    with pytest.raises(ValueError):
        hotel_booking_price(
            guest_age=25,
            room_type="standard",
            booking_day="weekday",
            stay_duration=15
        )

# Nicholas - TC10 — Invalid Age (usia negatif)
def test_invalid_age_negative():
    with pytest.raises(ValueError):
        hotel_booking_price(
            guest_age=-1,
            room_type="standard",
            booking_day="weekday",
            stay_duration=3
        )