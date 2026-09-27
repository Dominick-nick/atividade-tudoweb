# Inicialização de variáveis e contadores
total_entrevistados = 50
qtd_excelente = 0
qtd_ruim = 0

print("=== Pesquisa de Satisfação - Tudoweb ===")

# Estrutura de repetição para coletar dados dos entrevistados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado {i} de {total_entrevistados}")
    
    # Coleta de dados
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite o número correspondente à sua opinião (1, 2 ou 3): "))
    
    # Validação simples para garantir uma opção válida
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida!")
        opiniao = int(input("Digite novamente (1, 2 ou 3): "))
        
    # Contabilização das respostas solicitadas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1

# Exibição dos resultados finais ao término da pesquisa
print("\n" + "="*40)
print("RESULTADO FINAL DA PESQUISA")
print("="*40)
print(f"Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"Quantidade de respostas 'RUIM': {qtd_ruim}")
