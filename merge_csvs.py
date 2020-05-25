"""

Merge all CSVs in a directory into one CSV.
Assumes all CSVs have the same columns in the same order. 

Usage: `python merge_csvs.py`

"""

import os

CSVS_DIRECTORY = "."
OUTPUT_FILENAME = "output.csv"

first_done = False

with open(os.path.join(CSVS_DIRECTORY, OUTPUT_FILENAME), "w") as out:

    for file in os.listdir(CSVS_DIRECTORY):

        if file == OUTPUT_FILENAME or not file.endswith(".csv"):
            continue

        with open(os.path.join(CSVS_DIRECTORY, file), "r") as f:
            lines = list(f.readlines())

            if first_done:
                out.write("".join(lines[1:]))
            else:
                out.write("".join(lines))
                first_done = True

            print(file, len(lines))
