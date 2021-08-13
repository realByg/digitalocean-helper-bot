from tinydb import TinyDB, where
from datetime import datetime

db_file = 'db.json'


class AccountsDB:

    def __init__(self):
        db = TinyDB(db_file)
        self.accounts = db.table('Accounts')

    def save(self, email: str, token: str, remarks: str = ''):
        email = email.strip()
        token = token.strip()
        date = datetime.today().strftime('%Y-%m-%d')

        if self.accounts.get(where('token') == token):
            raise Exception('Token Exists')
        else:
            self.accounts.insert({
                'email': email,
                'token': token,
                'remarks': remarks,
                'date': date
            })

    def all(self):
        return self.accounts.all()

    def get(self, doc_id: int):
        return self.accounts.get(doc_id=int(doc_id))

    def remove(self, doc_id: int):
        self.accounts.remove(doc_ids=[int(doc_id)])
