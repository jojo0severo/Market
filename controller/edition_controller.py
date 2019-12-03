import sqlite3
import logging
from model.database_editor import DatabaseEditor


class EditionController:
    def __init__(self):
        self.database_editor = DatabaseEditor()

    def edit(self, transaction_type, transaction_name, transaction_value, transaction_date):
        info = {
            'transaction_type': transaction_type.lower(),
            'transaction_name': transaction_name,
            'transaction_value': float(transaction_value.replace(',', '.')),
            'transaction_date': transaction_date
        }
        try:
            self.database_editor.edit(info)
            return 'Transação alterada com sucesso'

        except sqlite3.IntegrityError as e:
            logging.error('IntegrityError on Edition\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except sqlite3.OperationalError as e:
            logging.error('OperationalError on Edition\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'

        except Exception as e:
            logging.error('Unknown error on Edition\n ---> ' + str(e))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'
