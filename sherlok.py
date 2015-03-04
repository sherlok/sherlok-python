import requests # pip install requests


class Sherlok(object):


    '''
    @param pipeline: the Sherlok pipeline to invoke
    @param text: the text to analyse
    @return: a tuple (begin, end, atype, attributes{})
    '''
    def annotate(self, pipeline, text, host='localhost', port=9600):

        resp = requests.post(
            'http://{}:{}/annotate/{}'.format(host, port, pipeline),
            params={'text': text})
        if resp.status_code != 200:
            raise Exception('Sherlok error: {} {}'.format(resp.status_code, resp.text))
        json = resp.json()

        for _, annotation in json['annotations'].iteritems():
            #print annotation
            # ignore DocumentAnnotation (contains the request text) and Sofa
            if annotation['@type'] not in [u'DocumentAnnotation', u'Sofa']:
                # begin and end of found annotation
                begin, end = annotation.get('begin', 0), annotation['end']
                # type of annotation
                atype = annotation['@type']
                # text
                txt = text[begin:end]
                # additional attributes
                attributes = {k:v for (k,v) in annotation.items()\
                    if k not in ['sofa', 'begin', 'end', '@type']}

                yield begin, end, txt, atype, attributes


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
