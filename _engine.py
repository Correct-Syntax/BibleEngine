## BibleEngine

import os
import re


PUNCUATION = [',', ';', ':', '.', '*', '?', '!', '-',
              '&', '"', '[', ']', '(', ')', '_', '{', '}'
              ]

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
           '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19', '20', '21', '22', '23', '24', '25',
           '26', '27', '28', '29', '30', '31', '32', '33',
           '34', '35', '36', '37', '38', '39', '40', '41',
           '42', '43', '44', '45', '46', '47', '48', '49',
           '50', '51', '52', '53', '54', '55', '56', '57',
           '58', '59', '60', '61', '62', '63', '64', '65',
           '66', '67', '68', '69', '70', '71', '72', '73',
           '74', '75', '76', '77', '78', '79', '80', '81',
           '82', '83', '84', '85', '86', '87', '88', '89',
           '90', '91', '92', '93', '94', '95', '96', '97',
           '98', '99', '100', '101', '102', '103', '104',
           '105', '106', '107', '108', '109', '110', '111',
           '112', '113', '114', '115', '116', '117', '118',
           '119', '120', '121', '122', '123', '124', '125',
           '126', '127', '128', '129', '130', '131', '132',
           '133', '134', '135', '136', '137', '138', '139',
           '140', '141', '142', '143', '144', '145', '146',
           '147', '148', '149', '150', '151', '152', '153',
           '154', '155', '156', '157', '158', '159', '160',
           '161', '162', '163', '164', '165', '166', '167',
           '168', '169', '170', '171', '172', '173', '174',
           '175', '176', '177', '178', '179', '180', '181',
           '182', '183', '184', '185', '186', '187', '188',
           '189', '190', '191', '192', '193', '194', '195',
           '196', '197', '198', '199', '200', '201', '202',
           '203', '204', '205', '206', '207', '208', '209',
           '210', '211', '212', '213', '214', '215', '216',
           '217', '218', '219', '220', '221', '222', '223',
           '224', '225', '226', '227', '228', '229', '230',
           '231', '232', '233', '234', '235', '236', '237',
           '238', '239', '240', '241', '242', '243', '244',
           '245', '246', '247', '248', '249', '250'
           ]


class WordEngine:

    def books():
        """ Returns a list of the books of the Bible. """
        books = [
            'Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua',
            'Judges', 'Ruth','I Samuel','II Samuel','I Kings','II Kings',
            'I Chronicles', 'II Chronicles', 'Ezra','Nehemiah','Esther',
            'Job','Psalms','Proverbs', 'Ecclesiastes','Song of Solomon',
            'Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea',
            'Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk',
            'Zephaniah','Haggai','Zechariah','Malachi',
            'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', 'I Corinthians',
            'II Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians',
            'I Thessalonians', 'II Thessalonians', 'I Timothy', 'II Timothy',
            'Titus', 'Philemon', 'Hebrews', 'James', 'I Peter', 'II Peter',
            'I John', 'II John', 'III John', 'Jude', 'Revelation'
            ]
        
        return books


    def clean_text(text, spaces=True):
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
        
    
    def check_text(input_text, correct_text):
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
        i_text = WordEngine.clean_text(input_text, spaces=False)
        c_text = WordEngine.clean_text(correct_text, spaces=False)

        #print(i_text)
        #print(c_text)
        
        ## If both texts are the same
        if i_text  == c_text:
            return True

        ## If both texts are not the same
        else:
            return False


    def get_chapter_text(text, chapter):
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


    def get_verse_text(text, chapter, verse):
        """ Returns a string of the verse.
        ====================================
        text: The (book) text from either a string, .txt or .bible file
        chapter: Chapter of the verse text to return
        verse: The verse to return from the given text and chapter
        """
        ## Get the chapter text
        input_text = WordEngine.get_chapter_text(text, chapter)

        ## Break the chapter text into verses
        txt = re.split("\n+", input_text)
        verse_text = txt[verse]

        return verse_text


    def get_rangeofverses_text(text, chapter, fromverse, toverse):
        """ Returns a string of the range of verses.
        ===============================================
        text: The (book) text from either a string, .txt or .bible file
        chapter: Chapter of the verses text to return
        fromverse: Verse number (int, NOT str) to start the range of text to return
        toverse: Verse number (int, NOT str) to end the range of text to return
        """
        ## Get the chapter text
        input_text = WordEngine.get_chapter_text(text, chapter)

        ## Define the start and end points of the range of verses
        section_start = input_text.find(('{}'.format(fromverse)))
        section_end = input_text.find(('{}'.format(toverse + 1)))

        ## Slice the text to get only the range of verses' text
        range_of_verses_text = (input_text[section_start:section_end])

        return range_of_verses_text


    def load_bible_file(bookname, py_version='34'):
        """ Opens and reads the input file. The input can only be a string of the path to
        the file and the book's name (not with the extension). This makes it simpler to
        open the desired book without having to put the ext. multiple times.
        ======================================================================
        bookname: The name of the book of the Bible as a string (e.g "the book's name")
        py_version: The user's currently installed version of Python (e.g v3.4 = '34')
        """
        ## Get the path
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        #os.path.join(BASE_DIR, 'BibleEngine')
        bookname = ('''{}/bibletexts/{}'''.format(os.path.join(BASE_DIR, 'BibleEngine'), bookname))

        try:
            ## If the file is .bible
            book = open("{}.bible".format(bookname), 'r').read()

        except:
            ## If the file is NOT .bible, it will fallback on this
            book = open("{}.txt".format(bookname), 'r').read()

        return book


class Memorize:
    
    def compare(filename, input_text, chapter, fromverse, toverse, py_version='34'):
        """ This is the main Memorization function. It compares the input text to the
        correct bible text from the module's library. It returns True if the text matches
        the correct text and False if it is incorrect.
        =================================================
        filename: The name of the book of the Bible as a string (e.g "the book's name")
        input_text: The user's text to be compared to the correct text of the Bible
        chapter: The chapter of the book of the Bible you want to memorize (filename)
        fromverse: Verse number (int, NOT str) to start the range of text to compare
        toverse: Verse number (int, NOT str) to end the range of text to compare
        py_version: The user's currently installed version of Python (e.g v3.4 = '34')
        """
        ## Load the given book of the Bible
        bookfile = WordEngine.load_bible_file(filename, py_version=py_version)

        ## Get the correct text
        correct_text = WordEngine.get_rangeofverses_text(bookfile, chapter,
                                                         fromverse, toverse)

        ## Compare the texts
        result = WordEngine.check_text(input_text, correct_text)

        return result

