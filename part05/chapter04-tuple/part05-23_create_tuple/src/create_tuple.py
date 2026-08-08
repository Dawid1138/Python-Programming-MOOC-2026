def create_tuple(x: int, y: int, z: int):
    list_tuple = [x, y, z]
    smallest = min(list_tuple)
    biggest = max(list_tuple)
    total = x + y + z
    tuple_result = (smallest, biggest, total)
    return tuple_result