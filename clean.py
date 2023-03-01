import csv

# Open the input CSV file
with open('input.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    # Open the output CSV file
    with open('output.csv', 'w', newline='', encoding='utf-8') as g:
        writer = csv.writer(g)
        # Loop through each row and check if column B contains "[deleted]"
        for row in reader:
            if '[deleted]' not in row[1]:
                # Write the row to the output CSV file if it doesn't contain "[deleted]"
                writer.writerow(row)

