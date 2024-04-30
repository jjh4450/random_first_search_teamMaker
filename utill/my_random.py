import os

def secure_random(min_value, max_value):
    if max_value < min_value:
        raise ValueError("max_value must be greater than min_value")
    elif (max_value - min_value) == 0:
        return max_value

    random_bytes = os.urandom(4)
    random_int = int.from_bytes(random_bytes, 'big')

    return min_value + random_int % (max_value - min_value)