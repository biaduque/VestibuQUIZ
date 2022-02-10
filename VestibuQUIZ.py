#Jogo educativo feito por Beatriz Duque e João Pedro

import time
import random
dificuldade = ""
pontos = 0
erros = 0
escs = [1,2,3,4,5,6,]
escsD = [1,2,3,4,5,6,7]
estudar = []
confirm = []

def baú():
    print('\n'
        '                                  ████████████████████████████████\n'  
        '                                ██░░░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██ \n' 
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██                          ██\n'
        '                              ██████████████████████      ████████████\n'
        '                              ██░░▒▒▒▒░░██░░▓▓▓▓▓▓▓▓  ██  ▓▓▓▓▓▓▓▓░░██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▓▓      ▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▓▓██████▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░▒▒▒▒░░██  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ██\n'
        '                              ██░░░░░░░░██                          ██\n'
        '                              ████████████████████████████████████████\n')
def AbrtJOGO():
    print('Atenção:Jogue em tela cheia')
    time.sleep(3)
    print('\n'
'                                      ,,   ,,                                                               \n'
'                              mm      db  *MM                      .g8""8q.   *7MMF*    7MF* 7MMF MMM"""AMV \n'
'                              MM           MM                    .dP     `YM.   MM       M    MM  M    AMV  \n'
'`7M*   `MF* .gP"Ya  ,pP"Ybd mmMMmm  `7MM   MM,dMMb.  `7MM  `7MM  dM       `MM   MM       M    MM  *   AMV   \n'
'  VA   ,V  ,M    Yb 8I   `*   MM      MM   MM    `Mb   MM    MM  MM        MM   MM       M    MM     AMV    \n'
'   VA ,V   8M"""""" `YMMMa.   MM      MM   MM     M8   MM    MM  MM.      ,MP   MM       M    MM    AMV   * \n'
'    VVV    YM.    , L.   I8   MM      MM   MM.   ,M9   MM    MM  `Mb.    ,dP*   YM.     ,M    MM   AMV   ,M \n'
'     W      `Mbmmd  M9mmmP*   `Mbmo .JMML. P^YbmdP*    `MbodYML.  `*bmmd**d      `bmmmmd*  .JMML.AMVmmmmMM  \n'
'                                                                       MMb                                  \n'
'                                                                        `bood*                              \n')
    global nome
    nome=str(input("Olá jogador, digite seu nome:"))
    print("                 ╔═══════════════════════════════════════════════╗\n"
          "                                   JOGADOR",nome.upper(),"          \n"
           "                 ║»»»»»»»»»»»»»»»»»VESTIBU QUIZ««««««««««««««««««║\n"
           "                 ║                 INSTRUÇÕES                    ║\n"
           "                 ║1) Suas habilidades serão testadas dentro da   ║\n"
           "                 ║área de exatas, humanas e biológicas           ║\n"
           "                 ║2) Acumule o maior número de pontos para con-  ║\n"
           "                 ║seguir o troféu maior.                         ║\n"
           "                 ║3) No final do jogo seu perfil de estudante se-║\n"
           "                 ║rá avaliado, por isso, responda com sabedoria. ║\n"
           "                 ║4) Selecione as anternativas digitando:        ║\n"
           "                 ║   A, B, C ou D                                ║\n"
           "                 ║5) Acerto= 1 ponto                             ║\n"
           "                 ╚═══════════════════════════════════════════════╝\n")
    time.sleep(3)
    print('\n'
          '                         ___   _____     _     ___   _____ \n'
          '                        / __| |_   _|   /_\   | _ \ |_   _|\n'
          '                        \__ \   | |    / _ \  |   /   | |  \n'
          '                        |___/   |_|   /_/ \_\ |_|_\   |_|  \n')
                                                                        
    comec = str(input("\n>>>>>Aperte ENTER para começar.\n"))

    
def Inicio():
    
    global dificuldade
    dificuldade = str(input("\nDigite o nível de dificuldade do jogo. Fácil ou Difícil: "))
    while  dificuldade.upper() != "DIFICIL" and dificuldade.upper() != "DIFÍCIL" and dificuldade.upper() != "FACIL" and dificuldade.upper() != "FÁCIL":
        dificuldade = str(input("Digite apenas fácil ou difícil, não importando letras maiúsculas ou minúsculas ou acento: "))
    else:
        if dificuldade.upper() == "FACIL" or dificuldade.upper() == "FÁCIL":
            global pontosF
            pontosF = questoesFaceis(pontos,erros)
        else:
            global pontosFD
            pontosFD = questoesDificeis(pontos,erros)

            
#ESSA FUNÇÃO ARMAZENA AS QUESTÕES DE NÍVEL FÁCIL EM LISTAS, FAZ AS PERGUNTAS E CONTA OS ERROS E ACERTOS

            
def questoesFaceis(pontos,erros):
    n = len(escs)
    x = 0
    quest = 0
    resp2 = ""
    z = 0
    resp = ""
    Port=["\nPORTUGUÊS"
        '\nSobre os adjetivos, é correto afirmar:\n'
               'a) Classe de palavras que se caracteriza por delimitar o substantivo, atribuindo-lhe qualidades, estados, aparência etc.\n'
               'b) Classe de palavra invariável que modifica o sentido do verbo, do adjetivo e do advérbio.\n'
               'c) Classe de palavra que vem antes do substantivo, indicando se ele é determinado ou indeterminado.\n'
               'd) Classe de palavra invariável que exprime estados emocionais.\n'
               'e) Conjuntos de verbos que, em uma determinada frase, desempenham valor de um único verbo.\n',
               "\nPORTUGUÊS"
            '((UFPA) No trecho “Basta chegar a Pequim para desnudar a farsa de que a China é o chão de fábrica do planeta, mas não tem acesso aos bens que produz.”\n'
            'a expressão metafórica em destaque indica que os chineses\n'
            'a) produzem muito.\n'
            'b) não são consumistas.\n'
            'c) produzem com pouca qualidade.\n'
            'd) não precisam daquilo que produzem.\n'
            'e) não produzem aquilo de que precisam.\n',
          "\nPORTUGUÊS"
          "\nIndique qual é a frase cujo uso do “porquê” está correto."
"\na) Ontem fomos à praia porquê fazia sol."
"\nb) Por que recebi ontem, fui ao mercado fazer compras."
"\nc) Fernanda não foi trabalhar hoje porque está doente."
"\nd) Mudei de canal por quê quis."
"\ne) O paciente não entendeu o por que de tanta preocupação.",
          "\nPORTUGUÊS"
          "\nAssinale a única alternativa que possui uma oração sem sujeito:"
"\na) Gosto de chuva."
"\nb) Anunciaram o lançamento do novo computador."
"\nc) Faz muito frio em Londres."
"\nd) Não se falava sobre outro assunto.",
"\nPORTUGUÊS"
          "\nA alternativa em que o acento indicativo de crase não procede é:"
"\na) Tais informações são iguais às que recebi ontem."
"\nb) Perdi uma caneta semelhante à sua."
"\nc) A construção da casa obedece às especificações da Prefeitura."
"\nd) O remédio devia ser ingerido gota à gota, e não de uma só vez."
"\ne) Não assistiu a essa operação, mas à de seu irmão.",
          "\nPORTUGUÊS"
          "\nMarque a alternativa cujos substantivos recebem o acréscimo de &#39;es&#39;"
"\npara a marcação do plural:"
"\na) cor, hambúrguer, hotel."
"\nb) humor, mulher, anel."
"\nc) colher, cor, chafariz."
"\nd) sabor, cadeira, elevador."
"\ne) rumor, chafariz, céu."]

    Hist=["\nHISTÓRIA"
           "\n(UFRJ) Para garantir a posse da terra, Portugal decidiu colonizar o Brasil. Mas, para isso, seria preciso desenvolver uma atividade econômica lucrativa.\n"
               'A solução encontrada foi implantar em certos trechos do litoral:\n'
               'a) a produção açucareira.\n'
               'b) a exploração do ouro.\n'
               'c) a extração do pau-brasil.\n'
               'd) a criação de gado.\n'
               'e) o comércio de especiarias.\n',
           "\nHISTÓRIA"
           "\nO país que atuava como parceiro econômico de Portugal na produção do"
"\naçúcar por meio do financiamento dos engenhos, refinamento do açúcar"
"\ne distribuição da mercadoria pela Europa foi:"
"\na) Holanda."
"\nb) Espanha."
"\nc) França."
"\nd) Índia."
"\ne) Cabo Verde.",
        "\nHISTÓRIA"
           "\nUm dos fatos importantes que contribuíram efetivamente para o ingresso"
"\ndo Brasil na Segunda Guerra Mundial foi:"
"\na) o ataque de aviões japoneses ao Forte de Copacabana."
"\nb) o torpedeamento de navios brasileiros por submarinos alemães."
"\nc) a invasão do estado do Amazonas por tropas nazistas."
"\nd) a tomada do arquipélago de Fernando de Noronha pela marinha"
"\nfascista italiana."
"\ne) o bombardeamento da cidade de São Paulo por aviões da Força"
"\nAérea Alemã."]
    
    Mat=["\nMATEMÁTICA"
        '\nA respeito das regras da adição e subtração envolvendo números positivos e negativos, assinale a alternativa correta:\n'
               'a) O resultado da adição de dois números inteiros sempre será um número positivo.\n'
               'b) O resultado da subtração de dois números inteiros sempre será um número negativo.\n'
               'c) O resultado da subtração de dois números inteiros poderá ser um número positivo ou um número negativo, dependendo do módulo desses números.\n'
               'd) A soma de dois números negativos sempre tem como resultado um número positivo.\n'
               'e) A subtração entre dois números negativos sempre tem como resultado um número negativo.\n',
          "\nMATEMÁTICA"
          "\nQual o valor de x na equação abaixo?"

    "\n15x + 132 = 25x + 72"

    "\na) x = 6"
"\nb) x = 7"
"\nc) x = 8"
"\nd) x = 9"
"\ne) x = 10)",
          "\nMATEMÁTICA"
          "\nA respeito da multiplicação e divisão entre números positivos e"
"\nnegativos, assinale a alternativa correta:"
"\na) O produto entre dois números negativos sempre terá como resultado"
"\num número também negativo."
"\nb) O produto entre dois números positivos poderá ter resultado negativo,"
"\ndependendo de quais forem esses números."
"\nc) A divisão entre dois números negativos sempre terá como"
"\nresultado um número positivo."
"\nd) A divisão entre um número negativo e um número positivo poderá ter"
"\num resultado positivo ou negativo, dependendo do módulo dos dois"
"\nnúmeros."
"\ne) As regras para encontrar o sinal do resultado de uma multiplicação"
"\nnão se aplicam à divisão.",
          "\nMATEMÁTICA"
          "\nQual é a área de uma esfera cujo raio mede 63 cm? Considere π = 3."
"\na) 47628 cm 2"
"\nb) 48628 cm 2"
"\nc) 49628 cm 2"
"\nd) 50000 cm 2"
"\ne) 51628 cm 2",
"\nMATEMÁTICA"
          "\nQual a área e o perímetro de um campo de futebol, de base 25 m e altura"
"\n5 m?"
"\na) A= 100m², P= 50m"
"\nb) A= 150 m², P= 60m"
"\nc) A= 125 m², P= 60 m"
"\nd) A= 120 m², P= 50 m"]
    
    Fis=["\nFÍSICA"
        '"\nLeia as seguintes afirmações a respeito da aceleração.\n'
               'I) A aceleração é uma grandeza escalar, definida pela razão entre a variação da velocidade e variação do tempo.\n'
               'II) A aceleração determina a taxa de variação das posições de um móvel.\n'
               'III) A aceleração é uma grandeza vetorial, sua determinação depende da razão entre a variação da velocidade e a variação do tempo.\n'
               'Está certo o que se afirma em:\n'
               'a) I\n'
               'b) II\n'
               'c) III\n'
               'd) I e II\n'
               'e) II e III\n',
          "\nFÍSICA"
          "\nMarque a afirmativa correta:"
"\na) Todos os imãs possuem dois polos, o polo norte e o sul. O polo sul é o"
"\npositivo de um imã, enquanto o norte é negativo."
"\nb) Ao quebrar um imã, os seus polos são separados, passando a existir"
"\num imã negativo e outro positivo."
"\nc) Ao aproximar os polos iguais de um imã, eles repelem-se."
"\nQuando polos diferentes aproximam-se, eles atraem-se."
"\nd) Os materiais ferromagnéticos são os que não podem ser atraídos por"
"\nimãs.",
          "\nFÍSICA"
          "\n(PUC-MG) Na questão a seguir assinale a afirmativa INCORRETA."
"\na) Todos os materiais expandem-se quando aquecidos."
"\nb) A temperatura de fusão de uma substância depende da pressão."
"\nc) Durante uma mudança de fase, a temperatura permanece constante."
"\nd) A temperatura em que a água ferve depende da pressão."]
    
    Quim=["\nQUÍMICA"
        "\n(Vunesp-SP) Sabe-se que a chuva ácida é formada pela dissolução, na"
"\nágua da chuva, de óxidos ácidos presentes na atmosfera. Entre os pares"
"\nde óxidos relacionados, qual é constituído apenas por óxidos que"
"\nprovocam a chuva ácida?"
"\na) Na 2 O e NO 2"
"\nb) CO 2  e MgO"
"\nc) CO 2  e SO 3"
"\nd) CO e NO 2"
"\ne) CO e NO",
          "\nQUÍMICA"
        '\n(UFJF-MG) Associe as afirmações a seus respectivos responsáveis:\n'
               'O átomo não é indivisível e a matéria possui propriedades elétricas (1897).\n'
               'II- O átomo é uma esfera maciça (1808).\n'
               'III- O átomo é formado por duas regiões denominadas núcleo e eletrosfera (1911).\n'
               'a) I - Dalton, II - Rutherford, III - Thomson.\n'
               'b) I - Thomson, II - Dalton, III - Rutherford.\n'
               'c) I - Dalton, II - Thomson, III - Rutherford.\n'
               'd) I - Rutherford, II - Thomson, III - Dalton.\n'
               'e) I - Thomson, II - Rutherford, III - Dalton.\n']

    Geo=["\nGEOGRAFIA"
        'Sobre as empresas multinacionais, também chamadas de transnacionais ou globais, podemos elencar as seguintes características, exceto:\n'
               'a) Domínio de tecnologias avançadas\n'
               'b) Descentralização industrial\n'
               'c) Procura por mão de obra barata\n'
               'd) Descentralização científica e administrativa\n'
               'e) Investimento em tecnologia\n',
          "\nGEOGRAFIA"
          "\nAssinale um dos eventos abaixo enumerados que não possui relação"
"\ndireta com o processo de globalização:"
"\na) A difusão dos comércios localizados em oposição às"
"\ncorporações internacionais."
"\nb) A formação de blocos econômicos regionais."
"\nc) A propagação do inglês como idioma universal."
"\nd) O “encolhimento” do mundo graças à redução das dificuldades de"
"\ncomunicação e transporte entre as diferentes regiões do planeta.",
          "\nGEOGRAFIA"
          "\nUma das medidas internacionais de combate ao aquecimento global"
"\nmais divulgadas pela imprensa em todo o mundo foi o Protocolo de"
"\nKyoto, que teve como objetivo principal:"
"\na) Proliferar ações de aumento da vegetação existente no planeta."
"\nb) Diminuir as emissões de gases poluentes na atmosfera."
"\nc) Pressionar os países desenvolvidos a contribuir menos com a"
"\nelevação das temperaturas."
"\nd) Conservar as algas marinhas, responsáveis pela disponibilidade do"
"\noxigênio na atmosfera.",
          "GEOGRAFIA\n"
          "Sobre o Aquecimento Global, é correto dizer que:"
"\na) é um evento exclusivamente climático"
"\nb) é uma ocorrência exclusivamente temporal atmosférica"
"\nc) é um fenômeno climático com efeitos na dinâmica do tempo"
"\nmeteorológico"
"\nd) é uma dinâmica meteorológica que podem acarretar efeitos climáticos"
"\ne) ocorre em uma escala muito ampla para ser chamado de clima ou de"
"\ntempo",
          "\nGEOGRAFIA"
          "\nJulgue as afirmações abaixo:"
"\nI – A escala Celsius atribui 0° para o ponto de fusão do gelo e 100º para"
"\no ponto de ebulição da água;"
"\nII – O limite inferior para a escala Kelvin corresponde a -273°C;"
"\nIII – 1°C equivale a 1°F."
"\nEstão corretas:"
"\na) I e II apenas"
"\nb) I e III apenas"
"\nc) I, II e III"
"\nd) II e III apenas"
"\ne) I apenas"]


    
    #ESSE WHILE É O QUE CORRE PELAS LISTAS DE FORMA RANDOMICA COLOCANDO AS QUESTÕES PARA O USUÁRIO RESPONDER EM ORDEM ALEATÓRIA.
    while True:

        
        erroEspec = 0
        esc1 = random.randrange(0,n)
        resp = ""
        z = 0

        
        #VARIÁVEL erroEspec SERVE PARA CONTAR OS ERROS ESPECÍFICOS EM MATÉRIAS E ADICIONAR NA LISTA estudar AS MATÉRIAS COM MAIS ERROS.
        erroEspec = 0
        confirm = []
        if escs[esc1] != -1:
            if esc1 == 0:
                k = random.randrange(0,len(Port))
                if k == 0:
                    resp2 = "A"
                elif k == 1:
                    resp2 = "A"
                elif k == 2:
                    resp2 = "C"
                elif k == 3:
                    resp2 = "C"
                elif k == 4:
                    resp2 = "D"
                elif k == 5:
                    resp2 = "C"
                quest = quest + 1
                print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                print(Port[k])
                resp = str(input("Digite a letra da resposta correta: "))
                while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                if resp.upper() == resp2:
                    pontos = pontos + 1
                else:
                    erros = erros + 1
                    erroEspec = erroEspec + 1
                if erroEspec == 1:
                    estudar.append("Português.")
                confirm = []
                x = x + 1
                escs[0] = -1
            elif esc1 == 1:
                k = random.randrange(0,len(Hist))
                if k == 0:
                    resp2 = "A"
                elif k == 1:
                    resp2 = "A"
                elif k == 2:
                    resp2 = "B"
                quest = quest + 1
                print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                print(Hist[k])
                resp = str(input("Digite a letra da resposta correta: "))
                while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                if resp.upper() == resp2:
                    pontos = pontos + 1
                else:
                    erros = erros + 1
                    erroEspec = erroEspec + 1
                if erroEspec == 1:
                    estudar.append("História.")
                z = z + 1
                x = x + 1
                confirm = []
                escs[1] = -1
            elif esc1 == 2:
                while True:
                    k = random.randrange(0,len(Mat))
                    while k in confirm:
                        k = random.randrange(0,len(Mat))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "C"
                    elif k == 1:
                        resp2 = "A"
                    elif k == 2:
                        resp2 = "C"
                    elif k == 3:
                        resp2 = "A"
                    elif k == 4:
                        resp2 = "C"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Mat[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Matemática.")
                    z = z + 1
                    x = x + 1
                    if z == 2:
                        break
                confirm = []
                escs[2] = -1
                z = 0
            elif esc1 == 3:
                while True:
                    k = random.randrange(0,len(Fis))
                    while k in confirm:
                        k = random.randrange(0,len(Fis))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "C"
                    elif k == 1:
                        resp2 = "C"
                    elif k == 2:
                        resp2 = "A"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Fis[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Física.")
                    z = z + 1
                    x = x + 1
                    if z == 2:
                        break
                confirm = []
                escs[3] = -1
                z = 0
            elif esc1 == 4:
                k = random.randrange(0,len(Quim))
                if k == 0:
                    resp2 = "C"
                elif k == 1:
                    resp2 = "B"
                quest = quest + 1
                print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                print(Quim[k])
                resp = str(input("Digite a letra da resposta correta: "))
                if resp.upper() == resp2:
                    pontos = pontos + 1
                else:
                    erros = erros + 1
                    erroEspec = erroEspec + 1
                if erroEspec == 1:
                    estudar.append("Química.")
                confirm = []
                escs[4] = -1
                z = 0
                x = x + 1
            elif esc1 == 5:
                k = random.randrange(0,len(Geo))
                if k == 0:
                    resp2 = "D"
                elif k == 1:
                    resp2 = "B"
                elif k == 2:
                    resp2 = "B"
                elif k == 3:
                    resp2 = "C"
                elif k == 4:
                    resp2 = "A"
                quest = quest + 1
                print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                print(Geo[k])
                resp = str(input("Digite a letra da resposta correta: "))
                while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                if resp.upper() == resp2:
                    pontos = pontos + 1
                else:
                    erros = erros + 1
                    erroEspec = erroEspec + 1
                if erroEspec == 1:
                    estudar.append("Geografia")
                x = x + 1
                confirm = []
                escs[5] = -1
                z = 0
            confirm = []
            z = 0
            if x == 8:
                return pontos,erros
        else:
            x = x + 0


            
def questoesDificeis(pontos,erros):
    n = len(escsD)
    k = 0
    x = 0
    Port = ["\nPORTUGUÊS"
        "\n(Mackenzie 2008) Considere as seguintes afirmações sobre Os Lusíadas:"
    "\nI.	É um poema épico que tem como núcleo narrativo as origens históricas de Portugal, relatadas pela voz do próprio poeta."
    "\nII.	 Embora pertença à Épica, incorpora à sua linguagem traços estilísticos do gênero lírico, em episódios antológicos como o da “Inês de Castro” e o da “Ilha dos Amores”, por exemplo."
    "\nIII.	 Obedece a uma regularidade formal, valendo-se de versos decassílabos, traço valorizado no Renascimento."
    "\na) se apenas as afirmações I e II estiverem corretas." 
    "\nb) se apenas as afirmações II e III estiverem corretas."
    "\nc) se apenas as afirmações I e III estiverem corretas."
    "\nd) se apenas a afirmação III estiver correta."
    "\ne) se todas as afirmações estiverem corretas.",
            "\nPORTGUÊS"
    "\n(Mackenzie 2014) Sobre a primeira fase do Movimento Modernista, ao qual a crítica vincula Manuel Bandeira, todas as alternativas estão corretas, EXCETO:"
    "\na) buscava inspiração nas ideologias concretistas para simplificação poética."
    "\nb) objetivava o rompimento com as estruturas artísticas do passado."
    "\nc) apresentava, em um primeiro momento, um caráter anárquico e destruidor."
    "\nd) valorizava a língua “brasileira”."
    "\ne) a postura nacionalista, do final dos anos 1920, apresentava uma vertente crítica e uma vertente ufanista.",
            "\nPORTGUÊS"
    "\n(Mackenzie 2012) O valor do prefixo da palavra agramática encontra-se também em:" 
    "\na) anagrama."
    "\nb) acrópole." 
    "\nc) adjunto."
    "\nd) amoral."
    "\ne) análise."]
    Mat = ["\nMatemática"
           "\n(Mackenzie 2008) Para se cadastrar em um site de compras, cada cliente digitava uma senha com quatro algarismos."
           "\nCom o objetivo de aumentar a segurança o site, todos os clientes foram solicitados a adotar notas senhas com "
           "\ncinco algarismosSe definirmos o nível de segurança como a quantidade possível de senhas, então a segurança desse site aumentou em: "
    "\nA)10%"
    "\nb)25%"
    "\nc)125%"
    "\nd)900%"
    "\ne)1100%",
           "\nMatemática"
    "\n(Mackenzie 2014) Um professor de matemática entrega aos seus alunos uma lista contendo 10 problemas e avisa que 5 deles"
    "\nserão escolhidos ao acaso para compor a prova final. Se um aluno conseguiu resolver, corretamente, apenas 7 dos 10 problemas,"
    "\na probabilidade de que ele acerte todos os problemas da prova é:"
    "\na)   7/84"
    "\nb)   21/84"
    "\nc)   59/84"
    "\nd)   77/84"
    "\ne)   1"]
    Geog = ["\nGEOGRAFIA"
        "\n(Mackenzie 2019) Sabendo que o fuso horário do Sudão do Sul é determinado exclusiva e estritamente por sua localização"
            "\ngeográfica e que o fuso horário adotado em São Paulo é UTC-3: é correto afirmar que um passageiro de um voo saindo de "
            "\nSão Paulo, no dia 20 de setembro de 2016, às 11h em horário local, com duração de 10 (dez) horas,"
    "\na)   poderá, no momento da partida, adiantar seu relógio em 10 (dez) horas que, ao chegar, marcará exatamente o horário local do destino."
    "\nb)   poderá, no momento da partida, atrasar seu relógio em 6 (seis) horas que, ao chegar, marcará exatamente o horário local do destino."
    "\nc)   poderá, no momento da chegada, adiantar seu relógio em 6 (seis) horas para ajustá-lo ao horário local."
    "\nd)   poderá, no momento da chegada, atrasar seu relógio em 10 (dez) horas para ajustá-lo ao horário local."
    "\ne)   poderá, no momento da chegada, atrasar seu relógio em 3 (horas), já que se encontra situado na faixa UTC+3, para ajustá-lo ao horário local.",
    "\nGEOGRAFIA"
    "\n(Mackenzie 2014) Um grupo de alunos do curso de graduação em Engenharia Ambiental pretende realizar um Estudo de Campo multidisciplinar "
    "\nem uma área determinada da Ilha do Cardoso, litoral Sul do Estado de São Paulo. Para tanto, utilizarão um mapa que apresenta "
    "\nescala numérica de 1: 5000, em que será traçado um retângulo com 4 cm de altura e 2 cm de base. No terreno, a área total a ser estudada mede"
    "\na)   20 m^2"
    "\nb)   200m^2"
    "\nc)   2000m^2"
    "\nd)   20000m^2"
    "\ne)   200000m^2",
    "\nGEOGRAFIA"
    "\n(Mackenzie 2009)A respeito das recentes descobertas de jazidas petrolíferas no Brasil, considere as afirmações:"
    "\nI.   O pré-sal é uma camada de rochas-reservatório que se encontra abaixo de uma extensa camada de sal, "
        "desde o litoral do Estado do Espírito Santo até o litoral de Santa Catarina;"
    "\nII.  Tupi, Júpiter, Carioca, Pão-de-Açúcar, Iara, Guará, Bem-Te-Vi, Parati e Marfim Sul são reservatórios em área do Pré-Sal, já licitados para exploração;"
    "\nIII. A produção de petróleo nessas áreas, apesar de importante, não revela uma possível auto-suficiência brasileira no setor, "
    "\ndevido à forte dependência do consumo desse combustível no país. Então,"
    "\na) apenas I e III estão corretas." 
    "\nb) apenas I e II estão corretas." 
    "\nc) apenas II e III estão corretas." 
    "\nd) I, II e III estão corretas."
    "\ne) apenas III está correta.",
    "\nGEOGRAFIA"  
    "\n(Mackenzie 2012)"
    "\nI.   combustíveis fósseis." 
    "\nII.  energia hidrelétrica. "
    "\nIII. energia nuclear." 
    "\nIV.  etanol." 
    "\nV.   energia eólica."
    "\nDesses 5 tipos," 
    "\na)   apenas um é renovável"
    "\nb)   apenas dois são renováveis."
    "\nc)   apenas três são renováveis."
    "\nd)   apenas quatro são renováveis."
    "\ne)   todos são renováveis."]
    Quim = ["\nQUÍMICA"
            "\n(Mackenzie 2017) Assinale a alternativa que apresenta compostos químicos que possuam, respectivamente, "
            "\nligação covalente polar, ligação covalente apolar e ligação iônica."
    "\na) H2O, CO2 e NaCl"
    "\nb) CCl 4, O3 e HBr."
    "\nc) CH4, SO2 e HI."
    "\nd) CO2, O2 e KCl."
    "\ne) H2O, H2 e HCl.",
    "\nQUÍMICA"
    "\n(Mackenzie 2009) Na Terra, há dois gases no ar atmosférico que, em conseqüência de descargas elétricas em tempestades (raios),"
    "podem reagir formando monóxido de nitrogênio e dióxido de nitrogênio. As fórmulas dos reagentes e dos produtos da reação citada são respectivamente"
    "\na)   H2 e O2 ; N2 e N2O."
    "\nb)   O2 e N2O ; N2 e NO."
    "\nc)   N2 e O2 ; NO e NO2."
    "\nd)   O2 e N2 ; N2O e NO"
    "\ne)	N2 e H2 ; N2O e N2O4."]
    Bio = ["\nBIOLOGIA"
           "\n(Mackenzie 2017) O avanço da medicina é responsável pelo aumento da expectativa de vida de muitas"
           "\npessoas portadoras de genes que causam doenças graves. Assim, podemos dizer que a medicina "
           "\na) vai contra a seleção natural, prejudicando a permanência da espécie humana. "
           "\nb) vai contra a seleção natural, favorecendo a permanência da espécie humana. "
           "\nc) vai contra o processo de mutação, prejudicando a permanência da espécie humana." 
           "\nd) tem sido favorável à seleção natural, sendo positiva para a permanência da espécie humana." 
           "\ne) tem sido favorável à ocorrência da mutação, favorecendo a permanência da espécie humana.",
            "\nBIOLOGIA"
            "\n(Mackenzie 2009) Rubéola, dengue, caxumba e febre amarela são alguns tipos de doenças causadas por vírus. A respeito delas, é correto afirmar que"
    "\na)   todas podem ser combatidas por vacinação"
    "\nb)   apenas 3 delas são transmitidas por insetos."
    "\nc)   duas delas são transmitidas por mosquitos da mesma espécie."
    "\nd)   todas elas têm um hospedeiro intermediário."
    "\ne)   apenas uma delas pode ser transmitida por meio de contato direto com pessoas doentes.",
            "\nBIOLOGIA"
           "\n(Mackenzie 2012) Uma mulher daltônica"
    "\na)   poderá ter filhos do sexo masculino não daltônicos."
    "\nb    somente terá filhas daltônicas."
    "\nc)   é obrigatoriamente filha de pai daltônico."
    "\nd)   um de seus avós é certamente daltônico."
    "\ne)   poderá ser heterozigota para o gene do daltonismo.",
            "\nBIOLOGIA"
           "\n(Mackenzie 2011) A respeito da dengue, considere as afirmações abaixo."
    "\nI. A melhor forma de combate à doença é o combate ao mosquito transmissor, esteja ele na fase adulta ou no estágio larval."
    "\nII.  Pessoas com a doença não podem tomar medicamentos à base de ácido salicílico, que pode provocar quadro hemorrágico. "
    "\nIII. Tanto o mosquito macho quanto a fêmea são transmissores do vírus causador da doença. "
    "\nIV.  Todos os mosquitos dessa espécie são capazes de provocar a doença."
    "\nAssinale" 
    "\na) se somente I e II estiverem corretas." 
    "\nb) se somente I e III estiverem corretas. "
    "\nc) se somente I e IV estiverem corretas. "
    "\nd) se somente II e III estiverem corretas. " 
    "\ne) se somente II e IV estiverem corretas. "]
    Hist = ["\nHISTÓRIA"
    "\n(Mackenzie 2014) Nelson Mandela (1918-2013), líder sul-africano, o primeiro presidente da África do Sul livre e ganhador"
    "\ndo Prêmio Nobel da Paz de 1993. Sua luta durante mais de 67 anos em prol dos direitos humanos foi marcada por:"
    "\nI. Oposição ao governo representante de uma minoria branca que, desde o século XIX, governava a África do Sul e,"
    "\nmesmo rompendo com a dominação colonial inglesa, impôs à grande maioria da população negra um severo regime de segregação racial – o apartheid."
    "\nII. Resistência à longa permanência do regime racista da África do Sul, oficializado desde 1948. A extensa duração desse regime deveu-se, especialmente,"
    "pela grande indiferença por parte da opinião pública internacional à política segregacionista"
    "\nIII. A Luta junto às comunidades internacionais em defesa da liberdade e igualdade do povo sul africano. O governo sul-africano diante das sanções"
    "\ncomerciais sofridas começou a revogar o regime segregacionista em 1991,culminando na aprovação do projeto de Constituição que estabeleceu"
    "\na democracia plena, assim como pôs fim ao apartheid. Assinale a alternativa correta."
    "\na) Apenas a I está correta."
    "\nb) Apenas a II está correta."
    "\nc) Apenas a III está correta." 
    "\nd) Apenas a II e a III estão corretas."
    "\ne) Apenas a I e a III estão corretas.",
    "\nHISTÓRIA"
    "\n(Mackenzie 2012)" 
"\nMilu: Tintim, há dois, lá atrás, conversando. "
"\nTintim: Meus queridos amigos, hoje vou falar sobre seu país: a Bélgica!...."
"\nO processo histórico que possibilitou a fala de Tintim"
"\na) denomina-se colonialismo clássico e foi marcado pela conquista de territórios africanos e asiáticos"
"\nb) refere-se à conquista do Congo pela Bélgica"
"\nc) denomina-se imperialismo neocolonialista e foi marcado pela disputa e conquista de territórios africanos e asiáticos por potências europeias"
"\nd) esteve na origem dos conflitos que resultaram na Segunda Guerra Mundial"
"\ne) foi marcado pela disputa de territórios na África e Ásia por potências europeias em decorrência dos problemas gerados pelo nascente"
"\ncapitalismo concorrencial e industrial na Europa Moderna.",
    "\nHISTÓRIA"
    "\n(Mackenzie 2011) No conturbado período após a Segunda Grande Guerra, a causa imediata que levou à invasão anglo-francesa no Egito, em 1956, foi"
    "\na) a nacionalização do Canal de Suez, pelo governo egípcio, contrariando aos interesses ingleses e franceses para a região."
    "\nb) o embargo realizado pelo governo egípcio, impedindo a passagem de petroleiros franceses, ingleses e norte-americanos pelo Canal de Suez."
    "\nc) a deposição do Rei Farouk e a subida ao poder de uma junta militar ligados à ala radical do movimento islâmico."
    "\nd) o auxílio militar egípcio dado aos movimentos de libertação da Argélia e do Marrocos"
    "\ne) a nacionalização de companhias de comércio estrangeiras localizadas em território egípcio"]
    Fis = ["\nFÍSICA"
           "\n(Mackenzie 2014). Dois resistores com resistências elétricas R1 e R2 são associados em série e depois em paralelo."
           "\nCada associação é submetida à mesma diferença de potencial elétrico U. Considerando a potência dissipada"
           "\nna associação em série representada por PS e na associação em paralelo por PP , é correto afirmar que"
    "\na) PS é menor que PP ."
    "\nb) PS é maior que PP ."
    "\nc) PS é igual a PP . "
    "\nd) d) A comparação entre PS e PP dependem do valor de U"
    "\ne) n.d.a.",
        "\nFÍSICA"
    "\n(Mackenzie 2009) Um objeto real se encontra sobre o eixo principal de um espelho côncavo, de distância focal 10 cm,"
    "\ne a 20 cm do vértice do espelho. Sendo obedecidas as condições de Gauss, sua imagem é"
    "\na) real e direta."
    "\nb) real e invertida"
    "\nc) virtual e direta"
    "\nd) virtual e invertida"
    "\ne) imprópria, localizada no infinito",
        "\nFÍSICA"
    "\n(Mackenzie 2011)"
    "\nUm estudante observa que um raio luminoso, propagando-se no ar (índice de refração = 1), ao atingir a superfície de separação de um meio transparente,"
    "\nsob o ângulo de incidência i, tem o seu raio refletido perpendicular ao seu respectivo raio refratado. Após algumas considerações,"
    "\nesse estudante concluiu, corretamente, que o índice de refração desse meio é igual a"
    "\na) i"
    "\nb) tg i"
    "\nc) sen i"
    "\nd) cos i"
    "\ne) sec i"]
    quest = 0
    resp2 = ""
    while x != 7:
        erroEspec = 0
        esc1 = random.randrange(0,n)
        resp = ""
        z = 0



        #VARIÁVEL erroEspec SERVE PARA CONTAR OS ERROS ESPECÍFICOS EM MATÉRIAS E ADICIONAR NA LISTA estudar AS MATÉRIAS COM MAIS ERROS.
        erroEspec = 0
        confirm = []
        if escsD[esc1] != -1:
            if esc1 == 0:
                while True:
                    k = random.randrange(0,len(Port))
                    while k in confirm:
                        k = random.randrange(0,len(Port))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "B"
                    elif k == 1:
                        resp2 = "A"
                    elif k == 2:
                        resp2 = "D"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Port[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 1:
                        estudar.append("Portugês")
                    z = z + 1
                    if z == 1:
                        break
                confirm = []
                escsD[0] = -1
                z = 0
                x = x + 1
            elif esc1 == 1:
                while True:
                    k = random.randrange(0,len(Hist))
                    while k in confirm:
                        k = random.randrange(0,len(Hist))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "C"
                    elif k == 1:
                        resp2 = "A"
                    elif k == 2:
                        resp2 = "A"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Hist[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("História")
                    z = z + 1
                    if z == 2:
                        break
                confirm = []
                escsD[1] = -1
                z = 0
                x = x + 1
            elif esc1 == 2:
                while True:
                    k = random.randrange(0,len(Mat))
                    while k in confirm:
                        k = random.randrange(0,len(Mat))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "D"
                    elif k == 1:
                        resp2 = "A"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Mat[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Matemática")
                    z = z + 1
                    if z == 2:
                        break
                confirm = []
                escsD[2] = -1
                x = x + 1
                z = 0
            if esc1 == 3:
                while True:
                    k = random.randrange(0,len(Fis))
                    while k in confirm:
                        k = random.randrange(0,len(Fis))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "A"
                    elif k == 1:
                        resp2 = "A"
                    elif k == 2:
                        resp2 = "A"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Fis[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Física")
                    z = z + 1
                    if z == 2:
                        break
                confirm = []
                escsD[3] = -1
                x = x + 1
                z = 0
            elif esc1 == 4:
                while True:
                    k = random.randrange(0,len(Quim))
                    while k in confirm:
                        k = random.randrange(0,len(Quim))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "D"
                    elif k == 1:
                        resp2 = "C"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Quim[k])
                    resp = str(input("Digite a letra da resposta correta: ")) 
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: ")) 
                    print(resp,resp2)
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Química")
                    z = z + 1
                    if z == 2:
                        break
                confirm = []
                escsD[4] = -1
                x = x + 1
                z = 0
            elif esc1 == 5:
                while True:
                    #se a pergunta já foi sorteada, o jogo escolhe outra automaticamente.
                    k = random.randrange(0,len(Geog))
                    while k in confirm: #confirm é a lista que  é formada toda vez que uma questão é escolhida
                        k = random.randrange(0,len(Geog))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "C"
                    elif k == 1:
                        resp2 = "D"
                    elif k == 2:
                        resp2 = "B"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Geog[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 1:
                        estudar.append("Geografia")
                    z = z + 1
                    if z == 1:
                        break
                confirm = []
                escsD[5] = -1
                x = x + 1
                z = 0
            elif esc1 == 6:
                while True:
                    k = random.randrange(0,len(Bio))
                    while k in confirm:
                        k = random.randrange(0,len(Bio))
                    confirm.append(k)
                    if k == 0:
                        resp2 = "B"
                    elif k == 1:
                        resp2 = "C"
                    elif k == 2:
                        resp2 = "C"
                    elif k == 3:
                        resp2 = "A"
                    quest = quest + 1
                    print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  » QUESTÃO",quest," « ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
                    print(Bio[k])
                    resp = str(input("Digite a letra da resposta correta: "))
                    while resp.upper() != "A" and resp.upper() != "B" and resp.upper() != "C" and resp.upper() != "D" and resp.upper() != "E":
                        resp = str(input("Digite somente letras disponíveis: "))
                    if resp.upper() == resp2:
                        pontos = pontos + 1
                    else:
                        erros = erros + 1
                        erroEspec = erroEspec + 1
                    if erroEspec == 2:
                        estudar.append("Biologia")
                    z = z + 1
                    if z == 2:
                        break
                confirm = []
                escsD[6] = -1
                x = x + 1
                z = 0
        else:
            x = x + 0
    else:
        return pontos,erros
def saida():
    print('\n'
          '\n'
          '\n'
          '\n'
      '                                     __..._   _...__\n'
      '                                _..-"      `Y`      "-._\n'
      '                                \  Análise  |  desem-   /\n'
      '                                \\   de     |  penho   //\n'
      '                                \\\         |         ///\n'
      '                                 \\\ _..---.|.---.._ ///\n'
      '                                  \\`_..---.Y.---.._`//\n'
      '                                  '                  '\n')
    print('                              chegou a hora da verdade!')
    time.sleep(2)
    if dificuldade.upper() == "FÁCIL" or dificuldade.upper() == "FACIL":
        print("\n"*3)
        print('═══════════════════════════════════════RESULTADOS═════════════════════════════════════════\n'
              '                                                                                          \n'
              '                                                                                          \n'
              ' Matérias para se estudar mais:',estudar,'                                \n'
              ' ACERTOS:',pontosF[0],'ERROS:',pontosF[1],'                               \n'
              '                                                                                          \n'
              '══════════════════════════════════════════════════════════════════════════════════════════\n')        
        if pontos==8:
            baú()
            print('você conseguiu pontos o suficiente para abrir o maior baú! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
'             ___________\n'
'             ._==_==_=_.\n'
'            .-\:      /-.\n'
'           | (|:.     |) |\n'
'            *-|:.     |-*\n'
'              \::.    /\n'
'               *::. .*\n'
'                 ) (\n'
'               _.' '._\n'
'              `"""""""`\n')
            print('Parabéns Vestibulando, você ganhou o maior troféu do jogo! Continue assim e bom vestibular!!! #PartiuMack')
        elif pontos>=4 and pontos<=7:
            baú()
            print('você conseguiu pontos o suficiente para abrir o prêmio de prata! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
      

              ' .-=========-.\n'
              ' \*-=======-*/\n'
              ' _|   .=.   |_\n'
              '((|  {{2}}  |))\n'
              ' \|   /*\   |/\n'
              '  \__ *** __/\n'
              '    _`) (`_\n'
              ' _ /_______\_\n'
              '/_____________\ \n')
            print('É, ta quase lá! Mais um pouquinho e você G A B A R I T A essa prova!')
        else:
            baú()
            print('poxa! você conseguiu pontos apenas para abrir o menor baú! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
                    '              .__.\n'
                    '             (|  |)\n'
                    '              (  )\n'
                    '              _)(_ \n')
            print('Troféuzinho de participação??? Tá precisando estudar mais pro vestibular. Corre que ainda dá tempo!O maior prêmio é a sua vaga!.')
    
    else:
        print("\n"*3)
        print('═══════════════════════════════════════RESULTADOS═════════════════════════════════════════\n'
              '                                                                                          \n'
              '                                                                                          \n'
              ' Matérias para se estudar mais:',estudar,'                                                 \n'
              ' ACERTOS:',pontosFD[0],'ERROS:',pontosFD[1],'                                              \n'
              '                                                                                          \n'
              '══════════════════════════════════════════════════════════════════════════════════════════\n')
        
        if pontos>=10 and pontos<=12:
            baú()
            print('você conseguiu pontos o suficiente para abrir o maior baú! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
'             ___________\n'
'             ._==_==_=_.\n'
'            .-\:      /-.\n'
'           | (|:.     |) |\n'
'            *-|:.     |-*\n'
'              \::.    /\n'
'               *::. .*\n'
'                 ) (\n'
'               _.' '._\n'
'              `"""""""`\n')
            print('Parabéns Vestibulando, você ganhou o maior troféu do jogo! Continue assim e bom vestibular!!! #PartiuMack')
        elif pontos>=5 and pontos<=9:
            baú()
            print('você conseguiu pontos o suficiente para abrir o prêmio de prata! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
      

              ' .-=========-.\n'
              ' \*-=======-*/\n'
              ' _|   .=.   |_\n'
              '((|  {{2}}  |))\n'
              ' \|   /*\   |/\n'
              '  \__ *** __/\n'
              '    _`) (`_\n'
              ' _ /_______\_\n'
              '/_____________\ \n')
            print('É, ta quase lá! Mais um pouquinho e você G A B A R I T A essa prova!')
        else:
            baú()
            print('poxa! você conseguiu pontos apenas para abrir o menor baú! Aperte enter para abrir e ver seu prêmio')
            input()
            print('\n'
                    '  .__.\n'
                    ' (|  |)\n'
                    '  (  )\n'
                    '  _)(_ \n')
            print('Troféuzinho de participação??? Tá precisando estudar mais pro vestibular. Corre que ainda dá tempo!O maior prêmio é a sua vaga!')

def creditos():
    print('\n'
        '            ╔═════════════════════════════════════════════════════════════════════╗\n'
        '            ║                        OBRIGADO POR JOGAR!!!                        ║\n'
        '            ╠═════════════════════════════════════════════════════════════════════╣\n'   
        '            ║Classificação indicativa: 14+                                        ║\n'
        '            ║Desenvolvedores: Beatriz Duque | João Pedro Belforti                 ║\n'
        '            ║Perguntas Fáceis: Brasil Escola                                      ║\n'
        '            ║Perguntas Difíceis: VestibularMackenzie                              ║\n'
        '            ╚═════════════════════════════════════════════════════════════════════╝\n')
    time.sleep(1)
    print('\n'
    '                         AGRADECIMENTOS:')
    time.sleep(1)
    print('\n'
    ' Professora Kassya')
    time.sleep(1)
    print('\n'
    ' Professor Jean')
    time.sleep(1)
    print('\n'
    ' Universidade Presbiteriana Mackenzie')
    
def sair():
    False

def main():
    AbrtJOGO()
    Inicio()
    saida()
    creditos()
    sair()

#ProgramaPrincipal 
main()
