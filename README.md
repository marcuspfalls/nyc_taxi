# NYC Taxi Test

An exercise containing the code and results of the following 3 tasks:
* Data Exploration and Cleaning
* Data Summary 
* Model building 

## Data exploration and cleaning
clean_data.ipynb - Notebook containing the code of clean_data.py, with the code annotated with my justifications for each step. 

clean_data.py - Script that takes the downloaded .csv file as input, and outputs another .csv with two extra columns for duration and speed, and outliers and erroneous data removed. 

tlc_yellow_trips_2018_11_22_CLEAN.csv - Output of clean_data.py

## Data Summary 
data_summary.ipynb - Notebook containing each of the steps of the analysis, including all the code of the section. Includes a summary of the interpretation of the data at the end. 

make_loc_time_csvs.py - Script which sorts the data by time in hours and place, and with the number of trips in each. It produces two csvs, one with pickup times and one with dropoff times. 

pickup_timeplace.csv & dropoff_timeplace.csv - Outputs of make_loc_time_csvs.py

time_place_plotting.py - Takes the previously produced .csvs as input and produces a plot of subplots containing a map of New York with the number of rides in each zone for every hour. It does this for pickups and dropoffs. 

pickup_locs_hourly.png & dropoff_locs_hourly.py - outputs of time_place_plotting.py

## Model Building
model_building.ipynb - Notebook containing the code and plots for task 3. At the bottom is a written analysis of the data and a proposal for a model. 

tips_analysis.py - Script that reformats the data to analyse tips and produces scatterplots based on it. 

totalcost-tip.png & totalcost-ratio.png - Outputs of tips_analysis.py
