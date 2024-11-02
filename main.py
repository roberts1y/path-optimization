import fields2cover as f2c
import matplotlib.pyplot as plt

def setup_boundary(coords):
    """Initialize the boundary for the coverage area."""
    return f2c.Boundary(coords)

def initialize_planner(boundary):
    """Initialize the coverage path planner with the defined boundary."""
    planner = f2c.CoveragePlanner(boundary)
    return planner

def generate_coverage_path(planner):
    """Generate the coverage path within the boundary."""
    path = planner.generate_path()
    return path

def plot_coverage_path(planner, path):
    """Visualize the coverage path."""
    planner.plot_path(path)
    plt.title("UAV Coverage Path within Polygonal Boundary")
    plt.xlabel("X Coordinate (m)")
    plt.ylabel("Y Coordinate (m)")
    plt.grid()
    plt.show()

def main():
    # Define the polygonal area to be covered
    boundary_coords = [(5, 0), (10, 5), (5, 10), (0, 5)]  # Example: Diamond-shaped boundary
    boundary = setup_boundary(boundary_coords)

    # Initialize planner with the defined boundary
    planner = initialize_planner(boundary)

    # Generate and visualize the coverage path
    path = generate_coverage_path(planner)
    plot_coverage_path(planner, path)

if __name__ == "__main__":
    main()