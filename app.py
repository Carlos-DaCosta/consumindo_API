from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import bebida
from modelos.cardapio.prato import prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = bebida('Suco de melancia', 5.0, 'Grande')
prato_pao = prato('Pão', 2.00, 'o melhor')

def main():
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()