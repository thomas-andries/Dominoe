# import the required library
import math

def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    cosinus = math.cos(math.radians(angle_in_degrees))
    cosinus = round(cosinus, 2)
    print(cosinus)
