#!/usr/bin/env python
import os
import sys
import json
import importlib


def parse_arguments():
  """Parse the problem number from command line arguments
  """

  if (len(sys.argv) < 2):
    print("Specify the problem number as a positional argument")
    sys.exit(1)
  return sys.argv[1]


def extract_runner(problem_number):
  """Dynamically import and return runner function for a problem
  """

  try:
    module = importlib.import_module(f"problems.{problem_number}")
    return module.run
  except ModuleNotFoundError:
    return lambda: print(f"No module found for problem {problem_number}")


def run():
  """Main entrypoint
  """

  # Parse the arguments to get the problem number
  problem_number = parse_arguments()

  # Get the runner function for that problem
  runner = extract_runner(problem_number)

  # Import the JSON test cases
  cases = []
  with open(os.path.join(os.path.dirname(__file__), "problems", problem_number, "cases.json")) as cases_file:
    cases = json.loads(cases_file.read())

  # Run the runner function
  for index, case in enumerate(cases):
    # Run the solution
    result = runner(*case["input"])
    # Determine if it was successful
    success = result == case["output"]
    # Output the result
    print(f"Case #{index + 1}: {'Succeeded' if success else 'Failed'}")
    # If it failed, output a diff
    if not success:
      print(f"\tExpected: {case['output']}")
      print(f"\tReceived: {result}")


if __name__ == "__main__":
  # Launch the runner
  run()
