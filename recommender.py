#!/usr/bin/env python
#
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

    def make_me_a_match(self, scores=None):
        matches = {}
        if not scores:
          scores = self.my_picks
        for reviewer in self.dataset:
          #matches[reviewer] = self.measures.euclidean_distance(scores, reviewers[reviewer])
          matches[reviewer] = self.measures.euclidean_distance(scores, self.dataset[reviewer])

        sorted_matches = sorted(matches.items(), key=operator.itemgetter(1))
        #return sorted_matches[0][0]
        return sorted_matches

    def distance_matrix(self):
        distance_matrix = {}
        for reviewer in self.dataset:
          distance_matrix[reviewer] = self.make_me_a_match(self.dataset[reviewer])
        return distance_matrix

