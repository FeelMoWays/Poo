import datetime as dt
from decimal import Decimal
from random import choice,randint
from custom_module import generate_time_travel_message
year = dt.datetime.now().year
time = dt.datetime.now().time()
base_cost = Decimal('1000.00')
test_year = randint(2000,3000)
if test_year > year:
    final_cost = base_cost * abs(test_year-year)
else:
    final_cost = base_cost * abs(year - test_year)
possible_choices = ["Hot Topic 2000's","Nuevo York",'First Showing of Dark Knight',"Cyberpunk 2077 release"]
destination = choice(possible_choices)
print(generate_time_travel_message(test_year,destination,final_cost))