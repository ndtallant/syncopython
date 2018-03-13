'''
Classes that form the basis for syncopython
The rhythm string for each limb will be parsed and joined
to output to drumseq.py as I develop a backend.
'''
import re
import unittest
import io
from drummer import Transcription, RhythmString

class TestTranscription(unittest.TestCase):

    def complex_transcription(self):
        input_stream = io.StringIO('''
        36 | 1&, ,e,e | Bassdrum
        38 | ,2a,ea,4a| Snare
        42 | 1e&a,2&,3e&a,4&a| Closed HH
        ''')

        t = Transcription(input_stream)
        out_string = t.output_drumseq()
        expected_out = '''
        # 1...2...3...4...
        36 x.x.......x..x.. Bassdrum
        38 ....x..x.x.xx..x Snare
        42 xxxxx.x.xxxxx.xx Closed HH
        '''
        assert out_string.strip() == expected_out.strip()
        # Black box testing - only public use

    def test_simple_transcription(self):
        input_string = '''
        36 | 1&, ,e,e | Bassdrum
        '''.strip()
        input_stream = io.StringIO(input_string)

        t = Transcription(input_stream)
        out_string = t.output_drumseq()
        expected_out = '''
        # 1...2...3...4...
        36 x.x......x...x.. Bassdrum
        '''
        print('input_string: ' + input_string)
        print('out_string: ' + out_string)
        self.assertEqual(expected_out.strip(), out_string.strip())
        # Black box testing - only public use
