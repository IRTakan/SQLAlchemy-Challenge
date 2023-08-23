# SQLAlchemy-Challenge

The SQLAlchemy challenge involved planning a vacation to Honolulu, Hawaii and runnnig a climate analysis about the area. I had to 
perform these tasks.

--Part 1: Analyze and Explore the Climate Data--

In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. 
Specifically,  udse SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, completed the following steps:

- Precipitation Analysis
I found the most recent date in the dataset. Using that date, I got the previous 12 months of precipitation data by
querying the previous 12 months of data. Then created a plot the results by using the DataFrame plot method and
used Pandas to print the summary statistics for the precipitation data.

- Station Analysis
For this analysis I designed a query to calculate the total number of stations in the dataset and also find the most-active
stations (that is, the stations that have the most rows). The list of stations and observation counts are also in descending order.

Then I had to design a query to get the previous 12 months of temperature observation (TOBS) data. Which involved filtering
by the station that has the greatest number of observations. Query the previous 12 months of TOBS data for that station, and then 
plot the results as a histogram with bins=12.

