# levenshtein calculation

This repo calculates uses the levenshtein distance to calculate the distance between
strings. 

## Data

In this specific case a dog data set is used which can be found here

https://data.stadt-zuerich.ch/dataset/sid_stapo_hundenamen/download/20210103_hundenamen.csv

All entries in the column `HUNDENAME` will be used to calculate the distance to the name `Luca`. 


## Process description

This repo consists basically just of one function which calculates the levenshtein distances between a 
column of a pandas data frame and the name `Luca`. 

### Limitations

Due to the fact that there are no further task specifications all names in the data set will not be pre-processed. 
Typical steps could be 

* get rid of "" (e.g. in "Bo"" Bendy of Treegarden)
* convert all letters to lowercase (luca and Luca is the same name but in this case would have a distance of 1)
* ...


## Repo usage

If one wants to test the function this can be easily achieved by using the `Pipfile` and `Pipfile.lock`.