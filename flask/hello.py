from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "bye!"

@app.route("/username/<name>/<int:number>")
def greet (name,number):
    return f"hello there {name} , you are {number} years old"






if __name__ =="__main__":
    app.run(debug= True)
    
    
# decorators

# def upper_decor(fun):
#     def wrapper(name):
#         result = fun(name)
#         return result.upper()
#     return wrapper

# @ upper_decor
# def hello_decor(name):
#     return "hello" + name

# print(hello_decor(" sahid"))


