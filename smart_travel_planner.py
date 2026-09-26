"""A beginner-friendly console travel planner."""

FOOD_COST_PER_TRAVELER_PER_DAY = 25.00


def get_positive_integer(prompt):
    """Read an integer that must be greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def get_non_negative_float(prompt):
    """Read a cost that must be zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Please enter a number, such as 125.50.")


def calculate_transportation_cost(cost_per_traveler, number_of_travelers):
    """Return the total transportation cost."""
    return cost_per_traveler * number_of_travelers


def calculate_hotel_cost(cost_per_day, number_of_days):
    """Return the total hotel cost."""
    return cost_per_day * number_of_days


def calculate_food_cost(number_of_travelers, number_of_days):
    """Return food cost using the program's daily food estimate."""
    return FOOD_COST_PER_TRAVELER_PER_DAY * number_of_travelers * number_of_days


def calculate_activity_cost(cost_per_traveler, number_of_travelers):
    """Return the total activity cost."""
    return cost_per_traveler * number_of_travelers


def calculate_overall_trip_cost(
    transportation_cost, hotel_cost, food_cost, activity_cost
):
    """Return the combined cost of the trip."""
    return transportation_cost + hotel_cost + food_cost + activity_cost


def calculate_cost_per_traveler(overall_cost, number_of_travelers):
    """Return the average trip cost for one traveler."""
    return overall_cost / number_of_travelers


def calculate_average_daily_cost(overall_cost, number_of_days):
    """Return the average cost for one travel day."""
    return overall_cost / number_of_days


def display_trip_summary(travel_information, costs):
    """Display the collected information and calculated costs."""
    print("\n" + "=" * 48)
    print("SMART TRAVEL PLANNER - TRIP SUMMARY")
    print("=" * 48)
    print(f"Traveller name       : {travel_information['traveller_name']}")
    print(f"Destination          : {travel_information['destination']}")
    print(f"Number of travellers  : {travel_information['number_of_travellers']}")
    print(f"Number of travel days : {travel_information['number_of_days']}")
    print("-" * 48)
    print(f"Transportation cost   : ${costs['transportation']:,.2f}")
    print(f"Hotel cost            : ${costs['hotel']:,.2f}")
    print(f"Food cost             : ${costs['food']:,.2f}")
    print(f"Activity cost         : ${costs['activity']:,.2f}")
    print("-" * 48)
    print(f"Overall trip cost     : ${costs['overall']:,.2f}")
    print(f"Cost per traveller    : ${costs['per_traveller']:,.2f}")
    print(f"Average daily cost    : ${costs['daily_average']:,.2f}")
    print("=" * 48)


def main():
    """Collect trip details, calculate costs, and display a summary."""
    print("Welcome to Smart Travel Planner")
    print(f"Food estimate: ${FOOD_COST_PER_TRAVELER_PER_DAY:.2f} per traveller per day")

    traveller_name = input("Enter traveller name: ").strip()
    while not traveller_name:
        print("Traveller name cannot be empty.")
        traveller_name = input("Enter traveller name: ").strip()

    destination = input("Enter destination: ").strip()
    while not destination:
        print("Destination cannot be empty.")
        destination = input("Enter destination: ").strip()

    number_of_travellers = get_positive_integer("Enter number of travellers: ")
    number_of_days = get_positive_integer("Enter number of travel days: ")
    transportation_per_traveller = get_non_negative_float(
        "Enter transportation cost per traveller: $")
    hotel_per_day = get_non_negative_float("Enter hotel cost per day: $")
    activity_per_traveller = get_non_negative_float(
        "Enter activity cost per traveller: $")

    travel_information = {
        "traveller_name": traveller_name,
        "destination": destination,
        "number_of_travellers": number_of_travellers,
        "number_of_days": number_of_days,
    }

    transportation = calculate_transportation_cost(
        transportation_per_traveller, number_of_travellers
    )
    hotel = calculate_hotel_cost(hotel_per_day, number_of_days)
    food = calculate_food_cost(number_of_travellers, number_of_days)
    activity = calculate_activity_cost(
        activity_per_traveller, number_of_travellers
    )
    overall = calculate_overall_trip_cost(transportation, hotel, food, activity)

    costs = {
        "transportation": transportation,
        "hotel": hotel,
        "food": food,
        "activity": activity,
        "overall": overall,
        "per_traveller": calculate_cost_per_traveler(
            overall, number_of_travellers
        ),
        "daily_average": calculate_average_daily_cost(overall, number_of_days),
    }

    display_trip_summary(travel_information, costs)


if __name__ == "__main__":
    main()
