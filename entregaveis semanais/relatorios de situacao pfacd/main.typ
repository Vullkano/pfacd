#import "template.typ": *
#show: project

#let freitas = "Diogo Alexandre Alonso de Freitas"
#let botas = "João Francisco Botas"
#let allan = "Allan Kardec Rodrigues"
#let marco = "Marco Esperança"
#let plancha = "André Plancha"
#show regex("[Ss]print[s]?"): emph // italic on sprints, https://www.dicio.com.br/palavras-com-sprint/
#[
  #set par(leading:5pt)
  #align(center, text(17pt)[
    *Análise e Previsão de Alterações no Funcionamento da Rede:*
  ])
  #v(-1em)
  #align(center, text(15pt)[
    *Relatórios de Situação e Planos da Semana de PFACD*
  ])
  #v(-0.8em)
  #grid(
    columns: (1fr, 1fr, 1fr),
    align(center)[
      #plancha \
      105289, CDC2 \
      #link("mailto:Andre_Plancha@iscte-iul.pt")
    ],
    align(center)[
      #botas \
      104782, CDC1 \
      #link("mailto:Joao_Botas@iscte-iul.pt")
    ],
    align(center)[
      #marco\
      110451, CDC1 \
      #link("mailto:marco_esperanca@iscte-iul.pt")
    ]
  )
  #grid(
    columns: (1fr, 1fr),
    align(center)[
      #allan \
      103380, CDC1 \
      #link("mailto:aksrs@iscte-iul.pt")
    ],
    align(center)[
      #freitas\
      104841, CDC1 \
      #link("mailto:daafs@iscte-iul.pt")
    ]
  )
]

#outline(title: "Índice", indent: 1.5em)
#pagebreak()


= II. Plano semanal: 22 fevereiro (Semana 2 - 3)

== Informação da Reunião
A reunião foi feita ontem (21/2), e todos os membros do grupo estiveram presentes. Os porta-vozes de #freitas e #marco, e próxima semana será #botas o porta-voz, desta vez elegido pelo professor, posteriormente à reunião.
=== Feedback geral e recomendações
- O relatório semanal entregado foi demasiado denso, e recomendou fazer por tópicos;
- Temos de ser mais específicos com as datas de entrega e conteúdos dos sprints;
- Embora a falta de dados possa ser problemática, não impossiblita o tema escolhido, sendo que podemos fazer uma análise geográfica e setorial;
- Incluir o tema mais claro nos entregáveis.
=== Informações e Conclusões
- A reunião com a entidade será daqui a 2 semanas (semana 4);
- A entidade não irá disponibilizar dados pré 2020 até abril, e recomenda que usemos os dados de indicadores gerais por concelho pois incluem dados desde 2014;
- O professor não obteu resposta do IPMA.
- O professor pode disponibilizar dados sobre incêndios urbanos, provenciados pela ANAPEC.
- O tema escolhido será sobre as alterações assinaláveis no funcionamento da rede durante os períodos de vigência dos avisos de perturbações atmosféricas (Projeto 3), o qual nós decidimos como objetivo principal a análise e previsão no funcionamento da rede (potencialmente de forma contínua e de forma difusa).
- Até abril, devemos já ter um primeiro modelo e avaliação supervisionada, o qual estará presente no 3º sprint;
- Depois de abril, será feita um segundo ciclo do CRISP-DM, de forma a rever as conclusões e assumpções nas várias fases iniciais do processo, e encontrar outras formas de limpeza e preparação dos dados.

== Plano semanal
Esclarecendo as dúvidas que tinhamos sobre o tema, esta semana iremos começar em contreto a análise à volta dele. Especificamente, iremos: 

- Organizar e sincronizar áreas de trabalho
- Pedir os dados adicionais recomendados e necessários
- Analisar a tabela de indicadores de continuidade de serviço 
- Começar e adiantar o 1º sprint

=== Organizar e sincronizar áreas de trabalho

Neste momento, estamos a usar várias ferramentas para organizar a informação colecionada e sincronizar trabalho. O nosso plano é completar a sincronização das áreas de trabalho para poder trabalhar em síncrono. Mais especificamente, vamos usar:

- O _git_ e _github_ para organizar documentos encontrados úteis (como o manual de ligações da e-redes), e partilhar e sincronizar _scripts_ e _notebooks_;
- _Typst Web Application_ #footnote[https://typst.app/] + _PowerPoint_, para sincronizar a escrita dos relatórios e dos sprints;
- _pixi_ #footnote[https://pixi.sh/latest/], para poder sincronizar bibliotecas de python e outras ferramentas, usando _Conda_, de forma a ter um ambiente reproduzível;

entre outras que possivelmente surgem-se úteis durante a semana

=== Pedir dados acidionais
Como recomendado, iremos pedir vários dados adicionais para a elaboração do projeto. Em princípio, iremos pedir:

- Dados meteorológicos (temperatura, precipitação, humidade, intensidade e direção do vento, pressão atmosferica, trovoada, descargas elétricas), geofísicos (sismos), e potencialmente climáticos (ondas de calor, monitorização da seca) ao IPMA;
- Dados de incêndios urbanos ao professor (provenciados pela ANEPC, disponibilizadas pelo professor)

Adicionalmente, iremos pesquisar sobre dados demográficos de Portugal que nos possem ser úteis. Estes provavelmente estarão disponiveis na plataforma PORDATA.

=== Analisar a tabela de indicadores de continuidade de serviço

TODO// , FREITAS (inclui o que esperamos encontrar)

=== Começar e adiantar o 1º sprint

O primeiro sprint será principalmente sobre BU. Planeamos que o sprint terá uma descrição da entidade, um entendimento detalhado do problema que vamos analisar, uma revisão da literatura relevante, e uma descrição dos dados que nos são disponíveis que nos possam ser úteis, ambos da entidade e de terceiros#footnote[Dependente da disponibilização dos dados até a data planeada de entrega do sprint pelos terceiros]. Planeamos que, para terça-feira (27/2) teremos já um primeiro rascunho (pelo menos da organização do documento), de forma a o professor poder dar _feedback_.

= I. Relatório de Situação: 20 fevereiro (Semana 2)
Esta semana passada, devido à natureza do projeto, começámos a fazer a fase inicial do projeto. Isto significa que fizemos uma investigação superficial à entidade dos dados, uma descrição dos dados que nos são disponíveis no momento e das variáveis de tais, e começamos a fazer algumas visualizações iniciais. Adicionalmente, requesitamos os dados adicionais ao professor. Estes progressos foram de grande parte feitos de forma independente, devido à natureza do realizado, às limitações descritas a seguir, e ao Carnaval.

Devido aos dados limitados que nós temos acessos, e devido à falta de comunicação que tivémos até ao momento, as análises feitas foram substancialmente limitadas ao conhecimento e informação disponível pelos membros do grupo. Esperamos que a reunião presencial esclareça variás dúvidas que o grupo tem, diretamente ou indiretamente.

== Planeamento das entregas
Antes da pausa letiva da Páscoa, planeamos já ter concluído, ou quase concluído, até à fase de Feature Engineering; ou seja, planeamos ter finalizadas as fases de entendimento do negócio, de reconhecimento dos dados e de transformação e extração de variáveis. Como estimativa planeamos entregar:
// POR FAVOR VERIFICAR ISTO e se isto é antes da pausa letiva
- O primeiro sprint na semana 3 (26/2 - 3/3, próxima semana), // BOTAS: talvez um pouco humilde, face ao que foi dito mais para a frente
- O segundo  sprint na semana 6 (18/3 - 24/3),
- O terceiro sprint na semana 9 (8/4 - 14/4).
Estas estimativas são completamente dependentes da disponibilização de dados adicionais pelo distribuidor, e não são definitivas. Como solicitado, cada sprint será alinhada com as primeiras fases do CRISP-DM. Para esse fim, os sprints serão sobre Business Understanding (BU), Data Understanding (DU), e Data Preparation (DP). Esperamos que mais promenores sobre o que cada sprint precisará fique mais claro na reunião de quarta e ao longo do tempo.

== Problemas que bloquearam o trabalho durante a semana
Apesar de existirem vários dados presentes na fonte disponibilizada pela *E-REDES*#footnote[#link("https://e-redes.opendatasoft.com/explore/")], estes são limitados devido às suas datas, que a maioria é de 2021 para a frente, tornando-se dificil fazer comparações com a época do covid-19 e da crise económica de 2008 (entre outras). 

Na mesma fonte, existem também tabelas com variáveis "codificadas", tornando-se dificil a compreensão de muitos dados apresentados. Isto nota-se especialmente nas tabelas de indicadores de continuidade de serviço #footnote[Exemplo: #link("https://e-redes.opendatasoft.com/explore/dataset/12-continuidade-de-servico-indicadores-gerais-de-continuidade-de-servico/table/")]

Também se torna dificil relacionar os dados que temos acesso atualmente com dados metereológicos e afim, sendo que não encontramos nenhuns dados públicos históricos, inclusive no website do *IPMA*. Os dados que encontramos utéis sobre o tópico são sobre séries longas #footnote[#link("https://www.ipma.pt/pt/oclima/series.longas/list.jsp")], e a maioria são de 2020 para traz, por distrito (não estando todos) e a intervalos mensais, apenas tendo acesso a conjunto de indicadores sobre a temperatura, precipitação e pressão (excepto Lisboa). A utilidade destes dados é volátil e debativel.

// Outra possibilidade, seria também utilizar dados estatísticos apresentados no site da *PORDATA* (#link("https://www.pordata.pt/")), mas estes necessitam de ser estudados e tratados, já que alguns destes se encontram em NUTS III.

== Riscos que podem prever para o desenvolvimento do projeto e planos de contigência

Neste momento, devido à inclareza do que o objetivo principal do projeto é, potenciais riscos e os seus planos de contigência tornam-se difícl de calcular. Devido a tal, ainda gostaríamos de ter mais informação adicional e trocar impressões com o professor antes de responder a esta questão. O nosso principal risco no momento é na disponibilização dos dados adicionais. Isto deve-se ao facto da nossa ideia inicial ser estudar as crises pandémica e económica mas não termos dados de antes de 2020 em bases de dados que achámos relevante estudar. Se a disponibilizção não acontecer num futuro próximo, será provavelmente necessário uma mudança radical do plano atual. 

// Botas - Alerta: Escrita MUITOOOOO SUS

== Progressos feitos

=== Descrições dos dados e análise da entidade

Com isto que dissemos das informações e variáveis existentes na base de dados, podemos referir que nesta semana procurámos fazer uma pequena descrição de cada uma das 21 bases de dados e ver possíveis lacunas que estas continham, verificando limites de datas nos dados (concluindo que não são de todo estandardizados entre as 21), e verificar a importância que poderão ter para o projeto. Esta descrição está disponível no primeiro rascunho do primeiro sprint. 

As descrições não estão completas, sendo que neste momento ainda esperamos pelos dados adicionais requesitados.

Na execução disto, foram também descobertas diversas informações sobre a E-REDES, o que nos levou a encontrar diversos documentos e informações relacionadas com o projeto. Estes documentos e informações foram partilhados entre o grupo, e no futuro é planeado sincronizar e disponibilizar estas. Diversas informações mais gerais foram também anotadas e estão disponíveis no mesmo rascunho.

=== Análise dos dados e Visualizações

#align(center)[
  #figure(
  grid(
    columns: 2,
    rows: 1,
    image("ConsumoDiarioPorHoraAgosto.svg", width: 100%),
    image("ConsumoPORHORACascais2023AgostoDia9.svg", width: 80%),
  ),
  caption: [
    Consumo energético diário no mês de agosto em Cascais, por dia
  ],
)<ConsumoCascaisPorDia>
]

Na @ConsumoCascaisPorDia podemos visualizar o consumo, em 2023, em Cascais. À esquerda, podemos realizar uma breve comparação de todos os dias, enquanto o gráfico da direita demonstra como foi o consumo só do dia 9 no mesmo local. Para, uma evolução ao longo do mês, abaixo será possivel visualizar o respetivo consumo de cascais ao longo de todo o mês de agosto (é importante referir que a _label x_ encontra-se codificada em horas, desde o dia 1/00:00h até ao dia 31/23:00h).

#figure(
  image("ConsumoEnergeticoCascaisAgostoInteiro.svg"),
  caption: [Consumo energético no mês de agosto em Cascais, contínuo]
)  <ConsumoCascaisCont>

A @ConsumoCascaisCont demonstra que o consumo energético é, de certa forma, cíclico, isto é, usando os gráficos anteriores como base, em praticamente todos os dias, existe um maior consumo às 14h e um menor consumo ás 23h.

*NOTA*: Apenas possuimos estes dados na época de Agosto de 2023 e, apesar desta limitação, gostariamos de realizar os mesmo gráficos para uma zona turística/férias a fim de comparar o consumo. // Plancha: n percebi nada :)

== Próxima semana
//PLANCHA: acho q ta mal escrito / Freitas: Está mesmo mal escrito

Para avançar neste projeto é importantíssimo ter a reunião de amanhã, pois o grupo acredita que poderá esclarecer as várias questões que possui, desde a obtenção total dos dados, como a escolha do tema em si. Esperamos ter o primeiro sprint acabado na próxima semana, esse em princípio será o foco da próxima semana. Isto será dependente do resultado da reunião de amanhã, da data da reunião com a entidade, e da disponibilização dos dados adicionais.

Esperamos, depois da reunião, conseguir arranjar um objetivo claro e fixo, a fim de, finalmente, criar o foco essencial para prosseguir no trabalho de forma eficaz e produtiva.
