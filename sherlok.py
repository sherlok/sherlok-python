import requests # pip install requests


class Sherlok(object):


    '''
    @param pipeline: the Sherlok pipeline to invoke
    @param text: the text to analyse
    @return: a tuple (begin, end, atype, attributes{})
    '''
    def annotate(self, pipeline, text, host='localhost', port=9600, view='_InitialView'):

        resp = requests.post(
            'http://{}:{}/annotate/{}'.format(host, port, pipeline),
            params={'text': text})
        if resp.status_code != 200:
            raise Exception('Sherlok error: {} {}'.format(resp.status_code, resp.text))
        json = resp.json()

        for annot_type, annotations in json['_views'][view].iteritems():

            # ignore DocumentAnnotation (contains the request text) and Sofa
            if annot_type not in [u'DocumentAnnotation', u'Sofa']:
                for a in annotations:
                    begin, end = a['begin'], a['end']
                    txt = text[begin:end]
                    # additional attributes
                    attributes = { k:v for (k,v) in a.items() \
                        if k not in ['sofa', 'begin', 'end'] }
                    yield begin, end, txt, annot_type, attributes


    def select(self, annotations, type):
        return [a for a in annotations if a[3] == type]


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
