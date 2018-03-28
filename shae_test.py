# assume input is two lists of tuples: [(title,score)]
def movies_in_common(movie_list1, movie_list2):
    titles1 = set(dict(movie_list1).keys())
    titles2 = set(dict(movie_list2).keys())
    common_titles = titles1.intersection(titles2)
    return common_titles

# assume input is two lists of tuples
def order_matched_titles_and_scores(movie_list1, movie_list2):
    common_titles = movies_in_common(movie_list1, movie_list2)
    print "CommonTitles: %s" % common_titles
    common_movies1 = common(movie_list1, common_titles)
    print "CommonMovies1: %s" % common_movies1
    common_movies2 = common(movie_list2, common_titles)
    print "CommonMovies2: %s" % common_movies2
    return (sorted(common_movies1), sorted(common_movies2))

def common(movie_list, titles):
    return [m for m in movie_list if m[0] in titles]


m1 = [('Moana',1), ('Frying Nemo',0), ('Pocahontas',0)]
m2 = [('Moana',0), ('Frying Nemo',0), ('ToyStory',1)]

def check():
    assert order_matched_titles_and_scores(m1,m2) == ([('Frying Nemo',0),('Moana',1)], [('Frying Nemo',0), ('Moana',0)])
    return "Yup, it works or you would have seen a failed assertion"

check()
