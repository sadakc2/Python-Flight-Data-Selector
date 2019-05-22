# Python-Flight-Data-Selector

1.	Description of calculations/algorithms for selecting:
•	Best of each category
I calculated the best of each category essentially the same way. One category that is calculated differently from the others, however, is Month. Since I decided to make a separate list for each month, I did not have to worry about weighing the rows. I made a list for each month and then called the findBestMonth() function passing the next month each time. Instead, I was able to calculate the mean of the departures performed column, the departures scheduled column, and the seats column separately for each month one at a time. Once the mean for each of the three columns was calculated for a month, I calculated the score. The score was calculated in this case by dividing the mean of the month’s departures scheduled by the mean of the month’s departures performed to find the average success rate of flights not being cancelled. For user display purposes, I also calculated the average percentage by multiplying the average by 100.  Then I multiplied this average by the month’s mean of seats. I then appended a list that included the month’s score, name, average percentage, and average seats to a list called bestMonth. Once I completed this process for each month, I sorted bestMonth descending and was able to display the months in order from best to worst. 

For calculating the best Carrier, Origin City, Destination City, Aircraft, Origin State, Destination State, and Distance I used a different algorithm than the one used for Month. These seven categories all used the same algorithm. However, to make this description clearer while not becoming redundant I will discuss this algorithm in terms of finding the best carrier. However, it is true that the algorithm is the same for each category, it would just create and use a different list depending on the criterion selected. To calculate the best carriers, I first got the number of unique carriers in the large dataset. The number of items in this list equals the number of unique carriers in the big dataset. I then set a tuple of (0,’’,0,0) to each spot in a list entitled bestAirline. I then would go row by row the large dataset and get each row’s departures scheduled, departures performed, and seats. If the number departures performed was greater than the number of departures scheduled, I set the average to one since I did not want to show the user flights that they could not take since they weren’t even scheduled in the first place. I then had to figure out a way to weigh each row so that the score wouldn’t be skewed depending on the number of flights that row consisted of since each row could represent many more than just one flight. For example, without weighing the rows, a row with 9 departures performed and 10 departures scheduled with 1000 seats would get a score 100 points higher than a row with 80 departures performed and 100 departures scheduled with 1500 seats. This should not be the case because the larger dataset is more representative of the likelihood that a flight will occur and 80/100 is a better representation of a flight’s chances than 9/10. So even if the 9/10 row would initially get a higher score than the 80/100 row, the user should be shown that the 80/100 row is a better option. To weigh the rows, I calculated a variable called divider at the beginning of the program. This value is the mean of the entire dataset’s departures performed column. Now when calculating the score, I would first calculate a new departures performed score which would be the row’s departures performed divided by the divider. The reason I decided to divide the row’s departures performed by the divider is because this would make a larger disparity between rows similar to the example rows listed earlier in this section in favor of the one with the larger sample size. I would use this new departures performed when calculating the row’s average. I also divided the row’s seats by the divider to create disparity between seats from a row with lower departures performed with row from higher departures performed. The score was then calculated by multiplying the new average and the new seats. Using the example from before, the divider would be (9+80)/2 = 44.5, the departures performed for the 9/10 row would be 9/44.5=.20225 and seats would be 1000/44.5=22.47. The score for this row would be (.20225/10)*22.47 = .45449. For the 80/100 row, the new departures performed would be 80/44.5 = 1.79775, the new seats would be 1500/44.5=33.707 and the score would be (1.79775/100)*33.707=.605967 placing the 80/100 row above the 9/10 row. For each row, I got the carrier name and found the index of that carrier name in the list of all unique carriers created at the beginning of the program. I then got the previous score from that index and added the current score to that and put it back in the same index. In each index, I stored a tuple including the previously mentioned score, the carrier name, the average percentage and the seats. At the end of going through each row of the dataset, I sorted the bestAirline list and pulled the top 10 carrier names and other data attributes to display to the user. The only difference between the algorithm for Best Distance is that I also grabbed the distance from the row and have a series of if-else statements to determine which range to group the row into based on the instructions for the program. I used the range index for the bestDistance array. 
•	Best when combining categories
To calculate the best of combinations I used a different algorithm. The combinations I filter by are Carrier and Month, Origin State and Month, and Destination City and Month. I used the same algorithm for each of these, so to make the description clearer I will discuss the algorithm regarding finding the best Origin State and Month. To do this, I created a function called findbetOrgStinMo() and passed it topMonth. topMonth is a variable found right before the function is called by getting the month from the first index of sortedBestMonth(). Each iteration that this function is called, it gets the next best month.  The loop that finds topMonth loops three times and calls the functions once per iteration to pass the function the top three best months. Once the topMonth was passed to the function, it went through a series of if-else statements to determine the month number based on the string it was passed. Once the month number was determined, a dataframe was created from the large dataset with only rows that include that topMonth number. I then found the total number of unique Origin States and created a list of that length and set each tuple in each index to (0,’’,0,0). I then went row by row through this smaller dataframe consisting of only rows containing topMonth. I then proceeded with the same algorithm listed in the previous section about finding the best of individual categories. I went row by row through the small data frame and found the departures performed, departures scheduled, seats, calculated the divider (the average of the huge data sets departures performed), the new departures performed (departures performed/divider), new seats (seats/divider), the new average (new departures performed/departures scheduled), and then calculated the score for that row (new average* new seats). I then added this current score to the previous score found in the index belonging to the origin state found from the orgStateList. I repeated this process for each row and then sorted the list at the end to determine the best origin states per best month. 
•	Best based on user selection
For user mode, I first store the value(s) chosen by the user. I then go into a series of if-else statements that check to see which option(s) the user selected. If the selection value for a particular choice is “—select—” it means the user did not select anything in that category. If the selection value for a particular choice is anything other than “—select—” then it means the user did select something for that category. I allow the following selections: only Month, only Carrier, only Origin City, only Destination City, only Distance, Month and Carrier, Month and Carrier and Destination City, and Month and Carrier and Destination City and Origin City. The choice(s) selected would determine which if-else statement I entered. Once in an if-else, I created a dataframe that held rows that contained each specified criterion. If there were multiple criteria selected, I used a compound AND statement to make sure each row put in to the new dataframe contained all necessary values, not just one of them or a few of them.  I then continued with the same algorithm from the previous sections of the write up. I went row by row through the small data frame and found the departures performed, departures scheduled, seats, calculated the divider (the average of the huge data sets departures performed), the new departures performed (departures performed/divider), new seats (seats/divider), the new average (new departures performed/departures scheduled), and then calculated the score for that row (new average* new seats). I then appended the score, average percentage, index, and seats to a list called resultsLofL (standing for results list of lists). I repeated this process for each row and then sorted the list at the end to determine the best origin states per best month. I used labels to print the results in user mode. I then sorted resultsLofL. If there were at least ten results from a query, the first three were green, the last three were red, and the middle ones were gold to give the user visualization of the flight choices. If there were fewer than ten results for a query, I decided to display them all as green. 
2.	Description of how program was coded
I began coding my program in February. The first part of the program I worked on was getting a very basic GUI using Python3 and Tkinter. To do this, I researched the best tools to create a GUI using Python and how to download them. Once I had all of the necessary software and packages installed, I was able to create a GUI that had a button to quit the application. From then, I worked on creating a more useful initial window that included a button for Auto Mode, User Mode, and Quit. From here, I went to make the User Window that appeared once User Mode is clicked. I decided which categories I wanted the user to be able to search by and then began learning how to create drop down menus using Tkinter. Once I learned how to make a drop-down menu, I loaded the data into my program so that I could begin dynamically loading the choices available for each drop down. Once I had the data loaded into my program, I learned how to dynamically load the data into the drop-down menus by finding the unique values from each column I wanted to allow the user to filter by and then turning this dataframe of unique values into a list. Once I figured this out, I learned how to store a value chosen by the user into a variable to be used later. From here, I began to try to filter the data by one value chosen from the user at a time. At first, I just wanted to display the best flight based on a chosen criterion. However, my initial algorithm was wrong. I went along with this algorithm for a long time though because I was not aware that it was wrong until Dr. Garrison gave me that feedback after we turned in our prototypes. The reason my algorithm was wrong was because it calculated scores on a row by row basis without first weighing each row. Weighing each row is necessary because one row does not necessarily equal only one flight, so it is not mathematically sound to take a percentage of each row and average them together at the end. It was difficult for me to come up with an algorithm I felt was viable, but I did this by writing out example numbers on a piece of paper and playing with numbers until I found a way to make the rows with lower departures scheduled consistently score lower than rows with more departures scheduled. This algorithm is discussed in the algorithm portion of the write up. Even before I got my algorithm to something I was happy with, I spent a good bit of time making my user interface look how I wanted it to. At first, I spent more time on the user mode user interface because that code is what I spent more time on in the beginning. Once I was happy with that interface, I began working on the auto mode display. At first, I tried to display these results in the same way that user mode does, however labels were not feasible because There was too much data being displayed for it to look readable. Originally, the lines of code that took care of this were terribly redundant in my code. I went back later and made some of the code to display results into functions to clean up the code. I went back through a large portion of my code and consolidated a number of repetitive sections of code into functions. When coding this project, it seemed like when I got on a roll of coding new functions it was good to keep going and adding new combinations of choice available to the user. Once I felt confident that I was getting the correct results and outputting a handful of them, I went through the process of making displaying output an iterable process to display more. 
3.	Description of any intermediate files
•	ProjectDataEDITED.csv
•	Got rid of unnecessary columns
•	Got rid of rows where there were no seats
•	Main file used with this program
•	CarrierData.csv
•	Has very small number of rows each with a different carrier listed 
•	Used 12 smaller excel files each containing only one month to test the best month algorithm. I did not save these because I could easily get each one by going to ProjectDataEDITED.csv and filter the month column by a month number.
4.	Identify GUI, OS, and Python version used
•	GUI – Tkinter
•	OS – MacOS Mojave
•	Python version – Python3
5.	Results of Auto Mode with explanation of why these recommendations were made and the supporting table of statistics/calculations
•	Shown on Auto Mode Documentation which is attached at the end of the document
•	When displaying results to the user in auto mode, I used a treeview. I displayed the chosen criteria, the unweighted departures performed to departures scheduled percentage, the unweighted number of seats, and the weighted score. I did not want to display so much that I overwhelmed the user but I also wanted it to be clear that there was weighing of rows being done. 
6.	Results/tests showing Manual Mode with explanations and supporting table of statistics/calculations
•	Shown on User Mode Documentation which is attached at the end of the document
•	When displaying results to the user in user mode, I used labels. I displayed the carrier, departure city, the destination city, the distance, the unweighted departures performed to departures scheduled percentage, the unweighted number of seats, and the weighted score. I did not want to display so much that I overwhelmed the user but I also wanted it to be clear that there was weighing of rows being done. I also felt like with auto mode, the user may have been looking for flight suggestion ideas. For example, maybe they wanted to know what the best month to fly is so they found that on auto mode and then went to user mode and picked that month and their favorite city. 
7.	Description of how program was tested and validated
My program was tested by using small data sets for various sets of chosen criteria. Small data sets were necessary because I was unable to test the large dataset myself by actually performing the math calculations on paper, but I was able to with datasets consisting of only a few rows. There were a number of program aspects I definitely wanted to make sure were tested. These included:
•	When fewer than 10 results are generated for a search, all of the results need to be displayed without throwing a segmentation fault error for trying to display something in a list index that is not there
•	Make sure user is told when it is not possible to perform a certain combination in user mode 
•	Make sure user is told when there were no found results for a combination to search by that is allowed if that is what happened. Don’t just leave the screen blank 
•	Allow the user to reset options in user mode so the user does not have to close that part of the application to search on different criteria
•	Make sure rows with a larger data set (more departures scheduled) represented score higher than those with a smaller data set (fewer departures scheduled). I did this by creating the table listed below and crunching numbers to test the validity of my algorithm. I understand, however, that these numbers are not a great representation because there are not enough rows to thoroughly test the system and seats are still able to play a potentially unwanted role in skewing the score as is seen with the score between UAL and EA airlines. However, I think this is okay because there is not a drastic difference in the number departures scheduled and performed for these two rows and the number of seats wasn’t drastically higher. This is using the CarrierData.csv
•	Testing the results of best Carrier based on smaller data set
	DP	DS	Divider	Seats	newDP	newSeats	Score
AA	107	108	37	13696	2.89	370.16	9.905
Delta	70	70	37	7699	1.89	208.08	5.6376
UAL	19	19	37	2432	0.51	65.73	1.764
EA	24	24	37	1200	0.649	32.43	0.8769
PSA	1	1	37	65	0.027	1.757	0.0474
SW	1	1	37	50	0.027	1.35	0.03654

In addition to these tests, I also used the data file ProjectDataEDITED.csv file in Excel to match results. When testing the system, I would filter on the columns in Excel in some of the same ways I could filter on the columns by using my application. For example, I could calculate the divider variable for the data by highlighting the departures performed column and view the mean in the bottom right hand corner of Excel. I could also filter by the same airline that a user selected, the destination city, departure city, and month to run numbers. 
	DP avg	DS avg	Seats avg	Score	Order
Jan	31.906	33.900	3293.172	3099.467	11
Feb	32.233	32.860	3345.32	3281.488	10
March	36.614	37.729	3813.718	3701.011	3
April	33.713	34.19	3534.545	3485.23	6
May	34.310	34.798	3616.808	3566.087	5
June	29.936	31.605	3158.438	2991.65	12
July	33.015	33.794	3446.172	3366.733	8
August	33.434	34.229	3502.623	3421.27	7
September	33.328	35.276	3546.310	3350.477	9
October	39.759	40.324	4180.81	4122.231	1
November	36.569	36.767	3800.41	3779.94	2
December	35.225	35.826	3665.09	3603.61	4
•	Testing the results of best Month. I did this by filtering the large dataset by each month one at a time and finding the mean departures performed (DP), mean departures scheduled (DS), mean seats, score (DP avg/DP sched)*Seats avg. The order that resulted from this testing is the same order that appears on the application.
 
8.	Acknowledgment of any collaboration efforts. For example, design might have been modified based on a question in class about another student’s design
•	George informed me after asking Dr. Garrison a question over email that for auto mode we needed a minimum of three combinations of at least two criterion each
•	Daniel taught me that pandas and Tkinter existed for python. I had never heard of those things before the start of this project
•	George suggested how beneficial a reset button might be to the user, so I implemented one 
