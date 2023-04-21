import sys
import os

# Check if correct number of command-line arguments are provided
if len(sys.argv) != 2:
    print("Usage: python text_to_srt.py <input_file>")
    sys.exit(1)

# Input file path
input_file = sys.argv[1]

# Check if input file exists
if not os.path.isfile(input_file):
    print(f"Error: Input file '{input_file}' not found.")
    sys.exit(1)

# Generate output file name
output_file = os.path.splitext(input_file)[0] + '.srt'

srt_lines = []
counter = 1

# Read input file
with open(input_file, 'r') as f:
    lines = f.readlines()

# Loop through each line in the input file
for line in lines:
    if line.strip() != '':
        # Extract start and end timestamps and subtitle text from the line
        start_time = line.split('->')[0].strip()
        end_time = line.split('->')[1].strip()
        subtitle_text = line.split(']')[1].strip()

        # Create SRT formatted line
        srt_line = f"{counter}\n{start_time} --> {end_time}\n{subtitle_text}\n\n"

        srt_lines.append(srt_line)
        counter += 1

# Write output to SRT file
with open(output_file, 'w') as f:
    f.writelines(srt_lines)

print(f"SRT file created successfully at: {output_file}")
