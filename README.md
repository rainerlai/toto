[Purpose of the Script]
The purpose of this Python script is to automate the process of checking lottery tickets against the winning numbers for Singapore's TOTO lottery system. The script reads ticket numbers from a CSV file, compares them to the draw's winning numbers and an additional number, and determines if the tickets qualify for a prize based on predefined prize tiers. This tool is designed to save time, eliminate manual errors, and provide quick feedback for lottery participants.

[How the Script Works]
Input Data:

The script reads a CSV file (tickets.csv) containing lottery ticket numbers. Each ticket is listed in a single row, with numbers separated by commas.
The user provides the winning numbers (a set of six main numbers) and the additional number from the lottery draw.

Processing the Tickets:

Each ticket is read and converted into a list of numbers.
The script checks each ticket against the winning numbers and the additional number.
For "system bets" (tickets containing more than six numbers), the script generates all possible combinations of six numbers and evaluates each combination.
Determining Prizes:

The script compares the ticket's numbers to the winning numbers and additional number to calculate the number of matches.
Based on the matches, the script determines the prize tier for the ticket (e.g., Group 1 for 6 main numbers, Group 2 for 5 main numbers plus the additional number, etc.).

Output Results:

The script outputs the results for each ticket, including:
The full ticket details.
The number of main and additional matches.
The prize tier (if applicable) or a "No Prize" message.
Expected Results and Benefits
Expected Results:

The script will produce a detailed list of results for all tickets in the CSV file, indicating which tickets have won a prize and the corresponding prize tier.

[Benefits Over Manual Inspection]

Efficiency: Processes hundreds of tickets in seconds, compared to the hours it might take to manually check.

Accuracy: Eliminates the potential for human errors in identifying matching numbers or calculating prize tiers.

Ease of Use: Only requires the user to input the winning numbers and have a properly formatted CSV file of tickets.

By using this script, lottery participants can quickly check their tickets without the need for tedious manual verification.

*****Disclaimer*****
This Python script is provided for use freely with no restrictions, but users must use it at their own risk. While the script aims to be accurate, the original author provides no guarantees of its correctness or assurance against errors. Users are advised to double-check their results and confirm any winnings through official channels.

Additionally, the author does not encourage gambling. Lottery and other gambling activities should only be played responsibly and within one's means. If you or someone you know may have a gambling problem, please seek appropriate support or assistance.
