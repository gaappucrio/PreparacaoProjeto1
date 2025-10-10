# Ideia para a estrutura do pacote de Python do GAAP

## Hierarquia dos módulos

gaaplib/

│

├─ io/		→ Entrada e saída de dados

├─ table/	→ Manipulação e formatação de tabelas

├─ plot/	→ Geração padronizada de gráficos

├─ text/	→ Geração de citações, LaTeX e relatórios

├─ project/	→ Organização, automação e logs

└─ utils/	→ Funções auxiliares e conveniências gerais


## Módulo 1 - io

Entrada, saída e padronização de dados.

**Objetivo:**

Simplificar a leitura, validação e conversão de dados experimentais ou simulados, garantindo a consistência interna para formatos utilizados pelo grupo e formatos esperados pelas funções.

**Principais funcionalidades:**

- *load_data(path)*: Lê arquivos CSV ou Excel automaticamente, detectando delimitadores e tipos de dados (opção para excel em inglês e em português já que algumas coisas mudam como delimitador de algarismo).

- *validate_data(df,rules=None)*: Verifica consistência dos dados conforme regras definidas pelo usuário (valores ausentes, faixas permitidas de variáveis por coluna, tipos incorretos, presença de valores negativos, etc., gerando um relatório)

- *convert_format(input_path,output_path,format='csv'|'excel'|'json')*: Converte entre formatos comuns de dados, permitindo padronizar a entrada e saída de resultados.

## Módulo 2 - table

Manipulação e formatação de tabelas.

**Objetivo:**

Facilitar a criação de subtabelas, combinações de dados e exportação em formatos adequados para relatórios e artigos.

**Principais funcionalidades:**

- *subset_table(df,rows=None,cols=None)*: Cria subtabelas a partir da seleção de colunas e/ou linhas específicas.

- *merge_tables(df_list, on=None, how='outer')*: Une múltiplas tabelas de forma segura e padronizada, evitando perda de dados.

- *summarize_table(df)*: Gera uma tabela-resumo com estatísticas básicas (média, desvio padrão, mínimo e máximo).

- *to_latex_table(df, caption=None, label=None, style='default')*: Converte uma tabela em código LaTeX formatado para publicação, com controle de arredondamento e notação científica.

- *to_markdown_table(df)*: Gera tabela em formato Markdown, útil para relatórios rápidos ou README.

## Módulo 3 - plot

Padronizar a criação de figuras e gráficos, garantindo consistência visual e qualidade de exportação entre os trabalhos do grupo.

**Objetivo:**

Simplificar a leitura, validação e conversão de dados experimentais ou simulados, garantindo a consistência interna para formatos utilizados pelo grupo e formatos esperados pelas funções.

**Principais funcionalidades:**

- *plot_data(df, x, y, kind='line'|'scatter'|'bar', style='default')*: Gera gráficos básicos com aparência uniforme (fontes, cores, tamanhos, dpi).

- *set_style(style='paper'|'presentation'|'dark')*: Aplica estilos predefinidos conforme o contexto (artigo científico, apresentação (ex. fundo transparente), etc.).

- *save_plot(fig, name, formats=('png','pdf','svg'))*: Salva a figura em múltiplos formatos, com nomes e metadados consistentes.

## Módulo 4 - text

Geração de citações, LaTeX e relatórios.

**Objetivo:**

Automatizar partes do processo de escrita científica, desde a geração de citações até a formatação de resultados em LaTeX ou Markdown.

**Principais funcionalidades:**

- *generate_citation(doi, style='APA'|'ABNT'|'BibTeX')*: Obtém metadados de um DOI e gera a citação formatada conforme o estilo desejado. Pode exportar diretamente um arquivo .bib.

- *format_reference_list(dois, style='ABNT')*: Gera uma lista de referências completa a partir de múltiplos DOIs.

- *generate_latex_table(df, caption=None, label=None)*: Gera código LaTeX para tabelas de resultados (função complementar ao módulo table).

## Módulo 5 - project

Organização e automação de projetos.

**Objetivo:**

Fornecer uma estrutura padrão e ferramentas para registro de experimentos, garantindo rastreabilidade e padronização dos projetos de pesquisa.

**Principais funcionalidades:**

- *new_project(name)*: Cria uma estrutura de diretórios padrão para novos projetos (data/, scripts/, results/, figures/, docs/).

- *log_run(params, output_path='logs/')*: Registra informações de execução (data, tempo, parâmetros e resultados) para rastreabilidade.

- *generate_readme(template='default')*: Cria um README inicial padronizado com seções básicas (objetivo, estrutura, instruções).

- *check_project_health()*: Verifica se todos os diretórios e arquivos essenciais estão presentes, ajudando a manter a organização. Mais para uso de verificação.

## Módulo 6 - utils

Funções auxiliares e conveniências gerais.

**Objetivo:**

Agrupar pequenas ferramentas que melhoram a produtividade e a consistência dos trabalhos.

**Principais funcionalidades:**

- *convert_units(value, from_unit, to_unit)*: Conversor genérico de unidades utilizando, existem pacotes de python que ajudam nisso também dado o nome de cada unidade.

- *time_execution(func)*: Decorador que mede o tempo de execução de uma função e salva no log.

- *standardize_filename(name, prefix='exp', ext='.csv',timestamp=True)*: Gera nomes de arquivos padronizados, como 2025_10_02_exp_001_results.csv.

- *random_seed(seed=None)*: Define e registra a semente aleatória para garantir reprodutibilidade.

  ## Módulo 7 - imlatex

Acomodar em documentos *latex* imagens. 

**Principais funcionalidades:**

- *generate_subplots(imagens, ncols)*:  Gerar em *latex* o código para o posicionamento de subplots (figuras lado a lado), incluindo as legendas individuais e a legenda principal que corresponde ao grupo de gráficos. A função recebe um conjunto de imagens e o número de colunas desejado.

- *big_figure(imagem)*: Configurar um documento em latex, usando pacotes como afterpage, para garantir que a figura recebida ocupe exatamente uma página inteira e a numeração do documento volte ao normal depois.

- mais ideias?

  ## Módulo 8


  ## Módulo 9


  
