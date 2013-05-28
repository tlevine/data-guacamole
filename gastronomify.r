# simple guacamole
# http://www.theyummylife.com/guacamole
guacamole <- c(
  4,   # ripe medium-size avocados; Haas recommended, if available
  1/2, # teaspoon garlic powder
  1/2, # teaspoon kosher salt
  1/2, # teaspoon freshly ground black pepper
  # OPTIONAL ADDITIONS:
  1,   # tablespoon fresh lime juice
  1/4  # cup chopped cilantro
       # hot green chili (2 serranos or 2-3 jalapenos), finely diced
# 1/2, # small white onion, finely diced
# 1    # medium tomato, deseeded & chopped in 1/4" pieces
)

# https://data.cityofnewyork.us/Education/Math-Test-Results-2006-2012-District-All-Students/7yig-nj52?
if (!('math.tests' %in% ls())) {
  math.tests <- read.csv('http://data.cityofnewyork.us/api/views/7yig-nj52/rows.csv?accessType=DOWNLOAD')
}
math.tests <- math.tests[c('District', 'Grade', 'Year', 'Number.Tested', 'Mean.Scale.Score', 'Num.Level.1', 'Num.Level.2', 'Num.Level.3', 'Num.Level.4')]
math.tests <- subset(math.tests, Grade != 'All Grades')
