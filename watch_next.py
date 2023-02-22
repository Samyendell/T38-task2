
import spacy
nlp = spacy.load('en_core_web_md')


def movie_recommendation():
    '''This funciton recommends a moive to watch based on the similarity of the given movie to a list of movies
    '''
    
    movie_to_compare = nlp('''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
        the I lluminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
        Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.''')
    
    movie_sim = []
    
    # load and store data from text file and alter it to a list with the movie name as a seperate index
    with open("movies.txt", "r") as movie_file:
        movie_file = movie_file.readlines()
        movie_file = "".join(movie_file)
        movie_file = movie_file.replace("\n", "*").replace(":", "*").split("*")
    
    # iterate through all the descriptions 
        for i in range(len(movie_file)):
            if i % 2 != 0:

                similarity = nlp(movie_file[i]).similarity(movie_to_compare)
                movie_sim.append(similarity)

    # find the most similars index and print the movie name
    highest_sim = max(movie_sim)
    index_high = movie_sim.index(highest_sim) + 1
    movie_index = (index_high * 2) - 2

    print(f"You should watch this movie next: {movie_file[movie_index]}")
    

movie_recommendation()

