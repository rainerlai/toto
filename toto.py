import csv
from itertools import combinations

# Updated prize tiers based on the new rules
PRIZE_TIERS = {
    (6, False): "Group 1 (6 main numbers)",  # 6 main numbers
    (5, True): "Group 2 (5 main + additional)",  # 5 main + additional
    (5, False): "Group 3 (5 main numbers)",  # 5 main
    (4, True): "Group 4 (4 main + additional)",  # 4 main + additional
    (4, False): "Group 5 (4 main numbers)",  # 4 main
    (3, True): "Group 6 (3 main + additional)",  # 3 main + additional
    (3, False): "Group 7 (3 main numbers)",  # 3 main
}

def check_tickets(csv_file, winning_numbers, additional_number):
    """
    Checks tickets in a CSV file against the winning numbers and additional number.

    :param csv_file: Path to the CSV file containing tickets.
    :param winning_numbers: A set of six winning numbers.
    :param additional_number: The additional number drawn.
    :return: None
    """
    print(f"Attempting to open: {csv_file}")
    
    try:
        # Open the file with UTF-8 encoding to handle potential BOM (Byte Order Mark)
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            tickets = []
            for row in reader:
                try:
                    # The ticket is in a single cell as a comma-separated string
                    ticket = list(map(int, row[0].split(',')))  # Split the string into numbers
                    tickets.append(ticket)
                except ValueError as e:
                    # Print an error message if any value is not an integer
                    print(f"Skipping invalid ticket: {row} - Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found. Please check the file path.")
        return
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}. Try checking or converting the file encoding.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    print("\nResults:")
    for i, ticket in enumerate(tickets, start=1):
        ticket_set = set(ticket)

        # Handle System Bets (System 7 to System 12)
        if len(ticket_set) > 6:
            combinations_list = list(combinations(ticket_set, 6))
        else:
            combinations_list = [ticket_set]

        best_result = None

        # Check each combination for matches
        for combination in combinations_list:
            combination_set = set(combination)
            main_matches = len(combination_set & winning_numbers)
            has_additional = additional_number in combination_set

            # Determine the prize based on matches
            prize_key = (main_matches, has_additional)
            if prize_key in PRIZE_TIERS:
                prize = PRIZE_TIERS[prize_key]
                if not best_result or list(PRIZE_TIERS.keys()).index(prize_key) < list(PRIZE_TIERS.keys()).index(best_result):
                    best_result = prize_key

        # Output the result for this ticket
        if best_result:
            main_matches, has_additional = best_result
            prize = PRIZE_TIERS[best_result]
            print(
                f"Ticket {i}: {ticket} - {main_matches} main matches{' + additional' if has_additional else ''} - {prize}"
            )
        else:
            print(f"Ticket {i}: {ticket} - No Prize")

# Example usage
if __name__ == "__main__":
    # Define winning numbers and the additional number
    winning_numbers = {9, 11, 24, 29, 39, 46}  # Replace with actual draw numbers
    additional_number = 31  # Replace with the actual additional number

    # Path to the CSV file containing tickets
    csv_file = "tickets.csv"  # Replace with the path to your CSV file

    print("Winning Numbers:", winning_numbers)
    print("Additional Number:", additional_number)
    
    check_tickets(csv_file, winning_numbers, additional_number)
