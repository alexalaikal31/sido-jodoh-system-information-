import collections
import json
maximilian='saya mau berkata saya mau pergi kepada paman saya'
alex=maximilian.lower()
cio_list=alex.split(' ')
ambil=collections.Counter(cio_list).most_common()
data_JSON = json.dumps(ambil)
print(data_JSON)
type(data_JSON)
