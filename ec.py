class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.duringtrans = False
        self.changetrans = {}
        self.beforetrans = {}

    def begin_transaction(self):
        if self.duringtrans:
            raise Exception("ERROR")
        self.duringtrans = True
        self.changetrans = {}
        self.beforetrans = {}

    def put(self, key, value):
        if not self.duringtrans:
            raise Exception("ERROR")
        if key not in self.beforetrans:
            self.beforetrans[key] = self.db.get(key, None)
        self.changetrans[key] = value

    def get(self, key):
        if self.duringtrans and key in self.changetrans:
            return self.changetrans[key]
        return self.db.get(key, None)

    def commit(self):
        if not self.duringtrans:
            raise Exception("ERROR")
        for key, value in self.changetrans.items():
            self.db[key] = value
        self.duringtrans = False
        self.changetrans = {}
        self.beforetrans = {}

    def rollback(self):
        if not self.duringtrans:
            raise Exception("ERROR")
        self.duringtrans = False
        self.changetrans = {}
        self.beforetrans = {}


