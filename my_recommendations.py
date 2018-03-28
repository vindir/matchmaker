#!/usr/bin/env python

from recommender import Recommender

# Define some test data to act as movies to use
movies = [ 'Moana', 'Frying Nemo', 'Pocahontas', 'ToyStory', 'LionKing', 'Frozen' ]
reviewers = {
    "Janice" : [3, 7, 4, 9, 9, 7],
    "Bob" : [7, 5, 5, 3, 8, 8],
    "Joe" : [7,5,5,0,8,4],
    "Claudia" : [5,6,8,5,9,8],
    "Peter" : [5,8,8,8,10,9],
    "Kenneth" : [7,7,8,4,7,8]
}

# Update test data to match contribution from Shae
reviewers_ng = {}
for reviewer in reviewers:
  movie_mashup = []
  for n,movie in enumerate(movies):
    movie_mashup.append((movies[n], reviewers[reviewer][n]))
  reviewers_ng[reviewer] = movie_mashup

my_picks = [5, 10, 3, 7, 9, 7]

matchmaker = Recommender(reviewers, my_picks)
favorite_reviewer = matchmaker.make_me_a_match()
print favorite_reviewer

import pprint

pprint.pprint(matchmaker.distance_matrix())
