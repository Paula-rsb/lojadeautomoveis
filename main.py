from veiculo import Veiculo
from carro import Carro

caminhao_azul = Veiculo('azul', 6,'ford', 10)

print ('CAMINHÃO AZUL')
print ('cor: ', caminhao_azul.cor)
print ('Número de Rodas:', caminhao_azul.rodas)
print ('Marca: ', caminhao_azul.marca)
print ('Tanque: ', caminhao_azul.tanque)
caminhao_azul.abastecer(25)
print ('Tanque Abastecido',caminhao_azul.tanque)

print('')

carro_verde = Carro ('verde', 4, 'audi', 30)

print ('CARRO VERDE')
print ('cor: ', carro_verde.cor)
print ('Marca: ', carro_verde.marca)
print ('Tanque: ', carro_verde.tanque)
carro_verde.abastecer(40)
print ('Tanque Abastecido', carro_verde.tanque)