import servicos.database as db
import models.Aluno as Aluno
import pyodbc


def incluir(Aluno):
    count = db.cursor.execute("""
    INSERT INTO boletim2 (nomealuno, materia, nota1, nota2, media, situacao)
    VALUES (?,?,?,?,?,?)""",
                              Aluno.nome, Aluno.materia, Aluno.n1, Aluno.n2, Aluno.media, Aluno.situacao).rowcount
    db.cnxn.commit()


def alterar(Aluno):
    cursor = db.cnxn.cursor()
    params = (Aluno.nome, Aluno.materia, Aluno.n1, Aluno.n2, Aluno.media, Aluno.situacao, Aluno.id)
    count = db.cursor.execute("""
        UPDATE boletim2 SET nomealuno = ?, materia = ?, nota1 = ?, nota2 = ?, media = ?, situacao = ?
        WHERE id = ?
    """, params).rowcount
    db.cnxn.commit()


def selecionarId(id):
    db.cursor.execute("SELECT * FROM boletim2 WHERE ID = ?", id)
    alunoList = []

    for row in db.cursor.fetchall():
        alunoList.append(Aluno.Aluno(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    return alunoList[0]


def excluir(id):
    count = db.cursor.execute("""
    DELETE FROM boletim2 WHERE id = ?""",
                              id).rowcount
    db.cnxn.commit()


def selecionarTodos():
    db.cursor.execute("SELECT * FROM boletim2")
    alunoList = []

    for row in db.cursor.fetchall():
        alunoList.append(Aluno.Aluno(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    return alunoList
