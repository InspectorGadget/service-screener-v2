import json

import constants as _C
from frameworks.Framework import Framework

class WAFS(Framework):
    def __init__(self, data):
        super().__init__(data)
        pass
    
if __name__ == "__main__":
    data = json.loads(open(_C.FRAMEWORK_DIR + '/api.json').read())
    # print(data)
    o = WARS(data)
    o.readFile()
    # o.obj()
    o.generateMappingInformation()