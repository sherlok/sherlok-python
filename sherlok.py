import requests # pip install requests

# For Python3 compatibility
import sys
from six import iteritems
if sys.version_info > (3,):
    long = int

class SherlokError(Exception):
    def __init__(self, message, errorLog, response=None):

        # Call the base class constructor with the parameters it needs
        super(SherlokError, self).__init__(message)

        self.errorLog = errorLog
        self.response = response

        
class SherlokResult(object):
    def __init__(self, text, annotations, refs = {}):
        self.text = text
        self.annotations = annotations
        self.refs = refs
    def __iter__(self):
        return self.annotations


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
    def annotate(self, text, filter = False, timeout=1.0, nbRetries=5):

        # On occasions, the post request hangs for a long time. 
        # From run to run, it does not seem to hang on the same publications, so 
        # it appears to be independant of the request but more to be a bug related
        # to communication. A default 1s timeout has been added to avoid hanging 
        # for too long. Since this issue appears to be mainly independant of the 
        # request, we can just catch the timeout exception and retry. We retry up
        # to 5 times by default. 

        for retry in range(nbRetries):
            try:        
                resp = requests.post(
                    'http://{}:{}/annotate/{}'.format(self.host, self.port, self.pipeline),
                     data={'text': text}, timeout=timeout)
                break            
            except requests.Timeout:
                if retry == nbRetries-1:
                    raise
                else:
                    continue            
            
        if resp.status_code != 200:
            log =   ("##################### ERROR LOG #########################\n" +
                    str(text) + "\n" + 
                    "##########################################################\n" + 
                    str(resp) + "\n" + 
                    str(type(resp)) + "\n" + 
                    str(dir(resp)) + "\n" + 
                    str(resp.content) + "\n" + 
                    str(resp.headers) + "\n" + 
                    str(resp.ok) + "\n" + 
                    str(dir(resp.raw)) + "\n" + 
                    str(resp.reason) + "\n" + 
                    str(resp.request) + "\n" + 
                    str(resp.status_code) + "\n" + 
                    str(resp.text) + "\n" + 
                    str(resp.url) + "\n" + 
                    str(resp.raise_for_status) + "\n")
            raise SherlokError('Sherlok error: {} {}'.format(resp.status_code, resp.text), log, resp)
        json = resp.json()
        refs = json['_referenced_fss']
        return_annots = []

        for annot_type, annotations in iteritems(json['_views'][self.view]):

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

        return SherlokResult(text, return_annots, refs)


    # def keep_largest(self, annotations):

    #     largests = []
    #     for a in annotations:
    #         print 'largest in obs=', a
    #         is_larger = False
    #         for i, largest in enumerate(largests):
    #             # is a larger than largest?
    #             if (a[0] >= largest[0]) and (a[1] <= largest[1]):
    #                 del largests[i]
    #                 is_larger = True
    #         if is_larger:
    #             largests.append(a)
    #     return largests
