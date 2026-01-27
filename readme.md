## Block Planting Dataset (https://data.cityofnewyork.us/Environment/Block-Planting/h426-x5gi/about_data)
##edstem workspace ()

Why did I choose this dataset?
I chose it because I was thinking of some of the events my department and the office of sustainability hosts sometimes.
As an environmental studies major, understanding how the urban jungle of NYC tries to incorporate nature is super interesting.
I also had the opportunity to visit some greenspaces and understand the history of protests behind that in NYC.


Three Data Questions
—————
# 1. How many blocks cannot be planted?
  cannot_plant = sum(1 for row in blocks if row["DoNotPlant"] == "1")
  print("Cannot be planted:", cannot_plant)

"cannot be planted" maps onto the column titled "DoNotPlant", which is kept using numbers to represent yes or no


# 2. How many blocks have been surveyed?
  surveyed = sum(1 for row in blocks if row["BlkSurv"] == "1")
  print("Surveyed:", surveyed)

BlkSurv similarly maps onto this question, except it counts whenever a block has "1" in this column, meaning that it has been surveyed.


# 3. How many blocks were planted in Spring 2009?
  spring09_planted = sum(
      1 for row in blocks
      if row["PlntSeas"] == "Spring09" and row["BlkPlnt"] == "1"
  )
  print("Planted in Spring09:", spring09_planted)

In the PlntSeas column, the date is mapped as "SeasonYear", so all that the code needed to do was count everytime there was an instance of Spring09.


# What the data cannot answer
The data cannot answer why exactly a block is plantable or not. We know the yes/no, but not the why.
It would probably either need a specific list of statuses to be selected from. In addition, we don't know if blocks can be re-surveyed or not:
this also goes back to the unknown of "why a block is unplantable".
