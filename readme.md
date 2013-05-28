Data Guacamole
=====
This is a gastronomification of 
[New York City math tests scores](https://data.cityofnewyork.us/Education/Math-Test-Results-2006-2012-District-All-Students/7yig-nj52),
based on [this guacamole recipe](http://www.theyummylife.com/guacamole).

Install `R` and then `plyr` and `reshape2`.

    R -e 'install.packages(c("plyr", "reshape2"))'

Then run the recipe-generator like so.

    ./gastronomify.r

The results will go to [`data_guacamole.csv`](data_guacamole.csv).

The resulting table tells you, in order, how much of the different ingredients
to combine in the guacamole. Each ingredient represents the average test score
for a particular grade, and each recipe represents a particular year. The
ingredients and their corresponding grades are listed below.

* Ripe medium-size avocados; Haas recommended, if available (grade 3)
* Teaspoons of garlic powder (grade 4)
* Teaspoons of kosher salt (grade 5)
* Teaspoons of freshly ground black pepper (grade 6)
* Tablespoons of fresh lime juice (grade 7)
* Cups of chopped cilantro (grade 8)
