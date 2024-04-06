Daniela={
    'nome':'Daniela',
    'sobrenome':'souza',
    'profissao':'analista de sistemas',
    'filhos':'helena'
} 
#como trazer o Valor do meu X?   
#for x in Daniela:
   # print(x+':'+Daniela[x])
  #GET é usado para fazer uma analise  se existe ou se nao existe
print(Daniela.get('idade','esta informaçao nao consta cadastro'))
print(Daniela.get('nome','esta informaçao nao consta no cadastro')) 
