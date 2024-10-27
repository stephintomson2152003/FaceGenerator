import random

def generate_random_rgb():
    """Generates a random RGB value with one channel as 255 and others as 0."""
    # Choose a random channel to set to 255
    channel = random.choice([0, 1, 2])
    rgb = [0, 0, 0]
    rgb[channel] = 256
    return rgb

def create_random_grid(size=12):
    """Creates a grid of random RGB values."""
    return [[generate_random_rgb() for _ in range(size)] for _ in range(size)]

def save_grids_to_file(filename="random_rgb_grids.txt", num_grids=5, grid_size=12):
    with open(filename, "w") as file:
        for i in range(num_grids):
            file.write(f"Grid {i + 1}:\n")
            grid = create_random_grid(grid_size)
            for row in grid:
                file.write(f"{row}\n")
            file.write("\n")

save_grids_to_file()
