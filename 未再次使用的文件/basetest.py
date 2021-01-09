import functions
import base64
from hashlib import md5
cash = base64.b64encode("9aRrXp9XXAPjVIiB1GuE".encode("utf-8")).decode("utf-8")
print(cash)

cash2 = base64.b64decode(cash).decode("utf-8")
print(cash2)
print(md5("20201114000616170今天地铁上明显少了很多人。——网易云音乐热评9aRrXp9XXAPjVIiB1GuE".encode("utf-8")).hexdigest())
command_output = functions.yiyan(False)
print(functions.baidufanyi(command_output['yiyan'] + "——" + command_output['from'],"en"))