# O Objetivo é trocar os valores das variáveis a fim de
# ordenar a lista.
# No fim o num_1 será o menor valor e o num_3 o maior!

# Inicio...
num_1 = 3
num_2 = 2
num_3 = 1
var = 0

# Primeira Acção
# 3, 2, 1
if num_1 > num_2:
    var = num_1 # Caso verdadeiro, fazer a troca dos números de posição
    num_1 = num_2
    num_2 = var
# 2, 3, 1
if num_2 > num_3:
    var = num_2
    num_2 = num_3
    num_3 = var        
# 2, 1, 3
if num_1 > num_2:
    var = num_1
    num_1 = num_2
    num_2 = var

    
##################################################################
# Para simplificar, vamos fazer a seguinte alteração do código!

num_1 = 3
num_2 = 2
num_3 = 1
# var = 0

# Primeira Acção
# 3, 2, 1
if num_1 > num_2:
    num_1, num_2 = num_2, num_1 # Faz a mesma coisa economizando 2 linhas.
# 2, 3, 1
if num_2 > num_3:
    num_2, num_3 = num_3, num_2       
# 2, 1, 3
if num_1 > num_2:
    num_1, num_2 = num_2, num_1


# Quer testar? Use estes números!
# (1,2,3)
# (1,3,2)
# (2,3,1)
# (2,1,3)
# (3,1,2)
# (3,2,1)


