#!/usr/bin/env python
#
#
# Here we can implement a basic set of classes to handle creating
# recommendations from a given data set

from similaritymeasures import Similarity
import operator

class Recommender():
    """ What kind of recommender am I?  The existential question remains. """
    def __init__(self):
        self.measures = Similarity()
        self.dataset = {
            "Claudia" : [('Moana', 5), ('Frying Nemo', 6), ('Pocahontas', 8), ('Full Metal Racket', 5), ('LionKing', 9), ('Frozen', 8)] ,
            "Kenneth" : [('Moana', 7), ('Frying Nemo', 7), ('Spitoon', 8), ('ToyStory', 4), ('LionKing', 7), ('Frozen', 8)] ,
            "Joe" : [('Moana', 7), ('Simple Green', 5), ('Pocahontas', 5), ('ToyStory', 0), ('LionKing', 8), ('Frozen', 4)] ,
            "Janice" : [('Moana', 3), ('Frying Nemo', 7), ('Freaky Friday', 4), ('ToyStory', 9), ('LionKing', 9), ('Frozen', 7)] ,
            "Peter" : [('Moana', 5), ('Frying Nemo', 8), ('Pocahontas', 8), ('Date Night', 8), ('LionKing', 10), ('Frozen', 9)] ,
            "Bob" : [('Moana', 7), ('Frying Nemo', 5), ('Pocahontas', 5), ('Titanic', 3), ('LionKing', 8), ('Frozen', 8)] ,
         }


    def get_suggestions(self, k, username):
        if not reviews_for(username):
            print "Please add an initial rating set for user!"
        distance_array = generate_distance_array_for(username)
        most_similar_reviewer = get_most_similar_from(distance_array)
        top_k_suggerstions = find_suggestions_using(most_similar_reviewer)
        return top_k_suggerstions


    def add_user_ratings(self, username, ratings):
        self.dataset[username] = ratings


    def common_titles(self, movie_list1, movie_list2):
      titles1 = set(dict(movie_list1).keys())
      titles2 = set(dict(movie_list2).keys())
      common_titles = titles1.intersection(titles2)
      return common_titles


    def values_for(self, rating_list):
      return set(dict(rating_list).values())


    def generate_common_ratings(self, movie_list, titles):
        return [m for m in movie_list if m[0] in titles]


    def movies_in_common(self, movie_list1, movie_list2):
        common_titles = self.common_titles(movie_list1, movie_list2)
        common_ratings1 = self.generate_common_ratings(movie_list1, common_titles)
        common_ratings2 = self.generate_common_ratings(movie_list2, common_titles)
        return (sorted(common_ratings1), sorted(common_ratings2))


    def build_distance_array_for(self, username, scores=None):
        matches = {}
        if not scores:
          scores = self.dataset.get(username)
        print "Scores: %s" % scores
        current_dataset = self.dataset
        del(current_dataset[username])

        for reviewer in current_dataset:
          user_common_movies, reviewer_common_movies = self.movies_in_common(scores, current_dataset[reviewer])
          matches[reviewer] = self.measures.euclidean_distance(
                                            self.values_for(user_common_movies),
                                            self.values_for(reviewer_common_movies))

        sorted_matches = sorted(matches.items(), key=operator.itemgetter(1))
        return sorted_matches

    def distance_matrix(self):
        distance_matrix = {}
        for reviewer in self.dataset:
          distance_matrix[reviewer] = self.make_me_a_match(self.dataset[reviewer])
        return distance_matrix
