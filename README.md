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

<img src="https://github.com/IRTakan/SQLAlchemy-Challenge/blob/main/Images/precip.png?raw=true" width=500 height=400>

- Station Analysis
  
For this analysis I designed a query to calculate the total number of stations in the dataset and also find the most-active
stations (that is, the stations that have the most rows). The list of stations and observation counts are also in descending order.

Then I had to design a query to get the previous 12 months of temperature observation (TOBS) data. Which involved filtering
by the station that has the greatest number of observations. Query the previous 12 months of TOBS data for that station, and then 
plot the results as a histogram with bins=12 and close the session.

<img src="https://github.com/IRTakan/SQLAlchemy-Challenge/blob/main/Images/tobs.png?raw=true" width=500 height=400>

--Part 2: Design Your Climate App

After running the analysis I designed a Flask API based on the queries that you were developed. These are the routes:

--List all the available routes.

- /api/v1.0/precipitation

Converted the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
The returned the JSON representation of your dictionary.

- /api/v1.0/stations

Returned a JSON list of stations from the dataset.

- /api/v1.0/tobs

Queried the dates and temperature observations of the most-active station for the previous year of data. Then
return a JSON list of temperature observations for the previous year.

- /api/v1.0/<start> and /api/v1.0/<start>/<end>

Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculated TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

*Technologies used: Microsoft Visual Studio Code

For a specified start date and end date, calculated TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

