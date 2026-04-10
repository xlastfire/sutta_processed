from glob import glob
import os
import json

output_file = 'paths'
files = glob('*.json')

# Load existing data
if os.path.isfile(output_file):
    with open(output_file, 'r') as f:
        data = json.load(f)
else:
    data = []

initial_count = len(data)

# Filter out the output file itself if it's in the same directory
files = [f for f in files if f != output_file]

for file in files:
    name = os.path.splitext(file)[0]
    if name not in data:
        data.append(name)

final_count = len(data)
new_entries = final_count - initial_count

# Save and print results
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"--- Results ---")
print(f"Files found in folder: {len(files)}")
print(f"Existing entries:      {initial_count}")
print(f"New entries added:     {new_entries}")
print(f"Total entries now:     {final_count}")