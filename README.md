# sqlalchemy challenge

For this module challenge, we were supposed to pretend we were going to vacation to hawaii and we were trying to see how the sea would impact the trip planning. 

Part 1: Analyze and Explore Climate Data

For this section, we were supposed to use two coding tools we have learned, Python and SQLAlchemy to do climate analysis on a climate database. This was supposed to work with a SQLite database which had the data. 
1. Connecting the database with a create_engine() and reflecting the tables with automap_base()
2. Establishing the session with the newly connected database 
3. Then the next step was performing the precipitation analysis  
    a)finding the most recent date 
    b)retrieving the last 12 months of data 
    c)taking the data into a pandas data frame to plot the data using Matplotlib 
    d) printing a summary of the precipitation data
4. The last step was performing a station analysis 
    a)finding the number of stations in the dataset 
    b)finding the most active station and the associated temperature stats 
    c) Querrying the 12 months of temperature oberservation for the active sation 
    d) Plotting the temperature oberservation data 

Part 2: Designing the climate app 

For this section, we were creating a Flask API based off the previous python code. 
We had to create the Flask app and define its routes 
1. Displaying the avidable routes 
2. /api/v1.0/precipitation: It gets the last 12 months of precipitation data as JSON
3. /api/v1.0/stations: This returns the JSON list of stations 
4.  api/v1.0/tobs: This gets temperature observations for the most active station's data for last year
5.  /api/v1.0/<start> and /api/v1.0/<start>/<end>: This returns the JSON lists of temperature statistics for a specified range of dates.
6. Using the jsonify function to convert the data into valid JSON feedback 

For the project, I attended one study session on Wednesday, August 23th at 6:00 with Steve Thomas where I got help with multiple problems with my Flask App. I also used the module directions to help me do the challenge.




