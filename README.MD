# Desafio de Projeto:

*Projeto de um sistema bancário desenvonvido para a conclusão do módulo "Sintaxe Básica com Python", este projeto atende às exigências especificadas para o desafio do [bootcamp](https://web.dio.me/track/engenharia-dados-python) da NTT DATA*

### Exigências:

**Sistema Bancário com três operações disponíveis:** 
Depósito, saque e extrato

**Valor máximo de saque =** R$ 500

**Limite diário de saque =** 3 operações

**Manter o registro de todas as operações e o saldo final da conta no extrato.**

### Sobre:

Este sistema bancário foi desenvolvido para um único usuário e permite a seleção de uma operação por vez: **Depósito**, **Saque** ou **Extrato**. De acordo com os requisitos solicitados, o sistema impõe um limite no número de saques diários e também no valor máximo de cada saque. Ele permite depósitos e atualiza o extrato conforme a operação e o valor informado pelo usuário.

Caso o usuário escolha uma operação que não esteja entre as opções do menu, será exibida uma mensagem de erro, solicitando que ele insira uma operação válida.

Utilizando a estrutura de repetição `while`, o sistema mantém o código em loop, solicitando que o usuário selecione uma nova operação até que a opção de saída `[0]` seja escolhida.

