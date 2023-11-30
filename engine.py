## BibleEngine

import os
import re
import collections 

# The base directory of this module (to help locate the bibletext files)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Puncuation that will be removed from the text
PUNCUATION = [
    ',', ';', ':', '.', '*', '?', '!', '-', '+',
    '&', '"', '[', ']', '(', ')', '_', '{', '}'
    ]

# Generate a list of numbers strings
NUMBERS = [
    str(i) for i in range(1, 250)
    ]

# List of books in the Bible
BIBLEBOOKS_LIST = [
    'Genesis',
    'Exodus',
    'Leviticus',
    'Numbers',
    'Deuteronomy',
    'Joshua',
    'Judges',
    'Ruth',
    '1 Samuel',
    '2 Samuel',
    '1 Kings',
    '2 Kings',
    '1 Chronicles',
    '2 Chronicles',
    'Ezra',
    'Nehemiah',
    'Esther',
    'Job',
    'Psalms',
    'Proverbs',
    'Ecclesiastes',
    'Song Of Solomon',
    'Isaiah',
    'Jeremiah',
    'Lamentations',
    'Ezekiel',
    'Daniel',
    'Hosea',
    'Joel',
    'Amos',
    'Obadiah',
    'Jonah',
    'Micah',
    'Nahum',
    'Habakkuk',
    'Zephaniah',
    'Haggai',
    'Zechariah',
    'Malachi',
    'Matthew',
    'Mark',
    'Luke',
    'John',
    'Acts',
    'Romans',
    '1 Corinthians',
    '2 Corinthians',
    'Galatians',
    'Ephesians',
    'Philippians',
    'Colossians',
    '1 Thessalonians',
    '2 Thessalonians',
    '1 Timothy',
    '2 Timothy',
    'Titus',
    'Philemon',
    'Hebrews',
    'James',
    '1 Peter',
    '2 Peter',
    '1 John',
    '2 John',
    '3 John',
    'Jude',
    'Revelation'
    ]

# Map the books of the Bible to the names of the files
BIBLEBOOK_TO_FILENAME_DICT = {
    'Genesis': 'Genesis',
    'Exodus': 'Exodus',
    'Leviticus': 'Leviticus',
    'Numbers': 'Numbers',
    'Deuteronomy': 'Deuteronomy',
    'Joshua': 'Joshua',
    'Judges': 'Judges',
    'Ruth': 'Ruth',
    '1 Samuel': '1Samuel',
    '2 Samuel': '2Samuel',
    '1 Kings': '1Kings',
    '2 Kings': '2Kings',
    '1 Chronicles': '1Chronicles',
    '2 Chronicles': '2Chronicles',
    'Ezra': 'Ezra',
    'Nehemiah': 'Nehemiah',
    'Esther': 'Esther',
    'Job': 'Job',
    'Psalms': 'Psalms',
    'Proverbs': 'Proverbs',
    'Ecclesiastes': 'Ecclesiastes',
    'Song Of Solomon': 'SongOfSolomon',
    'Isaiah': 'Isaiah',
    'Jeremiah': 'Jeremiah',
    'Lamentations': 'Lamentations',
    'Ezekiel': 'Ezekiel',
    'Daniel': 'Daniel',
    'Hosea': 'Hosea',
    'Joel': 'Joel',
    'Amos': 'Amos',
    'Obadiah': 'Obadiah',
    'Jonah': 'Jonah',
    'Micah': 'Micah',
    'Nahum': 'Nahum',
    'Habakkuk': 'Habakkuk',
    'Zephaniah': 'Zephaniah',
    'Haggai': 'Haggai',
    'Zechariah': 'Zechariah',
    'Malachi': 'Malachi',
    'Matthew': 'Matthew',
    'Mark': 'Mark',
    'Luke': 'Luke',
    'John': 'John',
    'Acts': 'Acts',
    'Romans': 'Romans',
    '1 Corinthians': '1Corinthians',
    '2 Corinthians': '2Corinthians',
    'Galatians': 'Galatians',
    'Ephesians': 'Ephesians',
    'Philippians': 'Philippians',
    'Colossians': 'Colossians',
    '1 Thessalonians': '1Thessalonians',
    '2 Thessalonians': '2Thessalonians',
    '1 Timothy': '1Timothy',
    '2 Timothy': '2Timothy',
    'Titus': 'Titus',
    'Philemon': 'Philemon',
    'Hebrews': 'Hebrews',
    'James': 'James',
    '1 Peter': '1Peter',
    '2 Peter': '2Peter',
    '1 John': '1John',
    '2 John': '2John',
    '3 John': '3John',
    'Jude': 'Jude',
    'Revelation': 'Revelation'
    }



class Cache(collections.deque):
    """ A thin wrapper around deque. """
    def __init__(self):
        # Create the deque with a set allowed max size
        collections.deque.__init__(self, iterable=[], maxlen=10)

    def save_cache_file(self):
        with open('bibleengine.cache', 'a') as file:
            file.write('djndknddnnddnd')
            file.close()


    def cache_append(self, bookname, chapter, fromverse, toverse, text):
        """ Appends text to the cache. """
        text_dict = {
            "book": bookname,
            "chapter": chapter,
            "fromverse": fromverse,
            "toverse": toverse,
            "text": text
            }
        print('Cached: ', text_dict)
        self.append(text_dict)


    def cache_maxsize(self):
        """ Gets the maximum size of the cache. """
        return 10

    def cache_size(self):
        """ Gets the current size of the cache. """
        return len(self)

    def cache_isfull(self):
        """ Checks whether the cache is full. """
        return len(self) == 10

    def cache_isempty(self):
        """ Checks whether the cache is empty. """
        return len(self) == 1







class WordEngine(object):
    def __init__(self, should_cache=True):
        self.should_cache = should_cache
        self.cache = Cache()

    def dump_cache(self):
        self.cache.save_cache_file()

    @property
    def should_cache_text(self):
        return self.should_cache

    @property
    def get_bible_books(self):
        """ Returns a list of the books of the Bible. """
        return BIBLEBOOKS_LIST

    def get_verses_text(self, bookname, chapter, fromverse, toverse):
        """ Returns a string of the verses specified.
        =================================================
        bookname: The name of the book of the Bible as a string (e.g "the book's name")
        chapter: The chapter of the book of the Bible you want to memorize (filename)
        fromverse: Verse number (int, NOT str) to start the range of text to compare
        toverse: Verse number (int, NOT str) to end the range of text to compare
        """
        bookfile = self.load_bible_file(bookname)
        text = self.get_rangeofverses_text(bookfile, chapter, fromverse, toverse)

        # Here is the first cached text
        if self.should_cache_text:
            # bookname, chapter, fromverse, toverse, text
            self.cache.cache_append(bookname, chapter, fromverse, toverse, text)

        return text


        


    def clean_text(self, text, spaces=True):
        """ Cleans the input text of any puncuation and optionally, of any spaces.
        Returns a string of the text.
        ====================================
        text: The text which is to be cleaned
        spaces: Whether or not to keep the spaces. 
        """
        ## Append the letters in the text to a list
        text_list = []
        for word in text:
            for letter in word:
                ## If the text includes puncuation, remove it
                if letter in PUNCUATION:
                    del letter

                ## If the text includes numbers, remove them
                elif letter in NUMBERS:
                    del letter

                ## If the character is a "\n", append a space to the list
                elif letter in ['\n']:
                    text_list.append('')

                ## Append the character to the list
                else:
                    text_list.append(letter)

        ## Build a string from the text list
        text_string = ""
        for letter in text_list:
            text = (text_string + letter)
            text_string = text

        ## If the spaces are to be kept
        if spaces == True:
            return text_string

        ## If the spaces are to be removed
        if spaces == False:
            ## Take out all the spaces in the text
            text = re.findall(r'\S', text_string)

            ## Rebuild the text into a string
            text_string = ""
            for letter in text:
                text = (text_string + letter)
                text_string = text
                
            return text_string
        
    
    def check_text(self, input_text, correct_text):
        """ Checks the input text against the correct text to see if they match
        and returns either True or False.
        ====================================
        input_text: The text which is to be compared to the correct text
        correct_text: The "correct" text to compare the "input" text to ("the standard")
        """
        ## Make both texts lowercase
        input_text = (input_text.lower())
        correct_text = (correct_text.lower())

        ## Remove puncuation the text
        i_text = self.clean_text(input_text, spaces=False)
        c_text = self.clean_text(correct_text, spaces=False)

        #print(i_text)
        #print(c_text)
        
        ## If both texts are the same
        if i_text == c_text:
            return True

        ## If both texts are not the same
        else:
            return False


    def get_chapter_text(self, text, chapter):
        """ Returns a string of the chapter.
        ====================================
        text: The (book) text from either a string, .txt or .bible file
        chapter: Chapter of the text to return
        """
        ## Define the start and end points of the chapter
        chapter_start = text.find(('CHAPTER {}'.format(chapter)))
        chapter_end = text.find(('CHAPTER {}'.format(chapter + 1)))

        ## Slice the text to get only the chapter text
        chapter_text = (text[chapter_start:chapter_end])

        return chapter_text


    def get_verse_text(self, text, chapter, verse):
        """ Returns a string of the verse.
        ====================================
        text: The (book) text from either a string, .txt or .bible file
        chapter: Chapter of the verse text to return
        verse: The verse to return from the given text and chapter
        """
        ## Get the chapter text
        input_text = self.get_chapter_text(text, chapter)

        ## Break the chapter text into verses
        txt = re.split("\n+", input_text)
        verse_text = txt[verse]

        return verse_text


    def get_rangeofverses_text(self, text, chapter, fromverse, toverse):
        """ Returns a string of the range of verses.
        ===============================================
        text: The (book) text from either a string, .txt or .bible file
        chapter: Chapter of the verses text to return
        fromverse: Verse number (int, NOT str) to start the range of text to return
        toverse: Verse number (int, NOT str) to end the range of text to return
        """
        ## Get the chapter text
        input_text = self.get_chapter_text(text, chapter)

        ## Define the start and end points of the range of verses
        section_start = input_text.find(('{}'.format(fromverse)))
        section_end = input_text.find(('{}'.format(toverse + 1)))

        ## Slice the text to get only the range of verses' text
        range_of_verses_text = (input_text[section_start:section_end])

        return range_of_verses_text


    def load_bible_file(self, bookname):
        """ Opens and reads the input file. The input can only be a string of the path to
        the file and the book's name (not with the extension). This makes it simpler to
        open the desired book without having to put the ext. multiple times.
        ======================================================================
        bookname: The name of the book of the Bible as a string (e.g "the book's name")
        """

        biblebookname = BIBLEBOOK_TO_FILENAME_DICT[bookname]
        path = os.path.join(BASE_DIR, 'BibleEngine')
        bookname = ('{}/bibletexts/{}'.format(path, biblebookname))
        book = open('{}.txt'.format(bookname), 'r').read()
        return book


    def compare_verses(self, filename, input_text, chapter, fromverse, toverse):
        """ This compares the input text to the correct bible text from the
        module's library. It returns True if the text matches the correct text
        and False if it is incorrect.
        =================================================
        filename: The name of the book of the Bible as a string (e.g "the book's name")
        input_text: The user's text to be compared to the correct text of the Bible
        chapter: The chapter of the book of the Bible you want to memorize (filename)
        fromverse: Verse number (int, NOT str) to start the range of text to compare
        toverse: Verse number (int, NOT str) to end the range of text to compare
        """
        ## Load the given book of the Bible
        bookfile = self.load_bible_file(filename)

        ## Get the correct text
        correct_text = self.get_rangeofverses_text(bookfile, chapter, fromverse, toverse)

        ## Compare the texts
        result = self.check_text(input_text, correct_text)

        return result

