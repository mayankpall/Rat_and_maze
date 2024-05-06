def is_valid_move(maze, visited, row, col):
    rows = len(maze)
    cols = len(maze[0])
    return row >= 0 and row < rows and col >= 0 and col < cols and maze[row][col] == 0 and not visited[row][col]

def dfs(maze, visited, row, col, dest_row, dest_col, path):
    if row == dest_row and col == dest_col:
        return True
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if is_valid_move(maze, visited, new_row, new_col):
            visited[new_row][new_col] = True
            path.append((new_row, new_col))
            
            if dfs(maze, visited, new_row, new_col, dest_row, dest_col, path):
                return True
            
            path.pop() # Backtrack
            visited[new_row][new_col] = False
    
    return False

def find_path_dfs(maze, start_row, start_col, dest_row, dest_col):
    rows = len(maze)
    cols = len(maze[0])
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start_row][start_col] = True
    
    path = [(start_row, start_col)]
    
    if dfs(maze, visited, start_row, start_col, dest_row, dest_col, path):
        return path
    else:
        return None

def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in path:
                print("P", end=" ")  # Print path marker
            elif maze[i][j] == 1:
                print("#", end=" ")  # Print wall
            else:
                print(".", end=" ")  # Print empty space
        print()

# Example usage:
maze = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0]
]

start_row, start_col = 0, 0
dest_row, dest_col = 3, 3

path = find_path_dfs(maze, start_row, start_col, dest_row, dest_col)
if path:
    print("Path found by DFS:", path)
    print("Maze with path:")
    print_maze_with_path(maze, path)
else:
    print("No path found by DFS.")
