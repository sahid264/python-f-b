from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTBieW80dGgyc3RzOHVmYWY4NHhrMHBxd3F4ejRldWFkd2h6cm4weCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.webp'/>"




@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style ='color:red'> Too high, try again</h1>" \
            "<img src= 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemo2NnNjNzJvMDR1MzhhaTg5M2k4ZXZ0Z25iZzByM2cwbjR0OXA0NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YKroe55zFMIwpmBCu6/giphy.webp'/>"
            
    elif guess < random_number:
        return "<h1 style= 'color= red'>Too low, try again </h1>" \
               "<img src = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2JmYjd0MXVhOWY2NjY5dmx1dzd5cDNrdDE4dTUyenAzNWZlaHp3NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wdh1SvEn0E06I/giphy.webp'/>"
               
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnN1ejV1Zm94NnI5bDg2dTI3eHpsYmlhemV0ZnJ0cmd2cmhrbDJsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iowmvjVUnDFGU/giphy.webp'/>"
                


if __name__ == "__main__":
    app.run(debug=True)

            
    
