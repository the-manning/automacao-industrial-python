import os

# Estruturas de dados para armazenamento
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []
contador_caixas = 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_peca(peso, cor, comprimento):
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão (95g - 105g)")
    if cor not in ['azul', 'verde']:
        motivos.append("Cor inválida (deve ser azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão (10cm - 20cm)")
    return motivos

def cadastrar_peca():
    global contador_caixas
    print("\n--- 1. CADASTRAR NOVA PEÇA ---")
    try:
        id_peca = input("ID da Peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor (azul/verde): ").strip().lower()
        comprimento = float(input("Comprimento (cm): "))
        
        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento
        }
        
        motivos_reprovacao = validar_peca(peso, cor, comprimento)
        
        if motivos_reprovacao:
            peca["motivos"] = motivos_reprovacao
            pecas_reprovadas.append(peca)
            print(f"\n❌ Peça {id_peca} REPROVADA.")
            print("Motivos:", ", ".join(motivos_reprovacao))
        else:
            caixa_atual.append(peca)
            print(f"\n✅ Peça {id_peca} APROVADA e adicionada à caixa atual.")
            
            # Verifica se a caixa atingiu a capacidade máxima
            if len(caixa_atual) == 10:
                caixas_fechadas.append({
                    "numero_caixa": contador_caixas,
                    "pecas": caixa_atual.copy()
                })
                print(f"📦 CAIXA {contador_caixas} FECHADA (10 peças atingidas). Nova caixa iniciada.")
                contador_caixas += 1
                caixa_atual.clear()
                
    except ValueError:
        print("\n⚠️ Erro de entrada. Certifique-se de digitar números válidos para peso e comprimento.")
    input("\nPressione ENTER para voltar ao menu...")

def listar_pecas():
    print("\n--- 2. LISTAR PEÇAS ---")
    print("\n--- PEÇAS APROVADAS ---")
    total_aprovadas = 0
    # Lista das caixas fechadas
    for caixa in caixas_fechadas:
        for p in caixa["pecas"]:
            print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm (Caixa {caixa['numero_caixa']})")
            total_aprovadas += 1
    # Lista da caixa atual em andamento
    for p in caixa_atual:
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm (Caixa Atual - Em aberto)")
        total_aprovadas += 1
        
    if total_aprovadas == 0: print("Nenhuma peça aprovada cadastrada.")
    
    print("\n--- PEÇAS REPROVADAS ---")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada.")
    else:
        for p in pecas_reprovadas:
            print(f"ID: {p['id']} | Motivo(s): {', '.join(p['motivos'])}")
            
    input("\nPressione ENTER para voltar ao menu...")

def remover_peca():
    print("\n--- 3. REMOVER PEÇA ---")
    id_remover = input("Digite o ID da peça que deseja remover: ")
    removida = False
    
    # Procura nas reprovadas
    for p in pecas_reprovadas:
        if p["id"] == id_remover:
            pecas_reprovadas.remove(p)
            removida = True
            break
            
    # Procura na caixa atual
    if not removida:
        for p in caixa_atual:
            if p["id"] == id_remover:
                caixa_atual.remove(p)
                removida = True
                break
                
    # Procura nas caixas fechadas
    if not removida:
        for caixa in caixas_fechadas:
            for p in caixa["pecas"]:
                if p["id"] == id_remover:
                    caixa["pecas"].remove(p)
                    removida = True
                    break
                    
    if removida:
        print(f"🗑️ Peça {id_remover} removida com sucesso do sistema.")
    else:
        print(f"⚠️ Peça {id_remover} não encontrada.")
        
    input("\nPressione ENTER para voltar ao menu...")

def listar_caixas():
    print("\n--- 4. LISTAR CAIXAS FECHADAS ---")
    if not caixas_fechadas:
        print("Nenhuma caixa foi fechada ainda (necessário 10 peças aprovadas por caixa).")
    else:
        for caixa in caixas_fechadas:
            print(f"📦 Caixa {caixa['numero_caixa']} - {len(caixa['pecas'])} peças armazenadas.")
    print(f"\n(Caixa atual em andamento possui {len(caixa_atual)} peças)")
    input("\nPressione ENTER para voltar ao menu...")

def gerar_relatorio():
    print("\n--- 5. RELATÓRIO FINAL ---")
    total_aprovadas = sum(len(c["pecas"]) for c in caixas_fechadas) + len(caixa_atual)
    total_reprovadas = len(pecas_reprovadas)
    
    print(f"✅ Total de Peças Aprovadas: {total_aprovadas}")
    print(f"❌ Total de Peças Reprovadas: {total_reprovadas}")
    print(f"📦 Quantidade de Caixas Fechadas: {len(caixas_fechadas)}")
    
    if total_reprovadas > 0:
        print("\n--- Motivos das Reprovações ---")
        for p in pecas_reprovadas:
            print(f"Peça ID {p['id']}: {', '.join(p['motivos'])}")
            
    input("\nPressione ENTER para voltar ao menu...")

def main():
    while True:
        limpar_tela()
        print("="*40)
        print(" SISTEMA DE QUALIDADE E ARMAZENAMENTO")
        print("="*40)
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar_peca()
        elif opcao == '2': listar_pecas()
        elif opcao == '3': remover_peca()
        elif opcao == '4': listar_caixas()
        elif opcao == '5': gerar_relatorio()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()