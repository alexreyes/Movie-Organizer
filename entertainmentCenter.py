import fresh_tomatoes
import media 

lion_king = media.Movie("The Lion King", 
    "A movie about lions",
    "http://massimages.mobi/wp-content/uploads/lion-king-cover-controversy-photograph-2.jpg", 
    "https://www.youtube.com/watch?v=4sj1MT05lAA")

spirited_away = media.Movie("Spirited Away",
    "A movie about a girl who discovers a secret place.",
    "http://www.nausicaa.net/miyazaki/sen/poster_images/USA_full.jpg",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk")

kingsman = media.Movie("Kingsman: Secret Service",
    "A parody spy movie",
    "http://fwooshflix.thefwoosh.com/files/2015/02/Kingsman-The-Secret-Service-poster.jpg",
    "https://www.youtube.com/watch?v=kl8F-8tR8to")

parks_and_rec = media.Movie("Parks and Recreation",
    "A mocumentary about the parks and rec office.",
    "http://images.moviepostershop.com/parks-and-recreation-tv-movie-poster-2009-1020482255.jpg",
    "https://www.youtube.com/watch?v=jcyH-qIPKMA")

rick_and_morty = media.Movie("Rick and Morty", 
    "A hilarious cartoon about a kid and his genius grandfather.",
    "https://image.tmdb.org/t/p/w1920/4LIf49No2uCJYJyaMykrVfXzIUn.jpg",
    "https://www.youtube.com/watch?v=90wG8ObCBE0")

silicon_valley = media.Movie("Silicon Valley", 
    "A hilarious parody of the tech capital of the world.",
    "http://oyster.ignimgs.com/wordpress/stg.ign.com/2015/03/427358_MKT_PA_SiliconValley_S2-KA-v12rev2-720x1066.jpg",
    "https://www.youtube.com/watch?v=63UNmod8zf0")

movies = [silicon_valley, rick_and_morty, kingsman, lion_king, spirited_away, parks_and_rec]

fresh_tomatoes.open_movies_page(movies)
