from random import *



#        Rede emissora       Abreviatura   Digs inic IIN   Nro digitos
#      American Express          AE           34,37           15
#  Dinners Club International    DCI       309,36,38,39       14
#       Discover Card            DC             65            16
#          Maestro               M        5018,5020,5038     13,19
#        Master Card             MC          50-54,19         16
#       Visa Electron            VE     4026,426,4405,4508    16
#           Visa                 V        4024,4532,4556     13,16

t_ae = ('American Express', 'AE', ('34','37'), ('15',))
t_dci = ('Diners Club International', 'DCI', ('309', '36', '38', '39'), ('14',))
t_dc = ('Discover Card', 'DC', ('65',), ('16',))
t_m = ('Maestro', 'M', ('5018', '5020', '5038'), ('13', '19'))
t_mc = ('Master Card', 'MC', ('50', '51', '52', '53', '54', '19'), ('16',))
t_ve = ('Visa Electron', 'VE', ('4026', '426', '4405', '4508'), ('16',))
t_v = ('Visa', 'V', ('4024', '4532', '4556'), ('13', '16'))

t_cartoes = (t_ae,t_dci,t_dc,t_m,t_mc,t_ve,t_v)



# 1: Companhias aereas
# 2: Companhias aereas e outras tarefas futuras da industria
# 3: Viagens e entretenimento e bancario / financeiro
# 4: Servicos bancarios e financeiros
# 5: Servicos bancarios e financeiros
# 6: Merchandising e bancario / financeiro
# 7: Petroleo e outras atribuicoes futuras da industria
# 8: Saude, telecomunicacoes e outras atribuicoes futuras da industria
# 9: Atribuicao nacional

t_cat_ent = ((1,'Companhias aereas'),
             (2,'Companhias aereas e outras tarefas futuras da industria'),
             (3,'Viagens e entretenimento e bancario / financeiro'),
             (4,'Servicos bancarios e financeiros'),
             (5,'Servicos bancarios e financeiros'),
             (6,'Merchandising e bancario / financeiro'),
             (7,'Petroleo e outras atribuicoes futuras da industria'),
             (8,'Saude, telecomunicacoes e outras atribuicoes futuras da industria'),
             (9,'Atribuicao nacional'))



def calc_soma(n):
    """
    Recebe uma cadeia de carateres (numero de cartao sem o ultimo digito). 
    Devolve a soma dos digitos da cadeia de acordo com o algoritmo de Lunh.
    """
    
    # Comecamos por percorrer os caracteres de n, e juntamos a cada caracter o que estava à sua direira, do lado esquerdo, invertendo o numero. Caso um dos caracteres nao seja um algarismo, chamamos a atencao ao utilizador para o erro.
    # Seguidamente, percorremos a cadeia recem criada. OS caracteres nas posicoes impares da cadeia anterior (indices 0,2,4,..) vao ser multiplicados por 2. Se a multiplicacao der um resultado superior a 9, subtrai-se 9. Os caracteres nas posicoes pares vao para a nova cadeia sem qualquer alteracao.
    # Finalmente percorremos os elementos da cadeia e somamos, convertidos a inteiros.
    
    
    comp = len(n)
    num_invertido , num_invertido2 = '' , ''
    soma_luhn = 0
    
    for e in n:
   
        if '0' <= e <= '9': 
            num_invertido = e + num_invertido
                
        else:
            raise ValueError ('function calc_soma(): O string recebido apenas pode conter digitos')
        
        
    for i in range(comp):
        
        if i%2 == 0:
            resultado = eval(num_invertido[i]) * 2
                
            if resultado > 9:
                num_invertido2 = num_invertido2 + str(resultado - 9)
                    
            else:
                num_invertido2 = num_invertido2 + str(resultado)
        
        else:
            num_invertido2 = num_invertido2 + (num_invertido[i])
    

    for e in num_invertido2:
        soma_luhn = soma_luhn + eval(e)
     
    return soma_luhn    


def luhn_verifica(ccred):
    """
    Esta funcao recebe uma cadeira de caracteres, representando um numero de cartao
    Devolve verdadeiro, se o numero passar o algoritmo de Luhn, e falso caso contrario
    """
    
    # Primeiro criamos uma nova cadeia, n, com os digitos do cartao de credito sem o de controle.
    # Usamos a funcao calc_soma para somar os digitos do cartao de acordo com o algoritmo de Luhn e juntamos o digito de controle. Caso este ultimo nao seja um algarismo, chamamos a atencao ao utilizador para o erro.
    # Caso o resto da divisao por 10 seja 0, a funcao devolve o valor logico True.   
    

    n = ccred[:-1]
    dig_verificacao = ccred[-1]
        
    if '0' <= dig_verificacao <= '9':
        soma = calc_soma(n) + eval(dig_verificacao)
            
    else:
        raise ValueError ('function luhn_verifica() O string recebido apenas pode conter digitos')   
    
    return soma % 10 == 0


def comeca_por(cad1,cad2):    
    """
    Esta funcao devolve verdadeiro se cad1 comecar por cad2 
    Em caso contrario devolve falso
    """
    
    # Criamos uma nova cadeia, inicio_cad1, que contem os primeiros caracteres da cad1, de forma a serem tantos como em cad2.
    # Se as duas cadeias comparadas forem iguais, a funcao devolve o valor logico True.
    

    inicio_cad1 = cad1[:(len(cad2))]
    return inicio_cad1 == cad2


def comeca_por_um(cad,t_cads):
    """
    Recebe uma cadeia de caracteres, cad, e um tuplo de cadeias de caracteres, t_cads
    Devolve verdadeiro apenas se cad comecar por um dos elementos do tuplo
    """
    
    # Percorremos as varias cadeias de caracteres do tuplo t_cads e, atraves da funcao comeca_por, vemos se a cadeia "cad" comeca por alguma das cadeias do tuplo "t_cads".


    for e in t_cads:
    
        if (comeca_por(cad,e)):
            return True
     
    return False



def valida_iin(ccred):
    """
    Recebe uma cadeia de caracteres, representando um numero de cartao. 
    Devolve a cadeia de caracteres correspondente a rede emissora do cartao, se existir.. 
    Em caso contrario devolve a cadeia vazia. Apenas verifica os digitos iniciais e o comprimento da cadeia
    """

    # Vai ser usado o tuplo que contem todas as informacoes sobre os diferentes tipos de cartao definido nas linhas de codigo iniciais.
    # Sao acedidas as informacoes no indice 0 (Rede Emissora), 2 (Digitos iniciais IIN) e 3 (Numero de Digitos).
    
    # Percorremos o tuplo com as informacoes sobre os cartoes. Se a cadeia de caracteres introduzida comecar por alguma das cadeias no indice 2 de t_cartoes e tiver o comprimento especificicado no indice 3, devolvemos a rede emissora a qual corresponde essas 2 condicoes. 

    
    comp = str(len(ccred))
              
    for e in t_cartoes:
        
        if comeca_por_um(ccred,e[2]) and comp in e[3]:    
            return e[0]
        
    return ''


def categoria(cad):
    """
    Recebe uma cadeia de carateres
    Devolve uma cadeia correspondente a categoria da entidade correspondente ao primeiro carater da cadeia.
    """
    
    # Vai ser usado o tuplo que contem todas as informacoes sobre as categorias das entidades definido nas linhas de codigo iniciais.
    # Sao acedidas as informacoes no indice 0 (Digito Inicial) e 1 (Categoria).  
    
    # Caso o primeiro caracter nao seja um algarismo, chamamos a atencao ao utilizador para o erro. Caso seja, percorremos o tuplo com as informacoes sobre as categorias das entidades, e devolvemos a entidade correspondente ao digito inicial.
    
        
    if '0' <= cad[0] <= '9':

        c1=eval(cad[0])

        for e in t_cat_ent:
        
            if c1==e[0]:
                return e[1]
        
        
    else:
        raise ValueError ('function categoria(): O primeiro digito da cadeia nao e valido')

        

def verifica_cc(num_cartao):
    """
    Recebe um numero correspondente a um cartao de credito, determina se e correto.
    Devolve a rede emissora e a categoria da entidade.
    """

    # Em primeiro lugar, convertemos para uma cadeia de caracteres o numero de cartao fornecido pelo utilizador.
    # Caso este nao verifique o algoritmo de Luhn ou a funcao valida_iin tenha devolvido a cadeia vazia, indicamos ao utilizador que o numero nao e valido. Caso contrario, devolvemos a categoria e a rede emissora.
        
    
    ccred = str(num_cartao)
        
    if not luhn_verifica(ccred) or valida_iin(ccred) == '':
        return 'cartao invalido'

    return (categoria(ccred), valida_iin(ccred))
    

def digito_verificacao(n):
    """
    Recebe uma cadeia de caracteres, representando um numero de cartao sem o ultimo digito.
    Devolve o digito de verificacao que lhe devera ser acrescentado (em cadeia de caracteres)
    """
    
    # Para obtermos o digito de verificacao, comecamos por somar todos os digitos do cartao, com excecao do de controle. Caso o resto da soma por 10 seja diferente de 0, o digito sera a diferenca entre 10 e esta. Caso seja 0, e este o digito de verificacao. 

    soma = calc_soma(n)
    
    dig_ver = 0    
    
    if soma%10 != 0:
        dig_ver = 10 - soma%10
        
            
    return str(dig_ver)
        

def escolhe_iin_comp(abv):
    """
    Recebe como argumento uma cadeia de caracteres correspondentes a abreviatura de uma entidade emissora 
    Devolve uma cadeia de caracteres de digitos iniciais e um comprimento de cartao
    """    
    
    # Vai ser usado o tuplo que contem todas as informacoes sobre os diferentes tipos de cartao definido nas linhas de codigo iniciais.
    # Sao acedidas as informacoes no indice 1 (Abreviatura), 2 (Digitos iniciais IIN) e 3 (Numero de Digitos). 
    
    # Iremos percorrer o tuplo com todas as informacoes sobre os tipos de cartao. Quando se chegar a informacao correspondente a entidade emissora introduzida, escolhemos aleatoriamente os digitos iniciais e o comprimento do cartao.
    
        
    for e in t_cartoes:
                
        if e[1] == abv:
            dig_in = e[2][int(random() * len(e[2]))]
            comp = int(e[3][int(random() * len(e[3]))])   
                
    return (dig_in,comp)  
        

def gera_num_cc(abv):
    """
    Recebe como argumento uma cadeia de caracteres correspondentes a abreviatura de uma entidade emissora 
    Devolve um numero de cartao de credito valido
    """
    
    # Ao recebermos a indicacao de que entidade se pretende gerar um numero, usamos a funcao auxiliar escolhe_iin_comp para escolher aleatoriamente os digitos iniciais e o comprimento do cartao.
    # O numero final comeca por ser os digitos iniciais, juntando a estes, do lado direito, numeros aleatorios ate chegarmos ao comprimento pretendido menos 1. O ultimo digito sera o digito de verificacao.
        
    dig_iniciais , comp = escolhe_iin_comp(abv)     
    num_cc = dig_iniciais
           
    for i in range(comp-len(dig_iniciais)-1):  
        num_cc = num_cc + str(int(random()*10))       
            
    num_cc = num_cc + digito_verificacao(num_cc)
        
    return int(num_cc)   
    
            

