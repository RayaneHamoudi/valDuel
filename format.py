import json

# Step 1: Load the JSON data from the file (even if it's all one line)
with open('response (3).json', 'r') as f:
    data = json.load(f)

# Step 2: Write it back with indentation (pretty-print)
with open('yourfile_pretty(3).json', 'w') as f:
    json.dump(data, f, indent=4)