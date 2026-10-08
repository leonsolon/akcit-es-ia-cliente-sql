# Cliente SQL da livraria

Este é um exemplo simples para o C4 do curso. A aplicação em Gradio executa instruções SQL em um banco SQLite fictício de uma livraria, com duas tabelas (`autores` e `livros`) e poucos registros de exemplo. Na primeira inicialização, o arquivo `livraria.db` e as tabelas são criados automaticamente.

O exemplo serve como ponto de partida. No curso, precisamos detalhar melhor o projeto e produzir artefatos de engenharia de software, como ADRs (registros de decisões arquiteturais), requisitos e outros documentos pertinentes.

## Requisitos

- Python 3.9 ou superior
- pip

## Passo a passo

1. Abra um terminal na pasta do projeto.
2. (Opcional, recomendado) Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   No Windows, ative com `.venv\Scripts\activate`.

3. Instale as dependências da interface. O projeto usa Gradio 4.44.1 e restringe `huggingface-hub` à série 0.x para manter a compatibilidade:

   ```bash
   pip install -r requirements.txt
   ```

   Isso instala `gradio==4.44.1` e `huggingface-hub>=0.25.2,<1.0`.

4. Inicie o cliente Gradio:

   ```bash
   python app.py
   ```

5. Abra no navegador o endereço local mostrado no terminal (normalmente `http://127.0.0.1:7860`). Digite SQL no campo e clique em **Executar SQL** ou pressione Ctrl+Enter. O resultado das consultas aparece na tabela abaixo; mensagens de erro do SQLite aparecem logo acima dela.

## Exemplos de SQL

Listar livros com seus autores:

```sql
SELECT livros.titulo, autores.nome AS autor, livros.ano, livros.preco
FROM livros
JOIN autores ON livros.autor_id = autores.id;
```

Filtrar livros publicados depois de 1970:

```sql
SELECT titulo, ano, estoque
FROM livros
WHERE ano > 1970;
```

O cliente executa uma instrução por vez. Instruções que alteram dados, como `INSERT`, `UPDATE` e `DELETE`, também são aceitas e confirmadas no banco.
