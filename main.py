from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType


phonebook = {
    "bob": 79222,
    "alice": 2555,
    "jack": 2400,
}

square = {x: x*x for x in range(7)}
# print(square)
# print(phonebook['bob'])



d = OrderedDict(one=1, two=2, three=3)
d['four'] = 4
# print(d)
# print(d['two'])
# print(d.values())


dd = defaultdict(list)
dd['dogs'].append('Rufus')
dd['cats'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
# print(dd['dogs'])



dict_1 = {"one":1, "two":2}
dict_2 = {"three":3, "four":4}
chain_both = ChainMap(dict_1,dict_2)
# print(chain_both)
# print(chain_both['three'])
# print(chain_both['one'])



write_able = {'one':1, 'two':2}
read_able  = MappingProxyType(write_able)
# read_able['one'] = 11   #not supported
# print(read_able['one'])
# write_able['one']  = 11     # supported
# print(write_able['one'])




