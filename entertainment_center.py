# python3
import media
import fresh_tomatoes


# instantiate movies
mindhorn = media.Movie(
'Mindhorn',
'Former television actor finds himself by understanding " \
"that selfhood is a fiction',
'https://upload.wikimedia.org/wikipedia/en/c/c5/Mindhorn.png',  # NOQA
'https://www.youtube.com/watch?v=lA5njebTiZY')  # NOQA

psychoRaman = media.Movie('Pyscho Raman',
'This might be a question on the state monopoly on violence," \
" or just some Jungian shadow-self craziness',
'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Raman_Raghav_2.png/220px-Raman_Raghav_2.png',  # NOQA
'https://www.youtube.com/watch?v=wjGiRMca0xE')  # NOQA

wizardpeople = media.Movie('Wizard People, Dear Reader',
'It\'s arguable whether or not this is actually a movie." \
" A re-telling of some other movie maybe you\'ve seen before',
'https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Wizardpeople.jpg/220px-Wizardpeople.jpg',  # NOQA
'https://www.youtube.com/watch?v=sTPfMk34lz8')  # NOQA

blechtrommel = media.Movie('The Tin Drum',
'Nazi Germany also had its light-hearted moments. Or maybe not.',
'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NjEzNjU0N15BMl5BanBnXkFtZTcwOTI1OTUyMQ@@._V1_UY268_CR4,0,182,268_AL_.jpg',  # NOQA
'https://www.youtube.com/watch?v=2ewzWkFZOFk')  # NOQA


# place movies into list
movies = [mindhorn, psychoRaman, wizardpeople, blechtrommel]


# generates html based on movie list
fresh_tomatoes.open_movies_page(movies)
