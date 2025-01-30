from sistema_ecommerce import Cliente, Pedido, Produto, Pagamento, Entrega
import pytest

def test_cliente_vinculado_ao_pedido():
    cliente = Cliente(1, "João Silva", "Rua das Flores, 123")
    pedido = Pedido(101, cliente)
    assert pedido.cliente.id == cliente.id

def test_adicionar_produtos_ao_pedido():
    cliente = Cliente(1, "Maria Souza", "Avenida Paulista, 456")
    pedido = Pedido(102, cliente)
    produto = Produto(1001, "Notebook", 3500.0)
    pedido.adicionar_produto(produto, 2)
    assert len(pedido.itens) == 2
    assert pedido.itens[0].nome == "Notebook"

def test_calcular_total_pedido():
    cliente = Cliente(1, "Carlos Oliveira", "Praça da Sé, 789")
    pedido = Pedido(103, cliente)
    produto1 = Produto(1003, "Livro", 89.90)
    produto2 = Produto(1004, "Caneta", 2.50)
    pedido.adicionar_produto(produto1, 2)
    pedido.adicionar_produto(produto2, 5)
    total = pedido.calcular_total()
    assert total == (89.90 * 2) + (2.50 * 5)

def test_pagamento_aprovado():
    cliente = Cliente(1, "Ana Costa", "Rua XV de Novembro, 101")
    pedido = Pedido(104, cliente)
    pedido.adicionar_produto(Produto(1005, "Fone de Ouvido", 250.0), 1)
    pagamento = Pagamento(pedido, "Cartão")
    pagamento.processar_pagamento()
    assert pagamento.status_pagamento == "Aprovado"
    assert pedido.status == "Pago"

def test_pagamento_recusado():
    cliente = Cliente(1, "Pedro Rocha", "Alameda Santos, 202")
    pedido = Pedido(105, cliente) 
    pagamento = Pagamento(pedido, "Pix")
    pagamento.processar_pagamento()
    assert pagamento.status_pagamento == "Recusado"
    assert pedido.status == "Aguardando Pagamento"

def test_ciclo_entrega():
    cliente = Cliente(1, "Luiza Fernandes", "Rua Oscar Freire, 303")
    pedido = Pedido(106, cliente)
    pedido.adicionar_produto(Produto(1006, "Mochila", 300.0), 1)
    pagamento = Pagamento(pedido, "Boleto")
    pagamento.processar_pagamento()
    entrega = Entrega(pedido, "BR123456789")
    entrega.iniciar_entrega()
    entrega.finalizar_entrega()
    assert pedido.status == "Entregue"
    assert entrega.status_entrega == "Entregue"

def test_cliente_historico_pedidos():
    cliente = Cliente(1, "Fernando Lima", "Rua das Palmeiras, 12")
    pedido1 = Pedido(107, cliente)
    pedido2 = Pedido(108, cliente)
    cliente.adicionar_pedido(pedido1)
    cliente.adicionar_pedido(pedido2)
    assert len(cliente.historico_pedidos) == 2
    assert cliente.historico_pedidos[0].id == 107
    assert cliente.historico_pedidos[1].id == 108

def test_adicionar_produto_quantidade_invalida():
    cliente = Cliente(1, "Ricardo Silva", "Avenida Brasil, 222")
    pedido = Pedido(109, cliente)
    produto = Produto(1007, "Teclado", 150.0)
    with pytest.raises(ValueError, match="Quantidade deve ser positiva"):
        pedido.adicionar_produto(produto, -1)

def test_transicao_status_invalida():
    cliente = Cliente(1, "Patrícia Moura", "Rua do Comercio, 99")
    pedido = Pedido(110, cliente)
    pedido.adicionar_produto(Produto(1008, "Mouse", 120.0), 1)
    pagamento = Pagamento(pedido, "Pix")
    pagamento.processar_pagamento()
    with pytest.raises(ValueError, match="Transição inválida"):
        pedido.atualizar_status("Entregue")

def test_iniciar_entrega_sem_pagamento():
    cliente = Cliente(1, "Gabriela Santos", "Avenida Central, 300")
    pedido = Pedido(111, cliente)
    pedido.adicionar_produto(Produto(1009, "Monitor", 800.0), 1)
    entrega = Entrega(pedido, "BR987654321")
    with pytest.raises(ValueError, match="Pedido não está pago"):
        entrega.iniciar_entrega()
