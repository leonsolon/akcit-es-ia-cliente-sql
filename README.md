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

## Prompts para continuar o projeto

Os prompts abaixo podem ser usados como ponto de partida em uma ferramenta de IA. Ajuste-os conforme as decisões e os objetivos do curso.

### Criar esta aplicação

> Crie uma aplicação simples em Python com uma interface Gradio que receba uma instrução SQL, execute-a em um banco SQLite fictício para uma livraria e apresente o resultado ou uma mensagem de erro. Use poucas tabelas e poucos registros de exemplo. Inclua o banco SQLite, as dependências necessárias e um README com instruções para instalar e executar a aplicação.

### Planejar uma nova funcionalidade

> Analise o projeto atual e proponha uma funcionalidade para [descreva a funcionalidade]. Antes de alterar o código, identifique usuários, problema, escopo, dúvidas e impactos nas tabelas e na interface. Separe fatos encontrados no repositório de suposições e faça perguntas quando faltar informação importante. Ao final, sugira os artefatos de engenharia necessários para implementar a mudança.

### Registrar uma decisão arquitetural (ADR)

> Com base nos requisitos e no contexto deste repositório, escreva um ADR para decidir [descreva a decisão]. Inclua título, status, contexto, decisão, alternativas consideradas, consequências positivas e negativas, e data. Não invente requisitos nem decisões já tomadas; marque lacunas como perguntas. Salve no diretório de ADRs acordado para o projeto.

### Detalhar requisitos

> Elabore os requisitos para a funcionalidade [descreva a funcionalidade] neste cliente SQL. Liste histórias de usuário, requisitos funcionais e não funcionais, regras de negócio, critérios de aceite verificáveis e casos de erro. Indique prioridade e dependências. Diferencie requisitos confirmados de suposições e aponte dúvidas em aberto.

### Planejar e criar testes

> A partir dos requisitos e critérios de aceite de [funcionalidade], proponha uma estratégia de testes para este projeto Python/Gradio/SQLite. Cubra os fluxos esperados, erros, limites e persistência dos dados; identifique o que deve ser unitário e o que precisa de integração. Depois implemente os testes necessários sem depender de dados reais nem alterar o banco de desenvolvimento. Informe os comandos para executá-los.

### Projetar uma mudança de esquema SQLite

> Para atender [requisito], proponha a alteração necessária no esquema SQLite. Explique tabelas, colunas, chaves, restrições e migração dos dados existentes. Considere como preservar o banco atual e como validar a migração. Registre decisões arquiteturais relevantes e critérios de aceite antes de implementar.

### Atualizar a documentação após implementar

> Revise a implementação de [funcionalidade] neste repositório e atualize a documentação afetada. Mantenha o README voltado à instalação, execução e uso; documente decisões em ADRs e requisitos no local definido pelo projeto. Relacione cada afirmação à implementação ou aos requisitos existentes e sinalize qualquer divergência encontrada.
