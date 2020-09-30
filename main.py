from teste import criar_conta,deposita,saca,extrato
from conta import ContaCorrente

conta = ContaCorrente(540,"IgorLousada",50000)
conta1 = ContaCorrente(540,"IgorLousada",50000,3000)

conta.extrato()
conta1.extrato()
conta.deposita(1000)
conta1.deposita(1000)
conta.extrato()
conta1.extrato()
conta.transfere(conta1,4000)
conta.extrato()
conta1.extrato()

