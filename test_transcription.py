'''
Classes that form the basis for syncopython
The rhythm string for each limb will be parsed and joined
to output to drumseq.py as I develop a backend.
'''
import re
import unittest
import io
import difflib
import pytest
from transcription import Transcription, RhythmString

class TestTranscription(unittest.TestCase):

    def setUp(self):
        self.t = Transcription()

    def complex_transcription(self):
        input_str = '''
        36 | 1 & ,    ,3 & ,     | Bassdrum
        38 |     ,2   ,    ,4    | Snare
        42 | 1e&a,2e&a,3e&a,4e&a | Closed HH
        '''

        self.t.feed(input_str)
        out_string = t.output_drumseq()

        expected_out = '''
        #  1...2...3...4...\n36 x.x.......x..x.. Bassdrum\n38 ....x..x.x.xx..x Snare\ \n
        42 xxxxx.x.xxxxx.xx Closed HH
        '''
        assert out_string.strip() == expected_out.strip()
        # Black box testing - only public use
 
    def test_simple_transcription(self):
        input_string = '''
        36 | 1&, ,e,e | Bassdrum
        '''.strip()

        t = Transcription(input_string)
        out_string = t.output_drumseq()
        expected_out = '''
        #  1...2...3...4...\n36 x.x......x...x..  Bassdrum
        '''
        print('input_string: ' + input_string)
        print('out_string: ' + out_string)
        self.assertEqual(expected_out.strip(), out_string.strip())
        # Black box testing - only public use
