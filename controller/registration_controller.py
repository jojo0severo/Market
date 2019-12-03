import logging
import sqlite3
from model.database_register import DatabaseRegister


class RegistrationController:
    def __init__(self):
        self.database_register = DatabaseRegister()
        self.last_registration = None

    def register(self, transaction_type, transaction_name, transaction_value, transaction_date):
        info = {
            'transaction_type': transaction_type.lower(),
            'transaction_name': transaction_name,
            'transaction_value': float(transaction_value.replace(',', '.')),
            'transaction_date': transaction_date
        }
        try:
            self.database_register.register(info)
            self.last_registration = info
            return 'Transação cadastrada com sucesso'

        except sqlite3.IntegrityError as e:
            logging.error('IntegrityError on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

        except sqlite3.OperationalError as e:
            logging.error('OperationalError on Registration\n ---> ' + str(e) + '\nInformation sent: ' + str(info))
            return 'Houve um erro interno na aplicação.\nPor favor contate o desenvolvedor.'

        except Exception as e:
            logging.error('Unknown error on Registration\n ---> ' + str(e))
            return 'Houve um erro interno na aplicação\nPor favor contate o desenvolvedor.'
