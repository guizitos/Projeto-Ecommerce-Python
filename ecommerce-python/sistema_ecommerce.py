class Produto:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, id: int, nome: str, endereco: str):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.historico_pedidos = []

    def adicionar_pedido(self, pedido):
        self.historico_pedidos.append(pedido)

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

    def atualizar_status(self, novo_status: str):
        status_validos = ["Aguardando Pagamento", "Pago", "Enviado", "Entregue"]
        if novo_status not in status_validos:
            raise ValueError(f"Status inválido: {novo_status}")
        
        # Lógica de transição de status
        if self.status == "Aguardando Pagamento" and novo_status == "Pago":
            self.status = novo_status
        elif self.status == "Pago" and novo_status == "Enviado":
            self.status = novo_status
        elif self.status == "Enviado" and novo_status == "Entregue":
            self.status = novo_status
        else:
            raise ValueError(f"Transição inválida: {self.status} -> {novo_status}")

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

class Entrega:
    def __init__(self, pedido: Pedido, codigo_rastreamento: str):
        self.pedido = pedido
        self.codigo_rastreamento = codigo_rastreamento
        self.status_entrega = "Aguardando Envio"

    def iniciar_entrega(self):
        if self.pedido.status == "Pago":
            self.status_entrega = "Em Transporte"
            self.pedido.atualizar_status("Enviado")
        else:
            raise ValueError("Pedido não está pago")

    def finalizar_entrega(self):
        if self.status_entrega == "Em Transporte":
            self.status_entrega = "Entregue"
            self.pedido.atualizar_status("Entregue")
        else:
            raise ValueError("Entrega não iniciada")

