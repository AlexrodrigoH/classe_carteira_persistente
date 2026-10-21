import estado_carteira

saldo_inicial = 0
saldo_inicial = float(saldo_inicial)
referencia = estado_carteira.Carteira(saldo_inicial, "ref")
save = estado_carteira.Arquivos()
while True:
    try:
        print("1 - Colocar dinehiro\n2 - Retirar dinheiro\n")
        opcao = int(input())
        valor = float(input("valor: R$"))
        if opcao == 1:
            referencia.saldo = referencia.saldo + valor
            referencia.status = "deposito"
            save.save(referencia)
            continue
        elif opcao == 2:
            referencia.saldo = referencia.saldo - valor
            referencia.status = "saque"
            save.save(referencia)
            continue
        else:
            break
    except ValueError:
        break