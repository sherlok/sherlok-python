A Python client for Sherlok
===========================

`Sherlok <http://sherlok.io/>`_ is a flexible and powerful open source, distributed, real-time text-mining engine.



.. code:: python

    pip install --upgrade sherlok

    from sherlok import Sherlok

    s = Sherlok('neuroner')

    # returns a list of tuples (begin, end, text, annotation_type, attributes{})
    print s.annotate('layer 4 neuron')

    [(0, 14, 'layer 4 neuron', u'Neuron', {}),
     (8, 14, 'neuron',  u'Neuron', {}),
     (8, 14, 'neuron',  u'NeuronTrigger', {}),
     (0, 7,  'layer 4', u'Layer', {u'ontologyId': u'HBP_LAYER:0000004'})]


    # filtering and finding the text back
    txt = 'parvalbumin-positive fast-spiking basket cells, somatostatin-positive regular-spiking bipolar and multipolar cells, and cholecystokinin-positive irregular-spiking bipolar and multipolar cells'
    morphology = s.annotate(txt, u'Morphology')
    for (start, end, text, _type, properties) in morphology:
        print text, properties[u'ontologyId']

    basket HBP_MORPHOLOGY:0000019
    bipolar HBP_MORPHOLOGY:0000006
    multipolar HBP_MORPHOLOGY:0000035
    bipolar HBP_MORPHOLOGY:0000006
    multipolar HBP_MORPHOLOGY:0000035
