# Guia Synesis — Indice

193 verbetes. Consulta rapida da linguagem Synesis.

> Gerado por `tools/generate_index.py`. Nao edite a mao.

## Panorama

*Comece por aqui.*

| Verbete | Descricao |
|---|---|
| [**Por onde começar**](GUIDE_START) | Os quatro arquivos de um projeto Synesis e a ordem de escrita. |
| [**Arquivos e extensões**](GUIDE_FILES) | Que arquivo guarda o que, e como eles se referenciam. |
| [**Os três primitivos**](GUIDE_PRIMITIVES) | SOURCE, ITEM e ONTOLOGY: proveniência, ocorrência, conceituacao. |
| [**Cadeias na pratica**](GUIDE_CHAINS) | Como desenhar RELATIONS e ARITY para cadeias que dizem algo. |
| [**Projetos conectados**](GUIDE_MULTIPROJECT) | Como vários projetos independentes se ligam por entidades compartilhadas. |
| [**O ecossistema**](GUIDE_ECOSYSTEM) | As ferramentas ao redor da linguagem e quando usar cada uma. |
| [**Revisar anotação de IA**](GUIDE_REVIEW) | O pipeline ACT: propor, canonizar e aceitar correções sem perder dados. |

## Blocos

*As estruturas da linguagem.*

| Verbete | Descricao |
|---|---|
| [**PROJECT**](BLOCK_PROJECT) | Ponto de entrada do projeto. Declara template, fontes e inclusões. |
| [**TEMPLATE**](BLOCK_TEMPLATE) | Define quais campos existem, de que tipo, e onde podem ser usados. |
| [**SOURCE / ITEM / ONTOLOGY FIELDS**](BLOCK_FIELDS_SPEC) | Lista quais campos são obrigatórios, opcionais ou pareados em cada escopo. |
| [**FIELD**](BLOCK_FIELD) | Define um campo: nome, tipo, escopo e regras de preenchimento. |
| [**SOURCE**](BLOCK_SOURCE) | Unidade de proveniência: de onde procede a informação. |
| [**ITEM**](BLOCK_ITEM) | Unidade de ocorrência: o que foi observado ou registrado. |
| [**ONTOLOGY**](BLOCK_ONTOLOGY) | Princípio organizador: o sistema conceitual que organiza as ocorrências. |
| [**QUESTIONS**](BLOCK_QUESTIONS) | Questões de competência: o que a estrutura do projeto precisa permitir responder. |
| [**PHASE**](BLOCK_PHASE) | Plano de produção: quais campos o synesis-coder gera em cada fase, e a partir de quê. |
| [**EXPORT**](BLOCK_EXPORT) | Declara os artefatos do projeto (JSON, CSV, XLS, ALPACA, OKF, SKOS) e executa todos com synesis export. |

## Tipos de campo

*O que cada TYPE aceita.*

| Verbete | Descricao |
|---|---|
| [**QUOTATION**](TYPE_QUOTATION) | Trecho literal transcrito da fonte. |
| [**CODE**](TYPE_CODE) | Um ou mais conceitos da ontologia atribuídos à unidade. |
| [**MEMO**](TYPE_MEMO) | Nota livre do pesquisador, sem estrutura fixa. |
| [**TEXT**](TYPE_TEXT) | Texto curto de uma linha. |
| [**CHAIN**](TYPE_CHAIN) | Cadeia de conceitos ligados por relações. |
| [**TOPIC**](TYPE_TOPIC) | Termo único, sem espaços, para agrupar unidades. |
| [**ENUMERATED**](TYPE_ENUMERATED) | Valor escolhido de uma lista fechada, sem ordem. |
| [**ORDERED**](TYPE_ORDERED) | Valor escolhido de uma lista fechada, com ordem. |
| [**SCALE**](TYPE_SCALE) | Valor numérico dentro de um intervalo declarado. |
| [**DATE**](TYPE_DATE) | Data. |

## Modificadores

*Propriedades de campo e de projeto.*

| Verbete | Descricao |
|---|---|
| [**SCOPE**](MOD_SCOPE) | Define em que tipo de bloco um campo pode ser usado. |
| [**DESCRIPTION**](MOD_DESCRIPTION) | Texto curto explicando o que um campo registra. |
| [**GUIDELINES**](MOD_GUIDELINES) | Instruções de preenchimento do campo, para o anotador humano ou para IA. |
| [**BUNDLE**](MOD_BUNDLE) | Campos que representam informação composta e so valem juntos. |
| [**ON BIBLIOGRAPHY / ON DATASET**](MOD_ON_BIBLIOGRAPHY) | Campo cujo valor vem do .bib ou de um dataset externo, não do .syn. |
| [**INCLUDE**](MOD_INCLUDE) | Declara os arquivos que compõem o projeto. |
| [**METADATA**](MOD_METADATA) | Bloco opcional do projeto com versão, autoria e datas. |
| [**IDENTIFIES / REFERS TO**](MOD_IDENTIFIES) | Liga projetos independentes: chave primaria e chave estrangeira. |
| [**ROLE**](MOD_ROLE) | Declara a função de um campo de ONTOLOGY no princípio organizador: rótulo, nota, hierarquia ou consolidação. |

## Ligacao entre projetos

*IDENTIFIES e REFERS TO.*

| Verbete | Descricao |
|---|---|
| [**Escopos e ligacao entre projetos**](LINKAGE_SCOPES) | Onde IDENTIFIES e REFERS TO podem ser declarados. |

## Ecossistema

*As ferramentas ao redor da linguagem.*

| Verbete | Descricao |
|---|---|
| [**synesis**](ECO_SYNESIS) | Compilador da linguagem: valida, compila e exporta. |
| [**synesis-lsp**](ECO_LSP) | Servidor LSP: realce, hover, autocomplete e navegacao. |
| [**synesis-coder**](ECO_CODER) | Gera anotacoes validas a partir de texto, guiado pelo template. |
| [**synesis-graph**](ECO_GRAPH) | Converte projetos compilados em bancos de grafo e visualizacoes. |

## Diagnosticos

*Todo erro, aviso e informacao do compilador.*

| Codigo | Situacao |
|---|---|
| [`SYNESIS_E001`](SYNESIS_E001) | Referencia @bibref nao encontrada no arquivo .bib. |
| [`SYNESIS_E002`](SYNESIS_E002) | ITEM sem SOURCE correspondente. |
| [`SYNESIS_E003`](SYNESIS_E003) | SOURCE sem ITEMs associados. |
| [`SYNESIS_E004`](SYNESIS_E004) | Codigo usado em ITEM/CHAIN sem definicao em ONTOLOGY. |
| [`SYNESIS_E005`](SYNESIS_E005) | ONTOLOGY presente mas template nao declara ONTOLOGY FIELDS. (erro 5). |
| [`SYNESIS_E006`](SYNESIS_E006) | Campo listado em SCOPE FIELDS cujo FIELD tem SCOPE diferente. (erro 6). |
| [`SYNESIS_E007`](SYNESIS_E007) | Violacao de ARITY em cadeia causal. |
| [`SYNESIS_E008`](SYNESIS_E008) | Chain qualificada usada mas template nao define RELATIONS. (erro 8). |
| [`SYNESIS_E009`](SYNESIS_E009) | Chain simples usada mas template exige RELATIONS. (erro 9). |
| [`SYNESIS_E010`](SYNESIS_E010) | Relacao nao definida no template. |
| [`SYNESIS_E011`](SYNESIS_E011) | Chain qualificada com estrutura incorreta. |
| [`SYNESIS_E013`](SYNESIS_E013) | Chain sem operador -> entre elementos. (erro 13). |
| [`SYNESIS_E014`](SYNESIS_E014) | Conceito em posicao de codigo com nome identico a uma relacao. (erro 14). |
| [`SYNESIS_E015`](SYNESIS_E015) | Conceito em chain contendo espacos. (erro 15). |
| [`SYNESIS_E016`](SYNESIS_E016) | Campo de BUNDLE ausente (violacao de pareamento). |
| [`SYNESIS_E017`](SYNESIS_E017) | Campos de BUNDLE com quantidades diferentes. |
| [`SYNESIS_E018`](SYNESIS_E018) | BUNDLE declarado com apenas um campo. (erro 18). |
| [`SYNESIS_E020`](SYNESIS_E020) | Campo REQUIRED ausente. |
| [`SYNESIS_E021`](SYNESIS_E021) | Campo FORBIDDEN presente. |
| [`SYNESIS_E022`](SYNESIS_E022) | Campo usado no arquivo nao esta definido no template. |
| [`SYNESIS_E023`](SYNESIS_E023) | Bloco ITEM sem nenhum campo. (erro 23). |
| [`SYNESIS_E026`](SYNESIS_E026) | Valor decimal em campo SCALE com intervalo inteiro. (erro 26). |
| [`SYNESIS_E027`](SYNESIS_E027) | Valor fora da lista ENUMERATED. |
| [`SYNESIS_E028`](SYNESIS_E028) | Tipo de valor incompativel com FieldSpec. |
| [`SYNESIS_E029`](SYNESIS_E029) | Valor fora do range ORDERED. |
| [`SYNESIS_E030`](SYNESIS_E030) | Valor SCALE fora do intervalo [min..max]. |
| [`SYNESIS_E032`](SYNESIS_E032) | Campo TOPIC recebendo valor com espacos. (erro 32). |
| [`SYNESIS_E033`](SYNESIS_E033) | Nome de codigo ou conceito com caracteres invalidos. (erro 33). |
| [`SYNESIS_E039`](SYNESIS_E039) | Campo listado em SCOPE FIELDS sem FIELD correspondente. (erros 39-41). |
| [`SYNESIS_E042`](SYNESIS_E042) | FIELD definido mas nao listado em nenhum SCOPE FIELDS. (erro 42). |
| [`SYNESIS_E047`](SYNESIS_E047) | TYPE CHAIN sem declaracao ARITY. (erro 47). |
| [`SYNESIS_E048`](SYNESIS_E048) | ARITY incompativel com numero de RELATIONS declaradas. (erro 48). |
| [`SYNESIS_E049`](SYNESIS_E049) | TYPE ORDERED sem bloco VALUES. (erro 49). |
| [`SYNESIS_E050`](SYNESIS_E050) | TYPE ENUMERATED sem bloco VALUES. (erro 50). |
| [`SYNESIS_E051`](SYNESIS_E051) | TYPE SCALE sem declaracao FORMAT. (erro 51). |
| [`SYNESIS_E052`](SYNESIS_E052) | Sintaxe invalida na declaracao FORMAT de campo SCALE. (erro 52). |
| [`SYNESIS_E053`](SYNESIS_E053) | Operador invalido na declaracao ARITY. (erro 53). |
| [`SYNESIS_E054`](SYNESIS_E054) | FORMAT declarado em campo que nao e TYPE SCALE. (erro 54). |
| [`SYNESIS_E055`](SYNESIS_E055) | ARITY declarado em campo que nao e TYPE CHAIN. (erro 55). |
| [`SYNESIS_E056`](SYNESIS_E056) | RELATIONS definido em campo que nao e TYPE CHAIN. (erro 56). |
| [`SYNESIS_E057`](SYNESIS_E057) | Dois ou mais blocos SCOPE FIELDS no mesmo template. (erro 57). |
| [`SYNESIS_E058`](SYNESIS_E058) | Valor em bloco VALUES com espaco no inicio ou fim. (erro 58). |
| [`SYNESIS_E059`](SYNESIS_E059) | Valores duplicados dentro de um mesmo bloco VALUES. (erro 59). |
| [`SYNESIS_E060`](SYNESIS_E060) | Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60). |
| [`SYNESIS_E061`](SYNESIS_E061) | Arquivo .syn no diretorio do projeto nao referenciado em INCLUDE ANNOTATIONS. (erro 61). |
| [`SYNESIS_E062`](SYNESIS_E062) | Arquivo .syno no diretorio do projeto nao referenciado em INCLUDE ONTOLOGY. (erro 62). |
| [`SYNESIS_E063`](SYNESIS_E063) | Arquivo .bib declarado no projeto nao encontrado no caminho indicado. (erro 63). |
| [`SYNESIS_E064`](SYNESIS_E064) | Nenhum arquivo .synp encontrado na raiz do workspace. |
| [`SYNESIS_E065`](SYNESIS_E065) | Bloco PROJECT sem declaracao TEMPLATE. (erro 65). |
| [`SYNESIS_E066`](SYNESIS_E066) | Dois blocos PROJECT no mesmo arquivo .synp. (erro 66). |
| [`SYNESIS_E068`](SYNESIS_E068) | Dois blocos ONTOLOGY com o mesmo nome de conceito. (erro 68). |
| [`SYNESIS_E069`](SYNESIS_E069) | Dois FIELD com o mesmo nome no template. (erro 69). |
| [`SYNESIS_E070`](SYNESIS_E070) | Mesmo @bibref declarado em dois blocos SOURCE no mesmo arquivo. (erro 70). |
| [`SYNESIS_E072`](SYNESIS_E072) | Entrada em arquivo .bib nao esta em formato BibTeX valido. (erro 72). |
| [`SYNESIS_E073`](SYNESIS_E073) | Arquivo .syn declarado em INCLUDE ANNOTATIONS nao encontrado. (erro 73). |
| [`SYNESIS_E074`](SYNESIS_E074) | Arquivo .syno declarado em INCLUDE ONTOLOGY nao encontrado. (erro 74). |
| [`SYNESIS_E075`](SYNESIS_E075) | Caminho declarado no .synp aponta para fora do diretorio do projeto. (erro 75). |
| [`SYNESIS_E076`](SYNESIS_E076) | Arquivo declarado no .synp existe mas nao pode ser lido/parseado. (erro 76). |
| [`SYNESIS_E077`](SYNESIS_E077) | Dois SOURCEs com o mesmo valor num campo IDENTIFIES. (erro 77). |
| [`SYNESIS_E078`](SYNESIS_E078) | IDENTIFIES/REFERS TO em campo que nao e SCOPE SOURCE. (erro 78). |
| [`SYNESIS_E079`](SYNESIS_E079) | Campo REQUIRED ... ON BIBLIOGRAPHY sem valor no .bib do SOURCE. (erro 79). |
| [`SYNESIS_E081`](SYNESIS_E081) | Dois membros declaram IDENTIFIES do mesmo rotulo no link step. (erro 81). |
| [`SYNESIS_E082`](SYNESIS_E082) | TYPE divergente entre campos da mesma entidade no link step. (erro 82). |
| [`SYNESIS_E084`](SYNESIS_E084) | INCLUDE SHARED usado com tipo diferente de ONTOLOGY. (erro 84). |
| [`SYNESIS_E085`](SYNESIS_E085) | Campo REQUIRED ... ON DATASET sem valor no registro do dataset TOML. (erro 85). |
| [`SYNESIS_E086`](SYNESIS_E086) | VALUES definido em campo que nao e ORDERED nem ENUMERATED. (erro 86). |
| [`SYNESIS_E087`](SYNESIS_E087) | Prefixo de indice `[N]` em VALUES de campo ENUMERATED. (erro 87). |
| [`SYNESIS_E088`](SYNESIS_E088) | Campo ORDERED escrito com o rotulo em vez do indice. (erro 88). |
| [`SYNESIS_E089`](SYNESIS_E089) | Mesma chave em dois arquivos da bibliografia ou do dataset. (erro 89). |
| [`SYNESIS_E090`](SYNESIS_E090) | Resumo dos codigos sem conceito na ontologia, quando a checagem esta desligada. |
| [`SYNESIS_E091`](SYNESIS_E091) | Linha de QUESTIONS fora da forma `<id>: <texto>`. |
| [`SYNESIS_E092`](SYNESIS_E092) | Questao com identificador e sem texto (`Q1:`). |
| [`SYNESIS_E093`](SYNESIS_E093) | Identificador de questao repetido no projeto. |
| [`SYNESIS_E094`](SYNESIS_E094) | Formato de EXPORT desconhecido ou ainda nao disponivel. |
| [`SYNESIS_E095`](SYNESIS_E095) | Propriedade fora das aceitas pelo formato. |
| [`SYNESIS_E096`](SYNESIS_E096) | Falta uma propriedade obrigatoria do formato. |
| [`SYNESIS_E097`](SYNESIS_E097) | Propriedade repetida no mesmo bloco. |
| [`SYNESIS_E098`](SYNESIS_E098) | Dois blocos do mesmo formato sem nome, ou nome repetido. |
| [`SYNESIS_E099`](SYNESIS_E099) | MAP (ou MAP RELATIONS) num formato que nao o usa. |
| [`SYNESIS_E100`](SYNESIS_E100) | GENERATED_AT que nao e data ISO 8601 com fuso. |
| [`SYNESIS_E101`](SYNESIS_E101) | Conceito citado num campo CODE do ONTOLOGY sem bloco ONTOLOGY. |
| [`SYNESIS_E102`](SYNESIS_E102) | Item vazio numa lista (`a, , b`) de um campo CODE do ONTOLOGY. |
| [`SYNESIS_E103`](SYNESIS_E103) | Dois blocos com nomes que so coincidem pela forma Unicode (NFC). |
| [`SYNESIS_E104`](SYNESIS_E104) | Papel fora do catalogo. |
| [`SYNESIS_E105`](SYNESIS_E105) | Papel previsto e ainda indisponivel (DIVISION). |
| [`SYNESIS_E106`](SYNESIS_E106) | LABEL, NOTE, HIERARCHY ou DIVISION sem especie. |
| [`SYNESIS_E107`](SYNESIS_E107) | Papel com tipo de campo incompativel. |
| [`SYNESIS_E108`](SYNESIS_E108) | ROLE num campo fora de SCOPE ONTOLOGY. |
| [`SYNESIS_E109`](SYNESIS_E109) | ROLE repetido no mesmo FIELD. |
| [`SYNESIS_E110`](SYNESIS_E110) | Dois campos com NOTE DEFINITION, ou dois com LABEL PREFERRED. |
| [`SYNESIS_E111`](SYNESIS_E111) | Campo HIERARCHY declarado REQUIRED. |
| [`SYNESIS_E112`](SYNESIS_E112) | Campo do ONTOLOGY com nome de chave canonica do JSON. |
| [`SYNESIS_E113`](SYNESIS_E113) | Mais de um termo em LABEL PREFERRED num conceito. |
| [`SYNESIS_E114`](SYNESIS_E114) | O mesmo termo em duas especies de LABEL no mesmo conceito. |
| [`SYNESIS_E115`](SYNESIS_E115) | O mesmo termo de LABEL em dois conceitos. |
| [`SYNESIS_E116`](SYNESIS_E116) | Termo de LABEL igual ao nome de outro conceito. |
| [`SYNESIS_E117`](SYNESIS_E117) | Conceito que aponta para si mesmo num campo HIERARCHY. |
| [`SYNESIS_E118`](SYNESIS_E118) | Ciclo na hierarquia (uniao das especies). |
| [`SYNESIS_E119`](SYNESIS_E119) | O mesmo par filho-pai em duas especies de HIERARCHY. |
| [`SYNESIS_E120`](SYNESIS_E120) | Bloco sem mencao em ITEM (CODE ou CHAIN) e sem descendente mencionado. |
| [`SYNESIS_E121`](SYNESIS_E121) | Hierarquia pela rota de nome (`parent`/`is_a`). |
| [`SYNESIS_E122`](SYNESIS_E122) | Relacao de MAP RELATIONS ausente das RELATIONS dos campos CHAIN. |
| [`SYNESIS_E123`](SYNESIS_E123) | Relacao presente em mais de um campo CHAIN, sem FROM. |
| [`SYNESIS_E124`](SYNESIS_E124) | Alvo de MAP RELATIONS fora de HIERARCHY KIND/PART/INSTANCE e RELATED. |
| [`SYNESIS_E125`](SYNESIS_E125) | A mesma relacao em dois MAP RELATIONS do bloco. |
| [`SYNESIS_E126`](SYNESIS_E126) | MIN_SOURCES que nao e inteiro >= 1. |
| [`SYNESIS_E127`](SYNESIS_E127) | NAMESPACE que nao e IRI absoluto terminado em / ou #. |
| [`SYNESIS_E128`](SYNESIS_E128) | LANGUAGE que nao e etiqueta BCP 47 bem formada. |
| [`SYNESIS_E129`](SYNESIS_E129) | prefLabel derivado do nome coincide com um rotulo de outro conceito. |
| [`SYNESIS_E130`](SYNESIS_E130) | prefLabel derivado coincide com altLabel/hiddenLabel do mesmo conceito (S13). |
| [`SYNESIS_E131`](SYNESIS_E131) | Dois recursos com o mesmo IRI (defesa). |
| [`SYNESIS_E132`](SYNESIS_E132) | Valores de TOPIC com a mesma identidade e grafias diferentes, unidos. |
| [`SYNESIS_E133`](SYNESIS_E133) | Propriedade fora de FIELDS, INPUT, RULES e OUTPUT (OUTPUT so em ONTOLOGY). |
| [`SYNESIS_E134`](SYNESIS_E134) | Propriedade repetida no bloco PHASE. |
| [`SYNESIS_E135`](SYNESIS_E135) | FIELDS, INPUT ou RULES sem campo; PHASE sem FIELDS. |
| [`SYNESIS_E136`](SYNESIS_E136) | Campo de FIELDS, INPUT ou RULES ausente do template. |
| [`SYNESIS_E137`](SYNESIS_E137) | O mesmo campo em FIELDS de duas fases. |
| [`SYNESIS_E138`](SYNESIS_E138) | Campo de ONTOLOGY numa PHASE ANNOTATIONS, ou de SOURCE/ITEM numa PHASE ONTOLOGY. |
| [`SYNESIS_E139`](SYNESIS_E139) | INPUT produzido só por uma fase POSTERIOR (ordem das fases). |
| [`SYNESIS_E140`](SYNESIS_E140) | Campos de um BUNDLE em fases diferentes. |
| [`SYNESIS_E141`](SYNESIS_E141) | Com blocos PHASE, campo REQUIRED que nenhuma fase produz. |
| [`SYNESIS_E142`](SYNESIS_E142) | PHASE ONTOLOGY sem OUTPUT num projeto sem exatamente um .syno elegivel. |
| [`SYNESIS_E143`](SYNESIS_E143) | OUTPUT fora dos .syno locais citados como arquivo. |
| [`SYNESIS_E144`](SYNESIS_E144) | Fases com o mesmo nome, ou nomes que viram a mesma variavel de ambiente. |
| [`SYNESIS_E145`](SYNESIS_E145) | Bloco cujo USE aponta para ele mesmo. |
| [`SYNESIS_E146`](SYNESIS_E146) | USE que aponta para um conceito que tambem e preterido. |
| [`SYNESIS_E147`](SYNESIS_E147) | Campo USE com mais de um conceito. |
| [`SYNESIS_E148`](SYNESIS_E148) | Bloco preterido com outros campos alem do USE. |
| [`SYNESIS_E149`](SYNESIS_E149) | Depois de resolver USE, um conceito seria pai de si mesmo. |
| [`SYNESIS_E150`](SYNESIS_E150) | ALIAS_LABEL fora de HIDDEN e ALTERNATIVE. |
| [`SYNESIS_E151`](SYNESIS_E151) | Nome preterido igual a um rotulo que o alvo ja tem. |
| [`SYNESIS_E152`](SYNESIS_E152) | REGISTRY que nao e um arquivo de texto utilizavel. |
| [`SYNESIS_E153`](SYNESIS_E153) | IRI registrado como publicado sem bloco nem USE que o substitua. |
| [`SYNESIS_E154`](SYNESIS_E154) | SKOS gerado viola condicao de integridade (S9, S13, S14, S27, S37) ou a regra de hierarquia aciclica do Synesis. |
| [`SYNESIS_E155`](SYNESIS_E155) | Verificacao editorial do SKOS gerado (sem prefLabel, sem posicao, esquema sem topo...). |
| [`SYNESIS_E156`](SYNESIS_E156) | REGISTRY com IRIs de outro NAMESPACE: nao sao conferidos (aviso; o namespace e do pesquisador). |
| [`SYNESIS_E157`](SYNESIS_E157) | REGISTRY e OUTPUT apontam para o mesmo arquivo: um sobrescreveria o outro. |
| [`SYNESIS_E158`](SYNESIS_E158) | Modo declarado (MAP de campos ou INSTRUCTION) sem `MAP ... TO OUTPUT`. |
| [`SYNESIS_E159`](SYNESIS_E159) | Nenhuma origem de instrucao, ou propriedade INSTRUCTION e MAP TO INSTRUCTION juntas. |
| [`SYNESIS_E160`](SYNESIS_E160) | Campo do MAP ausente do template. |
| [`SYNESIS_E161`](SYNESIS_E161) | O mesmo campo duas vezes no mesmo alvo. |
| [`SYNESIS_E162`](SYNESIS_E162) | Campo do OUTPUT tambem em INPUT ou INSTRUCTION: a resposta vazaria no prompt. |
| [`SYNESIS_E163`](SYNESIS_E163) | Campos de dois bundles diferentes: nao ha uma unidade unica por linha. |
| [`SYNESIS_E164`](SYNESIS_E164) | Campo de ONTOLOGY, ou de SOURCE com valor fora do .syn (ON BIBLIOGRAPHY/ON DATASET). |
| [`SYNESIS_E165`](SYNESIS_E165) | Alvo de MAP fora de INSTRUCTION/INPUT/OUTPUT, ou FROM nesses alvos. |
| [`SYNESIS_I080`](SYNESIS_I080) | INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80). |
| [`SYNESIS_I166`](SYNESIS_I166) | Parceiro qualificador (ENUMERATED/ORDERED/SCALE) do bundle iterador fora do mapa. |
| [`SYNESIS_I167`](SYNESIS_I167) | Modo Alpaca embutido com template cujo bundle de CHAIN tem qualificador. |
| [`SYNESIS_W031`](SYNESIS_W031) ⚠ | Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31). |
| [`SYNESIS_W067`](SYNESIS_W067) ⚠ | Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67). |
| [`SYNESIS_W071`](SYNESIS_W071) ⚠ | Dois blocos ONTOLOGY com description identica. (erro 71). |
| [`SYNESIS_W083`](SYNESIS_W083) ⚠ | REFERS TO cujo valor nao casa com nenhum IDENTIFIES no link step. (warning 83). |
