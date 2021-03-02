from flask import Flask, render_template
import random

app = Flask(__name__)
app.config["DEBUG"] = True

def calculate(set) : # Calculate the total weight of the given set
    return sum(item[1] for item in set) #list comprehension

# Determine which set is the heaviest
def measure(first_set, second_set, third_set) : 
    first_set_weight = calculate(first_set)
    second_set_weight = calculate(second_set)
    if first_set_weight == second_set_weight :
        return third_set # If the first 2 sets are equally heavy, the heavy set is the third one
    elif first_set_weight > second_set_weight :
        return first_set # If the first set is heavier than the second, the heavy set is the the first one
    return second_set # If the second set is heavier than the first one, then it is the heavy set

@app.route('/', methods=['GET'])

def home():
    balls =  [["a",4], ["b",4], ["c",5], ["d",4], 
                ["e",4], ["f",4], ["g",4], ["h",4]] 
    # Slice the set to subsets of 3,3,2
    heavy_set = measure(balls[0:3],balls[3:6],balls[6:8]) 
    # Check the number of balls in each set
    if len(heavy_set) == 2 :
        # If the set has 2 balls, pass those 2 balls and "0" to measure()
        result = measure([heavy_set[0]],[heavy_set[1]],0)
    else:
        # If the set has 3 balls, pass those 3 balls to measure()
        result = measure([heavy_set[0]],[heavy_set[1]],[heavy_set[2]])
    
    # print(str(heavy_set) + " has the heaviest ball")
    # print(result[0][0] + " is the heaviest ball")

    return render_template('index.html', balls = balls, heavy_set = heavy_set, result = result[0][0])

app.run()