class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): # self é para referenciar o objeto
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) # quando criar um objeto, ele vai para a propria lista da classe

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante1 = Restaurante('Madero', 'Gourmet')
restaurante2 = Restaurante('Bobs', 'FastFood')

Restaurante.listar_restaurantes()
