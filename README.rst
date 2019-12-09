-Project Description
  We made a website based on Django and Sqlite3 to track the squirrels in Central park in NYC.
  
  The initial dataset, 2018 Central Park Squirrel Census, is imported from https://data.cityofnewyork.us/api/views/vfnxvebw/rows.csv. Note: We set ‘unique squirrel id’ as the primary key, however, it's actually not unique. In fact, one row of the dataset represents one specific sighting. When we   import data to the database, the sightings with a repeated ‘unique squirrel id’ will not be imported.
  
  The function of the application are listed as follows,
1) We could first have a direct view of 100 unique squirrels’ exact locations on the map. 
  Located at: /map
2) We can see all sighings listed in one page, including sighting’s information: Squirrel Id, Latitude and Longitude.
  Located at: /sightings 
3) Next to each sighting, there is a link to edit the sighting. Located at: /sightings/<unique-squirrel-id>
4) There’s a link at the top right of the ‘sighting’ page, which allows us to add a new sighting.
  The information that’s required to enter are: Latitude, Longitude, Unique Squirrel ID, Shift and Date; whereas the optional fields are: Age, Primary Fur Color, Location, Specific Location and Other Activities. The remaining fields are checkboxes.
  Located at: /sightings/add
5) We selected five attributes in the dataset and calculated a particular stats over all sightings for each attribute.
  Located at: /sightings/stats

-Group name and Section
  Project Group 32, Section 2
  
-Team member and UNIs
  UNIs: [tc3026, cz2576]
  
-Server link
  https://my-project-tc-256223.appspot.com/sightings/
