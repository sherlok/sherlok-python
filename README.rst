A Python client for Sherlok
===========================

See <http://sherlok.io/>.


.. code:: python

    pip install --upgrade sherlok

    from sherlok import Sherlok

    annotations = Sherlok().annotate('neuroner', 'layer 4 neuron')
    print list(annotations)

    [(0, 14, u'Neuron', {}),
     (8, 14, u'Neuron', {}),
     (8, 14, u'NeuronTrigger', {}),
     (0, 7, u'Layer', {u'ontologyId': u'HBP_LAYER:0000004'})]

     # filtering and finding the text back

    s = Sherlok()
    txt = 'Accumbens nucleus shell neuron'
    brain_regions = s.select(s.annotate('neuroner', txt), 'BrainRegionProp')

    [(0, 17, u'BrainRegionProp', {})]

    for br in brain_regions:
        print txt[br[0]:br[1]]

    Accumbens nucleus
