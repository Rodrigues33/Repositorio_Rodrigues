Algoritmo "exe5_sexo"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Hiram Amaral 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : alunocetam22
// Data atual  : 25/03/2022
Var
// Seção de Declarações das variáveis
   sexo: caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreva("M = mulher | H = homem | O = outros")
   escreva("Digite uma sigla para seu sexo: ")
   leia(sexo)

   sexo <- maiusc(sexo)

   escolha sexo
      caso "m"
        escreva("voce e Mulher")
      caso "h"
        escreva("voce e Homem")
      caso "o"
        escreva("voce e outro")
      outrocaso
      escreva("Entrada invalida")
      fimescolha

Fimalgoritmo
