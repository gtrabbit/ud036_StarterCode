#python3
import webbrowser

#defines the movie class
class Movie():
	def __init__(self, movie_title, movie_synopsis, poster, trailer_URL):
		self.title = movie_title
		self.storyline = movie_synopsis
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer_URL
	#obvious, but this is called when posters are clicked on website to
	#open the youtube link
	def show_trailer():
		webbrowser.open(self.trailer_youtube_url)


