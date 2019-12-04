def cheating_probability(arr: [[int]]):
    P_FRONT = 0.3
    P_BACK = 0.2
    P_SIDES = 0.2
    P_DIAGONAL = 0.1
    ans = [[0.0 for col in range(len(arr[0]))] for row in range(len(arr))]

    for row in range(len(arr)):
        for col in range(len(arr[0])):
            current_branch = arr[row][col]
            probability = 0.0

            # Check Front
            if row - 1 >= 0 and arr[row - 1][col] == current_branch:
                probability += P_FRONT
            # Check Behind
            if row + 1 < len(arr) and arr[row + 1][col] == current_branch:
                probability += P_BACK
            # Check Left Side
            if (col - 1 >= 0 and arr[row][col - 1] == current_branch):
                probability += P_SIDES
            # Check Right Side
            if (col + 1 < len(arr[0]) and arr[row][col + 1] == current_branch):
                probability += P_SIDES
            # Check Upper Right Diagonal
            if row - 1 >= 0 and col + 1 < len(arr[0]) and arr[row - 1][col + 1] == current_branch:
                probability += P_DIAGONAL
            # Check Upper Left Diagnoal
            if row - 1 >= 0 and col - 1 >= 0 and arr[row - 1][col - 1] == current_branch:
                probability += P_DIAGONAL
            # Check Lower Left Diagonal
            if row + 1 < len(arr) and col - 1 >= 0 and arr[row + 1][col - 1] == current_branch:
                probability += P_DIAGONAL
            # Check Lower Right Diagonal
            if row + 1 < len(arr) and col + 1 < len(arr) and arr[row + 1][col + 1] == current_branch:
                probability += P_DIAGONAL

            ans[row][col] = probability

    for row in range(len(ans)):
        for col in range(len(ans[0])):
            print("{0:.1f}".format(ans[row][col]), end=' ')
        print("")
