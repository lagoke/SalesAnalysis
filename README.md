# Overview

This research work is focused on writing a Python script/application to read the content of my chosen dataset (which I downloaded from kaggle website), count the total number of records in it to verify it has loaded correctly and perform non-trivial operations on the records. 

Specifically, it performed data transformation or data conversion using functions like log and scaling while also performing reduction operation like min, max and mean on the data. The scripted result would be verified using Python libraries such as NumPy and Pandas.

Basically, I demonstrated the use of "try... except" as highlighted in the requirement given for this week. I used this when I was reading the CSV file with the reader() function. The try--- except is expected to take care of any error that flags up during the runtime of
the python script (File Not Found error). I had earlier imported the necessary libraries that would be needed for the program (e.g. CSV, NumPy, Pandas and Matplotlib).

To answere the questions I asked about the data as mentioned in the analysis section below, when I performed the non-trivial data transform operation of log by running function (transform_with_natural_log()), it confirmed that the first two highest sales values are 5512.32 and 4708.44 and it happened when the prices were the most expensive (114.84).

When I also performed the non-trivial data transform operation of scaling by running function (transform_with_scaling()), a standard deviation value of exactly 1 was realized and this happened when the highest sales (5512.32) was recorded.

When I performed the non-trivial data reduction operation of max by running function (min_max()), it confirmed that the highest quantity ordered (48) happened when the price (114.84) was the most expensive and this shot up the sales (5512.32).

The dataset I analyzed has 20 columns. Some of which are: (1) OrderNumber (2) QuntityOrdered (3) Price (4) Orderlinenumber (5) Sales , etc. I downloaded it from https://www.kaggle.com/datasets.

The dataset, as the name implies, contains sales data (amount, quantity, prices, etc). The records is about 2,748 but I extracted some of the records and then analyzed it. On close observation, I asked some questions which were later answered after the data analysis. Some of ny questions are listed below:

1) What were the highest sales when the prices were the most expensive? 
2) When the price per each product was the least expensive (81.35), did sales rise or fall?
3) What were the scenarios that surronded the lowest sales (2333.12)?



My purpose for writing this data analysis project is to be able to demonstrate the knowledge I had acquired during my study on Data analysis.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

Questions
1) What were the highest sales when the prices were the most expensive? 
2) When the price per each product was the least expensive (81.35), did sales rise or fall?
3) What were the scenarios that surronded the lowest sales (2333.12)?

Answers
1) The two highest sales (5512.32 and 4708.44) were realized when the prices were the most expensive (114.84). 
2) When the price per each product was the least expensive (81.35), the sales (2765.9) was not at the best figure and it was not also at the lowest count. One would expect higher sales when prices fall.
3) The lowest sales (2333.12) was realized when the price per product was the 3rd most expensive (101.44) out of the available prices.

# Development Environment

The IDE (Integrated development environment) is Visual studio.

The programming language I used for the data analysis is Python. The Numpy, Pandas and Matplotlib libraries/modules were of great significance.

# Useful Websites

* [Kaggle](https://www.kaggle.com/)
* [Data Science - Wikipedia](https://en.wikipedia.org/wiki/Data_science)
* [Overview of Pandas](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Numpy Cheat Sheet](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=152984014934&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=698229375028&utm_targetid=dsa-2219652735736&utm_loc_interest_ms=&utm_loc_physical_ms=9073716&utm_content=DSA~blog~Python&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-may24&gad_source=1&gclid=CjwKCAjwo6GyBhBwEiwAzQTmc_FOKLH1Mpi4lJsbEfGbvzwK_DjoIT7ST7MGP4wqv845UjnJzzaFUBoCEb0QAvD_BwE)

# Future Work

* I wish to analyze the whole data
* I wish to use R progreamming language for the analysis
