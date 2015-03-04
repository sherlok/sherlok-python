import unittest;

from sherlok import Sherlok

''' Requires a running Sherlok server'''
class TestSherlokClient(unittest.TestCase):

    def setUp(self):
        pass

    def test_opennlp_ners(self):
        pipeline = 'opennlp.ners.en'
        text = '''Jack Burton (born April 29, 1954 in El Paso), also known as Jake Burton, is an American snowboarder and founder of Burton Snowboards.'''
        annotations = list(Sherlok().annotate(pipeline, text))
        self.assertEqual(len(annotations), 3)
        for a in annotations:
            print a

    def test_filter(self):
        annotations = [
             (29, 33, u'x0', u'Neuron', {}),
             (0,   7, u'x1', u'Layer', {}),
             (8,  14, u'x2', u'NeuronWithProperties', {}),
             (19, 33, u'x3', u'NeuronWithProperties', {}),
             (19, 28, u'x4', u'BrainRegionProp', {})]
        selected = Sherlok().select(annotations, 'NeuronWithProperties')
        self.assertEqual(len(selected), 2)
        for s in selected:
            self.assertEqual(s[3], 'NeuronWithProperties')

    # def test_keep_largest(self):
    #     annotations = [(0, 4, u'a', {}), (0, 5, u'b', {}), (0, 7, u'c', {})]
    #     l = keep_largest(annotations)
    #     self.assertEqual(len(l), 1)
    #     self.assertEqual(l[0][2], 'c')

if __name__ == '__main__':
    unittest.main()
