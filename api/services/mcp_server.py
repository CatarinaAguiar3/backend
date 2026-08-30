from mcp.server.fastmcp import FastMCP

from .tabelas import criar_tabela_dados
from .disciplinas import (DisciplinaNaoEncontrada, cadastrar_disciplina_dados,
                          listar_disciplinas_dados)

from .alunos import (AlunoNaoEncontrado, atualizar_idade_dados,
                     cadastrar_aluno_dados, listar_alunos_dados,
                     remover_aluno_dados, media_idade_dados, contar_alunos_dados)

from .professores import (ProfessorNaoEncontrado, atualizar_idade_professor_dados,
                          cadastrar_professor_dados, listar_professores_dados,
                          remover_professor_dados, media_idade_professores_dados, contar_professores_dados)

from .graficos import gerar_grafico                    


# Instancia o servidor MCP que publica as funcoes de alunos como ferramentas.
mcp = FastMCP("Escola Backend")

# ===============#
# disciplinas.py #
# ===============#
@mcp.tool()
def listar_disciplinas():
    # Recupera as disciplinas do banco e converte a resposta em texto legivel.
    disciplinas = listar_disciplinas_dados()
    if not disciplinas:
        return "Nenhuma disciplina cadastrada."

    return "\n".join(
        f"{disciplina['nome']}: {disciplina['descricao']}"
        for disciplina in disciplinas
    )

@mcp.tool()
def cadastrar_disciplinas(nome: str, descricao: str):
    # Cadastra uma nova disciplina e devolve uma mensagem de confirmacao.
    disciplina = cadastrar_disciplina_dados(nome, descricao)
    return f"Disciplina cadastrada com sucesso: {disciplina['nome']} - {disciplina['descricao']}."


# ===========#
# Tabelas.py #
# ===========#
@mcp.tool()
def criar_tabela(query_criacao: str):
    # Cria tabela no banco de dados
    criar_tabela_dados(query_criacao)
    return "Tabela criada com sucesso."


# ===========#
# Alunos.py  #
# ===========#
@mcp.tool()
def listar_alunos():
    # Recupera os alunos do banco e converte a resposta em texto legivel.
    alunos = listar_alunos_dados()
    if not alunos:
        return "Nenhum aluno cadastrado."

    return "\n".join(f"{aluno['nome']} ({aluno['idade']} anos)" for aluno in alunos)


@mcp.tool()
def cadastrar_aluno(nome: str, idade: int):
    # Executa o cadastro e devolve uma mensagem de confirmacao.
    aluno = cadastrar_aluno_dados(nome, idade)
    return f"Aluno cadastrado com sucesso: {aluno['nome']} ({aluno['idade']} anos)."


@mcp.tool()
def atualizar_idade(nome: str, idade: int):
    # Atualiza a idade de um aluno e devolve o resultado da operacao.
    aluno = atualizar_idade_dados(nome, idade)
    return f"Idade atualizada para {aluno['nome']}: {aluno['idade']} anos."


@mcp.tool()
def remover_aluno(nome: str):
    # Remove o aluno selecionado e devolve a confirmacao da exclusao.
    aluno = remover_aluno_dados(nome)
    return f"Aluno removido: {aluno['nome']}."


@mcp.tool()
def media_idade():
    # Calcula a média de idade dos alunos.
    aluno = media_idade_dados()
    return f"A média de idade dos alunos é {aluno} anos."

@mcp.tool()
def contar_alunos():
    aluno = contar_alunos_dados()
    return f"Existem {aluno} alunos cadastrados."


# ===============#
# Professores.py #
# ===============#
@mcp.tool()
def listar_professores():
    # Recupera os professores do banco e converte a resposta em texto legivel.
    professores = listar_professores_dados()
    if not professores:
        return "Nenhum professor cadastrado."

    return "\n".join(f"{professor['nome']} ({professor['idade']} anos)" for professor in professores)


@mcp.tool()
def cadastrar_professor(nome: str, idade: int):
    # Executa o cadastro e devolve uma mensagem de confirmacao.
    professor = cadastrar_professor_dados(nome, idade)
    return f"Professor cadastrado com sucesso: {professor['nome']} ({professor['idade']} anos)."


@mcp.tool()
def atualizar_idade_professor(nome: str, idade: int):
    # Atualiza a idade de um professor e devolve o resultado da operacao.
    professor = atualizar_idade_professor_dados(nome, idade)
    return f"Idade atualizada para {professor['nome']}: {professor['idade']} anos."


@mcp.tool()
def remover_professor(nome: str):
    # Remove o professor selecionado e devolve a confirmacao da exclusao.
    professor = remover_professor_dados(nome)
    return f"Professor removido: {professor['nome']}."


@mcp.tool()
def media_idade_professores():
    # Calcula a média de idade dos professores.
    professor = media_idade_professores_dados()
    return f"A média de idade dos professores é {professor} anos."

@mcp.tool()
def contar_professores():
    professor = contar_professores_dados()
    return f"Existem {professor} professores cadastrados."




# ============#
# graficos.py #
# ============#
# Função para pegar a instrução para gerar o gráfico
@mcp.tool()
def gerar_graficos_tool(
        dados_json:str,
        tipo_grafico: str = "barras",
        titulo: str = "Gráfico",
        xlabel: str = "X",
        ylabel: str = "Y"
):
    # Gera um gráfico a partir de dados em formato JSON.
    return gerar_grafico(dados_json, tipo_grafico, titulo, xlabel, ylabel)

if __name__ == "__main__":
    # Permite executar este modulo diretamente como servidor MCP.
    mcp.run()
