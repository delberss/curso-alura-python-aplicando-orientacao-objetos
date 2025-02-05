class Restaurante:
    def __init__(self, nome, categoria): # self é para referenciar o objeto
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante1 = Restaurante('Madero', 'Gourmet')
restaurante2 = Restaurante('Bobs', 'FastFood')


restaurantes = [restaurante1, restaurante2]

print((restaurante1))
print(vars(restaurante2))
