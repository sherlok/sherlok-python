import unittest;

from sherlok import Sherlok

''' Requires a running Sherlok server'''
class TestSherlokClient(unittest.TestCase):

    def test_opennlp_ners(self):

        s = Sherlok('opennlp.ners.en')
        text = '''Jack Burton (born April 29, 1954 in El Paso), also known as Jake Burton, is an American snowboarder and founder of Burton Snowboards.'''
        annotations = s.annotate(text).annotations
        self.assertEqual(len(annotations), 3)
        for a in annotations:
            print a

    def test_filter(self):
        s = Sherlok('neuroner')

        annotations = s.annotate('layer 2/3 nest basket cell').annotations
        self.assertEqual(len(annotations), 8)

        selected = s.annotate('layer 2/3 nest basket cell', 'Layer').annotations
        self.assertEqual(len(selected), 1)


    # def test_keep_largest(self):
    #     s = Sherlok('nope')
    #     annotations = [(0, 4, u'a', {}), (0, 5, u'b', {}), (0, 7, u'c', {})]
    #     l = s.keep_largest(annotations)
    #     self.assertEqual(len(l), 1)
    #     self.assertEqual(l[0][2], 'c')

if __name__ == '__main__':
    unittest.main()
