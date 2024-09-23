from band import Band
from venue import Venue
from concert import Concert



def program():
    Band.drop_table()
    Venue.drop_table()
    Concert.drop_table()

    Band.create_table()
    Venue.create_table()
    Concert.create_table()
    
   