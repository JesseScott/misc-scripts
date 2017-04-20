#!/usr/bin/python

import csv


def read(file):
    """
    reads a tsv file and returns it as a list
    """
    print("### Reading " + file)
    with open(file, newline='\n') as f:
        return list(csv.reader(f))


def write(values):
    """
    writes a tsv file
    """
    with open("clean.tsv", "w") as f:
        writer = csv.writer(f, delimiter='\t')
        for v in values:
            writer.writerow(v)


def clean(values):
    """
    reads a csv/tsv file and returns it as a list
    """
    clean_values = []
    # iterate through the list
    for v in values:
        # split the string by tab
        parts = v[0].split('\t')
        # ensure we have 3 items in the new list
        # TODO - problematic, fix this
        if len(parts) == 3:
            # test if all parts have value
            valid = True
            for p in parts:
                if not p:
                    valid = False
            if valid:
                clean_values.append(parts)
    return clean_values

#####

# define the file
path = "data.tsv"

# read the file
data = read(path)

# clean the data
clean_data = clean(data)

# write the data
write(clean_data)


