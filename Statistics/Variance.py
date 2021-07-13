from Calculator.square import square
from Calculator.division import division
from Statistics.Statistics import mean

def variance(num):
    try:
        new_mean = mean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i-new_mean)
        return round(division(x, num_values), 5)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")