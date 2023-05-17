# Here's a shell script in Unix that extracts the Scheme Name and Asset Value fields from the given URL and saves them in a CSV file:

#!/bin/bash

URL="http://amfiindia.com/spages/NAVAll.txt"
OUTPUT_FILE="output.csv"

# Download the file
curl -o temp.txt "$URL"

# Extract Scheme Name and Asset Value fields and save to CSV
awk -F ';' '{print $1 "," $5}' temp.txt > "$OUTPUT_FILE"

# Cleanup temporary file
rm temp.txt

echo "Extraction complete. Results saved in $OUTPUT_FILE."

# Assumptions:

#The curl command is available to download the file from the given URL.
#The file is in a specific format with fields separated by semicolons (;).
#The Scheme Name is in the 1st field and the Asset Value is in the 5th field.
#The extracted data is saved in a CSV file named "output.csv" in the current directory.
