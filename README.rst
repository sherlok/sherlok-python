A Python client for Sherlok
===========================

See <http://sherlok.io/>.


.. code:: python

    pip install --upgrade sherlok

    from sherlok import Sherlok

    print list(Sherlok().annotate('neuroner', 'layer 4 neuron'))

    [(0, 14, 'layer 4 neuron', u'Neuron', {}),
     (8, 14, 'neuron',  u'Neuron', {}),
     (8, 14, 'neuron',  u'NeuronTrigger', {}),
     (0, 7,  'layer 4', u'Layer', {u'ontologyId': u'HBP_LAYER:0000004'})]


     # filtering and finding the text back
    s = Sherlok()
    txt = 'parvalbumin-positive fast-spiking basket cells, somatostatin-positive regular-spiking bipolar and multipolar cells, and cholecystokinin-positive irregular-spiking bipolar and multipolar cells'
    morphology = s.select(s.annotate('neuroner', txt), u'Morphology')
    for m in morphology:
        print m

    (175, 185, 'multipolar', u'Morphology', {})
    (163, 170, 'bipolar', u'Morphology', {})
    (98, 108, 'multipolar', u'Morphology', {})
    (86, 93, 'bipolar', u'Morphology', {})
    (34, 40, 'basket', u'Morphology', {})
