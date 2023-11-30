## Example

from BibleEngine.engine import Memorize, WordEngine

input = """
paul, a servant of yahushua christ called to be an apostle separated unto the gospel of
elohim which he had promised afore by his prophets in the holy Scriptures concerning his
son Yahushua Christ our master which was made of the seed of david according to the flesh
"""

example1 = WordEngine.clean_text(input, spaces=True)
print(example1)

example2 = Memorize.compare("Romans", input, 1, 1, 3)
print(example2)

