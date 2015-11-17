import requests # pip install requests


class SherlokResult(object):
    def __init__(self, annotations, refs = {}):
        self.annotations = annotations
        self.refs = refs

class Sherlok(object):
    '''
    @param pipeline: the Sherlok pipeline to invoke
    '''
    def __init__(self, pipeline, host='localhost', port=9600, view='_InitialView'):
        self.pipeline = pipeline
        self.host = host
        self.port = port
        self.view = view

    '''
    @param text: the text to analyse
    @return: a generator of tuples (begin, end, text, annotation_type, attributes{})
    '''
    def annotate(self, text, filter = False):

        resp = requests.post(
            'http://{}:{}/annotate/{}'.format(self.host, self.port, self.pipeline),
            params={'text': text})
        if resp.status_code != 200:
            raise Exception('Sherlok error: {} {}'.format(resp.status_code, resp.text))
        json = resp.json()
        refs = json['_referenced_fss']
        return_annots = []

        for annot_type, annotations in json['_views'][self.view].iteritems():

            # filter?
            if filter is False or annot_type == filter:

                # ignore DocumentAnnotation (contains the request text) and Sofa
                if annot_type not in [u'DocumentAnnotation', u'Sofa', u'FSArray']:

                    for a in annotations:
                        if isinstance(a, (int, long)): # a ref?
                            a = refs[str(a)]
                        begin, end = a['begin'], a['end']
                        txt = text[begin:end]
                        # additional attributes
                        attributes = { k:v for (k,v) in a.items() \
                            if k not in ['sofa', 'begin', 'end'] }
                        return_annots.append( (begin, end, txt, annot_type, attributes) )

        return SherlokResult(return_annots, refs)

# def keep_largest(self, annotations):
#     largests = []
#     for a in annotations:
#         print 'largest in obs=', a
#         is_larger = True
#         for i, largest in enumerate(largests):
#             # is a larger than largest?
#             if (a[0] >= largest[0]) and (a[1] <= largest[1]):
#                 is_larger = False
#         if is_larger:
#             largests.append(a)
#     return largest
