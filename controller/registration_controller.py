from model.database_register import DatabaseRegister


class RegistrationController:
    def __init__(self):
        self.database_register = DatabaseRegister()
        self.last_registration = None

    def register(self, info):
        try:
            if self.database_register.register(info):
                self.last_registration = info
                return 'Transação cadastrada com sucesso'

            else:
                return 'Transação não pode ser cadastrada'

        except Exception:
            pass

        return 'Erro no cadastro da transação'
