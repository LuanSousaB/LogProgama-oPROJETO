# Todas as funcionalidades do menu estão dispostas em função.

def cadastrar_aluno(alunos):
    m=input("Matrícula: ")
    if m in alunos:
        print("Aluno já existe")
        return
    n=input("Nome do aluno: ")
    alunos[m]={"nome":n,"disciplinas":set(),"notas":{}}
    print("Aluno cadastrado")

def cadastrar_disciplina(disciplinas):
    d=input("Código: ")
    if d in disciplinas:
        print("Disciplina existe")
        return
    n=input("Nome: ")
    disciplinas[d]={"nome":n,"alunos":set()}
    print("Disciplina cadastrada")

def matricular_aluno(alunos,disciplinas):
    m=input("Matrícula: ")
    if m not in alunos:
        print("Aluno não existe"); return
    d=input("Disciplina: ")
    if d not in disciplinas:
        print("Disciplina não existe"); return
    if d in alunos[m]["disciplinas"]:
        print("Já matriculado"); return
    alunos[m]["disciplinas"].add(d)
    alunos[m]["notas"][d]=[]
    disciplinas[d]["alunos"].add(m)
    print("Matriculado!")

def lancar_nota(alunos,disciplinas):
    m=input("Matrícula: ")
    if m not in alunos:
        print("Aluno n existe"); return
    d=input("Disciplina: ")
    if d not in alunos[m]["disciplinas"]:
        print("Não matriculado"); return
    try:
        n=float(input("Nota: "))
        alunos[m]["notas"][d].append(n)
        print("Nota lançada")
    except:
        print("Erro na nota")

def listar_alunos(alunos):
    for m,a in alunos.items():
        print(m,"-",a["nome"])

def listar_disciplinas(disciplinas):
    for d,dic in disciplinas.items():
        print(d,"-",dic["nome"])

def listar_alunos_disciplina(disciplinas,alunos):
    d=input("Disciplina: ")
    if d not in disciplinas:
        print("N existe"); return
    print("Alunos da",disciplinas[d]["nome"])
    for m in disciplinas[d]["alunos"]:
        print(m,"-",alunos[m]["nome"])

def exibir_boletim(alunos,disciplinas):
    m=input("Matrícula: ")
    if m not in alunos:
        print("Aluno n existe"); return
    print("Boletim de",alunos[m]["nome"])
    for d in alunos[m]["disciplinas"]:
        print(d,"-",disciplinas[d]["nome"],"notas:",alunos[m]["notas"][d])

def calcular_media_geral(alunos,m):
    if m not in alunos: print("N existe"); return None
    total=0;cont=0
    for notas in alunos[m]["notas"].values():
        for n in notas:
            total+=n;cont+=1
    if cont==0: return 0
    return total/cont

def aprovado_em_todas(alunos,m):
    if m not in alunos: print("N existe"); return None
    for notas in alunos[m]["notas"].values():
        media=sum(notas)/len(notas) if notas else 0
        if media<6.0: return False
    return True

def alterar_nome_aluno(alunos):
    m=input("Matrícula: ")
    if m not in alunos: print("N existe"); return
    n=input("Novo nome: ")
    alunos[m]["nome"]=n;print("Nome alterado")

def alterar_nome_disciplina(disciplinas):
    d=input("Código: ")
    if d not in disciplinas: print("N existe"); return
    n=input("Novo nome: ")
    disciplinas[d]["nome"]=n;print("Nome alterado")

def excluir_aluno(alunos,disciplinas):
    m=input("Matrícula: ")
    if m not in alunos: print("N existe"); return
    for d in alunos[m]["disciplinas"]:
        disciplinas[d]["alunos"].discard(m)
    del alunos[m];print("Aluno excluído")

def excluir_disciplina(disciplinas,alunos):
    d=input("Código: ")
    if d not in disciplinas: print("N existe"); return
    for m in disciplinas[d]["alunos"]:
        alunos[m]["disciplinas"].discard(d)
        if d in alunos[m]["notas"]: del alunos[m]["notas"][d]
    del disciplinas[d];print("Disciplina excluída")
