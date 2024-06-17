#import "setup/template.typ": *
#import "setup/sourcerer.typ": code
#include "setup/capa.typ"
#show: project
#counter(page).update(1)
// #import "@preview/algo:0.3.3": algo, i, d, comment, code //https://github.com/platformer/typst-algorithms
#import "@preview/tablex:0.0.8": gridx, tablex, rowspanx, colspanx, vlinex, hlinex, cellx
#import "@preview/big-todo:0.2.0": *
#show link: underline
#show ref: underline
#show link: set text(rgb("#004C99"))
#show ref: set text(rgb("#00994C"))
#set heading(numbering: "1.")
#show raw.where(block: false): box.with(
  fill: luma(240),
  inset: (x: 0pt, y: 0pt),
  outset: (y: 3pt),
  radius: 3pt,
)
#show heading.where(level: 1): set align(center)
#show heading.where(level: 1): set text(20pt)
#show heading.where(level: 1): box.with(
  fill: rgb("#ffdc01"),
  inset: (x: 120pt, y: 1pt),
  outset: (y: 5pt),
  radius: 5pt,
  stroke:.77pt+rgb("000"),
  width: 18cm,
  
)

// #page(numbering:none)[
//   #outline(indent: 2em)  
//   // #outline(target: figure)
// ]

#show outline.entry.where(
  level: 1
): it => {
  v(12pt, weak: true)
  strong(it)
}
#outline(indent: auto)

#show quote.where(block: false): it => {
  ["] + h(1pt, weak: true) + it.body + h(1pt, weak: true) + ["]
  if it.attribution != none [ (#it.attribution)]
}

#show quote: set text(black, weight: "bold", 12pt)


#pagebreak()

= Introdução


O presente trabalho foi realizado no âmbito da unidade curricular de Projeto final aplicado a Ciência de Dados, onde era pedido que escolhêssemos um tema e uma entidade para trabalhar com, ao mesmo tempo que éramos orientados por um docente da UC. Dentro das várias opções trabalhámos os dados da E-Redes, fornecidos pela OpenDataSoft#footnote[https://e-redes.opendatasoft.com/explore/?exclude.keyword=internal&sort=modified], com especial enfoque para as falhas na rede elétrica, onde fomos orientados pelo professor Luís Nunes.

O consumo de energia é um tema cada vez mais relevante e desafiador, impulsionado pela evolução da ciência, tecnologia e pela integração da energia na vida humana, surgindo, assim, novos problemas como a sustentabilidade, a segurança energética e o consumo consciente de energia.

Neste projeto, propomos utilizar o CRISP-DM (_Cross-Industry Standard Process for Data Mining_) para realizar uma análise aprofundada dos dados disponíveis no portal de dados abertos da E-Redes. O objetivo principal é prever o número de falhas energéticas, identificar os seus locais específicos, otimizar o processo de reconhecimento de incidentes e oferecer _insights_ para a implementação de medidas de segurança proativas, visando a prevenção de falhas no futuro.

O CRISP-DM é um modelo de processo de _data mining_ que descreve abordagens usualmente utilizadas por especialistas para "atacar" e resolver problemas. Ele é composto por seis fases:

1. *_Business Understanding_*: Definir os objetivos do projeto e entender as necessidades da E-Redes;\
2. *_Data Understanding_:* Explorar e analisar os dados disponíveis no portal de dados abertos da E-Redes e de outras entidades;\
3. *_Data Preparation_*: Limpar, transformar e preparar os dados para a análise;
4. *_Modelling_* Desenvolver modelos preditivos para prever o número e a localização de falhas energéticas;
5. *_Evaluation_*: Avaliar o desempenho dos modelos preditivos e selecionar o melhor modelo;
6. *_Deployment_*: Implementar o modelo selecionado na E-Redes e monitorizar seu desempenho.

Acreditamos que este projeto pode contribuir para uma gestão mais eficiente e resiliente da rede de distribuição elétrica da E-Redes, de forma a garantir um fornecimento de energia mais seguro e confiável para todos os consumidores.

#figure(
image("imagens/CRISP-DM.png", width: 53%),
  caption: [CRISP-DM]
)<Crisp-dm>

#pagebreak()

= Business Understanding

O consumo de energia tem vindo a tornar-se progressivamente um tema cada vez mais relevante e desafiador. Esta crescente relevância é impulsionada pela constante evolução da ciência e das tecnologias, que integram a energia na vida humana. Consequentemente, surgem novos problemas a serem combatidos, tais como a *sustentabilidade*, a *segurança energética* e o *consumo consciente de energia*.

A #link("https://www.e-redes.pt/pt-pt")[E-Redes] é uma distribuidora de energia em Portugal e líder no setor, com mais de 40 anos de história. Em 2023, contava com 6.4 milhões de clientes e uma rede de distribuição de 234.669 km, que permite satisfazer as necessidades de todos os clientes de forma prática e eficaz. A E-Redes adota um conjunto de máximas que asseguram um serviço de excelência de norte a sul do país, sendo fundamental a sua análise e estudo#footnote[https://www.e-redes.pt/pt-pt/noticias/2021/01/29/edp-distribuicao-agora-e-e-redes]:

- Garantir o fornecimento de eletricidade a todos os consumidores com qualidade, segurança e eficiência, através de linhas aéreas e cabos subterrâneos de baixa, média e alta tensão;
- Promover o desenvolvimento da rede de distribuição que suporte a transição energética;
- Assegurar, de forma isenta, a disponibilidade de serviços aos agentes de mercado.

Com este propósito em mente, a E-Redes dedica-se há mais de 40 anos a evoluir e a superar-se no setor energético. A sua missão é garantir que este fluxo vital, invisível, mas crucial, funcione de forma impecável, levando energia a todas as casas dos consumidores. Dia após dia, a empresa trabalha incansavelmente para que a luz nunca se apague. *Mas, e se falhar?*

Uma falha no fornecimento de energia teria consequências imediatas e devastadoras para a sociedade portuguesa. Serviços essenciais, como hospitais, sistemas de comunicação e transportes públicos, seriam paralisados, colocando em risco vidas e causando enormes transtornos na vida das pessoas. As atividades económicas e sociais também sofreriam um impacto imediato, com fábricas a parar, lojas a fechar e escolas a cancelar aulas. Para combater este problema, a E-Redes conta com trabalhadores preparados para lidar com qualquer tipo de acidente que possa ocorrer. No entanto, esta solução não é perfeita, pois a resolução dos problemas pode levar algumas horas, prejudicando todos os tipos de consumidores. *Mas e se fosse possível prever e identificar padrões nestes acidentes?*

Propomo-nos a realizar uma análise aprofundada dos dados disponíveis no portal de dados abertos da E-Redes, acessível em #link("e-redes.opendatasoft.com"). O nosso objetivo principal consiste na previsão não apenas do número de falhas energéticas, mas também na identificação dos seus locais específicos, visando contribuir para a implementação de inspeções mais controladas e reguladas. Além disso, almejamos identificar padrões recorrentes nas falhas energéticas, otimizando o processo de reconhecimento desses incidentes. Por exemplo, ao analisar se determinadas falhas estão associadas a condições climáticas específicas numa determinada localidade, pretendemos oferecer _insights_ que possam informar a implementação de medidas de segurança proativas, visando a prevenção de tais falhas no futuro. Este enfoque rigoroso e analítico visa fortalecer a eficácia das operações da E-Redes, contribuindo para uma gestão mais eficiente e resiliente da rede de distribuição elétrica.

Assim, o nosso foco incide, sobretudo, na seguinte questão, que será respondida no desenrolar do estudo:

#set quote(block: false)
#show quote: set align(center)

#quote[*Estudar as causas das quebras energéticas, prever e classificar padrões de tais eventos.*]

#align(center + horizon)[
  
#box(
  fill: rgb("#ffdc01"),
  inset: (x: 190pt, y: 1pt),
  outset: (y: 0pt),
  radius: 5pt,
  stroke:.77pt+rgb("000"),
)[#image("imagens/e-redes-logotipo.jpg", height: 7%)]

]

#pagebreak()
= Data Understanding


Uma #link("https://www.e-redes.pt/pt-pt/continuidade-de-servico")[quebra energética], segundo a E-Redes, ocorre quando a tensão de alimentação no ponto de entrega é inferior a 5% da tensão declarada. Se durar mais de 3 minutos, é considerada longa; se for inferior a um segundo é momentânea; as restantes são breves. Estas podem ser previstas (programadas) ou acidentais (inesperadas). Somado a isto, é importante ter em conta que a rede de distribuição pode ser:
- $bold("AT" arrow "Alta Tensão /" "MT" arrow "Média Tensão /" "BT" arrow "Baixa Tensão")$

== Indicadores gerais de continuidade de serviço
Estas quebras afetam a continuidade do serviço e, para avaliar esta continuidade, a E-Redes utiliza os seguintes indicadores gerais relativos aos pontos de entrega às instalações de consumo:

#figure(
  tablex(
    columns: 4,
    align: (col, row) => {
      if row == 0 {
        center
      } else if (1,2,3,4,5).contains(col) {
        center
      } else {center}
    },
    map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("ffd700") } else { none })
    },
  ),
    header-rows:1,
    header-columns:1,
    auto-lines: false,
    hlinex(stroke:0.5mm),
    [*Indicadores Gerais*], 
    // vlinex(stroke:0.2mm),
    [*Quantidade*], [*Duração*], [*Rede de Distribuição*],
    hlinex(stroke:0.5mm),

    [*SAIFI*], [F - Frequência], [-], [ (AT, MT, BT)],
    [*SAIDI*], [-] , [D - Duração], [ (AT, MT, BT)],
    [*MAIFI*], [F - Frequência] , [-], [ (AT, MT)],
    [*TIEPI*], [-] , [-], [(MT)],
    [*END*], [-] , [-], [(MT)],
    hlinex(stroke:0.2mm),
),
caption: [Principais indicadores gerais; período de cálculo: 1 ano (indicadores anuais)],
kind:table
) <indicadores_gerais>

Relativamente aos indicadores Gerais, temos os seguintes:
- Frequência Média de Interrupções Longas do Sistema (*SAIFI*) 
- Duração Média das Interrupções Longas do Sistema (*SAIDI*)
- Frequência Média das Interrupções Breve do Sistema (*MAIFI*)
- Tempo de Interrupção Equivalente da Potência Instalada (*TIEPI*)
- Energia Não Distribuída (*END*)

== Zonas de Qualidade de Serviço

#set text(11pt)
#set rect(
  inset: 15pt,
  fill: rgb("fff"),
  width: 10%,
  stroke: 0.1pt,
)

#align(horizon + center)[
  #figure(
  grid(
    columns: 2, 
    gutter: 1pt,
    rows: 1,
    image("imagens/ZonaQualidadeServico.png", width: 85%),
    
    rect(
      
      [
            
      #emph(text(rgb("#008000"))[
  _*Zona A:*_
])
    
      
  • Capitais de distrito e lugares com mais de 25000 clientes.
  
  • Infraestrutura elétrica mais desenvolvida e manutenção mais frequente.
      \
      
      #emph(text(rgb("#002379"))[
  _*Zona B:*_
])
      
  • Lugares com um número de clientes entre 2 500 e 25 000.
  
  • Qualidade do serviço média, com uma probabilidade de interrupções maior do que na Zona A.
      \
      
       #emph(text(rgb("#FF0000"))[
  _*Zona C:*_
])
      
  • Lugares com um número de clientes inferior a 2 500.
  
  • Infraestrutura elétrica menos desenvolvida e a manutenção menos frequente.

], width: 100%, radius: (
    left: 5pt,
    right: 5pt,
  ))

  ),
  caption: [
    Zonas de qualidade de serviço
  ],
)<qualidadeservico>
]

#set text(11pt)
== Mini-Revisão de literatura
#let etal = "et al."
#show "neurais": "neuronais"
A previsão de quebras energéticas é extensivamente explorada em literatura académica em vários contextos, objetivos e locais, especialmente no contexto de catástrofes naturais. Por exemplo,
#link("https://ieeexplore.ieee.org/document/8656482")[Cerrai #etal (2019)]
treinaram vários modelos para prever o número de quebras energéticas durante tempestades no nordeste dos Estados Unidos, utilizando variáveis de meteorologia, dados do bioma do local (o tipo de floresta que era, variáveis de vegetação da área), e variáveis da infraestrutura elétrica do local (número de transformadores, número de interruptores... por cada célula); os resultados depois são enviados para equipas de resposta para que elas se preparem adequadamente. // O artigo diferencia do nosso projeto principalmente no facto de eles 

Outros artigos, como o de #link("https://arxiv.org/abs/2404.03115")[Wang #etal (2024)], não têm este foco de desastre naturais. Eles usaram dois _perceptron_ multi-camadas (redes neuronais) para prever o número de utilizadores que perdem energia hora à hora numa área do estado de Michigan, concluindo que a inclusão de variáveis socio-económicas e demográficas sobre o local melhoraram os resultados.

Alguns artigos defletem de métodos de aprendizagem tradicionais, como o de #link("https://ieeexplore.ieee.org/document/8849044")[Zhang #etal (2019)]. Eles preveem o número de quebras energéticas anuais na área de Turim usando um Modelo Cinzento $"GM"(1,1)$, um método "clássico para estudar a tendência a partir de séries de dados discretos com amostras limitadas e informação inadequada", e otimização por enxame de partículas (PSO).

Finalmente, #link("https://www.mdpi.com/1233424")[Mahmoud #etal (2021)], na sua revisão sistemática em Manutenção preditiva em _Smart Grids_, dividem os métodos de previsão em métodos convencionais - método que olham para a eletricidade e infraestrutura diretamente para a previsão; e métodos de aprendizagem automática, como SVMs, ANNs, _Random Forests_, e RNNs. Eles associam análise de causas e técnicas adequadas, com base nos artigos que reviram. // Eles discutem também a motivações para da previsão de forma extensiva, e os desafios relacionados a tal. Sobre a primeira, os autores notam que a previsão leva a uma melhor experiência do consumidor, uma expansão da eficiência das redes (levando a diminuição de custos), a uma manutenção melhor, e a uma redução de emissões de gases com efeitos de estufa. Sobre a segunda, os autores mencionam cibersegurança (sendo que dados errados na rede por culpa de ciberataques pode danificar a rede), custo da  //nvm isto e geralmente sobre smart grid nao sobre a previsão

A nosso conhecimento, não existe nenhum artigo académico que faça previsão de quebras energéticas de nenhum local de Portugal.

== Problema $arrow$ Limitações iniciais

O primeiro grande desafio surgiu com a obtenção dos dados da E-Redes através do portal #link("https://e-redes.opendatasoft.com/pages/homepage/")[*_Open Data_*]. Os indicadores de continuidade de serviço estavam disponíveis apenas numa base #link("https://e-redes.opendatasoft.com/explore/dataset/12-continuidade-de-servico-indicadores-gerais-de-continuidade-de-servico/table/")[anual], o que inicialmente impossibilitava qualquer análise detalhada das quebras energéticas ao longo do tempo. Essa limitação prejudicou gravemente o início do projeto, pois, sem dados temporais detalhados, tornava-se inviável realizar uma análise precisa e significativa desde o começo. Consequentemente, isso afetou a nossa capacidade de conduzir estudos aprofundados e detalhados sobre a frequência e o impacto das quebras energéticas. Era necessário encontrar uma solução!

=== A Descoberta dos Eventos Excecionais

Após uma extensa pesquisa e análise, identificámos os #link("https://www.e-redes.pt/pt-pt/o-que-fazemos/qualidade-de-servico/eventos-excecionais")[eventos excecionais] como uma oportunidade única para estudar as quebras energéticas. Os eventos excecionais são ocorrências raras e significativas de interrupções no fornecimento de energia elétrica, documentadas detalhadamente no portal da E-Redes. Focar nesses eventos permitiu-nos não só compreender melhor as causas e os efeitos das quebras energéticas, mas também explorar as respostas e medidas adotadas pela operadora de rede para mitigar tais incidentes. Apesar de lidarmos com um número limitado de quebras energéticas (apenas aquelas avaliadas quanto à sua excecionalidade), esta foi a melhor solução encontrada. Além disso, analisamos os #link("https://www.e-redes.pt/pt-pt/o-que-fazemos/qualidade-de-servico/documentacao")[documentos de qualidade de serviço] para aprofundar o conhecimento sobre o tema.



=== Recolha dos dados

Inicialmente, enfrentámos o desafio de coletar os dados #link("https://iscteiul365-my.sharepoint.com/:x:/g/personal/daafs_iscte-iul_pt/EVxhhhvypW5DlfCuwT9QtiIBItRZoxkVG8VqgOHsr2nFBQ?e=gLGvPa")[manualmente], uma vez que os relatórios disponíveis consistiam, principalmente, em imagens de tabelas, impossibilitando a automação do processo (#link("https://www.e-redes.pt/sites/eredes/files/2023-04/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Junho%202022.pdf")[Link com um exemplo  de relatório]). No entanto, a nossa persistência levou-nos à descoberta de um recurso valioso: o #link("https://www.erse.pt/eletricidade/qualidade-de-servico/")[Power BI] da ERSE, que continha relatórios PDF bem estruturados e formatados. Esta ferramenta não só simplificou a coleta de dados, mas também proporcionou informações adicionais e contextuais que enriqueceram a nossa análise.

== Compreensão dos dados principais


De forma geral, cada relatório seguia um esquema de tabelas semelhante ao representado na @eventos_exc. Essas tabelas incluíam não apenas códigos, datas e clientes afetados, mas também os valores dos indicadores gerais, conforme descrito na @indicadores_gerais.

#set par(justify: false)
#set text(hyphenate: false)

#figure(
  tablex(
    columns: 9,
    align: center + horizon,
    header-rows: 1,
    header-columns: 1,
    auto-lines: true,
    stroke: 0.1mm,

    map-cells: cell => {
      if cell.y == 0 {
        cell.content = {
          let text-color = white
          set text(text-color)
          strong(cell.content)
        }
      }
      cell
    },

    map-rows: (row, cells) => cells.map(c => 
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("#010100") } else { none })
    }
  ),

    map-cols: (column, cells) => cells.map(c => 
      if c == none or c.y == 0 {
        c
      } else {
        (..c, fill: if column == 0 or column == 2 or column == 4 or column == 6 { rgb("#f8bf91") } 
        else if column == 1 or column == 3 or column == 5 { rgb("#fdd4b4") }
        else if column == 7 or column == 8 { rgb("#dadada") }
        else { none })
      }
    ),

    // Colunas
    [Código do Relatório],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Concelho Origem],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Data],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Nível De Tensão],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Causa],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Duração incidente],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Nº Cliente afetados],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Indicadores (...)],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 3, stroke: black + 0.1mm),
    [Decisão],
    
    [...], [...], [...], [...], [...], [...],[...], [...], [...],
    hlinex(stroke: 0.1mm),
    [...], [...], [...], [...], [...], [...], [...], [...], [...]
  )
,caption: [Esquema da tabela dos respetivos eventos excecionais dos relatórios de qualidade e serviço],
kind: table 
)<eventos_exc>

- *Código do Relatório*: identificador único que contém a data e número do evento;
//- *Concelho Origem*: local, ou em alguns casos locais, em que ocorreu o evento;
//- *Data*: dia, mês e ano em que o evento ocorreu 
- *Nível de tensão*: qual foi o tipo de rede de distribuição afetada (AT, MT, BT);/*(AT $arrow$ Alta Tensão, MT $arrow$ Média Tensão, BT $arrow$ Baixa Tensão)*/
- *Causa*: o que originou o evento (ex: Veículos, Aves, Furtos, Escavações, Descarga Atmosférica, entre outras);
- *Duração incidente*: quanto tempo, em minutos, durou o incidente;
- *Nº clientes afetados*: qual o número de clientes que foram afetados pelo evento;
//- *Indicadores*: indicadores gerais, já descritos na @indicadores_gerais;
- *Decisão*: evento considerado excecional $arrow$ _Sim_ / evento não considerado excecional $arrow$ _Não_

#set par(justify: true)
#set text(hyphenate: true)

No entanto, foi necessário realizar uma limpeza desses dados, como será discutido mais adiante (@TratarDadosExcecionais), pois o esquema das tabelas mudou ao longo dos anos e ainda existem alguns erros aparentes.

== Dados de Extras/Terceiros
Para enriquecer as conclusões do trabalho, foi necessário recolher dados de outras fontes, pois fatores relativos ao território e ao clima têm uma grande influência nas quebras energéticas. Abaixo, estão listados os respetivos dados que auxiliaram as conclusões ao longo do trabalho, com uma breve explicação dos mesmos nos anexos:

- Dados Meteorológicos $arrow$ *IPMA*: #ref(<IPMA>, supplement: none)
- Dados Territoriais $arrow$ *GPP*: #ref(<GPP>, supplement: none)
- Dados Socioeconómicos $arrow$ *Pordata*: #ref(<Pordata>, supplement: none)
- Localização das subestações $arrow$ *E-REDES*: #link("https://e-redes.opendatasoft.com/pages/capacidade_rececao_rnd/")[RND] _&_ #link("https://e-redes.opendatasoft.com/explore/dataset/postos-transformacao-distribuicao/table/")[PTD]
- Shapefile dos concelhos $arrow$ *dados.gov*: #link("https://dados.gov.pt/en/datasets/concelhos-de-portugal/")[shp]
- Zonas de Qualidade de Serviços $->$ #link("https://app.powerbi.com/view?r=eyJrIjoiZGIyYzlkYTEtYzVhMS00MTkxLWE5OGEtOWQzZTRlMThmM2NkIiwidCI6ImIwMzU0MDBkLTE3NzYtNDYyZi04YjIxLTYxMTYzYWI0MDNkZiIsImMiOjl9")[ERSE Power BI] (Secção "Postos de Transformação")

== Visualização do número das quebras energéticas


#figure(
  grid(
    columns: (400pt, 130pt), gutter: -10pt,
    rows: 1,
    align: (horizon + center),
    image("imagens/BarrasNumQuebEner.svg", width: 100%),
        rect([

À esquerda, podemos visualizar o número de interrupções energéticas que ocorreram em cada distrito. Lisboa destaca-se em primeiro lugar, de forma significativa, enquanto a Guarda é o distrito com o menor número de interrupções energéticas.
          
], inset: 7pt,
  fill: rgb("fff"),
  width: 110%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  )),
  ),
  caption: [
    _Barplot_ com o número de quebras energéticas por distrito
  ],
) <NumeroDeQuebrasEnergeticasBarras>

#figure(
  grid(
    columns: (300pt, 230pt), 
    gutter: 0pt,
    rows: 1,
    align: (horizon + center),
    rect([
O relatório dos eventos excecionais foca-se nos concelhos como ponto geográfico de análise. Assim, optou-se por usar os concelhos na representação visual para facilitar a compreensão dos dados e respeitar as informações fornecidas. Embora esta abordagem assuma que os concelhos são independentes entre si, consideramos que é a melhor forma de visualizar as informações.

Entre todos os concelhos, Lisboa destaca-se de forma significativa, apresentando o maior número de quebras energéticas. Este concelho registou um número de eventos excecionalmente elevado, o que o coloca numa posição de destaque, comparado com os restantes concelhos.

Por outro lado, alguns concelhos encontram-se representados a preto no mapa. Esta escolha visual deve-se à inexistência de quebras energéticas nestas localidades. Além disso, esta decisão também foi influenciada por uma deliberação do grupo, que será explicada mais à frente no relatório (@EliminarDados). Desta forma, procuramos proporcionar uma visualização clara e intuitiva dos dados relativos às interrupções energéticas em cada concelho.
], inset: 12pt,
  fill: rgb("fff"),
  width: 90%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  )),
  
  image("imagens/ConcelhosNumEventos.png", width: 100%),
  ),  
  caption: [
    _Barplot_ com o número de quebras energéticas por distrito
  ],
) <NumeroDeQuebrasEnergeticasMap>

\

= Data Preparation

\

== Tratamento dos dados principais <TratarDadosExcecionais>

\

Nesta secção, serão abordados todos os problemas que encontramos nos dados recolhidos nos diferentes relatórios da E-Redes, tanto na recolha, quanto no tratamento dos mesmos.

=== Evolução de tempo dos relatórios

No processo de recolha, deparamo-nos com um pequeno pormenor: com o passar do tempo, a E-Redes foi evoluindo a forma como guardava os dados relativos às quebras energéticas, resultando no surgimento de novas variáveis e no desaparecimento de outras. Um exemplo simples pode ser encontrado no seguinte #link("https://www.erse.pt/media/qzwn3hb2/td_janeiro_dezembro_2016-edpd.pdf")[link], onde podemos visualizar um relatório onde as tabelas possuem uma coluna intitulada de `Código do Relatório`, coluna esta que só existe nos relatórios de 2016.
Outro exemplo também pode ser o aparecimento da coluna `Qualidade de Energia Elétrica` em 2017 (#link("https://www.erse.pt/media/qzwn3hb2/td_janeiro_dezembro_2016-edpd.pdf")[Antes] $arrow$ #link("https://www.erse.pt/media/jpad2oun/td_janeiro_dezembro_2017-edpd.pdf")[Depois]).

Para superar este problema, foi necessário realizar vários testes e atualizar o código até conseguirmos ter sucesso. Este processo envolveu a adaptação contínua às mudanças nos relatórios, garantindo que todos os dados relevantes fossem corretamente identificados e integrados na nossa análise.

\

=== Datas inseridos de forma incorreta

#set text(10pt)

#figure(
  grid(
    columns: 2, gutter: 4pt,
    rows: 1,
    align: (horizon + center),
    rect([
      
Outro problema encontrado foram os valores incorretos relativos às datas dos incidentes. Em vez de apresentarem datas comuns como, por exemplo, #datetime.today().display(), apareciam números que, à primeira vista, pareciam incorretos e sem significado. Contudo, após uma breve pesquisa, descobrimos que esses números escondiam um segredo.

O Excel tem a capacidade de armazenar datas como números sequenciais para que possam ser usados em cálculos. Por padrão, o dia $1$ de janeiro de $1900$ é representado pelo número serial $1$, e o dia $1$ de janeiro de 2008 é o número serial $39448$ porque corresponde a $39448$ dias após $31$ de dezembro de $1899$.

Além disso, apenas as quebras energéticas ocorridas após 2020 (exceto em 2021) incluíam a hora exata dos incidentes. Infelizmente, foi necessário abdicar da precisão horária devido à falta de informação sobre o horário das restantes quebras energéticas.

], width: 98%, radius: (
    left: 5pt,
    right: 5pt,
  )),
    tablex(
    columns: (90pt, 90pt),
    rows: (60pt, 60pt),
    align: center + horizon,
    header-rows: 1,
    header-columns: 1,
    auto-lines: false,
    stroke: 0.1mm,

    map-cells: cell => {
      if cell.y == 0 {
        cell.content = {
          let text-color = white
          set text(text-color)
          strong(cell.content)
        }
      }
      cell
    },

    map-rows: (row, cells) => cells.map(c => 
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("#010100") } else { none })
    }
  ),

    map-cols: (column, cells) => cells.map(c => 
      if c == none or c.y == 0 {
        c
      } else {
        (..c, fill: if column == 0 or column == 2 or column == 4 or column == 6 { rgb("#f8bf91") } 
        else if column == 1 or column == 3 or column == 5 { rgb("#fdd4b4") }
        else if column == 7 or column == 8 { rgb("#dadada") }
        else { none })
      }
    ),

    // Colunas
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [DataOld],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [DataNew],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    
    [27/10/2017], [27/10/2017],
    hlinex(stroke: 0.1mm),
    [39448], [01/01/2008],
    hlinex(stroke: 0.1mm),
    [03/12/2019 11:09], [03/12/2019],
    hlinex(stroke: 0.1mm),
  )
  ),
  caption: [
    Tabelas com datas incorretas e solução encontrada para corrigir
  ],
) <DatasErradasEventoExcecional>

#set text(11pt)

=== Códigos do relatório inconsistentes

#set text(10pt)
#set par(justify: false)
#set text(hyphenate: false)

#figure(
  grid(
    columns: 2, gutter: 4pt,
    rows: 1,
    align: (horizon + center),
  
    tablex(
    columns: (65pt, 65pt, 65pt, 65pt),
    rows: (50pt, 50pt, 50pt, 50pt),
    align: center + horizon,
    header-rows: 1,
    header-columns: 1,
    auto-lines: true,
    stroke: 0.1mm,

    map-cells: cell => {
      if cell.y == 0 {
        cell.content = {
          let text-color = white
          set text(text-color)
          strong(cell.content)
        }
      }
      cell
    },

    map-rows: (row, cells) => cells.map(c => 
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("#010100") } else { none })
    }
  ),

    map-cols: (column, cells) => cells.map(c => 
      if c == none or c.y == 0 {
        c
      } else {
        (..c, fill: if column == 0 or column == 2 or column == 4 or column == 6 { rgb("#f8bf91") } 
        else if column == 1 or column == 3 or column == 5 { rgb("#fdd4b4") }
        else if column == 7 or column == 8 { rgb("#dadada") }
        else { none })
      }
    ),

    // Colunas
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [Código do Relatório (adaptado)],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [Concelho Origem],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [Data do incidente],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    [Nº Clientes Afetados],
    vlinex(start: 0, end: 1, stroke: white + 0.1mm),
    vlinex(start: 1, end: 4, stroke: black + 0.1mm),
    
    [2016_FEV_085], [ALMADA], [2016-02-24], [10],
    hlinex(stroke: 0.1mm),
    [2016_FEV_085], [ALMADA],
    [2016-02-27], [3],
    hlinex(stroke: 0.1mm),
    [2016_FEV_085], [ALMADA],
    [2016-02-28], [5],
    hlinex(stroke: 0.1mm),
  ),
  rect([

Relativamente ao Código do Relatório, existiam linhas que possuíam o mesmo código, mas apresentavam diferentes características das quebras (`Clientes afetados`, `indicadores gerais`, `Data do incidente`, etc...). Como esses casos não eram numerosos, optou-se por eliminar essas entradas para evitar discordâncias e erros na lógica dos eventos que pudessem comprometer o modelo no futuro.

], width: 95%, radius: (
    left: 5pt,
    right: 5pt,
  )),
  ),
  caption: [
    Tabelas com datas incorretas
  ],
kind:image
  
) <CodRelEventoExcecional>

#set text(11pt)
#set par(justify: true)
#set text(hyphenate: true)

=== Tratamento do número de quebras energéticas <EliminarDados>

#set text(10pt)

#figure(
  grid(
    columns: 2, gutter: 4pt,
    rows: 1,
    align: (horizon + center),
    rect([
      
Realizámos um tratamento minucioso dos dados provenientes de entidades externas, corrigindo valores omissos e erros de digitação. Restringimos o conjunto de dados ao período posterior a 2017, pois a partir de 2018 o número de eventos tornou-se mais uniforme, com cerca de 500 eventos por ano. Incluir dados anteriores a 2017 poderia prejudicar a consistência e precisão do modelo devido à disparidade no número de eventos e à maior incidência de erros nesses dados mais antigos.

], width: 98%, radius: (
    left: 5pt,
    right: 5pt,
  )),
image("imagens/eventos_por_mesano.png", width: 66%),
  ),
  caption: [
    _Jitterplot_ com as quebras energéticas disponíveis por mês e ano
  ],
) <DatasErradasEventoExcecional>

#set text(11pt)

== Criação de variáveis <variaveis>
=== Percentagem das zonas de qualidade de serviço
As #link("https://www.e-redes.pt/pt-pt/zonas-de-qualidade-de-servico")[Zonas de Qualidade de Serviço] (ZQSs) recolhidas, ao contrário da nossa expectativa, estão representadas por coordenadas geográficas, em vês de um conjunto de áreas ou freguesias/concelhos associados. Devido à sua definição, nós suspeitamos e assumimos que os pontos sejam apenas como a ERSE decidiu representar as áreas no documento fonte.

De forma a poder representar o concelho em termos de número de clientes no tal, usando as ZQSs, decidimos usar o rácio de zona X que o concelho tem comparados com as outras zonas. Esta solução podia assim cobrir casos onde um concelho tem apenas pontos de zona A (1:0:0) como capitais de distrito; concelhos que tem maioria zona A, mas alguns pontos de zona B (e.g. 9:1:0), potencialmente vindo de algumas localidades dentro do concelho que não passam os 25000 clientes; concelhos apenas com pontos de zona C (0:0:1), como alguns concelhos do interior; entre outros.

Veremos num exemplo prático o concelho de Santarém. Este concelho tem ao todo 100 coordenadas de ZQSs, sendo 67 delas classificadas como #emph(text(rgb("#008000"))[zona A]) e 33 delas #emph(text(rgb("#FF0000"))[zona C]) (ver @qualidadeservico). Visto que nenhuma é considerada #emph(text(rgb("#002379"))[zona B]), neste concelho, a `percentagem_zonaB` $ =0/100=0$. Da mesma forma, a `percentagem_zonaA`$ =67/100=#(67/100)$ e `percentagem_zonaC`$ =33/100=#(33/100)$.

Observando a @santarem_rqs verificamos que ter a percentagem é uma mais valia, dado que há um grande número de #text(rgb("#002379"))[_zonas B_] nos concelhos vizinhos ao de Santarém. Há também uma forte incidência de #text(rgb("#008000"))[_zonas A_] na cidade de Santarém dentro do concelho e alguma dispersão de #text(rgb("#FF0000"))[_zonas C_] por todo o concelho. Desta maneira conseguimos diferenciar bem dois concelhos vizinhos que tenham diferente número de zonas totais e A, B e C separadamente.

#figure(
image("imagens/santarem_rqs.png", width: 65%),
  caption: [Coordenadas de ZQSs de Santarém (área amarela) e arredores.\ A verde estão as zonas A, a azul as zonas B, e a vermelho as zonas C
  #footnote[Os pontos em forma de triângulo não representam zonas, apenas são resíduos do mapa, semelhante às estradas.]]
)<santarem_rqs>

=== Trigonometria Data <capConvTemp>


Na elaboração das nossas transformações e seleção de variáveis, deparámos-nos com o desafio de codificar a altura do ano e a altura do mês. Em outras palavras, poderíamos simplesmente ter registado os dias e meses decorridos, mas isso não informaria ao nosso modelo que a data é cíclica. Assim, acidentes que ocorrem no final de um ano teriam uma grande distância daqueles que ocorrem no início do ano seguinte. Por exemplo:

#let date = datetime(
  year:2022,
  month:12,
  day:30
)
#let sumi = duration(
  days:3
)

#let summed = date + sumi

#rect(
  inset: 5pt,
  radius: 3pt,
  stroke: 1pt + luma(180),
  fill: luma(250),
  width: 100%,)[
  $
"Tempo1": date.display("[day]/[month]/[year]") &=> date.ordinal() "dias ocorridos até ao final do ano" \
"Tempo2":summed.display("[day]/[month]/[year]") &=> summed.ordinal() "dias ocorridos até ao final do ano" \
sumi.days() &=> "dias de diferença entre as duas datas "
$

$ "Fórmula" => "dias ocorridos até o final do ano" * (2pi) /  "Nº de dias do ano" $

#align(center)[|_ *Tempo 1* _|]


$
date.display("[day]/[month]/[year]") &=> date.ordinal() * (2pi) /  365 $

$ sin(date.ordinal() * (2pi)/365) approx -0.01721 | cos(date.ordinal() * (2pi)/365) approx 0.99985 $

#align(center)[|_ *Tempo 2* _|]

$
summed.display("[day]/[month]/[year]") &=> summed.ordinal() * (2pi) /  365 $

$ sin(summed.ordinal() * (2pi)/365) approx 0.03442 | cos(summed.ordinal() * (2pi)/365) approx 0.99940 $
]



#figure(
  grid(
    columns: (200pt, 360pt), gutter: -1pt,
    rows: 1,
    align: (horizon + center),
    rect([
      

Na imagem ao lado, podemos visualizar as duas datas convertidas acima. É notório que elas agora se encontram próximas uma da outra, alcançando assim o objetivo de representar a ciclicidade das datas. Além disso, podemos utilizar o gráfico para analisar a distribuição dos eventos ao longo das estações do ano. Por exemplo, quando o valor de $cos(alpha)$ é próximo de 1 e o de $sin(alpha)$ é próximo de 0, estamos no inverno; já os valores opostos representam o verão.

], width: 95%, radius: (
    left: 5pt,
    right: 5pt,
  )),
    image("imagens/TrigDataAno.svg", width: 100%)
  ),
  caption: [
    Trigonometria do Ano
  ],
) <TrigonometriaAno>

Também é importante referir que o mesmo procedimento foi aplicado para os dias de cada um dos meses, ou seja, utilizamos a informação cíclica dos dias dentro de um mês. Desta forma, o modelo pode compreender padrões relacionadas com a altura do mês: o modelo pode, por exemplo detetar que na primeira quinzena de cada mês há uma maior incidência de quebras energéticas, ou aglomerar quebras energéticas das últimas e primeiras semanas do mês. 

=== Classe das causas

É fundamental ter em conta uma característica importantíssima das quebras energéticas: *a sua causa*; ou seja, a ação que originou a quebra energética. Esta característica é essencial para agrupar as diferentes quebras energéticas. No entanto, estas classes apresentam um grande desequilíbrio, com algumas causas semelhantes descritas de maneira diferente. No #ref(<DesequilibrioClassesCausas>, supplement: none), podemos visualizar um gráfico circular que ilustra a situação inicial, demonstrando um número muito elevado de classes, algumas das quais com um número baixo de ocorrências. Abaixo, podemos ver a solução encontrada para equilibrar as diferentes classes:


#figure(
  grid(
    columns: (250pt, 270pt), gutter: -1pt,
    rows: 1,
    align: (horizon + center),
    rect([
      Para resolver o desequilíbrio das classes, começamos por identificar causas de incidentes semelhantes, chegando a 4 _classes-chave_:
      
      • `Clima` $arrow$ Quebras energéticas causadas por condições climatéricas adversas
      
      • `Animais` $arrow$ Quebras energéticas causadas por Animais
      
      • `Humanos_Intenção` $arrow$ Quebras energéticas causadas por humanos, mas de forma intencional, como vandalismo e furto
      
      • `Humanos - Acidentes` $arrow$ Quebras energéticas causadas por humanos, mas de forma não intencional, como escavações e veículos.

Consequentemente, essas classes foram utilizadas como variáveis dummy.

], width: 95%, radius: (
    left: 5pt,
    right: 5pt,
  )),image("imagens/ClassAcidentes.svg", width: 100%)
  ),
  caption: [
    Distribuição das causas dos Incidentes
  ],
  kind:image
) <DistribuiçãoClassesQuebrasEner>

\


#pagebreak()
=== Percentagem de ruralidade de cada Concelho

#figure(
  grid(
    columns: (290pt, 272pt), gutter: -20pt,
    rows: 1,
    align: (horizon + center),
    rect([
  Inicialmente, esta variável representava uma taxa de ruralidade, ou seja, em cada concelho eram contadas as freguesias rurais e dividia-se esse número pelo total de freguesias, obtendo-se assim a taxa de ruralidade (mais detalhes disponíveis no #ref(<Tx.ruralidade>, supplement: none)). No entanto, durante a apresentação, um dos docentes sugeriu uma alteração. Em vez de se utilizar o número bruto de freguesias, foi proposto usar a área de cada freguesia. Como utilizámos um #link("https://dados.gov.pt/en/datasets/concelhos-de-portugal/")[_shapefile_], bastou simplesmente realizar:
  
• #text(10.8pt, weight: "bold")[`Freguesia['area_m2'] = Freguesia.geometry.area`]

  De seguida, bastou utilizar a mesma formula, com uma breve alteração:

• #text(10.7pt, weight: "bold")[Percentagem de Ruralidade = $sum(text("área das freguesias rurais")) / ("área total do concelho")$]

Se analisarmos, a figura assemelha-se bastante à da @Tx.ruralidadeImagem, mas possui algumas diferenças que enriquecem significativamente o modelo, como a noção da dimensão das freguesias rurais e urbanas.
  
], width: 95%, radius: (
    left: 5pt,
    right: 5pt,
  )),image("imagens/ConcelhosZonasRuraisPercentagem.png", width: 89%)
  ),
  caption: [
    Taxa de ruralidade de cada concelho
  ],
  kind:image
) <PercentagemDeRuralidade>

== _Datasets_ Finais

Após realizado todo o processo de limpeza e tratamento de dados, ficamos com dois _datasets_ finais:
// #todo("rever esta m**** pfv pq nao sei o q dizer - BOTAS")
#figure(
  tablex(
    columns: 2,
    align: (col, row) => {
      if row == 0 {
        center
      } else if (1,2).contains(col) {
        horizon + center
      } else {center}
    },
    header-rows:1,
    header-columns:1,
    auto-lines: false,
    [*_Dataset_ de eventos*], 
    vlinex(stroke:0.2mm),
    [*_Dataset_ com todos os dados diários*],
    hlinex(stroke:0.2mm),[Cada observação representa um evento excecional ou não previsto (tratados), e dados associados a tal (como a causa ou a rede de distribuição alvo); tirado das tabelas de decisão da ERSE, entre 2018 e 2023. Ao termos todos os eventos que ocorreram conseguimos identificar padrões nestes.], // Tem todos os dados das tabelas de decisão da ERSE, entre 2018 e 2023, mas também os dados explicados na @variaveis e dados de altitude que não foram mencionados nessa secção (altura máxima e mínima). Este conjunto de dados está agrupado por dados de concelho nas colunas criadas na secção já mencionada.
    [Cada observação representa um dia por concelho, e dados associados a tais, como dados metereologicos do dia, e dados demográficos do concelho, entre 2018 a 2023. O objetivo principal de ter este _dataset_ com todas as combinações possíveis é de poder prever casos em que estes eventos não existem.]

),
caption: [Conjuntos de dados final],
kind:table
)

Nós dividimos em dois _datasets_ para podermos ter os dados diários dos concelhos e dados sobre os eventos, para poder ter flexibilidade na modelação e não ter perda de informação caso fosse necessário. Esta divisão facilitou também a análise exploratória feita ao longo do projeto.

// A nossa ideia base era de detetar padrões pelas características intrínsecas aos eventos, como clientes afetados, indicadores gerais, causa, entre outras. Esta análise permite agrupar algum tipo de eventos e criar medidas preventivas para eventos da mesma espécie.

// Contudo, antes de realizar a deteção de padrões, seguimos uma recomendação de realizar um agrupamento de concelhos, tomando as suas características de população, densidade, etc. A este agrupamento caracterizamos de "*pré-_clustering_*" e será abordado na @Não_Supervisionada. Isto permitiu reduzir o peso que os concelhos teriam no agrupamento pelas características apenas, utilizando numa coluna o _cluster_ do agrupamento efetuado no *pré-_clustering_*.

#pagebreak()

= Modelling

\

Nesta fase do CRISP-DM, avançamos para a criação dos modelos. Serão explorados modelos de aprendizagem não supervisionada (@Não_Supervisionada) e modelos de aprendizagem supervisionada (@Supervisionada).

== Não Supervisionada <Não_Supervisionada>

Na implementação do modelo de não supervisionada, o grupo realizou vários testes e chegou à conclusão que existiam 2 grandes problemas que prejudicavam o modelo, sendo eles: 

- *Eventos excecionais de grande impacto:*
  - Devido à ocorrência de eventos excecionais de grande impacto (EEGIs), qualquer modelo desenvolvido acabava sempre por criar dois grupos distintos: um para os eventos excecionais de grande impacto e outro para aqueles que não o são, resultando num desequilíbrio que comprometia a interpretação e a precisão do modelo. Por isso, o grupo viu-se obrigado a retirar esses eventos (além de outras limitações, como a abrangência geográfica ou o tipo de tensão afetado). No #ref(<EventExcecGrandImpac>, supplement: none) encontram-se alguns exemplos destes EEGIs.

- *Características dos concelhos mais fortes que as características das quebras energéticas:*
  - O modelo considerava que as características dos concelhos tinham uma importância maior do que as características das quebras energéticas (Exemplo: #ref(<ClusterErradoExemplo>, supplement: none)). Para tentar resolver este problema, inicialmente tentamos fazer Análise de Componentes Principais (PCA), mas os resultados eram difíceis de interpretar. Assim, optamos por realizar o que nós chamámos de "pré-clustering".

=== Pré-Clustering <Pre_clustering>

Para iniciar o processo de pré-_clustering_, foram consideradas todas as características relacionadas com os concelhos discutidas ao longo do trabalho, abrangendo desde indicadores socioeconómicos até o número de subestações em cada concelho. Foi utilizado um modelo de _clustering_ hierárquico aglomerativo com o método de ligação de #link("https://en.wikipedia.org/wiki/Ward's_method")[Ward], para variância mínima. Abaixo, apresenta-se o dendrograma com os resultados obtidos:

#figure(
image("imagens/DendogramaConcelhosCluster.png", width: 80%),
  caption: [Dendrogramas Hierárquico dos Concelhos]
)<dendrogramasConcelhos>

É de notar que os concelhos de Lisboa e Porto ficaram separados em um _cluster_ apenas, daí a escolha dos 4 _clusters_ para não descaracterizar estes concelhos que são verdadeiros _outliers_ em termos energéticos. A Silhouette média para o modelo Agglomerative Clustering foi 0.1924.

#figure(
image("imagens/SilhouetteConcelhosCluster.svg", width: 65%),
  caption: [Silhueta dos clusters dos Concelhos]
)<SilhuetaConcelhos>

==== Visualização e interpretação dos clusters dos concelhos

\

#align(center)[#upper[*Cluster 0 $arrow$ Litoral e Zonas Industriais*]]

#figure(
  grid(
    columns: (350pt, 170pt), gutter: 0pt,
    rows: 1,
    align: (horizon + center),
    image("imagens/ClusterConcelho0.svg", width: 100%),
        rect([
• Altitudes reduzidas​

• Índice de envelhecimento reduzido​

• Elevado número de empregados no setor secundário

• Elevado número de zonas C
], inset: 20pt,
  fill: rgb("fff"),
  width: 100%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  ),),
  ),
  caption: [
    Cluster 0 $arrow$ Litoral e Zonas Industriais
  ],
) <ClusterConcelhos0>

\

#align(center)[#upper[*Cluster 1 $arrow$ Interior*]]

#figure(
  grid(
    columns: (170pt, 350pt), gutter: 0pt,
    rows: 1,
    align: (horizon + center),
        rect([
• Altitudes muito elevadas​

• População envelhecida​

• Elevada aposta na ruralidade e na agricultura​

• Fraco número de subestações

], inset: 20pt,
  fill: rgb("fff"),
  width: 100%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  ),),
  image("imagens/ClusterConcelho1.svg", width: 100%),
  ),
  caption: [
    Cluster 1 $arrow$ Interior
  ],
) <ClusterConcelhos1>

#align(center)[#upper[*Cluster 2 $arrow$ Arredores das grandes cidades*]]

#figure(
  grid(
    columns: (350pt, 170pt), gutter: 0pt,
    rows: 1,
    align: (horizon + center),
    image("imagens/ClusterConcelho2.svg", width: 100%),
        rect([
• Grande número de subestações​

• Elevado número de zonas B​

• Zonas pouco Rurais​

• Grande densidade Populacional
], inset: 20pt,
  fill: rgb("fff"),
  width: 100%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  ),),
  ),
  caption: [
    Cluster 2 $arrow$ Arredores das grandes cidades
  ],
) <ClusterConcelhos2>

\
#align(center)[#upper[*Cluster 3 $arrow$ Grandes Cidades*]]


#figure(
  grid(
    columns: (170pt, 350pt), gutter: 0pt,
    rows: 1,
    align: (horizon + center),
        rect([
• Número muito elevado de subestações​

• Número muito elevado de zonas A​

• Maior aposta no setor terciário​

• Elevada densidade populacional

], inset: 20pt,
  fill: rgb("fff"),
  width: 100%,
  stroke: 0.1pt, radius: (
    left: 5pt,
    right: 5pt,
  ),),
  image("imagens/ClusterConcelho3.svg", width: 100%),
  ),
  caption: [
    Cluster 3 $arrow$ Grandes Cidades
  ],
) <ClusterConcelhos3>

Agora que os clusters foram criados e interpretados, o próximo passo é substituir as numerosas variáveis que descrevem as características de cada concelho pelos seus valores de cluster, de forma semelhante a uma tabela dinâmica com variáveis dummy. Cada linha representará um concelho (onde ocorreu a quebra energética) e cada coluna corresponderá a um cluster (com o seu devido nome), onde o valor será 1 se o concelho pertencer ao cluster correspondente e 0 caso contrário.

Além disso, abaixo é possível visualizar um mapa onde a cor de cada concelho representa o seu cluster. Concelhos sem quebra energética são destacados a preto:

\

#figure(
image("imagens/ClusterConcelhoMapa.png", width: 73%),
  caption: [Mapa dos clusters dos concelhos]
)<dendrogramasConcelhos>

=== Clustering - Quebras energéticas
Agora que temos as características das quebras energéticas e os clusters atribuídos a cada concelho no conjunto de dados de _*eventos*_, podemos avançar com a criação do modelo.

#figure(
image("imagens/DendogramaClustersQuebrasEnergeticas.png", width: 95%),
  caption: [dendrogramas  Hierárquico das quebras energéticas]
)<dendrogramasQuebrasEnergeticas>

Aqui também foi utilizado um modelo de _clustering_ hierárquico aglomerativo com o método de ligação de #link("https://en.wikipedia.org/wiki/Ward's_method")[Ward], para variância mínima. 
Foi desafiante determinar o número ideal de clusters. Um número muito baixo resultaria em clusters demasiado amplos e pouco distintos, enquanto um número excessivo tornaria os clusters não só difíceis de interpretar, mas também propensos a capturar variações irrelevantes entre os concelhos. Por isso, foi chegado a um consenso definir 3 clusters como a melhor opção. A seguir, é possível visualizar a silhueta correspondente a esses clusters.

#figure(
image("imagens/SilhuetaClustersQuebrasEnergeticas.svg", width: 70%),
  caption: [Silhueta dos clusters dos Concelhos]
)<SilhuetasQuebrasEnergeticas>

A silhueta média do modelo _Agglomerative Clustering_ é 0.0930, o que indica uma estrutura e qualidade relativamente baixa. Este valor sugere que os clusters não estão claramente separados e há uma sobreposição considerável entre eles. Embora os clusters possam fornecer alguma informação útil, a sua definição não é robusta e as diferenças entre os grupos não são muito acentuadas.

==== Visualização e interpretação dos clusters das quebras energéticas
Primeiramente, é importante destacar que serão apresentadas as médias das variáveis de cada um dos clusters, acompanhadas por um mapa de incidência desses clusters em cada concelho. No mapa, quanto mais escuro estiver o concelho, maior será o número de clusters presentes nele.

\

#align(center)[#upper[*Cluster 0 $arrow$ Quebras de Baixo Impacto em Áreas Desenvolvidas por mão humana*]]

#align(center)[
 #figure(
  grid(
    columns: (320pt, 230pt), gutter: -20pt,
    rows: 1,
    align: (horizon + center),
    rotate(90deg)[
      #image("imagens/ClusterExplica0.svg", width: 100%)
    ], image("imagens/ClusterQuebraCluster_0.png", width: 100%),
  ),
  caption: [
    Cluster 0 $arrow$ Quebras de Baixo Impacto em Áreas Desenvolvidas por mão humana
  ],
) <NumeroDeQuebrasEnergeticasBarras0> 
]

As quebras energéticas deste cluster ocorrem predominantemente nas grandes cidades e nos seus arredores, onde a densidade populacional e a atividade urbana são mais intensas. Este cluster caracteriza-se por incidentes em sistemas de Baixa Tensão, que são comuns em áreas residenciais e comerciais onde a demanda por energia elétrica é elevada, mas não requer infraestruturas de Alta Tensão.

A maioria destas quebras energéticas são atribuídas a ações humanas, quer sejam resultantes de acidentes ou de atividades intencionais. Acidentes podem incluir falhas causadas por obras de construção, manutenção inadequada ou erros operacionais. As interrupções intencionais, por outro lado, podem envolver vandalismo, roubo de cabos ou outros atos maliciosos que visam a infraestrutura elétrica.

A confluência destes fatores – a ocorrência em zonas urbanas e periurbanas, a predominância de sistemas de Baixa Tensão e a origem humana das falhas – proporciona uma compreensão nítida dos desafios enfrentados na gestão da rede elétrica em áreas de alta densidade populacional.

#pagebreak()

#align(center)[#upper[*Cluster 1 $arrow$ Acidentes com Animais em Períodos Frios no Litoral e Zonas Industriais*]]

#align(center)[
 #figure(
  grid(
    columns: (320pt, 230pt), gutter: -20pt,
    rows: 1,
    align: (horizon + center),
    rotate(90deg)[
      #image("imagens/ClusterExplica1.svg", width: 100%)
    ], image("imagens/ClusterQuebraCluster_1.png", width: 100%),
  ),
  caption: [
    Cluster 1 $arrow$ Acidentes com Animais em Períodos Frios no Litoral e Zonas Industriais
  ],
) <NumeroDeQuebrasEnergeticasBarras1> 
]

As quebras energéticas neste cluster são frequentemente atribuídas a interferências causadas por animais, afetando principalmente áreas não classificadas como Baixa Tensão no litoral e zonas industriais de Portugal, em épocas frias e chuvosas. 

Este fenómeno é mais prevalente durante o início do ano, especialmente durante o Inverno (o $sin(alpha)$ e o $cos(alpha)$ são positivos, logo estamos no primeiro quadrante, e o $cos(alpha)$ $>$ $sin(alpha)$; para uma melhor visualização, poderá rever a @TrigonometriaAno), quando as temperaturas frias tendem a aumentar a procura de energia e ainda, devido às condições meteorológicas adversas, o comportamento dos animais tende a ser alterado, muitas vezes causado pela procura de calor ou alimento, que podem levar a incidentes que comprometem a rede elétrica. 

Estas interrupções sublinham a necessidade urgente de implementar estratégias de gestão da fauna e de infraestrutura elétrica específicas para estas regiões. Medidas como a proteção de equipamentos elétricos contra danos causados por animais e a adoção de tecnologias que minimizem o impacto dessas interferências são essenciais para assegurar a fiabilidade contínua do fornecimento de energia. Além disso, investimentos em monitorização avançada e resposta rápida a incidentes podem mitigar os efeitos adversos dessas quebras energéticas, garantindo assim um serviço elétrico mais estável e seguro para os residentes e indústrias locais.

#pagebreak()

#align(center)[#upper[*Cluster 2 $arrow$ Acidentes em Ondas de Calor no Interior*]]

#align(center)[
 #figure(
  grid(
    columns: (320pt, 230pt), gutter: -20pt,
    rows: 1,
    align: (horizon + center),
    rotate(90deg)[
      #image("imagens/ClusterExplica2.svg", width: 100%)
    ], image("imagens/ClusterQuebraCluster_2.png", width: 100%),
  ),
  caption: [
    Cluster 2 $arrow$ Acidentes em Ondas de Calor no Interior
  ],
) <NumeroDeQuebrasEnergeticasBarras2> 
]

As quebras energéticas neste cluster são frequentemente observadas no interior de Portugal durante o final do Verão (o $sin(alpha)$ e o $cos(alpha)$ são negativos, logo estamos no terceiro quadrante, e o $cos(alpha)$ $<$ $sin(alpha)$; para uma melhor visualização, poderá rever a @TrigonometriaAno), caracterizado por temperaturas extremamente elevadas e condições meteorológicas com pouco vento e chuva. Nesta época do ano, a demanda por energia atinge picos devido ao uso intensivo de ar condicionado e outros sistemas de refrigeração. As altas temperaturas também podem afetar diretamente a infraestrutura elétrica, aumentando o risco de falhas em equipamentos sensíveis ao calor.

A falta de vento e chuva contribui para um ambiente seco que pode ser propenso a incêndios florestais, representando um desafio adicional para a manutenção da rede elétrica. A combinação desses fatores sublinha a importância de medidas preventivas robustas, como a inspeção regular da infraestrutura e a implementação de tecnologias de monitorização climática avançada.

Para mitigar o impacto das quebras energéticas, é crucial desenvolver estratégias adaptadas às condições climáticas específicas do interior de Portugal. Isso inclui o reforço da resiliência da rede elétrica e a promoção de práticas sustentáveis ​​para garantir um fornecimento contínuo e confiável de energia durante períodos críticos de demanda e condições climáticas desfavoráveis.

#pagebreak()



== Supervisionada <Supervisionada>
=== Time Series <TimeSeries>
==== Previsão do valor absoluto

Esta foi, de longe, a fase mais complicada do trabalho. Como seria possível prever um evento raro? E de que maneira? Para tal, testámos vários métodos.

Primeiramente, tentamos prever os valores dos indicadores que tinham uma relação direta com as quebras energéticas. No entanto, após realizar um pequeno teste (#ref(<PrevisaoErradoExemplo>, supplement: none)), rapidamente percebemos que esta abordagem não seria a mais adequada. Isso ocorreu porque os valores dos indicadores gerais nos dias sem quebras energéticas não estavam disponíveis. Além disso, não faria sentido atribuir a esses dias o valor zero, uma vez que isso implicaria, incorretamente, que não houve pequenas quebras energéticas ou interrupções para manutenção, algo que não podíamos assegurar devido ao uso exclusivo de relatórios de eventos excecionais.

Em resposta à necessidade de prever o número de quebras energéticas diárias, optamos por utilizar o modelo _Long-Short Term Memory_ (LSTM). Essa escolha se baseou na robustez e nas características vantajosas do LSTM, que o tornam ideal para lidar com sequências temporais e dados complexos.

A seguir, apresentamos os resultados obtidos com a implementação do modelo LSTM (é importante ter em conta que todos os modelos de LSTM apresentados são referentes ao concelho de Lisboa, para simplificar a visualização):

#figure(
image("imagens/LSTMcountNormal.png", width: 110%),
  caption: [LSTM do Concelho de Lisboa]
)<LSTM_Normal>

Se analisarmos corretamente, é fácil concluir que este modelo não é bom, pois prevê quase sempre zero quebras energéticas. Este problema deve-se ao desequilíbrio existente entre as classes, havendo muito mais dias sem quebras energéticas do que com. Abaixo, podemos ver o quão desequilibradas são as classes:

#set par(justify: false)
#set text(hyphenate: false)

#figure(
  tablex(
    columns:2,
    align: center + horizon,
    header-rows:1,
    header-columns: 1,
    auto-lines: true,
    stroke: 0.1mm,
    repeat-header: true,

    map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("ffd700") } else { none })
    },
  ),

    map-column: (column, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if column == 1 { rgb("ffd700") } else { none })
    },
  ),
    
    // Colunas
    [*Número de Eventos Diários*],
    hlinex(stroke:0.5mm),
    [*Ocorrências*],      

    // Linhas
    [0],
    vlinex(stroke:0.5mm),
    [558072],
    [1],
    vlinex(stroke:0.5mm),
    [2737],
    [2],
    vlinex(stroke:0.5mm),
    [77],
    [3],
    vlinex(stroke:0.5mm),
    [9],
    [4],
    vlinex(stroke:0.5mm),
    [1],
)
,caption: [Ocorrência de eventos ao longo de 6 anos (2018 - 2023)],
kind:table 
)<QtdQuebrasDiarias>

#set par(justify: true)
#set text(hyphenate: true)

Com base nessa abordagem, para resolver o problema, começamos por atribuir pesos às classes. Isto significa que informamos o modelo para atribuir maior importância aos casos de quebras energéticas do que aos casos em que não há quebras. Os resultados obtidos foram os seguintes:

#figure(
image("imagens/LSTMcountWeight.png", width: 100%),
  caption: [LSTM com pesos do Concelho de Lisboa]
)<LSTM_Weight>

Embora os resultados apresentem uma melhoria em comparação ao modelo original, ainda não alcançam um nível satisfatório de precisão. Diante dessa constatação, optamos por simplificar o problema, focando na previsão binária de ocorrência ou não de quebras energéticas, em vez de tentar prever o número absoluto de eventos.

Essa mudança estratégica visa direcionar os esforços para um objetivo mais realista e alcançável, considerando as limitações do modelo e a natureza complexa do problema. Para uma análise mais crítica do modelo, abaixo podemos visualizar as métricas deste modelo:

#figure(code(  lang-box: (
    gutter: 5pt,
    radius: 3pt,
    outset: 3pt,
    fill: rgb("ffe05d"),
    stroke: 1pt + rgb("#3c79a9") 
  ), lang-box-contents:"",```python
  14/14 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step 
Mean Squared Error (MSE): 1.0896107969400848
Root Mean Squared Error (RMSE): 1.043844239788717
Mean Absolute Error (MAE): 1.0114270582506624
Mean Absolute Percentage Error (MAPE): 4506763245347768.0
Mean Bias Deviation (MBD): 0.9956297822771827
Explained Variance Score: -0.6175031679929905
  ```), caption: [Métricas do modelo LSTM com pesos])<metricasmodelobase>  


==== Previsão binária de ocorrência de eventos

A conversão do problema para binário foi uma etapa simples, bastando definir qualquer valor de quebra energética superior a zero como 1, exemplo: `QuebrasFinal["HouveEvento?"] = np.where(QuebrasFinal["n_incidentes"] > 0, 1, 0)`.

Apesar da expectativa de que a conversão em binário equilibraria as classes, a análise revela que o reequilíbrio não foi significativo, como evidenciado pela @QtdQuebrasDiariasBin.

#set par(justify: false)
#set text(hyphenate: false)

#figure(
  tablex(
    columns:2,
    align: center + horizon,
    header-rows:1,
    header-columns: 1,
    auto-lines: true,
    stroke: 0.1mm,
    repeat-header: true,

    map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("ffd700") } else { none })
    },
  ),

    map-column: (column, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if column == 1 { rgb("ffd700") } else { none })
    },
  ),
    
    // Colunas
    [*Ocorreu alguma quebra energética?*],
    hlinex(stroke:0.5mm),
    [*Ocorrências*],      

    // Linhas
    [0],
    vlinex(stroke:0.5mm),
    [558072],
    [1],
    vlinex(stroke:0.5mm),
    [2824],
    
)
,caption: [Ocorrência, binário, de quebras energéticas ao longo de 6 anos (2018 - 2023)],
kind:table 
)<QtdQuebrasDiariasBin>

#set par(justify: true)
#set text(hyphenate: true)

Mesmo assim, decidimos aplicar o mesmo modelo LSTM com os pesos, e o resultado foi o seguinte:

#figure(
image("imagens/LSTMBinWeight.png", width: 100%),
  caption: [Previsão binária com o LSTM com pesos do Concelho de Lisboa não tratado]
)<LSTMBin_Weight>

Embora o modelo apresente uma tendência em concentrar-se em valores entre 0,4 e 0,6, podemos ajustá-lo para melhorar o seu desempenho na classificação binária.

Ao definir uma reta de 0.5, podemos converter os valores acima desse limite em 1 (predizendo uma quebra energética) e os valores abaixo em 0 (predizendo a ausência de quebra). Essa estratégia visa forçar o modelo a tomar decisões mais definitivas, categorizando cada evento como 0 ou 1.

Os resultados obtidos com essa abordagem são apresentados a seguir:

#figure(
image("imagens/LSTMBinWeightTratado.png", width: 100%),
  caption: [Previsão binária com o LSTM com pesos do Concelho de Lisboa tratado]
)<LSTMBin_WeightTratado>

#figure(code(  lang-box: (
    gutter: 5pt,
    radius: 3pt,
    outset: 3pt,
    fill: rgb("ffe05d"),
    stroke: 1pt + rgb("#3c79a9") 
  ), lang-box-contents:"",```python
14/14 ━━━━━━━━━━━━━━━━━━━━ 0s 3ms/step 
Mean Squared Error (MSE): 0.24366735223373623
Root Mean Squared Error (RMSE): 0.49362673371053983
Mean Absolute Error (MAE): 0.49276345316532805
Mean Absolute Percentage Error (MAPE): 2105084156437207.8
Mean Bias Deviation (MBD): 0.44208170653475715
Explained Variance Score: -0.01320570042571756
  ```), caption: [Métricas do modelo LSTM com pesos])<metricasmodelobase>

=== Modelo supervisionada de classificação

Diante dos resultados insatisfatórios obtidos com o modelo LSTM na @TimeSeries, o grupo optou por explorar uma abordagem alternativa para o problema em questão. Reconhecendo a necessidade de uma solução mais robusta e confiável, a equipe decidiu direcionar seus esforços para modelos de classificação mais tradicionais.

Com base em conhecimento prévio e _expertise_ na área, o modelo Gradient Boosting foi selecionado como a ferramenta mais adequada para o desafio. A robustez e a confiabilidade deste modelo, reconhecido em diversos trabalhos realizados pelo grupo, faz-nos acreditar que este trará resultados mais positivos e consistentes. 

O grupo teve logo a noção que, caso aplicássemos os nossos dados binários no modelo, ele sofreria de #link("https://www.ibm.com/topics/overfitting")[Overfitting], graças ao grande desequilíbrio de classes (como é possível visualizar na @QtdQuebrasDiariasBin). Em #ref(<GradientBoostOverfitting>, supplement: none) é possível visualizar a respetiva matriz de confusão do modelo base com o #link("https://www.ibm.com/topics/overfitting")[Overfitting].

Para esta fase serão utilizadas duas abordagens: *Oversampling* e *Undersampling*

==== Oversampling

Nesta secção, aplicamos um oversampling clássico. A seguir, será demonstrada a _feature importance_ do modelo, bem como a matriz de confusão deste modelo quando aplicado na base de dados original. Isto porque faz mais sentido avaliar o nosso modelo com as métricas de um caso real em vez de um caso "sintético".

#figure(
  grid(
    columns: 2, gutter: -15pt,
    rows: 1,
    align: (horizon + center),
    image("imagens/OVERFeatureImportance.png", width: 100%),
    image("imagens/OVERconfusionMatrix.png", width: 80%),
  ),
  caption: [
    Gradient Boosting - Oversampling
  ],
) <OversampleGradientBoost>

#figure(code(  lang-box: (
    gutter: 5pt,
    radius: 3pt,
    outset: 3pt,
    fill: rgb("ffe05d"),
    stroke: 1pt + rgb("#3c79a9") 
  ), lang-box-contents:"",```python
Acurácia: 0.675
Precisão: 0.011
Recall: 0.728
F1-score: 0.022
  ```), caption: [Métricas do Gradient Boosting com oversampling])<metricasclassover>

É necessário analisar e avaliar as métricas com atenção! Apesar da `acurácia` ser elevada, a `precisão` e o `F1-Score` apresentam valores muito baixos, o que demonstra que o modelo não é totalmente fidedigno na previsão de ocorrências de quebras. Mesmo assim, ele aparenta conseguir identificar algumas quebras energéticas.

==== Undersampling

#figure(
  grid(
    columns: 2, gutter: -15pt,
    rows: 1,
    align: (horizon + center),
    image("imagens/UNDERFeatureImportance.png", width: 100%),
    image("imagens/UNDERconfusionMatrix.png", width: 80%),
  ),
  caption: [
    Gradient Boosting - Undersampling
  ],
) <UndersampleGradientBoost>

#figure(code(  lang-box: (
    gutter: 5pt,
    radius: 3pt,
    outset: 3pt,
    fill: rgb("ffe05d"),
    stroke: 1pt + rgb("#3c79a9") 
  ), lang-box-contents:"",```python
Acurácia: 0.637
Precisão: 0.010
Recall: 0.740
F1-score: 0.020
  ```), caption: [Métricas do Gradient Boosting com undersampling])<metricasclassunder>

Se comparados com atenção, tanto o _oversampling_ como o _undersampling_ apresentam resultados muito parecidos, quer seja pelas variáveis mais importantes, como pelas métricas. Mesmo assim, se tivéssemos que optar por uma delas, optaríamos pelo _oversampling_ devido ao maior valor no `F1-Score` e na `precisão`. Infelizmente, os resultados não foram muito enriquecedores.

\

= Tentativa de 2º iteração do CRISP-DM

Foi realizada uma segunda iteração do CRISP-DM, onde se apostou mais na fase de _modelling_, devido aos seus resultados não satisfatórios. Para tal, foi realizada uma elevada pesquisa, que consumiu uma maior parte do tempo.

Para esta segunda iteração, uma das nossas preocupações seria arranjar uma solução para deixar de assumir a independência entre concelhos. Algumas das formas que consideramos, em vês de treinar um concelho de cada vez e ter um modelo para cada concelho, seria 
treinar sobre os concelhos todos e o modelo iria prever para todos os dias e para todos os concelhos; 
ou usar um codificador do concelho (usando a informação demográfica e climática de tal), treinar e prever sobre o conjunto de teste, e de seguida usar um descodificador, semelhante ao apresentado na Figura 7 no artigo de #link("https://dl.acm.org/doi/10.1145/3450287")[Zhao (2021)]. Considerando a natureza do estudo de previsão de eventos, utilizar métricas de avaliação tradicionais pode conduzir a resultados inconclusivos e/ou conclusões erradas. Em vez disso, focamos na previsão de eventos em concelhos adjacentes no dia em que eventos reais ocorreram em um determinado concelhos. Essa abordagem alinha-se melhor com os nossos objetivos, pois não leva em consideração a distância entre os eventos previstos e os eventos reais.

== Distância entre eventos previstos


#figure(
  grid(
    columns: (310pt, 300pt), gutter: -30pt,
    rows: 1,
    align: (horizon + center),
    rect([
Para desenvolver métricas neste ciclo de avaliação, precisamos determinar a distância entre eventos previstos $hat(y)$ e eventos reais $y$. Essa distância é calculada considerando o número de dias entre as datas dos eventos e a distância geográfica entre os concelhos envolvidos. Optamos por calcular a distância usando o caminho mais curto entre os concelhos, em vez da distância euclidiana entre os seus centros, para refletir melhor o comportamento real das redes, mesmo que ambos os métodos frequentemente produzam resultados semelhantes. Implementamos um grafo de concelhos vizinhos e um algoritmo de caminho mais curto para facilitar este cálculo. Isso é particularmente útil quando concelhos próximos geograficamente estão separados por corpos de água, como Lisboa e Almada.

], width: 100%, radius: (
    left: 5pt,
    right: 5pt,
  )),
    image("imagens/distancia por grafo.drawio.svg", width: 70%)
  ),
  caption: [
    Distância geográfica entre concelhos implementada
  ],
)


Sendo $Lambda(y, hat(y))$ a distância o evento real $y$ e o evento previsto $hat(y)$, $P(y, hat(y))$ o tamanho do caminho mais pequeno entre os concelhos dos eventos, e $Delta(y, hat(y))$ a diferença de dias entre os eventos, assentámos na seguinte função:
$
  Lambda(y, hat(y)) &= beta_1 P(y, hat(y)) + beta_2|Delta(y, hat(y))|\
  ,
  beta_1 &= 7, beta_2 = 1 "(rácio de 7:1)" 
$
Este rácio significa que acertar ao lado do concelho terá a mesma distância do que acertar no concelho com uma semana de diferença. Achámos o rácio mostrado apropriado, sendo que achamos mais importante para o modelo acertar no concelho ou perto do concelho, do que acertar exatamente no dia. 

== Correspondência de eventos
Para elaborar as métricas, seria necessário primeiro determinar como devíamos ligar eventos reais e eventos previstos. Como achámos mais apropriado fazer correspondência bipartida #link("https://dl.acm.org/doi/10.1145/3450287")[(Zhao,2021)], isto consegue-se transformar em um #link("https://en.wikipedia.org/wiki/Assignment_problem")[problema de atribuição de tarefas]. Nós no início elaboramos uma heurística para ligar os eventos reais com eventos previstos, mas ao pesquisar melhor decidimos usar o algoritmo de Kuhn-Munkres (#link("https://en.wikipedia.org/wiki/Hungarian_algorithm")[_Hungarian method_]). Como este funciona não faz parte do âmbito deste projeto, mas de forma reduzida, este vai encontrar os melhores pares de eventos previstos e eventos reais, minimizando $sum_(l in L) Lambda(l_y, l_hat(y))$, sendo $l$ o par de evento real e evento previsto, e $L$ os pares resultados do algoritmo.

== Métricas de Avaliação
As métricas que desenvolvemos para esta segunda iteração são de dois tipos, baseados no estudo de #link("https://dl.acm.org/doi/10.1145/3450287")[Zhao (2021)]: 

- Qualidade de previsões, que avalia o quão perto o modelo prevê os eventos;
- Adequação de previsões, que avalia o desempenho do modelo a prever eventos.

Nesta primeira, desenvolvemos as seguintes métricas:
$
  delta_"normal" &= sum_(l in L)    Lambda(l_y, l_hat(y)) +&  &10 dot |\#Y - \#hat(Y)| \
  delta_"punishing" &= sum_(l in L) Lambda(l_y, l_hat(y)) +& 1&00 dot |\#Y - \#hat(Y)|
$
Estas métricas são simplesmente a soma das distâncias dos pares determinados, mas como pode haver eventos não previstos, ou eventos previstos a mais, é necessário adicionar o argumento da direita, para poder ter isso em conta. $delta_"punishing"$, comparado com $delta_"normal"$, vai punir 10 vezes mais quando o modelo prevê eventos a mais ou a menos, podendo assim verificar de forma mais precisa a qualidade de previsões.

No segundo tipo, vamos adicionar um limiar $t$, e designar todos os pares $Lambda(l_y, l_hat(y)) <= t$ como pares aceitáveis, classificando-os como _True Positives_ (TP). Com esta noção podemos usar a métrica de classificação $F_1$, levando à seguinte métrica:

$
  F_1 &= (2"TP")/(2"TP" + "FP" + "FN"), cases(
    "TP" &= \#{l in L : Lambda(l_y, l_hat(y)) <= t},
    "FN" &= \#{y      : (exists l_(y,hat(y)) :Lambda(l_y, l_hat(y)) >t or exists.not y)},
    "FP" &= \#{hat(y) : (exists l_(y,hat(y)) :Lambda(l_y, l_hat(y)) >t or exists.not hat(y) )}
  )\
$

Esta métrica vai medir, baseado num limiar adequado, o quão bom o modelo é a prever eventos. Nós recomendamos um $t = 25$, sendo que isto dá alguma liberdade do modelo prever em concelhos ao lado com alguma distância temporal também, mas este valor depende também do rácio usado para $Lambda$. Para prever exatamente para o dia, semelhante a um modelo de classificação de _time series_, $t = 0$ seria adequado.

== Modelação da segunda interação
Devido à falta de tempo, não foi possível implementar alguns dos modelos que prevíamos. No entanto, só como prova de conceito, treinámos dois modelos auto-regressivos: um AR e um ARIMA. Semelhante ao primeiro ciclo, assumimos independência entre concelhos e fizemos um modelo para cada concelho. Devido à natureza dos modelos, em vês de termos os eventos diários, acumulámos os eventos para ter uma tendência estritamente positiva. Analogamente também ao primeiro ciclo, treinámos 2018 a 2022, deixando 2023 como teste.
#figure(
image("imagens/acumulados.png", height:7cm), caption: [Representação de eventos acumulados]
)
Em conformidade com a primeira iteração também, na modelação, arredondámos para o inteiro mais perto depois da modelação. Desta forma, conseguimos extrair quando é que o modelo considerou evento e quando não.
=== AR(1,1)
O modelo teve os seguintes resultados:
- $delta_"normal" = 79982$
- $delta_"punishing" = 101672$
- $F_1 approx 0.0038$
- $\#hat(Y) - \#Y = 241$
#figure(
image("imagens/AR.png", height:7cm), caption: [Resultados do modelo AR(1,1) em Lisboa]
)<AR>

Os resultados indicam que há um número gigante de eventos previstos a mais, o modelo não tem boa qualidade de previsões devido aos altos $delta$, e não é um modelo adequado para previsão dos eventos, baseado no pequeno valor de $F_1$. Embora a @AR parece demonstrar um bom resultado em Lisboa, temos que ter em noção que isto não é um modelo de regressão, e que há muitos outros concelhos que não mostramos.

=== ARIMA(2,1,0)
Para determinar parâmetros ARIMA adequados, usámos o `auto_arima` da #link("https://pypi.org/project/pmdarima/")[package `pmdarima`] no concelho de Lisboa. Embora este possa não ser os melhores parâmetros para todos os concelhos, foi bom o suficiente para o que queremos demonstrar.
Os resultados foram os seguintes:
#let variacao = (old, new) => calc.round((old - new) * 100/old, digits: 2)

- $delta_"normal" = 69677$ (melhorou #variacao(79982, 69677)%)
- $delta_"punishing" = 81017$ (melhorou #variacao(101672, 81017)%)
- $F_1 approx 0.0043$ (melhorou #variacao(0.0043, 0.0038)%)
- $\#hat(Y) - \#Y = 126$ (melhorou #variacao(241, 126)%)

#figure(
  image("imagens/ARIMA.png", height:7cm), caption: [Resultados do modelo ARIMA(1,1) em Lisboa]
)<ARIMA>

Este modelo, independentemente do outro, continua a ter má qualidade, má adequabilidade, e continua a prever eventos a mais. Comparado com o modelo anterior, o modelo melhorou todas as métricas, mostrando que este modelo é melhor que o outro a prever os eventos. Olhando para a <ARIMA>, parece que este modelo não se adequa tanto como no modelo anterior em Lisboa; no entanto, lembrando que este não é um modelo de regressão, olhando para quando o modelo considera os eventos, até parece que o modelo está a prever relativamente perto dos dias reais, apenas não correspondendo à frequência de eventos que Lisboa apresenta.

#pagebreak()

= Conclusão e deployment

A deteção precisa de quebras de energia não previstas e excecionais continua a ser um desafio significativo hoje em dia. A raridade e a natureza complexa desses eventos dificultam o desenvolvimento de modelos eficazes. 


A falta de especificidade geotemporal impede análises precisas e previsões confiáveis. Além disso, os indicadores gerais de quebras de energia não possuem poder discriminatório suficiente para distinguir entre eventos distintos, exceto em casos excecionais de grande impacto. Apesar dos avanços alcançados no decorrer do projeto, os resultados atuais dos modelos demonstram limitações em termos de fidedignidade.

Embora os desafios persistam, o potencial para aprimorar a deteção de quebras de energia é considerável e traduz para um investimento em pesquisas futuras, como:

- Usar métodos de aprendizagem mais robustos​ para captar padrões complexos nos dados e lidar com maior volume de informações;

- Usar modelos que usam dados sobre o evento, como Cadeias de Markov Escondidas, ou tratar os eventos como censurados​;

- Recolha de dados mais integrada com a E-Redes, e implementação de sensores para uma previsão melhor;​

- Integração de dados das ilhas para uma análise mais aprofundada.

Este trabalho foi de extrema importância para percebermos como é o funcionamento de toda a rede elétrica e das quebras energéticas. 

Por fim, gostaríamos de agradecer à E-Redes pela disponibilidade de dados e o conhecimento especializado e ao nosso professor orientador Luís Nunes pela sua orientação inestimável e apoio contínuo.

Trabalhos futuros:
- https://dl.acm.org/doi/pdf/10.1145/3450287
- https://ragulpr.github.io/2016/12/22/WTTE-RNN-Hackless-churn-modeling/​​

#figure(
  image("imagens/MapaPrevisao.png", height:11cm), caption: [Previsão de quebras energéticas para o dia da apresentação utilizando o modelo LSTM]
)<ARIMA>

/*
#bibliography("setup/bib.yml", style: "ieee"/* style: "setup/apa.csl" */, full: false)

https://arxiv.org/abs/2309.11356 *COLOCAR DPS* -> EMM

https://www.diva-portal.org/smash/get/diva2:1636167/FULLTEXT01.pdf

*/


#pagebreak()
= Anexos
#set heading(numbering: (level1, level2,..levels ) => {
  if (levels.pos().len() > 0) {
    return []
  }
  ("Anexo", str.from-unicode(level2 + 64)/*, "-"*/).join(" ")
}) // seria so usar counter(heading).display("I") se nao tivesse o resto
//show heading(level:3)
== - IPMA <IPMA>
// #{repr((context {(heading.depth) == 1}))}
Nos dados fornecidos pela entidade tínhamos acesso a algumas estações espalhadas pelos distritos de Portugal Continental que continham a informação das variáveis mostradas na @IPMA_Estacoes e @IPMA_Variaveis.

\

#align(center)[
  #figure(
    tablex(
  columns: 2,
  stroke: black + 0.1mm,
  align: center + horizon,
  header-rows:0,
  header-columns: 0,

  map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("#cdf2ff") } else { none })
    },
  ),

   map-cells: cell => {
    if cell.x > -1 and cell.y == 0 {
      cell.content = {
        let text-color =  {
          rgb("#012160")
        }
        set text(text-color)
        strong(cell.content)
      }
    }
    cell
  },
  
  //colunas
  [Nº da Estação],
  hlinex(stroke:0.5mm),
  [Nome da Estação],

  //linhas
  [1200551], vlinex(stroke:0.5mm),[Viana do Castelo / Chafé	], 
  [1210622], [Braga / Merelim	], 
  [1200567], [Vila Real / Aeródromo	],
  [1200575], [Bragança], 
  [1200545], [Porto / Pedras Rubras	], 
  [1210702], [Aveiro / Universidade	],
  [1200560], [Viseu / Centro Coordenador	], 
  [1210683], [Guarda], 
  [1200548], [Coimbra / Cernache / Aeródromo],
  [1200570], [Castelo Branco], 
  [1210718], [Leiria], 
  [1210734], [Santarém / Fonte Boa  Est. Zootécnica],
  [1200571], [Portalegre], 
  [1200579], [Lisboa / Gago Coutinho], 
  [1210770], [Setúbal / Estação de Fruticultura],
  [1200558], [Évora / Aeródromo], 
  [1200562], [Beja], 
  [1200554], [Faro / Aeroporto],
  [1210615], [
PONTE DE LIMA / Escola Agrícola], 
  [1210716], [Ansião], 
), caption: [As diferentes estações do IPMA],
kind:table
) <IPMA_Estacoes>

]

\

#align(center)[
  #figure(
    tablex(
  columns: 3,
  stroke: black + 0.1mm,
  align: center + horizon,
  header-rows:0,
  header-columns: 0,

  map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("#cdf2ff") } else { none })
    },
  ),

   map-cells: cell => {
    if cell.x > -1 and cell.y == 0 {
      cell.content = {
        let text-color =  {
          rgb("#012160")
        }
        set text(text-color)
        strong(cell.content)
      }
    }
    cell
  },
  
  //colunas
  colspanx(2)[Variável], (),
  hlinex(stroke:0.5mm),
  [Descrição],

  //linhas
  [T_MED],[ºC], vlinex(stroke:0.5mm),[Temperatura média do ar a 1,5 m],
  [T_MAX], [ºC], [Temperatura máxima do ar a 1,5 m],
  [T_MIN], [ºC], [Temperatura mínima do ar a 1,5 m],
  [DD_MED], [º], [Rumo médio do vento],
  [DD_FFX], [º], [Rumo do vento máximo],
  [FF_MED], [m/s], [Intensidade média do vento 10 m],
  [DD_MAX], [m/s], [Intensidade máxima instantânea do vento],
  [PR_QTD], [mm], [Quantidade de precipitação]
), caption: [As diferentes variáveis fornecidas pelo IPMA],
kind:table
) <IPMA_Variaveis>
]
  
#pagebreak()
== - GPP - Gabinete de Planeamento, Políticas e Administração Geral <GPP>

#link("http://www.pdr-2020.pt/O-PDR2020/Arquitetura/Area-3-Ambiente-Eficiencia-no-Uso-dos-Recursos-e-Clima/Medida-8-Protecao-e-Reabilitacao-de-Povoamentos-Florestais/Acao-8.2-Gestao-de-Recursos-Cinegeticos-e-Aquicolas/Operacao-8.2.1-Gestao-de-Recursos-cinegeticos/Documentos-de-Suporte/Lista-de-Freguesias-Rurais-PDR-2020")[Programa de Desenvolvimento Rural] de 2020, que nos demonstra todas as freguesias que são consideradas _zonas rurais_, em Portugal Continental.

#align(center)[
  #figure(
image("imagens/ZonasRurais.png", width: 37%),
  caption: [Zonas Rurais em Portugal Continental]
)
]
\
== - Dados Demográficos - Pordata <Pordata>

- *#link("https://www.pordata.pt/municipios/densidade+populacional-452")[Densidade Populacional]:* Ao entendermos a distribuição da população no concelho, podemos identificar áreas com elevada densidade populacional, que podem enfrentar uma maior procura de energia, assim como áreas mais dispersas que podem ter necessidades diferentes em termos de infraestrutura energética.
- *#link("https://www.pordata.pt/municipios/indice+de+envelhecimento-458")[Índice de Envelhecimento]:* O conhecimento da proporção de idosos em relação à população mais jovem pode ajudar-nos a antecipar demandas específicas de energia, como cuidados de saúde, sistemas de aquecimento e adaptações para acomodar necessidades especiais.
- *#link("https://www.pordata.pt/municipios/populacao+empregada+segundo+os+censos+total+e+por+setor+de+atividade+economica-145")[Setor de Atividade]:* Ao analisarmos os setores económicos predominantes no concelho, podemos identificar padrões de consumo de energia em diferentes indústrias e setores, permitindo uma melhor alocação de recursos e planeamento energético.
#pagebreak()


== - Desequilíbrio das Classes <DesequilibrioClassesCausas>

#figure(
image("imagens/ClassAcidentesErrado.svg", width: 110%),
  caption: [Distribuição desequilibrada das causas dos incidentes]
)<ClassesDesequilibradas>

#rect(fill: rgb("ff6961"), inset: 12pt,
  width: 100%,
  stroke: 0.1pt,  radius: (
    left: 5pt,
    right: 5pt,
  ))[#quote(attribution: [Grupo E-REDES 3])[A imagem acima é meramente ilustrativa e não foi utilizada ou considerada pelo grupo ao longo do trabalho final, pelo que não deve ser interpretada ou tomada como referência para qualquer conclusão.]]

#pagebreak()

== - Taxa de ruralidade <Tx.ruralidade>

#figure(
  grid(
    columns: (250pt, 270pt), gutter: -1pt,
    rows: 1,
    align: (horizon + center),
    rect([
  Para esquematizarmos alguma informação relevante e não termos dados a mais, decidimos agregar as variáveis da `Zona Rural` e `Zona Urbana` que retirámos da @GPP. Estas duas variáveis representam o número de freguesias existentes em cada um dos concelhos, indicando quantas são consideradas rurais e quantas são consideradas urbanas, respetivamente.

Por isso, através do código desenvolvido na @txruralidadecode, foi produzido o coeficiente que designámos de "taxa de ruralidade", dado pela expressão: $text("Tx Ruralidade") = "Zona Rural" / ("Zona Urbana" + "Zona Rural")$.

Com isto conseguimos perceber se um concelho tem um rácio maior ou menor de freguesias rurais. Abaixo, podemos visualizar o respetivo código, como também três exemplos distintos no distrito de Braga, com valores diferentes de "taxa de ruralidade":

], width: 95%, radius: (
    left: 5pt,
    right: 5pt,
  )),image("imagens/ConcelhosZonasRuraisTxRuralidade.png", width: 100%)
  ),
  caption: [
    Taxa de ruralidade de cada concelho
  ],
  kind:image
) <Tx.ruralidadeImagem>

#figure(code(  lang-box: (
    gutter: 5pt,
    radius: 3pt,
    outset: 3pt,
    fill: rgb("ffe05d"),
    stroke: 1pt + rgb("#3c79a9") 
  ), lang-box-contents:"",```python
  file_path = data_folder / "ZonasCount.csv"
  ZonasRurais = pd.read_csv(file_path)
  ZonasRurais["Rural"] = ZonasRurais["Zona Rural"] / (ZonasRurais["Zona Urbana"] + ZonasRurais["Zona Rural"])
  ```), caption: [Cálculo da taxa de ruralidade _python_])<txruralidadecode>  

#figure(grid(
  columns:3,
  rows:2, align: center + horizon,
  gutter: 3pt,
  rect(width: 90%, radius: (
    left: 5pt,
    right: 5pt,))[Vila Nova de Famalicão: \ $"tx. ruralidade"=27/(27+7) equiv "tx. ruralidade" approx 0.79$],
  rect(width: 90%, radius: (
    left: 5pt,
    right: 5pt,))[Vizela: \ $"tx. ruralidade"=5/(5+0) equiv "tx. ruralidade" approx 1.00$],
  rect(width: 90%, radius: (
    left: 5pt,
    right: 5pt,))[Esposende: \ $"tx. ruralidade"=0/(0+7) equiv "tx. ruralidade" approx 0.00$],
  grid.cell(
    image(("imagens/image1.png"), width: 100%),
  ), grid.cell(
    image(("imagens/image2.png"), width: 75%)), grid.cell(
    image(("imagens/image3.png"), width: 45%)
)), caption: [Taxa de ruralidade para vários concelhos do distrito de Braga e contorno dos mesmos])

#set par(justify: true)
#set text(hyphenate: true)

== - Eventos excecionais de grande impacto <EventExcecGrandImpac>

#set par(justify: false)
#set text(hyphenate: false)

#figure(
  tablex(
    columns:8,
    align: center + horizon,
    header-rows:1,
    header-columns: 1,
    auto-lines: true,
    stroke: 0.1mm,
    repeat-header: true,

    map-rows: (row, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if row == 0 { rgb("ffd700") } else { none })
    },
  ),

    map-column: (column, cells) => cells.map(c =>
    if c == none {
      c
    } else {
      (..c, fill: if column == 1 { rgb("ffd700") } else { none })
    },
  ),
    
    // Colunas
    [*Nome*],
    hlinex(stroke:0.5mm),
    [*Tipo de Evento*], [*Período*],                   [*Média de duração da interrupção*],
    [*Impacto QEE*], 
    [*Nº pedidos atraso*], 
    [*Nº clientes afetados*], [*Boletim Informativo*],

    // Linhas
    [Temporal Região Sul],
    vlinex(stroke:0.5mm),
    [Trovoadas e inundações], [7 e 8/12/2022]   , [< 1 min], [signicativo],[13],[32 809],[#link("https://www.ipma.pt/pt/media/noticias/documentos/2022/precipitacao-intensa-lisboa_7_8_dez_vrs3.pdf")[Notícia IPMA]],
    [Depressão _Efrain_],  [Condições meteorológicas adversas] ,[12 a 13/12/2022] , [6 min], [signicativo], [43], [387 223],[#link("https://www.ipma.pt/pt/media/noticias/documentos/2022/precipitacao-pt100_12_13_dez_vrs3.pdf")[Notícia IPMA]],
    [Depressão Hortense],  [Condições meteorológicas adversas] ,[21 e 22/01/2021]  , [3 min],[signicativo],[15],[297 636],[#link("https://expresso.pt/sociedade/2021-01-21-Vento-chuva-e-mar-agitado-Portugal-continental-afetado-por-passagem-da-depressao-Hortense-ate-sexta-feira")[Notícia Expresso 21/1/2021]],
    [Deslastre de Carga Automático], [Sobrecarga e disparo de ligações],[24/07/2021] , [7 min, em média],[------],[exclusão do serviço],[977 394],[#link("https://www.e-redes.pt/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Deslastre%20de%20Frequ%C3%AAncia%20(2021).pdf")[ERSE]],
    [Rio Atmosférico], [Condições metereológicas adversas],[29/10/2021] , [3 min, em média],[significativo],[33],[237 413],[#link("https://www.e-redes.pt/sites/eredes/files/2022-03/Evento%20Excecional%20Tabela%20Decis%C3%A3o%20Rio%20Atmosf%C3%A9rico%20(2021).pdf")[ERSE]],
    [Depressão Glória], [Condições metereológicas adversas],[19/01/2020] , [7 min, em média],[significativo],[36],[181 984],[#link("https://www.e-redes.pt/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20depress%C3%A3o%20Gl%C3%B3ria.pdf")[ERSE]],
    [Depressão 1 e 2/03/2020], [Condições metereológicas adversas],[1 e 2/03/2020] , [3 min, em média],[relevante],[17],[266 104],[#link("https://www.e-redes.pt/sites/eredes/files/2021-03/Tabela%20de%20decis%C3%A3o%20-%20depress%C3%A3o%2001%20e%2002%20de%20mar%C3%A7o.pdf")[ERSE]],
    [Tempestade Helena], [Condições metereológicas adversas],[1/02/2019] , [3 min, em média],[significativo],[32],[240 299],[#link("https://www.e-redes.pt/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_depress%C3%A3o%20Helena.pdf")[ERSE]],
    [Depressões Elsa e Fabien], [Condições metereológicas adversas],[18 a 23/12/2019] , [1h 20min, em média, visto nas três tensões],[relevante],[800],[1 699 906],[#link("https://www.e-redes.pt/sites/eredes/files/2021-03/Tabela%20decis%C3%A3o_depress%C3%A3o%20Elsa%20e%20Fabien.pdf")[ERSE]]
)
,caption: [Eventos excecionais descritos entre o período de 2019 e 2022],
kind:table 
)<eventos_exc_extremos>

#pagebreak()

== - Exemplo de cluster "errado"<ClusterErradoExemplo>

#figure(
image("imagens/ClusterErradoDeProposito.png", width: 100%),
  caption: [Distribuição desequilibrada das causas dos incidentes]
)<ClusterErradoExemploGrafico>

#rect(fill: rgb("ff6961"), inset: 12pt,
  width: 100%,
  stroke: 0.1pt,  radius: (
    left: 5pt,
    right: 5pt,
  ))[#quote(attribution: [Grupo E-REDES 3])[A imagem acima é meramente ilustrativa e não foi utilizada ou considerada pelo grupo ao longo do trabalho final, pelo que não deve ser interpretada ou tomada como referência para qualquer conclusão.]]

#pagebreak()

== - Exemplo de previsão "errada"<PrevisaoErradoExemplo>

#figure(
image("imagens/PrevisãoDoSAIDIBT(min)Lisbon.png", width: 100%),
  caption: [Previsão do indicador SAIDI BT (min) em Lisboa]
)<PrevisaoErradoExemploGrafico>

#rect(fill: rgb("ff6961"), inset: 12pt,
  width: 100%,
  stroke: 0.1pt,  radius: (
    left: 5pt,
    right: 5pt,
  ))[#quote(attribution: [Grupo E-REDES 3])[A imagem acima é meramente ilustrativa e não foi utilizada ou considerada pelo grupo ao longo do trabalho final, pelo que não deve ser interpretada ou tomada como referência para qualquer conclusão.]]

#pagebreak()

== - Gradient Boosting com overfitting <GradientBoostOverfitting>

#figure(
image("imagens/OGconfusionMatrix.png", width: 100%),
  caption: [Matriz de confusão do Gradient Boosting com overfitting]
)<GradientBoostingOverfittingFigure>


/*
=== idk

#let ll = $l_(y,hat(y))$
$
  Lambda_"normal" &= sum_(l in L)Lambda(l) + alpha dot abs(\#Y-  \#hat(Y)), alpha = 10 \
  Lambda_"punishing" &= sum_(l in L)Lambda(l) + alpha dot abs(\#Y -  \#hat(Y)), alpha = 100 \
  "F1"_"ts" &= (2"TP")/(2"TP" + "FP" + "FN"), cases(
    "TP" &= \#{d: y_d = hat(y)_d = 1}\
    "FN" &= \#{d: y_d = 1 and hat(y)_d = 0}\
    "FP" &= \#{d:  y_d = 0and hat(y)_d = 1}\
  ) \
  "F1"_"events" &= (2"TP")/(2"TP" + "FP" + "FN"), cases(
    "TP" &= \#{ll     : Lambda(ll) < t},
    "FN" &= \#{y      : (exists l_(y,hat(y)) :Lambda(ll) >t or exists.not ll )},
    "FP" &= \#{hat(y) : (exists l_(y,hat(y)) :Lambda(ll) >t or exists.not ll )}
  )\
  t &= 7\
  l -> "link"\
  Lambda -> "distância"\
  Y -> "concelhos e datas real"\
  hat(Y) -> "concelhos e datas previsto"\
  alpha -> "peso na distância"\
  beta -> \
  "TP" -> "true positive", "FP" -> "false positive", "FN" -> "false negative"
$

/*
Info sobre Datasets:
1. Consumos mensais por concelho (https://e-redes.opendatasoft.com/explore/embed/dataset/3-consumos-faturados-por-municipio-ultimos-10-anos/table/?disjunctive.distrito&disjunctive.concelho)

  - Tem a data com mês e ano (entre 2020 e 2023, sendo 2020 poucos dados porque corta a meio este ano), tem localidade (nomeadamente distrito, concelho e freguesia)
  - informação sobre consumo, sendo energia ativa e nível de tensão da rede que pode ser mais do que um entre baixa, média e alta tensões
2. Consumos mensais por código postal (https://e-redes.opendatasoft.com/explore/embed/dataset/02-consumos-faturados-por-codigo-postal-ultimos-5-anos/table/?sort=-date)
  - data em formato mês e ano (entre 2021 e 2023 completos, 2020 pequena porção)
  - tem código postal de 4 dígitos distintos e energia ativa noutra coluna respetiva à area destes 4 dígitos
3. Caracterização de luminárias de Iluminação Pública (https://e-redes.opendatasoft.com/explore/embed/dataset/cadastro_iluminacao_publica/table/)
  - data com mês e ano em duas colunas distintas (aqui o mês aparece de 1 a 12 ao contrário das anteriores)
  - localidade (ou seja, distrito, concelho e freguesia)
  - tem informação sobre o número de luminárias (tem muitos valores baixos, os valores mais altos desta variável aparecem 1 vez só; distribuição -> https://e-redes.opendatasoft.com/explore/embed/dataset/cadastro_iluminacao_publica/analyze/?dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkNPVU5UIiwieUF4aXMiOiJtZXMiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjRkZEQzAwIn1dLCJ4QXhpcyI6Imx1bWluYXJpYXMiLCJtYXhwb2ludHMiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImNhZGFzdHJvX2lsdW1pbmFjYW9fcHVibGljYSIsIm9wdGlvbnMiOnt9fSwic2VyaWVzQnJlYWtkb3duVGltZXNjYWxlIjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D)
  - tem o tipo de lâmpada que tem classes tipo Mercúrio, LED, Sódio e a potencia total instalada em watts
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
  - a potência máxima admissível em kW (esta coluna não esta em numérico porque o campo tem numero + kW sempre)
  - tem os postos de ligação para instalações de PCVE
6. Total de unidades de produção para autoconsumo (https://e-redes.opendatasoft.com/explore/embed/dataset/8-unidades-de-producao-para-autoconsumo/table/)
  - tem data com ano e trimestre (ex: 2022T3)
  - distrito e concelho apenas, não tem freguesia
  - escalão de potência (em forma de intervalo porque esta do tipo ]30, 1000])
  - numero de instalações e a potencia total instalada em kW
7. Consumo Horário por Código Postal - 4 Dígitos (https://e-redes.opendatasoft.com/explore/embed/dataset/consumos_horario_codigo_postal/table/?sort=datahora)
  - tem data em formato dia, mês e ano com hora, contudo tem mais duas colunas com data e hora que esta incoerente com a 1ª coluna "Data/Hora" (1 de outubro de 2023 00:00 aparece mal com as outras duas colunas e 1 de novembro de 2022 00:00 aparece correto) *a investigar se for relevante estudar isto*
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
  - no momento em que vi tinha uma linha com tudo nulo e só com o campo da data preenchido
  - talvez são as interrupções no momento e que vai atualizando no momento
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
*/
  
/*
1 - CONSUMO  MENSAIS POR FREGUESIA                 - 3 anos e pouco

2 - CONSUMOS MENSAIS POR CODIGO POSTAL (4 digitos) - 3 anos e pouco

7 - CONSUMO  HORARIO POR CODIGO POSTAL (4 digitos) - 1 mês

9 - CONSUMO  HORARIO POR CODIGO POSTAL (7 digitos) - 1 mês (diferentes fsr)


4 - PARECE INTERESSANTE
15 - util se acompanhado pelo mapa possivelmente  (8)
*/

/*
#let ll = $l_(y,hat(y))$
$
  Lambda_"normal" &= sum_(l in L)Lambda(l) + alpha dot abs(\#Y-  \#hat(Y)), alpha = 10 \
  Lambda_"punishing" &= sum_(l in L)Lambda(l) + alpha dot abs(\#Y -  \#hat(Y)), alpha = 100 \
  "F1"_"ts" &= (2"TP")/(2"TP" + "FP" + "FN"), cases(
    "TP" &= \#{d: y_d = hat(y)_d = 1}\
    "FN" &= \#{d: y_d = 1 and hat(y)_d = 0}\
    "FP" &= \#{d:  y_d = 0and hat(y)_d = 1}\
  ) \
  "F1"_"events" &= (2"TP")/(2"TP" + "FP" + "FN"), cases(
    "TP" &= \#{ll     : Lambda(ll) < t},
    "FN" &= \#{y      : (exists l_(y,hat(y)) :Lambda(ll) >t or exists.not ll )},
    "FP" &= \#{hat(y) : (exists l_(y,hat(y)) :Lambda(ll) >t or exists.not ll )}
  )\
  t &= 7\
  Lambda(l) &= beta_1 dot "caminho mais pequeno entre grafo de concelhos" + \
  &+ beta_2 dot "diferença entre dias dos eventos",\
  beta_1 &= 7, beta_2 = 1 "(rácio de 7:1)" 
$
$
  l -> "link"\
  Lambda -> "distância"\
  Y -> "concelhos e datas real"\
  hat(Y) -> "concelhos e datas previsto"\
  alpha -> "peso na distância"\
  beta -> \
  "TP" -> "true positive", "FP" -> "false positive", "FN" -> "false negative"
$
*/


//#todo_outline