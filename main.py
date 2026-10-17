logs = [
    'LOGIN_FAILED',
    'LOGIN_SUCCESS',
    'LOGIN_FAILED',
    'LOGIN_FAILED',
    'LOGIN_SUCCESS'
]

contadores = {
    'LOGIN_FAILED':0,
    'LOGIN_SUCCESS':0,
    'DESCONHECIDO':0
}


for log in logs:
    if log == 'LOGIN_FAILED':
        contadores['LOGIN_FAILED'] += 1
    elif log == 'LOGIN_SUCCESS':
        contadores['LOGIN_SUCCESS'] += 1
    else: contadores['DESCONHECIDO'] += 1

print('Falhas:',contadores['LOGIN_FAILED'])
print('Sucessos:',contadores['LOGIN_SUCCESS'])
print('Desconhecidos:',contadores['DESCONHECIDO'])

total = sum(contadores.values())

print('Ao total existem',total,'registros.')

if contadores['LOGIN_FAILED'] >= 3:
    print('ALERTA: muitas falhas de login!')
else:
    print('Situação normal.')
