""" 
Escreva um programa que reflita essas mudanças e permita praticar com o conceito de listas. Sua tarefa:

etapa 1: criar uma lista vazia chamada beatles;
etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison;
etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;
etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista.
"""
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(f"Estes são so integrantes originais da banda Beatles {beatles}")
print("Adicione os seguintes membros a banda (Stu Sutcliffe e Pete Best), um de cada vez.")
for x in range(2):
    novos = input("Adicione um novo membro a banda: ")
    beatles.append(novos)

print(f"Essa é a nova banda {beatles}")
del beatles[3: ]
print(f"Stu Sutcliffe e Pete Best sairam da banda, ela ficou assim {beatles}")
beatles.insert(0,"Ringo Starr")
print(f"Ringo Starr entrou na banda e agora ela ficou assim {beatles}")