def generate_cubes_dict():
    cubes_dict = {}
    for i in range(1, 6):  # Iterate over the range
        cubes_dict[i] = i ** 3  # Compute cube and assign to dictionary
    print(cubes_dict)
