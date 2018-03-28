# matchmaker
Recommender group project programmed mob-style over lunches at Pindrop

## Definitions:
movie_rating tuples: (movie_name, rating)
list of movie_rating tuples: [(movie_name, rating), (movie_name, rating), (movie_name, rating)]

## Data Structures:
Movie Watchers dict: { 'movie_watcher' : set(movie_rating tuples]
Item-Item Correlations: Generated at runtime.  Otherwise we'd build a matrix.

## Execution Pseudo Flows:

### Add a new user:
1. Call recommender.py and pass it a file/stream of user scores
2. recommender.py assumes input scores are pre-formatted as expected
3. Format user scores into a list of movie_rating tuples
4. Add user scores to movie watchers dict

### Calculate Distance Array for user:
1. for each watcher in all movie watchers:
 a. create set of common movie keys present in watcher list intersecting current user
 b. construct rating-only list for current user and watcher using only intersected set
 c. calculate euclidean distance between watcher and current user and add to distance array

### Find closest watcher to current user:
1. sort distance array
2. pop off lowest scoring watcher
3. return rating array for lowest scoring watcher

### Find movie suggestions for user:
1. accept argument k as maximum suggestions requested
2. accept argument randomize as boolean dictating randomization of returns
3. validate distance array for user is generated and define as set A
4. find closest watcher to user
5. retrieve closest watcher set as B
6. find Ac ∩ B (complement of user set to watcher set)
7. sort Ac by rating
8. return top k Movies as suggestions
