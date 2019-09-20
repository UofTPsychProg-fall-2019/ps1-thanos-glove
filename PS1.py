#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% This is the final submission for Joseph Saito. The rest of the group (Tiana 
#Simovic, Benedict Park) will push a final submission for the whole group when 
#everyone finishes

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
coder1 = "hello world! python line " + "1"
print(coder1)

# second group member's error to fix
coder2 = Line 2: 'Hello there!' said + (the world)

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
coder3 =

# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt.index(-1)

# and then use missing_rt to remove the trial from rt
del rt[missing_rt]
clean_rt = rt

# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]

# try the same procedure. Does it work? 
# use a comment to explain why or why not below in comments
missing_rt = rt_trouble.index(-1)
del rt_trouble[missing_rt]

#JMS - The same procedure didn't work because it only removed the first
#instance that the value appeared in the list and not all of the instances 

# now write an if statement that you can use to remove the first missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.   

if rt.count(-1) > 0:
    missing_rt = rt.index(-1)
    del rt[missing_rt]
elif rt.count(-1) == 0:
    clean_rt = rt

# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

if data[0].count(-1) > 0:
    missing_rt = data[0].index(-1)
    del data[0][missing_rt]
    del data[1][missing_rt]
elif data[0].count(-1) == 0:
    clean_data = data
