# -*- coding: utf-8 -*-

#http://pydoc.net/infer/0.1/infer.classify/

###biblioteca para processamento de linuguagem natural.
import nltk

### baixar todos os pacotes do nltk
#nltk.download()

### Modulo para ler import requivo csv
import csv

### Modulo para criar a matriz de confusão.
#from nltk.metrics import ConfusionMatrix

#precision
from nltk.metrics import *

### Módulo para trabalhar com aleatório.
from random import randint

### Modulo para implementar interface gráfica
from tkinter import *

class IptablesLearning():
    ### O construtor da classe IpTablesLearning cria os elementos gráficos (widgets).
    def __init__(self, largura, altura, master=None):
        self.master = master
        self.largura = largura
        self.altura = altura

        self.Fundo = Frame(master)

        self.Fundo.pack(fill=BOTH, expand=1)

        self.tam_borda_titulo = int(int(self.largura) * (float(0.065)))
        self.tam_borda_esq = int(int(self.largura) * (float(0.10)))
        self.tam_borda_botoes = int(int(self.largura) * (float(0.35)))
        self.tam_borda_interior = int(int(self.largura) * (float(0.001)))

        # primeiro frame do formulario
        self.frame_titulo = Frame(self.Fundo, width=self.largura, height=50)
        self.frame_titulo.pack(side=TOP)
        #self.frame_titulo.pack_propagate(0)

        self.label = Label(self.frame_titulo, text='Digite a sua dúvida.', font=('Arial', 14, 'bold'))
        self.label.pack(side=LEFT, padx=self.tam_borda_titulo)

        # segundo frame do formulario
        self.frame_top = Frame(self.Fundo, width=self.largura, height=200)
        self.frame_top.pack(side=TOP)
        self.frame_top.pack_propagate(0)

        self.pergunta = Label(self.frame_top, text='Pergunta:')
        self.pergunta.pack(side=LEFT, anchor=N)

        self.pesquisa = Text(self.frame_top, width=98, height=195)
        self.pesquisa.pack(side=LEFT)
        self.pesquisa.pack_propagate(0)

        # terceiro frame do formulario
        self.frame_botoes = Frame(self.Fundo, width=self.largura, height=30)
        self.frame_botoes.pack(side=TOP)
        self.frame_botoes.pack_propagate(0)

        self.botao = Button(self.frame_botoes, text='Pesquisar', width=10, command=lambda: self.Pesquisar())
        self.botao.pack(side=LEFT, padx=(self.tam_borda_botoes, 0))
        self.botao.pack_propagate(0)

        self.sair = Button(self.frame_botoes, text='Sair', width=10, command=self.Sair)
        self.sair.pack(side=LEFT, padx=(20, self.tam_borda_interior))
        self.sair.pack_propagate(0)

        self.frame_saida = Frame(self.Fundo, width=self.largura, height=300)
        self.frame_saida.pack(side=TOP)
        self.frame_saida.pack_propagate(0)

        self.frame_regras = Frame(self.frame_saida, width=self.largura, height=150)
        self.frame_regras.pack(side=TOP)
        self.frame_regras.pack_propagate(0)

        self.regras = Label(self.frame_regras, justify=LEFT, wraplength=self.largura)
        self.regras.pack(side=TOP, anchor=NW)
        self.regras.pack_propagate(0)

        self.frame_explicacao = Frame(self.frame_saida, width=self.largura, height=150)
        self.frame_explicacao.pack(side=TOP)
        self.frame_explicacao.pack_propagate(0)

        self.explicacao = Label(self.frame_explicacao, justify=LEFT, wraplength=self.largura)
        self.explicacao.pack(side=TOP, anchor=NW)
        self.explicacao.pack_propagate(0)



    def Pesquisar(self):

        ### pega as informações digitadas no widget Text.
        pergunta = self.pesquisa.get(1.0, END)

        ### converte todas as palavras em minusculas.
        pergunta = pergunta.lower()

        #print('Frase em minuscula..:{}'.format(pergunta))

        ### Remove Pontuações.
        pergunta = self.RemovePontuacoes(pergunta)

        testestemming = []
        stemer = nltk.stem.RSLPStemmer()

        for (palavrastreinamento) in pergunta.split():
            comstem = [p for p in palavrastreinamento.split()]
            testestemming.append(str(stemer.stem(comstem[0])))

        #print (testestemming)
        novo = aplicacao.extrator_palavras(testestemming)
        resultado = aplicacao.classificador.classify(novo)

        ### Imprime a distribuição de probabilidade.
        #distribuicao = aplicacao.classificador.prob_classify(novo)
        #for classe in distribuicao.samples():
        #    print ("{} {:.2f}".format(classe, distribuicao.prob(classe)))

        #print ("resultado..:{}".format(resultado))

        if (resultado == 'https brute force'):
            lista_regras = []
            regra0 = 'Regras:'
            lista_regras.append(regra0)

            regra1 = "iptables -N SSL-Brute-Force"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -m tcp -p tcp --dport 443 -j SSL-Brute-Force"
            lista_regras.append(regra2)

            regra3 = "iptables -A SSL-Brute-Force -m state --state NEW -m recent --set --name SSL --rsource"
            lista_regras.append(regra3)

            regra4 = "iptables -A SSL-Brute-Force -m state --state NEW -m recent --rcheck --seconds 600 --hitcount 5 --name SSL --rsource -j LOG --log-prefix '[SSL Brute Force]'"
            lista_regras.append(regra4)

            regra5 = "iptables -A SSL-Brute-Force -m state --state NEW -m recent --rcheck --seconds 600 --hitcount 5 --name SSL --rsource -j DROP"
            lista_regras.append(regra5)

            regra6 = "iptables -A SSL-Brute-Force -j ACCEPT"
            lista_regras.append(regra6)

            # print (lista_regras, end='\n')

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \nOs cinco comandos primeiro, descarta as novas conexões com destino a porta 443, para novas conexões com a mesma origem, com um tempo menor que 10 minutos e com mais de 5 tentativas de conexão. Além disso, para todas as novas conexões bloqueadas é gerado um arquivo de log. O último comando aceita as novas conexões que não foram restringidas pelos comandos anteriores. '
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)


        elif (resultado == 'http brute force'):

            lista_regras = []
            regra1 = "iptables -N HTTP-Brute-Force"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -m tcp -p tcp --dport 80 -j HTTP-Brute-Force"
            lista_regras.append(regra2)

            regra3 = "iptables -A HTTP-Brute-Force -m state --state NEW -m recent --set --name HTTP --rsource"
            lista_regras.append(regra3)

            regra4 = "iptables -A HTTP-Brute-Force -m state --state NEW -m recent --rcheck --seconds 600 --hitcount 5 --name SSL --rsource -j LOG --log-prefix '[HTTP Brute Force]'"
            lista_regras.append(regra4)

            regra5 = "iptables -A HTTP-Brute-Force -m state --state NEW -m recent --rcheck --seconds 600 --hitcount 5 --name HTTP --rsource -j DROP"
            lista_regras.append(regra5)

            regra6 = "iptables -A HTTP-Brute-Force -j ACCEPT"
            lista_regras.append(regra6)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os cinco comandos primeiro, descarta as novas conexões com destino a porta 80, para novas conexões com a mesma origem, com um tempo menor que 10 minutos e com mais de 5 tentativas de conexão. Além disso, para todas as novas conexões bloqueadas é gerado um arquivo de log. O último comando aceita as novas conexões que não foram restringidas pelos comandos anteriores.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'ssh brute force'):
            lista_regras = []
            regra1 = "iptables -A INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --name CONSSH --set -j LOG --log-prefix 'CONEXÕES SSH'"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --name 'CONSSH' --rcheck --seconds 180 --hitcount 2 -j DROP"
            lista_regras.append(regra2)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino a porta 22, para novas conexões com a mesma origem, com um tempo menor que 3 minutos e com mais de 2 tentativas de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'syn flooding'):

            lista_regras = []
            regra1 = "echo 1 > /proc/sys/net/ipv4/tcp_syncookies"
            lista_regras.append(regra1)

            regra2 = "echo 2048 > /proc/sys/net/ipv4/tcp_max_syn_backlog"
            lista_regras.append(regra2)

            regra3 = "echo 3 > /proc/sys/net/ipv4/tcp_synack_retries"
            lista_regras.append(regra3)

            regra4 = "iptables -N syn-flood"
            lista_regras.append(regra4)

            regra5 = "iptables -A INPUT -i $WAN -p tcp --syn -j syn-flood"
            lista_regras.append(regra5)

            regra6 = "iptables -A syn-flood -m limit --limit 10/s --limit-burst 4 -j RETURN"
            lista_regras.append(regra6)

            regra7 = "iptables -A syn-flood -j DROP"
            lista_regras.append(regra7)

            explicacao = []
            texto = 'Explicação: Os três primeiros comandos acima, ativa syn cookies, backlog e synack_retires para sistemas operacionais linux. Os últimos quatro comandos, descarta as conexões syn tcp, com um tempo menor que 10 segundos e com um máximo de 4 tentativas de conexão.'
            explicacao.append(texto)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                print ("regras..:{}".format(regras))
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'form login brute force'):

            lista_regras = []
            regra1 = "iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT"
            lista_regras.append(regra1)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n O comando acima, aceita conexões com destino a porta 80, com um tempo menor que 25 minutos e com um máximo de 100 tentativas de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'rdp brute force'):

            lista_regras = []
            regra1 = "iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -p tcp --dport 3389 -m recent --update --seconds 180 -j DROP"
            lista_regras.append(regra2)

            regra3 = "iptables -A INPUT -p tcp --dport 3389 --tcp -flags syn,ack,rst syn -m recent --set -j ACCEPT"
            lista_regras.append(regra3)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino a porta 3389, para novas conexões com a mesma origem, com um tempo menor que 3 minutos. As novas conexões estabelecidas com as flags syn,ack,rst definidas são aceitas.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'ftp brute force'):

            lista_regras = []
            regra1 = "iptables -A INPUT -i eth0 -p tcp -m multiport --dports 20, 21 -m state --state NEW -m recent --set --name FTP"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -i eth0 -p tcp -m multiport --dports 20, 21 -m state --state NEW -m recent --check --seconds 60 --hitcount 4 --rttl --name FTP -j DROP"
            lista_regras.append(regra2)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino as portas 20, 21, para novas conexões com a mesma origem, com um tempo menor que 1 minuto e com mais de 4 tentativas de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'telnet brute force'):

            lista_regras = []
            regra1 = "iptables -A INPUT -p tcp --dport 23 -j DROP"
            lista_regras.append(regra1)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n O comando acima, descarta todas as conexões com destino a porta 23, por se tratar de uma servidor inseguro que não criptografa os dados transmitidos entre o servidor e cliente.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'mysql brute force'):

            lista_regras = []
            regra1 = "iptables -A INPUT -p tcp -m state --syn --state NEW --dport 3306 -m limit --limit 1/minute --limit -burst 1 -j ACCEPT"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -p tcp -m state --syn --state NEW --dport 3306 -j DROP"
            lista_regras.append(regra2)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino a porta 3306, para novas conexões com a mesma origem, com um tempo menor que 1 minuto e com mais de 1 tentativa de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'firebird brute force'):

            lista_regras = []

            regra1 = "iptables -A INPUT -p tcp -m state --syn --state NEW --dport 3050 -m limit --limit 1 / minute --limit -burst 1 -j ACCEPT"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -p tcp -m state --syn --state NEW --dport 3050 -j DROP"
            lista_regras.append(regra2)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino a porta 3050, para novas conexões com a mesma origem, com um tempo menor que 1 minuto e com mais de 1 tentativa de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

        elif (resultado == 'samba brute force'):

            lista_regras = []

            regra1 = "iptables -A INPUT -i eth0 -p udp --dport 137 -m state --state NEW -m recent --set --name  netbios-ns"
            lista_regras.append(regra1)

            regra2 = "iptables -A INPUT -i eth0 -p udp --dport 137 -m state --state NEW -m recent --update --seconds 20 --hitcount 2 --rttl --name netbios-ns -j DROP"
            lista_regras.append(regra2)

            regra3 = "iptables -A INPUT -i eth0 -p udp --dport 138 -m state --state NEW -m recent --set --name netbios-dgm"
            lista_regras.append(regra3)

            regra4 = "iptables -A INPUT -i eth0 -p udp --dport 138 -m state --state NEW -m recent --update --seconds 20 --hitcount 2 --rttl --name netbios-dgm -j DROP"
            lista_regras.append(regra4)

            regra5 = "iptables -A INPUT -i eth0 -p tcp --dport 139 -m state --state NEW -m recent --set --name netbios-ssn"
            lista_regras.append(regra5)

            regra6 = "iptables -A INPUT -i eth0 -p tcp --dport 139 -m state --state NEW -m recent --update --seconds 20 --hitcount 2 --rttl --name netbios-ssn -j DROP"
            lista_regras.append(regra6)

            regra7 = "iptables -A INPUT -i eth0 -p tcp --dport 445 -m state --state NEW -m recent --set --name microsoft-ds"
            lista_regras.append(regra7)

            regra8 = "iptables -A INPUT -i eth0 -p tcp --dport 445 -m state --state NEW -m recent --update --seconds 20 --hitcount 2 --rttl --name microsoft-ds -j DROP"
            lista_regras.append(regra8)

            ### atualiza o widget Label self.regras com as informações contidas na lista de string lista_regras.
            total_regras = ''
            for regras in lista_regras:
                total_regras = total_regras + regras + '\n'

            self.regras.config(text=total_regras)

            explicacao = []
            texto = 'Explicação: \n Os comandos acima, descarta as novas conexões com destino as portas 137, 138, 139 e 445, para novas conexões com a mesma origem, com um tempo menor que 20 segundos e com mais de 2 tentativas de conexão.'
            explicacao.append(texto)

            total_texto = ''
            for texto in explicacao:
                total_texto = total_texto + texto + '\n'

            ### atualiza o widget Label self.explicacao com as informações da variavel explicacao.
            self.explicacao.config(text=total_texto)

    def Sair(self):
        self.master.destroy()

    def preProcessamento(self, basetreinamento, baseteste):

        ### Cria uma lista de stopwords com o uso da biblioteca nltk.
        self.stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

        ### acrescenta novas stopwords para melhorar o algoritmo naive bayes.
        self.stopwordsnltk.append('vou')
        self.stopwordsnltk.append('tão')
        self.stopwordsnltk.append('vai')

        ### A variavel frasescomstemming guarda a base de dados preprocessada, ou seja, guarda as frases sem
        ### os stopwords e com apenas os radicais da palavras.
        self.frasescomstemmingtreinamento = self.aplicastemment(basetreinamento)
        self.frasecomstemmingteste = self.aplicastemment(baseteste)

        self.palavrastreinamento = self.buscapalavras(self.frasescomstemmingtreinamento)
        self.palavrasteste = self.buscapalavras(self.frasecomstemmingteste)

        self.frequenciatreinamento = self.busca_frequencia(self.palavrastreinamento)
        self.frequenciateste = self.busca_frequencia(self.palavrasteste)

        ### Imprime as 50 palavras mais frequentes.
        #print (self.frequenciateste.most_common(50))

        self.palavras_unicas_treinamento = self.busca_palavras_unicas(self.frequenciatreinamento)
        self.palavras_unicas_teste = self.busca_palavras_unicas(self.frequenciateste)

        #print ("Palavras Unicas treinamento..:{}".format(self.palavras_unicas_treinamento))
        #print("Palavras Unicas teste..:{}".format(self.palavras_unicas_teste))

        #self.caracteristicasfrase = self.extrator_palavras(['am', 'nov', 'dia'])

        ### A função apply_features vai fazer o preenchimento dos registros dos dados previsores com os valores True ou False.
        self.basecompletatreinamento = nltk.classify.apply_features(self.extrator_palavras,
                                                                    self.frasescomstemmingtreinamento)
        self.basecompletateste = nltk.classify.apply_features(self.extrator_palavras, self.frasecomstemmingteste)

        ### Pega os dados e cria a tabela de probabilidade.
        self.classificador = nltk.NaiveBayesClassifier.train(self.basecompletatreinamento)

        ### Mostra as classes alvo usadas pelo classificador.
        #print (self.classificador.labels())

        ### Imprime os radicais da 10 palavras mais informativas (tem maior peso).
        #print (self.classificador.show_most_informative_features(10))

    def ImprimeAcuracia(self):
        ### Mostrar a precisão do nosso algoritmo.
        return nltk.classify.accuracy(self.classificador, self.basecompletateste)

    def Avaliacao(self, matriz, beta=1):
        #Compute various performance metrics.

        # A dictionary with an entry for each metric.
        performance = dict()

        performance['confusionmatriz'] = matriz

        #Number of unique labels; used for computing medias.
        num_rotulos = len(matriz._confusion)

        #Accurancy
        performance['accuracy'] = matriz._correct / matriz._total
        #print (performance['accuracy'])

        #Recall
        media = media_ponderada = 0
        for label, index in matriz._indices.items():
            verdadeiros_positivos = matriz._confusion[index][index]
            total_positivos = sum(matriz._confusion[index])
            if total_positivos == 0:
                recall = int(verdadeiros_positivos == 0)
            else:
                recall = verdadeiros_positivos / total_positivos
            media += recall
            media_ponderada += recall * total_positivos
            key = 'recall-{0}'.format(label)
            performance[key] = recall
        performance['media recall'] = media / num_rotulos
        performance['recall ponderado'] = media_ponderada / matriz._total

        #Precision
        #Correctly classified positives / Total predicted as positive
        media = media_ponderada = 0
        for label, index in matriz._indices.items():
            verdadeiros_positivos = matriz._confusion[index][index]
            total_positivos = sum(matriz._confusion[index])
            predicted_positive = 0 # substract verdadeiros_positivos to get false_positive
            for i in range(num_rotulos):
                predicted_positive += matriz._confusion[i][index]
            if verdadeiros_positivos == predicted_positive == 0:
                precision = 1
            else:
                precision = verdadeiros_positivos / predicted_positive

            media += precision
            media_ponderada += precision * total_positivos
            key = 'precisao-{0}'.format(label)
            performance[key] = precision
        performance['media precisao'] = media / num_rotulos
        performance['precisao ponderada'] = media_ponderada / matriz._total


        '''
        #F-Mesasure
        #((1 + B ** 2) * precision * recall) / ((B ** 2) * precision) + recall)
        media = media_ponderada  = 0
        for label, index in matriz._indices.items():
            recall = performance['recall-{0}'.format(label)]
            precision = performance['precisao-{0}'.format(label)]
            total_positivos = sum(matriz._confusion[index])
            numer = ((1 + beta ** 2) * precision * recall)
            denom = (((beta ** 2) * precision) + recall)
            if denom  > 0:
                f_measure = numer / denom
            else:
                f_measure = 0
            media += f_measure
            media_ponderada += f_measure * total_positivos
            key = 'f-{0}'.format(label)
            performance[key] = f_measure
        performance['media f_measure'] = media / num_rotulos
        performance['f_measure ponderado'] = media_ponderada / matriz._total
        '''

        # F1-score
        # F1 = 2 * ((precision * recall) / (precision + recall))
        media = media_ponderada = 0
        for label, index in matriz._indices.items():
            recall = performance['recall-{0}'.format(label)]
            precision = performance['precisao-{0}'.format(label)]
            total_positivos = sum(matriz._confusion[index])
            numerador = (2 * precision * recall)
            denominador = precision + recall
            if denominador > 0:
                f1 = numerador / denominador
            else:
                f1 = 0
            media += f1
            media_ponderada += f1 * total_positivos
            key = 'f1-{0}'.format(label)
            performance[key] = f1
        performance['media f1'] = media / num_rotulos
        performance['f1 ponderado'] = media_ponderada / matriz._total

        #print (performance)
        return performance


    def ImprimeErros(self):
        erros = []
        for (frase, classe) in self.basecompletateste:
            #print (frase)
            #print (classe)
            resultado = self.classificador.classify(frase)
            if resultado != classe:
                erros.append((classe, resultado, frase))

        #O loop abaixo verifica as frases que estÃ£o sendo classificadas de forma
        #errada. E realizado um print da classe que deveria ser alcançada, o resultado
        #obtido pela rede neural e a frase em questão.

        for (classe, resultado, frase) in erros:
            print ("Classe..:{} // Classificado..:{} Frase..:{}".format(classe, resultado, frase))


    ### Cria a matriz de confusão.
    def GeraMatrizConfusao(self):
        esperado = []
        previsto = []

        for (frase, classe) in self.basecompletateste:
            resultado = self.classificador.classify(frase)

            previsto.append(resultado)
            esperado.append(classe)

            self.matriz = ConfusionMatrix(esperado, previsto)

        ### retorna a matriz de confusão
        return self.matriz

    ### criar uma lista de stopwords é util quando queremos remover stopwords
    ### muito especificas para o escopo de nossa aplicaÃ§Ã£o.
    def remove_stopwords(self, texto):
        frases = []
        for (palavras, classe) in texto:
            semstop = [p for p in palavras.split() if p not in self.stopwordsnltk]
            frases.append((semstop, classe))
        return frases

    ### remove as stopwords e tira os radicais das palavras para reduzir a dimensionalidade.
    def aplicastemment(self, texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasesstemming = []
        for (palavras, classe) in texto:
            comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in self.stopwordsnltk]
            frasesstemming.append((comstemming, classe))
        return frasesstemming

    def buscapalavras(self, frases):
        todaspalavras = []
        for (palavras, emocao) in frases:
            todaspalavras.extend(palavras)
        return todaspalavras

    def busca_frequencia(self, palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

    def busca_palavras_unicas(self, frequencia):
        freq = frequencia.keys()
        return freq

    def extrator_palavras(self, documento):
        doc = set(documento)
        caracteristicas = {}
        for palavras in self.palavras_unicas_treinamento:
            caracteristicas['%s' % palavras] = (palavras in doc)
        return caracteristicas

    def RemovePontuacoes(self, documento):
        pontuacoes = ['.', ',', '?', '!', ':', '...', '-']

        for i in range(0, len(pontuacoes)):
            if pontuacoes[i] == '-':
                documento = documento.replace(pontuacoes[i], " ")
            else:
                documento = documento.replace(pontuacoes[i],"")

        return documento

    def k_pastas(self, basecompleta, k):
        n = k
        splited = []
        len_l = len(basecompleta)

        for i in range(n):
            start = int(i * len_l / n)
            end = int((i + 1) * len_l / n)
            splited.append((basecompleta[start:end]))
            #print("k_pastas..:{}".format(splited))  # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]

            if start == 0:
                basetreinamento=basecompleta[end:len_l-1]
            elif start != 0 and end != len_l:
                baseTreino1 = basecompleta[0:start-1]
                baseTreino2 = basecompleta[end+1:]
                basetreinamento = baseTreino1 + baseTreino2
            elif end == len_l:
                basetreinamento = basecompleta[0:start-1]

            self.preProcessamento(basetreinamento, splited[i])


    def EmbaralhaDados(self, base):
        swap = ''
        for i in range(0, len(base)-1):
            pos1 = randint(0, len(base)-1)
            pos2 = randint(0, len(base)-1)
            swap = base[pos1]
            base[pos1] = base[pos2]
            base[pos2] = swap
        return base


def CarregaArquivo():
    X = []

    arquivo = open('perguntas-completas-banco-dados-iptables-ataques.csv', 'r', encoding='utf-8')
    leitor = csv.reader(arquivo)
    #next(leitor)

    for pergunta,classe in leitor:
        X.append((pergunta, classe))

    return X



if __name__ == "__main__":


    ### A variavel X contem as frases, as quais receberam um preprocessamento.
    ### Esse preprocessamento tem o objetivo de remover os caracteres especiais (numeros,etc) e a acentuação.
    ### Os caracteres especiais e a acentuação atrabalha o algoritmo de realizar o aprendizado.

    X=CarregaArquivo()
    tamanhoBase=len(X)

    root = Tk()
    root.resizable(width=False, height=False)
    #largura = root.winfo_screenwidth()
    #altura = root.winfo_screenheight()

    ### Criando um objeto para a classe IptablesLearning.
    aplicacao = IptablesLearning(850, 580, root)

    ### Embaralha os dados
    baseEmbaralhada=aplicacao.EmbaralhaDados(X)

    ### Chama o algoritmo da K-pastas para melhorar a performance de treinamento da
    ### rede neural.
    ### O valor 5 representa o tamanho dos blocos de particionamento utilizados pelo algoritmo k-pastas
    aplicacao.k_pastas(baseEmbaralhada, 5)

    ### Cria matriz de confusão.
    matrizconfusao=aplicacao.GeraMatrizConfusao()

    ### Calculando as metricas principais
    performance = aplicacao.Avaliacao(matrizconfusao, 1)

    ### Imprime a Acuracia
    #print ("Acuracia ..:{:.2f}%".format(aplicacao.ImprimeAcuracia()*100))

    ### Mostra a porcentagem de acertos do classificador. A acurácia é a quantidade de acertos dividido pelo total.
    #print ('Acurácia..:{:.2f}%'.format(performance['accuracy']*100))

    ### Obtem uma lista de tuplas a partir da posição 1.
    lista = list(performance.items())[1:]

    #print ("lista..:{}".format(lista))

    ###Imprime os resultados das métircas implementadas no método Avaliacao.
    for index in range(len(lista)):
        print ("{}..:{:.2f}%".format(lista[index][0], lista[index][1]*100))

    ###Mostra a matriz de confusão
    print("A matriz de confusão..:{}".format(matrizconfusao))


    ### Imprime dos erros.
    #aplicacao.ImprimeErros()

    ### Define o tamanho da janela
    aplicacao.master.geometry("%dx%d+%d+%d" % (850, 580, 0, 0))

    ### Define o titulo da janela.
    aplicacao.master.title('Sistema de Aprendizagem de Firewall')


    ### aplicacao.master.wm_attributes('-fullscreen', 1)
    root.mainloop()

    ### Define o titulo da janela.
    # aplicacao.master.title('Sistema de Aprendizagem de Firewall')

    ### Tamanho maximo para ser rediomensionado pelo mouse
    # aplicacao.master.maxsize(1024,768)

    ### Tamanho que a tela serÃ¡ exibida ao iniciar.
    # aplicacao.master.geometry("800x600")


