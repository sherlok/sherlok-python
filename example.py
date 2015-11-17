from sherlok import Sherlok # pip install sherlok

pipeline = 'bluima.regions_rules'
host = '128.178.97.193'

s = Sherlok(pipeline, host=host)

text = 'neocortex projects to the nucleus accumbens'
res = s.annotate(text)
print res.annotations

res.refs # in
