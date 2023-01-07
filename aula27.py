"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if(ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # vel. máx. do radar
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância que o radar pega

vel_maior_rad1 = velocidade > RADAR_1
range_menor_rad_1 = (LOCAL_1 - RADAR_RANGE)
range_maior_rad_1 = (LOCAL_1 + RADAR_RANGE)

range_menor = local_carro >= range_menor_rad_1
range_maior = local_carro <= range_maior_rad_1

multar_car_rad_1 = range_menor and range_maior

if vel_maior_rad1:
    print('Velocidade acima do radar!')

if multar_car_rad_1 and vel_maior_rad1:
    print('Multado no radar 1!')
