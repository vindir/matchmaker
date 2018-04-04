# MatchMaker
This is a recommender engine group project programmed mob-style over lunches at
Pindrop. The lesson to learn from this code is the effectiveness and simplicity
of using euclidean distance to create a "collaborative filtering" style engine.

What you'll find in the Recommender class is a succint example of a
'collaborative filtering' style recommendation engine.  This is extremely basic
compared to a modern analytical recomender system and in a whole different
domain from machine learning based systems, but what is interesting is that the
results obtained here are only marginally worse than those we could obtain given
much more complex and involved methodologies.

To see the current code in action run `python ./my_recommendations.py`

## Definitions:
movie_rating tuples: (movie_name, rating)
list of movie_rating tuples: [(movie_name, rating), (movie_name, rating), (movie_name, rating)]

## Data Structures:

Data set containing all ratings of all movie watchers:
dataset = {
           "Claudia" : [('Moana', 5), ('Frying Nemo', 6),
           "Kenneth" : [('Moana', 7), ('Full Metal Racket', 5)
          }

### Item-Item Correlations:

These are our reviewer similarity coefficients. A single distance array is
generated as a list of distance evaluations between the user and all other
users.

Correlations are generated at runtime.  Otherwise we'd build a matrix
or possibly develop a kd-tree.

example = [('Kenneth', 5.830951894845301),
           ('Joe', 6.164414002968976),
           (Janice', 6.4031242374328485),
           ('Bob', 7.0),
           ('Claudia', 8.602325267042627),
           ('Peter', 10.392304845413264)
          ]

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
1. sort distance array and pop out 0 distance matches
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
