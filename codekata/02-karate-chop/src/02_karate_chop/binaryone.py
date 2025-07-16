import math


def chop(val_int, array_of_int) -> int:
    """
    Takes an int and an array and returns the index of that value int.
    Returns -1 if the int isn't in the array.
    Assume the array is sorted.
    """
    if len(array_of_int) == 0:
        return -1
    index = recursion(val_int, array_of_int, 0, len(array_of_int))
    print(f"Verify array_of_int[{index}] = {array_of_int[index]} = {val_int}")
    return index


def recursion(val_int, array_of_int, lower_index, upper_index) -> int:
    if lower_index + 1 == upper_index:
        if val_int == array_of_int[lower_index]:
            return lower_index
        return -1

    # check if it's even in this bound
    if val_int > array_of_int[-1] or val_int < array_of_int[0]:
        return -1

    # its not at the final number, and its in the bound... time to split it again
    split = math.floor((upper_index - lower_index) / 2)

    print(
        f"lower = {array_of_int[lower_index : lower_index + split]} and higher = {array_of_int[lower_index + split : upper_index]}"
    )

    if val_int <= array_of_int[lower_index + split - 1]:
        return recursion(val_int, array_of_int, lower_index, lower_index + split)
    else:
        return recursion(val_int, array_of_int, lower_index + split, upper_index)


# this is an annoying and wanky way to do this, but I was playing with poetry set up so we go forth...
if __name__ == "__main__":
    import sys
    from ast import literal_eval

    target = int(sys.argv[1])
    array = literal_eval(sys.argv[2])

    result = chop(target, array)
    print(f"Result: {result}")
