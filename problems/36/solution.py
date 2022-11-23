"""Problem 36. Valid Sudoku
"""

from typing import List

def solution(board: List[List[str]]) -> bool:

  # Start with an empty bucket
  # Used to store found entries
  bucket = {}

  # Function to get a token for the current "square"
  # The term "square" refers to a section of a sudoku board
  def get_square(x, y):
    sx = (x // 3) + 1
    sy = (y // 3) + 1
    return f"{sx}{sy}"

  # Iterate through every entry in the board.
  for row, items in enumerate(board):
    for col, item in enumerate(items):

      # If the entry is empty, skip.
      if item == ".":
        continue

      # See if the entry exists elsewhere in the board column or row.
      ce = bucket.get(f"c{col}:{item}")
      re = bucket.get(f"r{row}:{item}")

      # See if the entry exists elsewhere in the square.
      sqr = get_square(col, row)
      se = bucket.get(f"s{sqr}:{item}")

      # If it exists in any of the criteria...
      if ce or re or se:
        # The board is invalid.
        return False
      else:
        # Otherwise, store the entry in the bucket.
        bucket[f"c{col}:{item}"] = True
        bucket[f"r{row}:{item}"] = True
        bucket[f"s{sqr}:{item}"] = True

  # No invalid entries were found, the board is valid.
  return True
