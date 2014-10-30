import winsound
import time
from fractions import Fraction

class Song:

	_steps = {
		'A': 9,
		'B': 11,
		'C': 0,
		'D': 2,
		'E': 4,
		'F': 5,
		'G': 7
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
			self.frequencies.append(self._calculate_frequency(note))
			self.miliseconds.append(self._calculate_miliseconds(length))

	def play(self):
		for frequency, miliseconds in zip(self.frequencies, self.miliseconds):
			if not frequency: time.sleep(miliseconds/1000)
			else: winsound.Beep(frequency, miliseconds)
			# time.sleep(0.1)

	def _calculate_frequency(self, note):
		if note.strip('+-#b') == 'R': return None
		steps = self._steps[note.strip('+-#b')]
		steps -= 12 * note.count('-')
		steps += 12 * note.count('+')
		steps -= note.count('b')
		steps += note.count('#')
		return int(self._base_frequency * (self._magic_number**steps))

	def _calculate_miliseconds(self, length):
		i = float(Fraction(length.strip('.')))
		if '.' in length:
			return int(self.whole_note_length /i*3/2)
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



