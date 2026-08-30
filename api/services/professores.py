from .mysql import conectar


class ProfessorNaoEncontrado(Exception):
    # Excecao usada quando uma operacao tenta acessar um professor inexistente.
    pass


def listar_professores_dados():
    # Consulta todos os professores e devolve a resposta em formato simples para a API.
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, idade FROM professores ORDER BY nome")
    dados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return [{"nome": nome, "idade": idade} for nome, idade in dados]


def cadastrar_professor_dados(nome: str, idade: int):
    # Insere um novo professor no banco e devolve os dados cadastrados.
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO professores(nome, idade) VALUES(%s, %s)",
        (nome, idade),
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return {"nome": nome, "idade": idade}


def atualizar_idade_professor_dados(nome: str, idade: int):
    # Atualiza a idade de um professor existente e valida se houve alteracao.
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        UPDATE professores  
        SET idade=%s
        WHERE nome=%s
        """,
        (idade, nome),
    )
    if cursor.rowcount == 0:
        cursor.close()
        conexao.close()
        raise ProfessorNaoEncontrado(f"Professor '{nome}' não encontrado.")
    conexao.commit()
    cursor.close()
    conexao.close()
    return {"nome": nome, "idade": idade}


def remover_professor_dados(nome: str):
    # Remove um professor pelo nome e aponta erro se nenhum registro for encontrado.
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM professores WHERE nome=%s", (nome,))
    if cursor.rowcount == 0:
        cursor.close()
        conexao.close()
        raise ProfessorNaoEncontrado(f"Professor '{nome}' não encontrado.")
    conexao.commit()
    cursor.close()
    conexao.close()
    return {"nome": nome}


def media_idade_professores_dados():
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT AVG(idade) FROM professores  
        """
    )
    #fetchone() busca a primeira linha retornada pelo SELECT e [0] pega o primeiro valor dessa linha
    media = cursor.fetchone()[0]
    # conexao.commit() # Aqui não precisa, só é usado se fosse alterar algo no banco de dados

    cursor.close()
    conexao.close()

    # return f"A média de idade é {media:.2f} anos."
    return f"{media:.2f} anos."



def contar_professores_dados():
    conexao = conectar()

    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT COUNT(*) FROM professores"""
    )
    contagem = cursor.fetchone()[0]
    # conexao.commit() # Aqui não precisa, só é usado se fosse alterar algo no banco de dados

    cursor.close()
    conexao.close()
    # return f"O número de professores cadastrados é {contagem}."
    return f"{contagem} professores cadastrados."