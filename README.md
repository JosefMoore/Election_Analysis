# Election_Analysis

## Overview of Election Analysis
--------------------------------
The purpose of this election analysis was to take an election file and find out winners of the election, number of votes, and votes per county for the commission. This was done by reading in a csv file full of election data and use for loops as well as if statements to parse through the data. 

## Election Audit Results
--------------------------------
* First, we learned that the total number of votes 369, 711. This was done by adding 1 to a total_votes variable outside a for loop while counting the rows of the file inside that for loop.

* Second, we learned that the winner of the election was Diane DeGette by a large margin at 73.8%. This was achieved by adding the candidate names to a list using an if statement with condidtionals to check if the name was in the list already. This was also used to count the votes for each candidate.

* Third, we learned that the county with the highest voter turnout was the Denver county. This was achieved with similar methods to finding the winning candidate, just looking for the county names instead.

## Election Audit Summary
-------------------------------
The solution we created to come up with these results is easily reusable. If the file provided uses the same format as the data we received, we can just plug in the file. If the file is different, we can modify some of the variables we used to identify columns containing candidate names and county names with just a change of the index. The script can also be changed to glean extra insight from any additonal data points in the file provided.