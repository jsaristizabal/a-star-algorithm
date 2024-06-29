# a-star-algorithm


This repository contains an implementation of the A* algorithm in Python, which generates a random n x m matrix with random start and end points, as well as randomly distributed obstacles.

## Description

The A* algorithm is a pathfinding algorithm used in graphs. It is commonly employed in route planning applications and games. This repository generates a random matrix representing the environment map, where the following are identified:

- **Start Point:** The initial position where the search will begin.
- **End Point:** The target position that needs to be reached.
- **Obstacles:** Cells that cannot be traversed.

## Features

- Generation of a random n x m matrix.
- Random selection of start and end points.
- Random distribution of obstacles in the matrix.
- Implementation of the A* algorithm to find the shortest path from the start point to the end point.

## Requirements

- Python 3.x
- Additional libraries (if any)

## Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/jsaristizabal/A_star_algorithm.git
```

## Example

Here is a visual example of what a generated matrix and the path found by the A* algorithm might look like:

```bash
· x · · · · · · · · 
· · · · · x · · · x 
· x x · · · · · · · 
x · x · · · · · · · 
x · · · · x · x · · 
· · · · · x · · · · 
· · · · · · x · · · 
· · · x @ @ @ @ @ S 
· · G @ @ · · · · · 
· x · · · x x · · · 
```

- `S`: Start point
- `G`: End point
- `x`: Obstacle
- `·`: Free path

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

