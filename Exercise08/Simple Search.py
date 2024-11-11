#Making a list of strings containing various names
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Writting the name which will be searched.
Search_name= "Sam"

#Using if, eles statements to Search the name in the list
if Search_name in Names:
 print("{Search_name} is on the list")
else:
  print("{Search_name} is not on the list")