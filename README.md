## tribehacksiii
Alixpartners-TribeHacks-Challenge-2017

## Inspiration
I elected to do the Alixpartners Tribehacks Challenge to gain more experience in MySQL and data analysis on large data sets

## What it does
The challenge was to create and analyze a database and tables regarding fraud transactions, then visualize and report the data

## How I built it
I used MySQL and Python. 

## Challenges I ran into
The very first challenge that I ran into was in Step 0. I had difficulty creating the MySQL tables. I was able to create the Fraud MySQL table, after a learning curve, but wasn't able to directly apply that methodology to the Untagged table. This was because the untagged data wasn't preprocessed and some rows had too much or too few information (determining the root of this problem took several hours and involved a lot of debugging). Once I narrowed down the cause of the problem, I spent time researching the LOAD DATA LOCAL INFILE command to determine if I could correct the problem with command parameters. This was not possible. To solve the issue, I elected to preprocess each CSV file and remove any row that didn't have exactly 55 columns (this number was determined by the number of headers - and thus the number of table columns). I did this using the CSV python package. I moved problem columns to reject files so the data could be examined at a later time. After this preprocessing, I was able to create the tables.

I ran into difficulty on Step 1 with the tagging process. I was able to create an extra tag column and initialize it to 0 with relatively little issue. But, I had trouble tagging rows (entries) in the untagged data who had matching accountIDs with flagged data. The code that I created didn't appear to terminate, leading me to believe that the code was incorrect. I tried executing it on a smaller number of rows as a test using the MySQL workbench, but the workbench kept dropping the connection. This led me to believe that the code was incorrect and I decided to explore other options. However, on a hunch, I decided to let the code run in the background while I researched a solution. This turned out to be fortuitous. The code finally completed in a little over an hour and the initial flagging was correct.

I decided to split the table at this point to make it easier to work with. I made an 'innocent' table of all unflagged entries (tag = 0) and made a new_fraud table from flagged entries. I then continued Step 1 on this new_fraud table to differentiate from fraud and prefraud.

Since I had conducted some preprocessing on the table during Step 0 and was running out of time, I then elected to move to Step 3. I analyzed each header using discrete and narrowed down the list to potential candidate for categorical variables. However, once I began building a trial risk table for some of the categorical variables, it became clear that I would have to complete the cleaning of the data before continuing. At this point, I ran out of time.

## Accomplishments that I'm proud of
I'm so proud of my work on this project. Though my field is OR, this is my first time creating a database and tables on a large scale and on uncleaned data. I'm so happy with what I've accomplished, though I wish I had an extra day to actually analyze the data and finish the full challenge.

## What I learned
I learned so much about MySQL. I had some experience with SQL in general, but nothing on this scale. I had never attempted anything like this. I've learned the Python MySQL connector from scratch this weekend, something that I think will be very useful to me in the future. I also learned how to create MySQL script files using the MySQL workbench (something I hadn't done before). This was something that I didn't learn until late the last night. If I were to attempt the challenge again, I would use the workbench and scripts or the AWS RDS system (also new to me) instead of Python. 

## What's next for Alixpartners-TribeHacks-Challenge-2017
Given time I would split my program more intelligently into separate program files to reduce computation time. I would then finish the preprocessing data and complete the risk tables. Then I would analyze the results and create a visual presentation to relay the results.
