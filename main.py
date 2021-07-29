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




arr = ['one', 'two', 'three']
# print(arr[1])
arr[1] = "done"
# print(arr[1])
del arr[2]
# print(arr)
arr.append(94)
# print(arr)



arr_2 = ('one','two','four', 4)
# print(arr_2)
# arr_2[2] = 3        # not supported
# print(arr_2)
arr_2 = arr_2 + (9,)
# print(arr_2)



import array
# single data-type arrays
arr_3 = array.array("f", (1,3,4,5,6))
# print(arr_3)
# arr_3[2] = "hi"     # not supported
# print(arr_3)




# strings are immutable array
arr_4 = "Hi,there"
# print(arr_4)
# arr_4[3] = "t"      # not supported
arr_4 = list(arr_4)
# print(arr_4)
arr_4[5] = "5"
# print(arr_4)




# bytes: Immutable Arrays of Single Bytes
arr_5 = bytes((0,22,22,66))     # bytes must be in range(0, 256)
# print(arr_5)
# arr_5[2] = 4    # not supported




# bytearray: Mutable Arrays of Single Bytes
arr_6 = bytearray((0,1,2,3,4))
# print(arr_6)
arr_6[2] = 7
# print(arr_6)

# Bytearrays can be converted back into bytes objects: (This will copy the data)
arr_6 = bytes(arr_6)
# print(arr_6)