class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        self.ativo = 'Ativo' if self.ativo else 'Inativo'
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
                print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
restaurante_livota = Restaurante('Livota Gourmet', 'Japonesa')
restaurante_batatinha = Restaurante('Batatinha Express', 'Fast-Food')


#restaurantes = [restaurante_livota,restaurante_batatinha]

print(vars(restaurante_livota))
print(vars(restaurante_batatinha))
print()
print(restaurante_livota)
print(restaurante_batatinha)
print()
Restaurante.listar_restaurantes()