#import "setup/template.typ": *
#include "setup/capa.typ"
#show: project
#counter(page).update(1)
// #import "@preview/algo:0.3.3": algo, i, d, comment, code //https://github.com/platformer/typst-algorithms
#import "@preview/tablex:0.0.8": gridx, tablex, rowspanx, colspanx, vlinex, hlinex

#page(numbering:none)[
  #outline(indent: 2em)  
  // #outline(target: figure)
]
#pagebreak()
#counter(page).update(1)

O consumo energético é bastante relevante e tem se vindo cada vez mais a tornar-se mais importante com a constante evolução das tecnologias e com o crescimento demográfico no país. Daí surge a necessidade de propor desafios e medidas trazendo ao de cima temas como a sustentabilidade, a segurança energética e o gasto consciente de energia. 

Sendo a E-Redes líder na distribuição de energia em Portugal, permite colmatar exatamente estas necessidades e trazer respostas a estas exigências de forma prática e eficaz. Conta com um conjunto de máximas que asseguram um serviço de excelência de norte a sul do país, sendo assim de extrema importância a sua análise e estudo #cite(<edp_missions>):

- Garantir fornecimento de eletricidade para todos os consumidores, com qualidade, segurança e eficiência, através de linhas aéreas e de cabos subterrâneos de baixa, média e alta tensão; 

- Promover desenvolvimento da rede de distribuição que suporte a transição energética;

- Assegurar, de forma isenta, a disponibilidade de serviços aos agentes de mercado.

Com este pensamento a E-Redes está há mais de 40 anos a desenvolver-se e a desafiar-se no setor energético para garantir que este caminho invisível, mas fundamental permita chegar às casas dos consumidores, de forma a ter certeza que no final do dia a luz não se apaga.


Após a caracterização e o enunciamento das propostas da E-Redes conseguimos compreender a importância na análise dos dados da maior distribuidora de energia em Portugal. Devemos dar _insights_ e contribuir com informação valiosa para ajudar na missão da E-Redes de ser uma referência a nível europeu. Com estes dados procuramos trazer relevância, mas também espírito crítico no que toca a gastos de energia ou de eventuais fatores ocultos presentes na falta de energia, que podem ser detetados previamente confrontando com a experiência passada de casos semelhantes. 

Assim, o nosso foco está incidido, sobretudo, na seguinte questão, que será respondida no desenrolar do estudo:

Estudar as causas das quebras energéticas, prever e classificar padrões de tais eventos.



#pagebreak()

Info sobre Datasets *BOTAS ESTÁ A VER DISTO*:
1. Consumos mensais por concelho (https://e-redes.opendatasoft.com/explore/embed/dataset/3-consumos-faturados-por-municipio-ultimos-10-anos/table/?disjunctive.distrito&disjunctive.concelho)

  - Tem a data com mês e ano (entre 2020 e 2023, sendo 2020 poucos dados porque corta a meio este ano), tem localidade (nomeadamente distrito, concelho e freguesia)
  - info sobre consumo, sendo energia ativa e nível de tensão da rede que pode ser mais do que um entre baixa, média e alta tensões
2. Consumos mensais por código postal (https://e-redes.opendatasoft.com/explore/embed/dataset/02-consumos-faturados-por-codigo-postal-ultimos-5-anos/table/?sort=-date)
  - data em formato mês e ano (entre 2021 e 2023 completos, 2020 pequena porção)
  - tem codigo postal de 4 digitos distintos e energia ativa noutra coluna respetiva à area destes 4 dígitos
3. Caracterização de luminárias de Iluminação Pública (https://e-redes.opendatasoft.com/explore/embed/dataset/cadastro_iluminacao_publica/table/)
  - data com mês e ano em duas colunas distintas (aqui o mês aparece de 1 a 12 ao contrário das anteriores)
  - localidade (ou seja, distrito, concelho e freguesia)
  - tem info sobre o número de luminárias (tem muitos valores baixos, os valores mais altos desta variável aparecem tipo 1 vez só  distribuição here -> https://e-redes.opendatasoft.com/explore/embed/dataset/cadastro_iluminacao_publica/analyze/?dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkNPVU5UIiwieUF4aXMiOiJtZXMiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjRkZEQzAwIn1dLCJ4QXhpcyI6Imx1bWluYXJpYXMiLCJtYXhwb2ludHMiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImNhZGFzdHJvX2lsdW1pbmFjYW9fcHVibGljYSIsIm9wdGlvbnMiOnt9fSwic2VyaWVzQnJlYWtkb3duVGltZXNjYWxlIjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D)
  - tem o tipo de lampada que tem classes tipo Mercurio, LED, Sodio e a potencia total instalada em watts
4. Indicadores de continuidade de serviço por concelho (https://e-redes.opendatasoft.com/explore/embed/dataset/12-continuidade-de-servico-indicadores-gerais-de-continuidade-de-servico/table/)
  - saifi at num, saidi at min, maifi at num, tiepi mt min, end mt mwh, saifi mt num, saidi mt min, maifi mt num, saifi bt num, saidi bt min (tem estas colunas numericas dps pesquisar)
  - tem o ano, nuts III, o concelho e o codigo do concelho e a zona rqs que pode ser:
    - Zona A – capitais de distrito e localidades com mais de 25000 clientes;
    - Zona B – localidades com número de clientes entre 2500 e 25000 clientes;
    - Zona C – os restantes locais;
    - Concelho. 
5. Pontos de ligação para postos de Carregamento de Veículos Elétricos (https://e-redes.opendatasoft.com/explore/embed/dataset/postos_carregamento_ves/table/)
  - tem a data em termos de trimestre do ano, ou seja, no tipo 2022T3
  - localidade (3 colunas com distrito, concelho e freguesia)
  - a potencia maxima admissivel em kW (esta coluna n esta em numerico pq o campo tem numero + kW sempre)
  - tem os postos de ligação para instalações de PCVE
6. Total de unidades de produção para autoconsumo (https://e-redes.opendatasoft.com/explore/embed/dataset/8-unidades-de-producao-para-autoconsumo/table/)
  - tem data com ano e trimestre (ex: 2022T3)
  - distrito e concelho apenas, nao tem freguesia
  - escalão de potencia (acho que em forma de intervalo pq esta do tipo ]30, 1000])
  - numero de instalações e a potencia total instalada em kW
7. Consumo Horário por Código Postal - 4 Dígitos (https://e-redes.opendatasoft.com/explore/embed/dataset/consumos_horario_codigo_postal/table/?sort=datahora)
  - tem data em formato dia, mes e ano com hora, contudo tem mais duas colunas com data e hora que esta incoerente com a 1ª coluna "Data/Hora" (1 de outubro de 2023 00:00 aparece mal com as outras duas colunas e 1 de novembro de 2022 00:00 aparece correto) *a investigar se for relevante estudar isto*
  - tem codigo postal com os primeiros 4 dígitos e energia ativa em kWh
8. Capacidade de Receção na Rede Nacional de Distribuição (RND) (https://e-redes.opendatasoft.com/explore/embed/dataset/capacidade-rececao-rnd/table/)
  - * tem so uma linha e tem um link que é um mapa* Capacidade de Receção na Rede Nacional de Distribuição (RND) https://e-redes.opendatasoft.com/pages/capacidade_rececao_rnd/
  /* pode ser interessante questionar a origem dos dados */
9. Consumo Horário por Código Postal - 7 Dígitos (https://e-redes.opendatasoft.com/explore/embed/dataset/consumo_horario_codigo_postal_7_digitos/table/?sort=codigo_postal)
  - tem 13 linhas com intervalos de codigos postais de quatro digitos e um link associado a cada um deles
  - dentro de cada link (ex: https://e-redes.opendatasoft.com/explore/embed/dataset/consumoshorariocodigopostal1000a2000/table/) temos o codigo postal com 7 digitos, a energia ativa em kWh Data/Hora numa coluna junta e separado em duas colunas também com a tal incongruência de horas como já tinha reparado no *tópico 7.*
10. Ligações à rede (https://e-redes.opendatasoft.com/explore/embed/dataset/16-pedidos-concluidos-plrs/table/)
  - tem a data em formato ano e semestre tanto junto numa coluna como separado em duas
  - concelho e o código do concelho
  - numero de pedidos de ligação à rede executados (vals numericos)
11. Número de contratos de energia ativos por tipo de contador (https://e-redes.opendatasoft.com/explore/embed/dataset/21-contadores-de-energia/table/)
  - tem data com mês e dia
  - localidade com distrito, concelho e freguesia
  - tem uma coluna se tem contador inteligente (com sim 
 ou não) e o número de CPEs
12. Número de locais de consumo de baixa tensão com Leituras Remotas (https://e-redes.opendatasoft.com/explore/embed/dataset/23-leituras-recolhidas-remotamente/table/?sort=-data)
  - data com ano e mês em numerico junto e separado em duas colunas
  - localidade com distrito, concelho e freguesia
  - numero de CPEs com leitura
13. Interrupções de Energia ativas (https://e-redes.opendatasoft.com/explore/embed/dataset/outages-per-geography/table/)
  - no momento em que vi tinha uma linha com tudo nulo e so com o campo da data preenchido *DEPOIS VER SE FOI ACRESCENTADO*
  - talvez são as interrupeções no momento e que vai atualizando no momento
14. Interrupções de Energia programadas (https://e-redes.opendatasoft.com/explore/embed/dataset/network-scheduling-work/table/)
  - tem infos relativas à data, localidade (tipo distrito e concelho)
  - tem data de inicio, data de fim e duração estimada que são momentos futuros e próximos (esta bd está em constante atualização, deve ser mais para API's)
15. Caracterização de Pontos de Consumo (CPEs), com contratos ativos (https://e-redes.opendatasoft.com/explore/embed/dataset/20-caracterizacao-pes-contrato-ativo/table/?disjunctive.tipo_de_instalacao)
  - tem data e mês em numericos 
  - tem localidade com distrito, concelho e freguesia e tem um identificador unico de distrito, concelho e freguesia
  - diz o tipo de instalação (se é publica, domestico, n domestico, etc.), nível de tensão com baixa, media, alta e muito alta tensoes como classes mas ainda se é normal ou especial
  - uma coluna com o numero de CPEs
16. Número de ordens de serviço remotas realizadas (https://e-redes.opendatasoft.com/explore/embed/dataset/15-ordens-de-servico/table/)
  - data com ano e mês em numerico junto e separado em duas colunas
  - localidade com distrito, concelho e freguesia e tem um identificador unico de distrito, concelho e freguesia
  - tipo de serviço e as ordens de serviço realizadas em numérico
17. Número de locais de consumo de baixa tensão com recolha de Diagramas de Carga (https://e-redes.opendatasoft.com/explore/embed/dataset/22-diagrama-de-carga-por-instalacao/table/)
  - data com ano e mês em numerico junto e separado em duas colunas
  - localidade com distrito, concelho e freguesia e tem um identificador unico de distrito, concelho e freguesia
  - se inclui mobilidade elétrica ou não e o número de CPEs com DCs recolhidos
18. Postos de Transformação Distribuição (PTD) (https://e-redes.opendatasoft.com/explore/embed/dataset/postos-transformacao-distribuicao/table/)
  - Nível de Utilização em % representado por um intervalo de valores
  - potência instalada em kVa (var numérica)
  - coordenadas geográficas com muitas casas decimais /* yupii */
19. Novas unidades de produção para Autoconsumo (https://e-redes.opendatasoft.com/explore/embed/dataset/26-centrais/table/)
  - data com ano e semestre
  - concelho e codigo de concelho em duas colunas diferentes 
  - potência de ligação em kW e número de processos concluídos
20. Novas ligações à rede de centros electroprodutores (https://e-redes.opendatasoft.com/explore/embed/dataset/25-plr-producao-renovavel/table/)
  - data com ano e semestre
  - concelho e codigo de concelho em duas colunas diferentes 
  - potência de ligação em kW e número de pedidos de ligação à rede executados
  - tem muito poucos dados (89 itens)
21. Novas ligações à rede associados à mobilidade elétrica (https://e-redes.opendatasoft.com/explore/embed/dataset/9-plr-mobilidade-eletrica/table/)
  - data com ano e semestre
  - concelho e codigo de concelho em duas colunas diferentes
  - número de pedidos de ligação à rede executados

1 - CONSUMO  MENSAIS POR FREGUESIA                 - 3 anos e pouco
2 - CONSUMOS MENSAIS POR CODIGO POSTAL (4 digitos) - 3 anos e pouco
7 - CONSUMO  HORARIO POR CODIGO POSTAL (4 digitos) - 1 mês
9 - CONSUMO  HORARIO POR CODIGO POSTAL (7 digitos) - 1 mês (diferentes fsr)

4 - PARECE INTERESSANTE
15 - util se acompanhado pelo mapa possivelmente  (8)

#pagebreak()

#bibliography("setup/bib.yml", style: "ieee"/* style: "setup/apa.csl" */, full: true)
