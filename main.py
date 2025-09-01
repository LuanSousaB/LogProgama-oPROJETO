# Menu principal contendo todas as chamadas de opções
# Laço em while true
from funcoes import *
from repositorio import *

def menu():
    print("\n===== SISTEMA ACADÊMICO =====")
    print("1. Cadastrar aluno")
    print("2. Cadastrar disciplina")
    print("3. Matricular aluno em disciplina")
    print("4. Lançar nota")
    print("5. Listar todos os alunos")
    print("6. Listar todas as disciplinas")
    print("7. Listar alunos de disciplina")
    print("8. Exibir boletim")
    print("9. Calcular média geral")
    print("10. Status de aprovação")
    print("11. Alterar nome aluno")
    print("12. Alterar nome disciplina")
    print("13. Excluir aluno")
    print("14. Excluir disciplina")
    print("0. Sair")

def main():
    while True:
        menu()
        op=input("Opção: ").strip()
        if op=="1": cadastrar_aluno(alunos)
        elif op=="2": cadastrar_disciplina(disciplinas)
        elif op=="3": matricular_aluno(alunos,disciplinas)
        elif op=="4": lancar_nota(alunos,disciplinas)
        elif op=="5": listar_alunos(alunos)
        elif op=="6": listar_disciplinas(disciplinas)
        elif op=="7": listar_alunos_disciplina(disciplinas,alunos)
        elif op=="8": exibir_boletim(alunos,disciplinas)
        elif op=="9": m=input("Matrícula: "); media=calcular_media_geral(alunos,m); print("Média:",media) if media is not None else None
        elif op=="10": m=input("Matrícula: "); s=aprovado_em_todas(alunos,m); print("APROVADO" if s else "REPROVADO") if s is not None else None
        elif op=="11": alterar_nome_aluno(alunos)
        elif op=="12": alterar_nome_disciplina(disciplinas)
        elif op=="13": excluir_aluno(alunos,disciplinas)
        elif op=="14": excluir_disciplina(disciplinas,alunos)
        elif op=="0": print("Saindo"); break
        else: print("Inválido")

main()
