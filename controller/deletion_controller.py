from model.database_deleter import DatabaseDeleter


class DeletionController:
    def __init__(self):
        self.database_deleter = DatabaseDeleter()
        self.last_deletion = None

    def delete(self, info):
        try:
            if self.database_deleter.delete(info):
                self.last_deletion = info
                return 'Transação removida com sucesso'

            else:
                return 'Transação não pode ser removida'

        except Exception:
            pass

        return 'Erro na remoção da transação'
