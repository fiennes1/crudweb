import servicos.database as db
import models.Aluno as estudantes


def incluir(estudantes):
    count = db.cursor.execute("""
    INSERT INTO boletim2 (nomealuno, materia, nota1, nota2, media, situacao)
    VALUES (?,?,?,?,?,?)""",
                              estudantes.nome, estudantes.materia, estudantes.n1, estudantes.n2, estudantes.media,
                              estudantes.situacao).rowcount
    db.cnxn.commit()


def alterar(estudantes):
    count = db.cursor.execute("""
    UPDATE boletim2 
    SET nomealuno = ?, materia = ?, nota1 = ?, nota2 = ?, media = ?, situacao = ?
    WHERE id = ?""",
                              estudantes.nome, estudantes.materia, estudantes.n1, estudantes.n2, estudantes.media,
                              estudantes.situacao, estudantes.id).rowcount
    db.cnxn.commit()


def selecionarId(id):
    db.cursor.execute("SELECT * FROM boletim2 WHERE ID = ?", id)
    alunoList = []

    for row in db.cursor.fetchall():
        alunoList.append(estudantes.Aluno(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

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
        alunoList.append(estudantes.Aluno(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    return alunoList
