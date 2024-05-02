def parse_input():
    grid = [list(map(int, input().split())) for _ in range(9)]
    allowed_numbers = list(map(int, input().split()))
    k = int(input())
    return grid, allowed_numbers, k

def print_output(result):
    if result == "Impossible":
        print(result)
    elif result == "Won":
        print(result)
    else:
        for cell in result:
            print(cell[0], cell[1])

def is_valid(grid):
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if grid[i][j] != 0 and grid[i][j] in row_set:
                return False
            row_set.add(grid[i][j])
            if grid[j][i] != 0 and grid[j][i] in col_set:
                return False
            col_set.add(grid[j][i])

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_set = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] != 0 and grid[i + x][j + y] in subgrid_set:
                        return False
                    subgrid_set.add(grid[i + x][j + y])

    return True

def solve(grid, allowed_numbers):
    # TODO: Implement a Sudoku solver
    pass

def count_modifications(grid, solved_grid):
    count = 0
    modifications = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0 and grid[i][j] != solved_grid[i][j]:
                count += 1
                modifications.append((i, j))
    return count, modifications

def main():
    grid, allowed_numbers, k = parse_input()

    if not is_valid(grid):
        print("Impossible")
        return

    # TODO: Call the Sudoku solver function
    solved_grid = solve(grid, allowed_numbers)

    if solved_grid is None:
        print("Impossible")
    else:
        modifications_count, modifications = count_modifications(grid, solved_grid)
        if modifications_count <= k:
            print("Won")
        else:
            print_output(modifications)

if __name__ == "__main__":
    main()