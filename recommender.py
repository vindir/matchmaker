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

# assume input is two lists of tuples: [(title,score)]
def movies_in_common(movie_list1, movie_list2):
    movie_dict1 = dict(movie_list1)
    movie_dict2 = dict(movie_list2)
    titles1 = set(movie_dict1.keys())
    titles2 = set(movie_dict2.keys())
    common_titles = titles1.intersection(titles2)
    return common_titles # returns a set of titles

# assume input is two lists of tuples
def order_matched_titles_and_scores(movie_list1, movie_list2):
    common_titles = movies_in_common(movie_list1, movie_list2)
    common_movies1 = common(movie_list1, common_titles)
    common_movies2 = common(movie_list2, common_titles)
    return (sorted(common_movies1), sorted(common_movies2))

def common(movie_list, titles):
    return [m for m in movie_list if m[0] in titles]


m1 = [('Moana',1), ('Frying Nemo',0), ('Pocahontas',0)]
m2 = [('Moana',0), ('Frying Nemo',0), ('ToyStory',1)]

def check():
    assert order_matched_titles_and_scores(m1,m2) == ([('Frying Nemo',0),('Moana',1)], [('Frying Nemo',0), ('Moana',0)])
    return "Yup, it works or you would have seen a failed assertion"
