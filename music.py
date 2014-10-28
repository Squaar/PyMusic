import winsound
import time

class Song:

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

	def __init__(self, notes, lengths, whole_note_length=2000):
		self.notes = notes
		self.lengths = lengths
		self.frequencies = []
		self.miliseconds = []
		self.whole_note_length = whole_note_length
		self.parse()

	def parse(self):
		for note, length  in zip(self.notes.split(), self.lengths.split()):
			self.frequencies.append(self._calculate_frequency(note.lower()))
			self.miliseconds.append(self._calculate_miliseconds(length))

	def play(self):
		for frequency, miliseconds in zip(self.frequencies, self.miliseconds):
			if not frequency: time.sleep(miliseconds)
			else: winsound.Beep(frequency, miliseconds)

	def _calculate_frequency(self, note):
		if note.strip('+-#b') == 'r': return None
		steps = self._steps[note.strip('+-#b')]
		steps -= 12 * note.count('-')
		steps += 12 * note.count('+')
		steps -= note.count('b')
		steps += note.count('#')
		return int(self._base_frequency * (self._magic_number**steps))

	def _calculate_miliseconds(self, length):
		i = int(length.strip('.'))
		if '.' in length:
			return int(self.whole_note_length /i*3/2))
		return int(self.whole_note_length / i)

	def morse(s):
		for i in s:
			if i == '.':
				winsound.Beep(2000, 100)
			elif i == '-':
				winsound.Beep(2000, 400)
			else:
				pass
			time.sleep(.01)

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

# star_wars.play()
# elder_scrolls.play()
# scale.play()
# chromatic.play()
# Song.morse('...---...-.-.')