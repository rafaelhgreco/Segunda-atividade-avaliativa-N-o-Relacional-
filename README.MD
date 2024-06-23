# Segunda atividade avaliativa
## Disciplina – Banco de Dados Não Relacional - DSM
## Grupo: Rafael Henrique Greco, Renan Teixeira e Rodrigo de Almeida
## Apache CouchDB

- **Link do tutorial**: https://youtu.be/YHI64nE2KmE?si=-f3BdGx5KoPdbRtn

## 1. Descrição Técnica do Banco Escolhido: Apache CouchDB

### Descrição do Apache CouchDB
O Apache CouchDB é um banco de dados NoSQL que armazena dados no formato JSON, facilitando a integração com aplicações web modernas. Ele utiliza JavaScript para escrever funções de consulta através de MapReduce, uma técnica poderosa para processar grandes volumes de dados. A API do CouchDB opera totalmente via HTTP, tornando o banco de dados acessível de qualquer lugar com conexão à internet.

### Vantagens do Apache CouchDB

- **Facilidade de Uso**: O CouchDB foi projetado com foco na simplicidade e acessibilidade. A interface Fauxton, acessível via web, torna a administração do banco de dados intuitiva e fácil, mesmo para usuários com menos experiência técnica.
- **Replicação Master-Master**: Diferentemente de muitos outros bancos de dados que utilizam modelos de replicação master-slave, o CouchDB suporta replicação master-master. Isso permite que qualquer instância do banco de dados receba e transmita atualizações, facilitando o desenvolvimento distribuído e melhorando a resiliência e a disponibilidade dos dados.

### Recursos Principais

- **Replicação de Dados Fácil**: A replicação no CouchDB é configurável de forma simples e pode ser realizada entre múltiplas instâncias na rede, seja na mesma máquina ou distribuídas globalmente. Isso é ideal para cenários que requerem alta disponibilidade e tolerância a falhas.
- **Interface Web para Administração**: O CouchDB inclui a interface Fauxton, uma ferramenta web que permite aos usuários gerenciar bancos de dados, documentos, visualizações e configurações de replicação de forma conveniente através de um navegador.
- **Compatibilidade com Múltiplas Plataformas**: Baseado em padrões web abertos, o CouchDB pode ser acessado e gerenciado a partir de qualquer plataforma, garantindo flexibilidade e portabilidade.
- **Segurança Robusta**: Oferece recursos abrangentes de segurança, incluindo autenticação robusta e controle de acesso detalhado a níveis de documento.
- **Escalabilidade Horizontal**: O CouchDB é projetado para escalar horizontalmente, permitindo aumentar a capacidade adicionando mais nós à rede sem downtime ou interrupções.

## 2. Configuração Mínima e Recomendada pelo Fabricante

### Configuração Mínima
- **CPU**: 1 GHz
- **Memória**: 1 GB RAM
- **Disco**: 10 GB (dependendo do volume de dados a ser armazenado)
- **Sistema Operacional**: Windows 7 ou superior, Mac OS X 10.8 ou superior, Linux (qualquer distribuição recente)

### Configuração Recomendada
- **CPU**: 2 GHz ou mais
- **Memória**: 4 GB RAM ou mais
- **Disco**: 100 GB ou mais com SSD para melhor desempenho em operações de I/O
- **Sistema Operacional**: Windows 10 ou superior, Mac OS X 10.12 ou superior, Linux (distribuições estáveis como Ubuntu 18.04 ou superior)

## 3. Processo de Instalação do Banco

### Instalação Tradicional no Windows
1. Baixe o instalador do Apache CouchDB do [site oficial](https://couchdb.apache.org/).
2. Execute o arquivo baixado e siga as instruções do assistente de instalação.
3. Configure o usuário administrador e as configurações de rede durante a instalação.

### Instalação em Container Docker
1. Instale o Docker em sua máquina.
2. Execute o seguinte comando para baixar e rodar o CouchDB em um container Docker:
   ```bash
   docker run -p 5984:5984 -d couchdb
3. Acesse http://localhost:5984/_utils para configurar o banco de dados usando a interface Fauxton.

## 4. CRUD
- **1.**: CRUD realizado direto na plataforma do CouchDB
- **2.**: Query de consulta no Mango Query
- **3.**: Script em Python para realizar CRUD



