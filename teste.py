

class Teste:
    def __init__(self,nota_1,nota_2,nota_op):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_op = nota_op

    @property
    def calc_op(self):
        self.nota_maior = self.nota_1 > self.nota_2
        if (self.nota_maior):
            if self.nota_2 <= self.nota_op:
                self.nota_2 = self.nota_op
        else:
            if self.nota_1 <= self.nota_op:
                self.nota_1 = self.nota_op

    @property
    def cal_media(self):
        self.media = (self.nota_1 + self.nota_2) // 2
        return self.media

    @property
    def printa_nota(self):
        if self.media > 5:
            print(f' sua nota 1 foi: {self.nota_1}\n nota 2 foi: {self.nota_2}\n com a media de: {self.media}\n '
                  f'Aprovado!!')
        else:
            print(f' sua nota 1 foi: {self.nota_1}\n nota 2 foi: {self.nota_2}\n com a media de: {self.media}\n '
                  f'Reprovado!!')


gustavo = Teste(4,3,9)
gustavo.calc_op
gustavo.cal_media
gustavo.printa_nota