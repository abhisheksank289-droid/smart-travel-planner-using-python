# Smart Travel Planner

`smart_travel_planner.py` is a beginner-friendly Python console program for
planning a trip and estimating its cost.

## What the program collects

- Traveller name
- Destination
- Number of travellers
- Number of travel days
- Transportation cost per traveller
- Hotel cost per day
- Activity cost per traveller

The program uses a built-in food estimate of **$25 per traveller per day**.
This keeps the required input list short while still calculating total food
cost. Change `FOOD_COST_PER_TRAVELER_PER_DAY` in the Python file to use a
different estimate.

## What it calculates

- Total transportation cost
- Total hotel cost
- Total food cost
- Total activity cost
- Overall trip cost
- Cost per traveller
- Average daily cost

## Python concepts demonstrated

- Variables and suitable data types: strings, integers, and floating-point numbers
- `input()` and type conversion with `int()` and `float()`
- Dictionaries to organize trip information and calculated costs
- Functions with parameters and return values
- Arithmetic operations
- Validation using loops, `try`/`except`, and conditions
- Formatted output using f-strings

## Validation rules

- The number of travellers must be greater than zero.
- The number of travel days must be greater than zero.
- Costs cannot be negative.
- Traveller name and destination cannot be empty.

## How to run

Open a terminal in this folder and run:

```text
python smart_travel_planner.py
```

The program displays a formatted trip summary after all details are entered.

The project uses only Python built-in features. It has no database, files,
APIs, external libraries, or classes.