#!/usr/bin/env python
#
# Here we can implement a basic set of classes to handle creating
# recommendations from a given data set

from similaritymeasures import Similarity
import operator

class Recommender():
    """ What kind of recommender am I?  The existential question remains. """
    def __init__(self, dataset=None, my_picks=None):
        self.measures = Similarity()
        self.dataset = dataset
        self.my_picks = my_picks

    def make_me_a_match(self):
        matches = {}
        for reviewer in self.dataset:
          matches[reviewer] = self.measures.euclidean_distance(my_picks, reviewers[reviewer])

        sorted_matches = sorted(matches.items(), key=operator.itemgetter(1))
        return sorted_matches[0][0]
        

movies = [ 'Moana', 'Frying Nemo', 'Pocahontas', 'ToyStory', 'LionKing', 'Frozen' ]
reviewers = {
    "Janice" : [3, 7, 4, 9, 9, 7],
    "Bob" : [7, 5, 5, 3, 8, 8],
    "Joe" : [7,5,5,0,8,4],
    "Claudia" : [5,6,8,5,9,8],
    "Peter" : [5,8,8,8,10,9],
    "Kenneth" : [7,7,8,4,7,8]
}

my_picks = [5, 10, 3, 7, 9, 7]

matchmaker = Recommender(reviewers, my_picks)
favorite_reviewer = matchmaker.make_me_a_match()
print favorite_reviewer

