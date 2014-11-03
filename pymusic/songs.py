from .music import Song

star_wars = Song(
	'D D D G D+ C+ B A G+ D+ C+ B A G+ D+ C+ B C+ A',
	'8 8 8 2 2  8  8 8 2  4  8  8 8 2  4  8  8 8  2'
)

elder_scrolls = Song(
	'C D Eb Eb F G G Bb F  G   F   Eb D C C D Eb Eb F G G Bb C+ Bb D+ C+ C+ D+ Eb+ D+ C+ Bb Ab G F Eb G F Eb D C',
	'8 8 2  8  8 2 8 8  2  32. 32. 8  8 2 8 8 2  8  8 2 8 8  2  8. 16 2  8. 16 4   4  4  4  4  4 2 8  8 2 8  8 2.'
)

green_greens = Song(
	'C+ C+ E+ G+ C++ B+ A+ G+ E+ G+ F+ D+ E+ D+ E+ D+ C+ G  G  C+ C+ E+ G+ C++ B+ A+ G+ E+ G+ F+ D+ E+ D+ E+ D+ C+ C+ C+ D+ E+ R C+ D+ C+',
	'2. 8. 16 8  8   8   8 4  8. 16 4  8. 16 4  8. 16 2. 8. 16 2. 8. 16 8  8   8  8  4  8. 16 4  8. 16 4  8. 16 1  8. 16 8  8  8 8  8  8'
)

mario = Song(
	'E+ E+ E+ R  C+ E+ G+ R G R C+ G  R E R  A B  R  Bb A G E+ G+ A+ F+ G+ R  E+ C+ D+ B  R',
	'16 8  16 16 16 8  8  8 8 8 8. 16 8 8 16 8 16 16 16 8 8 8  8  8  16 16 16 8  16 16 16 8'
)

pokemon = Song(
	'G- B- D  F# G G  G  G  G G G F F F F F F G  B D+ C  F F+ E+ Eb+ D+',
	'16 16 16 16 4 4 16 16 4 4 4 64/3 64/3 64/3 64/3 64/3 64/3 4. 8 2  4. 8 4 32 32  1'
)

scale = Song(
	'C D E F G A B C+',
	'4 '*8
)

chromatic = Song(
	'C C# D Eb E F F# G Ab A Bb B C+',
	'4 '*13
)