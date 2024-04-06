idade=int(input('digite idade'))
sexo=input('digite sexo m ou f').lower()
if idade< 18 and sexo =='m':
    print('homem menor de idade')
elif idade >=18 and sexo =='m':
    print('homem maior de idade')
elif idade< 18 and sexo =='f':
    print ('Mulher menor de idade')
elif idade >=18 and sexo =='f':
    print('mulher maior de idade')
else:
    print('erro entrada de dados')