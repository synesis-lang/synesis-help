# Guia Synesis — Indice

110 verbetes. Consulta rapida da linguagem Synesis.

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
| [**ONTOLOGY**](BLOCK_ONTOLOGY) | Unidade de conceituacao: o sistema conceitual que organiza as ocorrências. |

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
| [`SYNESIS_E060`](SYNESIS_E060) | \"Valor de ARITY nao e um inteiro (ex: 2.0). (erro 60).\ |
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
| [`SYNESIS_I080`](SYNESIS_I080) | \"INFO: projeto declara REFERS TO — referencia externa nao resolvida isolada. (info 80).\ |
| [`SYNESIS_W031`](SYNESIS_W031) ⚠ | Mesmo codigo repetido na mesma ocorrencia de campo CODE. (erro 31). |
| [`SYNESIS_W067`](SYNESIS_W067) ⚠ | Data MODIFIED anterior a data CREATED no bloco METADATA. (erro 67). |
| [`SYNESIS_W071`](SYNESIS_W071) ⚠ | Dois blocos ONTOLOGY com description identica. (erro 71). |
| [`SYNESIS_W083`](SYNESIS_W083) ⚠ | REFERS TO cujo valor nao casa com nenhum IDENTIFIES no link step. (warning 83). |
