# clp-programmer-python

Authors: Alexandre Monteiro Londe, Esdras Santos de Oliveira (Arduino/Hardware)
           Júlia Cordeiro e Silva, Nathan Silva Rodrigues (Python Interface)

ENGLISH
This code simulates a PLC programming interface, allowing the user to create a simple program using logic operators AND (^), OR (|) and NOT (!), accessing eight digital inputs and outputs (present in the Arduino), and also sixteen boolean memories (handled exclusively by the python software). The Arduino acts as a slave, only answering to serial queries from the python software (estabilish connection, read inputs, write outputs). The communication protocol was custom made for this application. The python interface also allows the user to load and save programs in simple text, and allows tracking the state of the inputs, outputs and boolean memories.

PORTUGUÊS
Esse código simula uma interface de programação de CLP, permitindo o usuário criar programas simples utilizando operadores lógicos AND (^), OR (|) e NOT (!), acessando oito entradas e saidas digitais (presentes no Arduino), e também dezesseis memórias booleanas (gerenciadas exclusivamente pelo software python). O Arduino atua como escravo, respondendo apenas a requisições seriais do software python (estabelecer conexão, ler entradas, escrever saidas). Um protocolo de comunicação específico foi criado para a aplicação. A interface python também permite o usuário salvar e carregar programas em texto simples, e permite acompanhar o estado das entradas, saídas e memórias booleanas.

Engenharia de Computação, IFTM, Campus Uberaba Parque Tecnológico 2022/2
