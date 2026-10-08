"""Cliente SQL simples para o banco SQLite de uma livraria."""

import sqlite3
from pathlib import Path

import gradio as gr


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "livraria.db"


def inicializar_banco():
    """Cria o banco e os dados de exemplo caso ainda não existam."""
    with sqlite3.connect(DB_PATH) as conexao:
        conexao.executescript(
            """
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                pais TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor_id INTEGER NOT NULL REFERENCES autores(id),
                ano INTEGER NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL DEFAULT 0
            );
            INSERT OR IGNORE INTO autores (id, nome, pais) VALUES
                (1, 'Clarice Lispector', 'Brasil'),
                (2, 'José Saramago', 'Portugal'),
                (3, 'Jorge Luis Borges', 'Argentina');
            INSERT OR IGNORE INTO livros (id, titulo, autor_id, ano, preco, estoque) VALUES
                (1, 'A hora da estrela', 1, 1977, 39.90, 8),
                (2, 'A paixão segundo G.H.', 1, 1964, 44.50, 5),
                (3, 'Ensaio sobre a cegueira', 2, 1995, 49.90, 6),
                (4, 'O Aleph', 3, 1949, 34.90, 3);
            """
        )


def executar_sql(sql):
    """Executa uma instrução SQL e devolve linhas ou o resultado da operação."""
    if not sql or not sql.strip():
        return [], "Digite uma instrução SQL para executar."

    try:
        with sqlite3.connect(DB_PATH) as conexao:
            conexao.execute("PRAGMA foreign_keys = ON")
            cursor = conexao.execute(sql)
            if cursor.description:
                colunas = [coluna[0] for coluna in cursor.description]
                linhas = [list(linha) for linha in cursor.fetchall()]
                return linhas, f"Consulta executada. {len(linhas)} linha(s) retornada(s)."
            return [], f"Comando executado. {cursor.rowcount} linha(s) afetada(s)."
    except sqlite3.Error as erro:
        return [], f"Erro SQLite: {erro}"


inicializar_banco()

with gr.Blocks(title="Cliente SQL — Livraria") as demo:
    gr.Markdown(
        "# Cliente SQL da livraria\n"
        "Escreva uma instrução SQL para consultar ou atualizar o banco SQLite. "
        "As tabelas disponíveis são `livros` e `autores`."
    )
    consulta = gr.Textbox(
        label="SQL",
        lines=7,
        value="SELECT livros.titulo, autores.nome AS autor, livros.ano, livros.preco\n"
        "FROM livros\nJOIN autores ON livros.autor_id = autores.id;",
        placeholder="SELECT * FROM livros;",
    )
    executar = gr.Button("Executar SQL", variant="primary")
    status = gr.Markdown()
    resultado = gr.Dataframe(label="Resultado", interactive=False, wrap=True)
    executar.click(fn=executar_sql, inputs=consulta, outputs=[resultado, status])
    consulta.submit(fn=executar_sql, inputs=consulta, outputs=[resultado, status])


if __name__ == "__main__":
    demo.launch()
