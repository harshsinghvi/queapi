class Que:
    def _data_validate(self):
        self._que['size']=len(self._que['data'])

    def __init__(self,elements=[], filename="nil" ):
        self._que={}
        self._que['size']=[]
        self._que['data']=elements
        self._que['size']=len(elements)
        if filename=="nil":
            self._file_handle=False
        else: 
            self._file_handle=True
            self._quefile=filename
            if os.path.exists(self._quefile):
                file=open(self._quefile)
                self._que = json.loads(file.read())    
                
            else:    
                file=open(self._quefile,'w')
                file.write(json.dumps(self._que))
            file.close()
            self._data_validate()

    def get(self):
        if not self._que['size']:
            raise Exception("QUE Exausted")
        temp=self._que['data'][0]
        del self._que['data'][0]
        self._data_validate()
        return temp

    def put(self,newElement=""):
        self._que['data'].append(newElement)
        self._data_validate()
        return 0

    def empty_que(self):
        self._que["data"]=[]
        self._data_validate()

    def is_empty(self):
        if self._que['size']:
            return 0
        else:
            return 1 
    
    def size(self):
            temp=self._que['size']
            return temp
    
    def top(self):
        if not self._que['size']:
            raise Exception("que empty")
        temp = self._que['data'][0]
        return temp

    def que(self):
        temp=self._que['data']
        return temp 

    def raw_que(self):
        temp=self._que
        return temp
