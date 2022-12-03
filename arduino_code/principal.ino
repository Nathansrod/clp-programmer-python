// ========== DECLARAÇÃO DE VARIÁVEIS ==========
// ========== LEDS
int led1 = 9;
int led2 = 8;
int led3 = 7;
int led4 = 6;
int led5 = 5;
int led6 = 4;
int led7 = 3;
int led8 = 2;

// ========== BOTÕES
int btn1  = 22;
int btn2  = 24;
int btn3  = 26;
int btn4  = 28;
int btn5  = 30;
int btn6  = 32;
int btn7  = 34;
int btn8  = 36;

// ========== ESTADO DO BOTÃO
int pressionado1 = 0;
int pressionado2 = 0;
int pressionado3 = 0;
int pressionado4 = 0;
int pressionado5 = 0;
int pressionado6 = 0;
int pressionado7 = 0;
int pressionado8 = 0;


// ========== VARIÁVEIS DE MANIPULAÇÃO
char cmd;
String instrucaoinicial;
String instrucaoFinal;
char estadoBtns[11];



// ========== INSTANCIAÇÃO........... ==========
void setup() {
  // ========== LEDS
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);


  // ========== BOTÕES
  pinMode(btn1, INPUT);
  pinMode(btn2, INPUT);
  pinMode(btn3, INPUT);
  pinMode(btn4, INPUT);
  pinMode(btn5, INPUT);
  pinMode(btn6, INPUT);
  pinMode(btn7, INPUT);
  pinMode(btn8, INPUT);

  Serial.begin(9600); //Inicia o Monitor Serial
}



// ========== CÓDIGO DE REPETIÇÃO.... ==========
void loop() {
  // ========== VALIDAÇÃO DA INSTRUÇÃO RECEBIDA
  if (Serial.available() > 0) {

    //PEGAR A INSTRUCAO
    instrucaoinicial = Serial.readStringUntil('#');

    if (instrucaoinicial[0] == '@')
    {
      instrucaoFinal = instrucaoinicial.substring(1, instrucaoinicial.length());

      if(instrucaoFinal=="ini")
      {
          Serial.print("@ack#");
      }

      if(instrucaoFinal=="read")
      {  // ========== ESTADO DO BOTÃO
        pressionado1 = digitalRead(btn1);  
        pressionado2 = digitalRead(btn2);
        pressionado3 = digitalRead(btn3);
        pressionado4 = digitalRead(btn4);
        pressionado5 = digitalRead(btn5);
        pressionado6 = digitalRead(btn6);
        pressionado7 = digitalRead(btn7);
        pressionado8 = digitalRead(btn8);
        
        estadoBtns[0] = '@';
        
        // Botão 1
        if(pressionado1 == 1)
        {
           estadoBtns[1]='1';
        }
        else
        {
          estadoBtns[1]='0';
        }


        // Botão 2
        if(pressionado2 == 1)
        {
           estadoBtns[2]='1';
        }
        else
        {
          estadoBtns[2]='0';
        }


        // Botão 3
        if(pressionado3 == 1)
        {
           estadoBtns[3]='1';
        }
        else
        {
          estadoBtns[3]='0';
        }


        // Botão 4
        if(pressionado4 == 1)
        {
           estadoBtns[4]='1';
        }
        else
        {
          estadoBtns[4]='0';
        }


        // Botão 5
        if(pressionado5 == 1)
        {
           estadoBtns[5]='1';
        }
        else
        {
          estadoBtns[5]='0';
        }


        // Botão 6
        if(pressionado6 == 1)
        {
           estadoBtns[6]='1';
        }
        else
        {
          estadoBtns[6]='0';
        }


        // Botão 7
        if(pressionado7 == 1)
        {
           estadoBtns[7]='1';
        }
        else
        {
          estadoBtns[7]='0';
        }


        // Botão 8
        if(pressionado8 == 1)
        {
           estadoBtns[8]='1';
        }
        else
        {
          estadoBtns[8]='0';
        }

      
         estadoBtns[9] = '#';
         estadoBtns[10] = '\0';
        

         Serial.print(estadoBtns);
      }
      
  
      if (instrucaoFinal.length() == 8)
      {
        for (int i = 0; i < 8; i++)
        {
          if (i == 0) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led1, HIGH);
            }
            else
            {
              digitalWrite(led1, LOW);
            }


          }

          if (i == 1) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led2, HIGH);
            }
            else
            {
              digitalWrite(led2, LOW);
            }
          }

          if (i == 2) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led3, HIGH);
            }
            else
            {
              digitalWrite(led3, LOW);
            }
          }


          if (i == 3) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led4, HIGH);
            }
            else
            {
              digitalWrite(led4, LOW);
            }
          }

          if (i == 4) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led5, HIGH);
            }
            else
            {
              digitalWrite(led5, LOW);
            }
          }


          if (i == 5) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led6, HIGH);
            }
            else
            {
              digitalWrite(led6, LOW);
            }
          }

          if (i == 6) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led7, HIGH);
            }
            else
            {
              digitalWrite(led7, LOW);
            }
          }

          if (i == 7) {
            if (instrucaoFinal[i] == '1')
            {
              digitalWrite(led8, HIGH);
            }
            else
            {
              digitalWrite(led8, LOW);
            }
          }

      
    


        }
        
          Serial.print("@rcv#");
      }
     



    }
  }

}
