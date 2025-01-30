# Ecommerce Python

Este projeto implementa um sistema simples de e-commerce em Python, incluindo funcionalidades básicas para gerenciamento de produtos, clientes, pedidos, pagamentos e entregas. Além disso, há um conjunto de testes automatizados usando `pytest` para validar o comportamento do sistema.

## 📌 Funcionalidades
- **Cadastro de Produtos**: Produtos possuem um identificador, nome e preço.
- **Gerenciamento de Clientes**: Os clientes possuem um identificador, nome, endereço e um histórico de pedidos.
- **Pedidos**: Um cliente pode criar um pedido e adicionar produtos a ele.
- **Pagamentos**: Um pedido pode ser pago através de diferentes métodos de pagamento.
- **Entrega**: O status de um pedido pode ser atualizado conforme sua entrega é processada.

---

## 📂 Estrutura do Código

### 📌 `Produto`
Classe que representa um produto no sistema.
```python
class Produto:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco
```
- `id`: Identificador único do produto.
- `nome`: Nome do produto.
- `preco`: Preço do produto.

### 📌 `Cliente`
Classe que gerencia os clientes do e-commerce.
```python
class Cliente:
    def __init__(self, id: int, nome: str, endereco: str):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.historico_pedidos = []
    
    def adicionar_pedido(self, pedido):
        self.historico_pedidos.append(pedido)
```
- `id`: Identificador do cliente.
- `nome`: Nome do cliente.
- `endereco`: Endereço do cliente.
- `historico_pedidos`: Lista de pedidos realizados pelo cliente.

### 📌 `Pedido`
Classe que gerencia pedidos feitos pelos clientes.
```python
class Pedido:
    def __init__(self, id: int, cliente: Cliente):
        self.id = id
        self.cliente = cliente
        self.itens = []
        self.status = "Aguardando Pagamento"
        self.valor_total = 0.0

    def adicionar_produto(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        self.itens.extend([produto] * quantidade)
    
    def calcular_total(self) -> float:
        self.valor_total = sum(produto.preco for produto in self.itens)
        return self.valor_total
```
- `id`: Identificador do pedido.
- `cliente`: Cliente que fez o pedido.
- `itens`: Lista de produtos no pedido.
- `status`: Status do pedido.
- `valor_total`: Valor total do pedido.

### 📌 `Pagamento`
Classe que gerencia o pagamento de pedidos.
```python
class Pagamento:
    def __init__(self, pedido: Pedido, metodo: str):
        self.pedido = pedido
        self.metodo = metodo
        self.status_pagamento = "Aguardando"

    def processar_pagamento(self):
        if self.pedido.calcular_total() > 0:
            self.status_pagamento = "Aprovado"
            self.pedido.atualizar_status("Pago")
        else:
            self.status_pagamento = "Recusado"
```
- `pedido`: Pedido associado ao pagamento.
- `metodo`: Método de pagamento (Cartão, Boleto, Pix etc.).
- `status_pagamento`: Indica se o pagamento foi aprovado ou recusado.

### 📌 `Entrega`
Classe que gerencia a entrega dos pedidos.
```python
class Entrega:
    def __init__(self, pedido: Pedido, codigo_rastreamento: str):
        self.pedido = pedido
        self.codigo_rastreamento = codigo_rastreamento
        self.status_entrega = "Aguardando Envio"
    
    def iniciar_entrega(self):
        if self.pedido.status == "Pago":
            self.status_entrega = "Em Transporte"
            self.pedido.atualizar_status("Enviado")
    
    def finalizar_entrega(self):
        if self.status_entrega == "Em Transporte":
            self.status_entrega = "Entregue"
            self.pedido.atualizar_status("Entregue")
```
- `pedido`: Pedido a ser entregue.
- `codigo_rastreamento`: Código de rastreamento da entrega.
- `status_entrega`: Status da entrega.

---

## 🧦 Testes Automatizados
Os testes foram implementados com `pytest` para garantir que o sistema funcione corretamente.

### 🔹 **Testes Implementados**

- `test_cliente_vinculado_ao_pedido()` – Verifica se o cliente é corretamente vinculado a um pedido.
- `test_adicionar_produtos_ao_pedido()` – Testa a adição de produtos a um pedido.
- `test_calcular_total_pedido()` – Testa o cálculo do valor total de um pedido.
- `test_pagamento_aprovado()` – Verifica se um pagamento é aprovado corretamente.
- `test_pagamento_recusado()` – Testa a recusa de um pagamento para um pedido sem produtos.
- `test_ciclo_entrega()` – Simula todo o ciclo de pedido, pagamento e entrega.
- `test_cliente_historico_pedidos()` – Verifica se os pedidos são corretamente adicionados ao histórico do cliente.
- `test_adicionar_produto_quantidade_invalida()` – Testa se uma exceção é levantada ao adicionar uma quantidade inválida de produtos.
- `test_transicao_status_invalida()` – Testa se uma transição inválida de status gera erro.
- `test_iniciar_entrega_sem_pagamento()` – Testa se um pedido não pago não pode ser enviado.

### 🚀 **Executando os Testes**
Para rodar os testes, utilize o seguinte comando:
```sh
pytest test_sistema.py -v
```
O `-v` ativa o modo verbose para uma saída mais detalhada.

---

## ⚙️ Como Executar o Projeto
1. Clone o repositório:
   ```sh
   git clone https://github.com/guizitos/Projeto-Ecommerce-Python.git
   ```
2. Entre na pasta do projeto:
   ```sh
   cd ecommerce-python
   ```
3. Instale as dependências:
   ```sh
   pip install pytest
   ```
4. Execute os testes:
   ```sh
   pytest test_sistema.py -v
   ```

---

## 📝 Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Faça um **fork** do repositório.
2. Crie uma **branch** com a nova funcionalidade (`git checkout -b minha-feature`).
3. Faça as alterações e **commite** (`git commit -m 'Minha nova feature'`).
4. Faça o **push** para o repositório (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

## 📝 Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

