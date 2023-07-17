from booking import Booking
import booking_constants
# WIP

with Booking() as bot:
    bot.land_first_page()
    print(f'Exiting {booking_constants.website}...')
    #bot.select_place(booking_constants.place)
    bot.select_dates(booking_constants.check_in, booking_constants.check_out)