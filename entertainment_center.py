import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

donnie_brasco = media.Movie("Donnie Brasco",
                            "Joseph Pistone (Johnny Depp) is an FBI agent who has infiltrated one of\
                             the major New York Mafia families and is living\
                             under the name Donnie Brasco",
                            "https://upload.wikimedia.org/wikipedia/en/b/bb/Donnie_brasco_ver2.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ilJ_ROLClZQ")

casino = media.Movie("Casino",
                     "Casino is a 1995 American epic crime drama film directed by Martin\
                      Scorsese and starring Robert De Niro, Joe Pesci,\
                      and Sharon Stone.It is based on the non-fiction\
                      book Casino: Love and Honor in Las Vegas",
                     "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=EJXDMwGWhoA")

goodfellas = media.Movie("Goodfellas",
                         "Goodfellas (stylized as GoodFellas) is a 1990 American crime film\
                          directed by Martin Scorsese. It is an adaptation\
                          of the 1986 non-fiction book Wiseguy by Nicholas\
                          Pileggi",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

once_upon_a_time_in_merica = media.Movie("Once Upon a Time in America",
                                         "Once Upon a Time in America is a 1984 Italian-American epic crime\
                                          drama film co-written and directed by Italian\
                                          filmmaker Sergio Leone and starring Robert De\
                                          Niro and James Woods",
                                         "https://upload.wikimedia.org/wikipedia/en/d/d8/Once_Upon_A_Time_In_America1.jpg",  # NOQA
                                         "https://www.youtube.com/watch?v=LcpCRyNo8T8")

king_of_new_york = media.Movie("King of New York",
                               "King of New York is a 1990 Italian-American crime thriller film,\
                                starring Christopher Walken, Laurence Fishburne, \
                                David Caruso, Wesley Snipes, Victor Argo, and \
                                Giancarlo Esposito",
                               "https://upload.wikimedia.org/wikipedia/en/3/36/King_of_new_york_ver1.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=z4bprq-BYi0")

a_bronx_tale = media.Movie("A Bronx Tale",
                           "A Bronx Tale is a 1993 American crime drama film set in the Bronx\
                            during the turbulent era of the 1960s. It was the\
                            directorial debut of Robert De Niro that follows \
                            a young Italian-American teenager in The Bronx, \
                            New York as his path in life is guided by two \
                            father figures, played by De Niro as his \
                            biological father and Chazz Palminteri as \
                            a local mafia boss. It was written by \
                            Palminteri, based partially upon his childhood",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/A_Bronx_Tale.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=z50PjmZYS4A")


# This function call opens a page of movies generated
# from the movies input, a list of movies instances.
movies = [toy_story, avatar, donnie_brasco, casino, goodfellas,
          once_upon_a_time_in_merica, king_of_new_york, a_bronx_tale]
fresh_tomatoes.open_movies_page(movies)

