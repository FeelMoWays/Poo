import turtle 
import pandas as pd
screen = turtle.Screen()
screen.title("US 50 States Game")
image = r'UdemyCourse\Day25\50 States\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv(r'UdemyCourse\Day25\50 States\50_states.csv')

turtle.mainloop()