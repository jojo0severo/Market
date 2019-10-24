from model.database_editor import DatabaseEditor


class EditionController:
    def __init__(self):
        self.database_editor = DatabaseEditor()

    def edit(self, info):
        try:
            if self.database_editor.edit(info):
                return 'Transação alterada com sucesso'

            else:
                return 'Transação não pode ser alterada'

        except Exception:
            pass

        return 'Erro na alteração da transação'
