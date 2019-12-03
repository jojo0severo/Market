import sqlite3
import logging
from model.database_deleter import DatabaseDeleter


class DeletionController:
    def __init__(self):
        self.database_deleter = DatabaseDeleter()
        self.last_deletion = None

    def delete(self, transaction_type, transaction_name, transaction_value, transaction_date):
        info = {
            'transaction_type': transaction_type.lower(),
            'transaction_name': transaction_name,
            'transaction_value': float(transaction_value.replace(',', '.')),
            'transaction_date': transaction_date
        }
        try:
            self.database_deleter.delete(info)
            self.last_deletion = info
            return 'Transação removida com sucesso'

        except sqlite3.IntegrityError as e:
            logging.error('IntegrityError on Deletion\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except sqlite3.OperationalError as e:
            logging.error('OperationalError on Deletion\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except Exception as e:
            logging.error('Unknown error on Deletion\n ---> ' + str(e))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'
