import csv
# Open the input CSV file
with open('input.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = []
    for row in reader:
        # Check if column 3 contains "[removed]"
        if "[deleted]" not in row[2]:
            rows.append(row)

# Open the output TXT file
with open('output_file.txt', 'w') as txtfile:
    # Extract column 3 from each row and write to the TXT file
    for row in rows:
        txtfile.write("User:\n\nReddit Comment: " + row[1] + "\n\n<|endoftext|>\n\n")

