import random

def generate_random_rgb():
    """Generated a random RGB value"""
    return [random.randint(0, 255) for i in range(3)]

def create_random_grid(size = 12):
    """Creates a size 12 grid of random RGB value"""
    return [[generate_random_rgb() for i in range(size)] for j in range(size)]

def save_grids_to_file(filename = "random_rgb_grids.txt", num_grids = 5, grid_size = 12):
    with open(filename, "w") as file:
        for i in range(num_grids):
            file.write(f"Grid {i + 1}:\n")
            grid = create_random_grid(grid_size)
            for row in grid:
                file.write(f"{row}\n")
            file.write("\n")

save_grids_to_file()