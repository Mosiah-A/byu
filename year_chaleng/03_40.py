'''
1.  Adicionar Novo Aluno
2. Atribuir Notas
3. Exibir Informações dos Alunos
4. Sair
'''
def main():

    answere = int(0)
    while answere != 4:
        print("Sistema de Gerenciamento de Notas")
        print('''
1. Adicionar Novo Aluno
2. Atribuir Notas
3. Exibir Informações dos Alunos
4. Sair
        ''')
        
        alunos_list= {
            #Mosiah: [nota1, nota2],
            'Mosiah': [ ],
        }
            
        if answere > int(4):
            print('opção invalida')
            answere = int(input('Escolha uma opção: '))
        else:
            answere = int(input('Escolha uma opção: '))
            if answere == 1:
                adicionar_novo_aluno(alunos_list)
            elif answere == int(2):
                atribuir_nota(alunos_list)
            elif answere == 3:
                exibir_informacoes_dos_alunos(alunos_list)
                


def adicionar_novo_aluno(aluno):
    
    novo_aluno = input('Insira o nome do novo aluno: ')
    aluno[novo_aluno] = []

    print()
    

def atribuir_nota(aluno):
    print('Escolha o aluno pelo número: ')
    for i, aluno_id in aluno:
        print(f'{aluno_id} {aluno[aluno_id]}')

    id_escolhido = input()
    
    
    nova_nota = int(input(f'Insira a nota : '))
    aluno_id.append()
    print('nota')

def exibir_informacoes_dos_alunos(aluno):
    print('exibir')

if __name__ == '__main__':
    main()