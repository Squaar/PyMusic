import winsound
import time

class SongPlayer:

	lengths = {
		'16': 125,
		'8':  250,
		'4':  500,
		'2':  1000,
		'1':  2000
	}

	_steps = {
		'a': 9,
		'b': 11,
		'c': 0,
		'd': 2,
		'e': 4,
		'f': 5,
		'g': 7
	}

	_magic_number = 2**(1/12)
	_base_frequency = 261.626 # middle C
	_whole_note_length = 2000

	def play(self, song):
		for note, length  in zip(song.notes.split(), song.lengths.split()):
			frequency = self._calculate_frequency(note)
			miliseconds = self._calculate_miliseconds(length)
			winsound.Beep(frequency, miliseconds)

	def _calculate_frequency(self, note):
		if note.strip('+-#b').lower() == 'R': return None
		steps = self._steps[note.strip('+-#b').lower()]
		if '-' in note:
			n = note.count('-')
			steps -= 12 * n
		elif '+' in note:
			n = note.count('+')
			steps += 12 * n
		if 'b' in note:
			steps -= note.count('b')
		if '#' in note:
			steps += note.count('#')
		return int(self._base_frequency * (self._magic_number**steps))

	def _calculate_miliseconds(self, length):
		if '.' in length:
			return int(2000 / int((int(length.strip('.'))<<int(1)) + int(length.strip('.'))/2))
		return int(self._whole_note_length / int(length))

	def morse(s):
		for i in s:
			if i == '.':
				winsound.Beep(2000, 100)
			elif i == '-':
				winsound.Beep(2000, 400)
			else:
				pass
			time.sleep(.01)

class Song:

	def __init__(self, notes, lengths):
		self.notes = notes
		self.lengths = lengths

star_wars = Song(
	'D D D G D+ C+ B A G+ D+ C+ B A G+ D+ C+ B C+ A',
	'8 8 8 2 2  8  8 8 2  4  8  8 8 2  4  8  8 8  2'
)

elder_scrolls = Song(
	'C D Eb Eb F G G Bb F  G  F  Eb D C C D Eb Eb F G G Bb C+ Bb D+ C+ C+ D+ Eb+ D+ C+ Bb Ab G F  Eb G F Eb D C',
	'8 8 2  8  8 2 8 8  2. 16 16 8  8 4 8 8 2  8  8 2 8 8  2  8. 16 2  8. 16 4   4  4  4  4  4 2. 8  8 2 8  8 2'
)

scale = Song(
	'C D E F G A B C+',
	'4 '*8
)

chromatic = Song(
	'C C# D Eb E F F# G Ab A Bb B C+',
	'4 '*13
)

# SongPlayer().play(star_wars)
# SongPlayer().play(elder_scrolls)
# SongPlayer().play(scale)
# SongPlayer().play(chromatic)
# morse('...---...-.-.')