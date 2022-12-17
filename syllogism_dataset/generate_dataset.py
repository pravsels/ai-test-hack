import csv
import sys
import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np
import random

# TODO:
# Vary order of the premises
# Change answer sometimes to 'yes'

# open the file in the write mode
output_path = 'two_premise_auguments.csv'
out = open(output_path, 'w')
# create the csv writer
writer = csv.writer(out)

# Load original dataset
input_path = 'Avicenna_Train.csv'
df = pd.read_csv(input_path)
count = 0
writer.writerow(["prompt", "classes", "answer_index"])


# Iterate over every syllogism (1 per row)
for index, row in df.iterrows():
    if row['Syllogistic relation'] == 'yes':
        # Build prompt

        prompt = 'Q: Given these premises; does the conclusion logically follow?\n'

        ordering = np.random.permutation(2)
        yes_no = True
        for i in range(len(ordering)):
            o = ordering[i]
            if o == 0:
                prompt = prompt + 'Premise ' + str(i+1) + ': ' + row['Premise 1'] + '\n'
            elif o == 1:
                prompt = prompt + 'Premise ' + str(i+1) + ': ' + row['Premise 2'] + '\n'
            """elif o == 2:
                # Caulate the prompt number to refer to 
                nums = [0, 1, 2]
                nums.remove(i)

                # Randomize which prompt are true or false
                rand_bool_1 = bool(random.getrandbits(1))
                rand_bool_2 = bool(random.getrandbits(1))
                yes_no = rand_bool_1 and rand_bool_2

                # Add prompt to string
                prompt = prompt + 'Premise ' + str(i+1)
                prompt = prompt + ': Premise {} is {}. Premise {} is {}.\n'.format(nums[0]+1, str(rand_bool_1).lower(), nums[1]+1, str(rand_bool_2).lower()) 
            """
        prompt = prompt + 'Conclusion: '  + row['Conclusion'] + '\n'
        prompt = prompt + 'A:'
        
        # Write to csv
        yes_no = not yes_no
        writer.writerow([prompt, "[\' Yes\',\' No\']", str(int(yes_no))])

        # Limit to 100 rows
        count += 1
        if (count > 100):
            break
