'''
Classes that form the basis for syncopython
The rhythm str for each limb will be parsed and joined
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

    def test_complex_transcription(self):
        input_str = ('36 | 1 & ,    ,3 & ,     | Bassdrum\n'
                     '38 |     ,2  a,    ,4e a | Snare\n'
                     '42 | 1e&a,2e&a,3e&a,4e&a | Closed HH')

        t = Transcription(input_str)        
        out_str = t.output_drumseq()

        expected_out = ('#  1...2...3...4...\n'
                        '36 x.x.....x.x.....  Bassdrum\n'
                        '38 ....x..x....xx.x  Snare\n'
                        '42 xxxxxxxxxxxxxxxx  Closed HH')

        assert out_str.strip() == expected_out.strip()
 
    def test_simple_transcription(self):
        input_str = '36 | 1 & , , e , e | Bassdrum'

                
        expected_out = ('#  1...2...3...4...\n'
                        '36 x.x......x...x..  Bassdrum')
        
        t = Transcription(input_str)
        out_str = t.output_drumseq()

        self.assertEqual(expected_out.strip(), out_str.strip())

    def test_linear(self):
        input_str = ('36 | 1  a,    ,3  a,     | Bassdrum\n'
                     '38 |  e  ,2 & , e   ,4 &  | Snare\n'
                     '42 |   & , e a,  & , e a | Closed HH')
        
        expected_out = ('#  1...2...3...4...\n'
                        '36 x..x....x..x....  Bassdrum\n'
                        '38 .x..x.x..x..x.x.  Snare\n'
                        '42 ..x..x.x..x..x.x  Closed HH')

        t = Transcription(input_str)
        out_str = t.output_drumseq()

        self.assertEqual(expected_out.strip(), out_str.strip())

