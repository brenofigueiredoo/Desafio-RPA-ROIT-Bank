### Sobre ###
Desafio feito pela ROIT Bank em parceria com a Kenzie Academy Brasil. Esse teste tem como intuito avaliar conhecimentos básicos, sendo que o principal objetivo é analisar o
raciocínio lógico e a capacidade de solucionar problemas, mesmo que ainda desconhecidos.

**Processo de Negórcio**
* Criar uma automação que navegue pelo site do IBGE e busque os dados de CNAE das secções A, B e C.
* Capturar todas as informações de cada secção e inserir em uma planilha.
* Desenvolver um Script em python que ao final do processo será chamado dentro da sua automação para
ler a planilha, transformar o texto das descrições para minúsculo e remover acentos das colunas de texto e
remover tudo que for diferente de número das colunas de códigos exceto da coluna Código Secção.

### Observação ###
* Versão do Python Utilizada: `3.10.11`
* Na pasta do script em python, `DesafioRPAByROIT\ScriptFormat` execute no Prompt de Comando `pip install -r requirements.txt`

### Documentation is included in the Documentation folder ###


### REFrameWork Template ###
**Robotic Enterprise Framework**

* Built on top of *Transactional Business Process* template
* Uses *State Machine* layout for the phases of automation project
* Offers high level logging, exception handling and recovery
* Keeps external settings in *Config.xlsx* file and Orchestrator assets
* Pulls credentials from Orchestrator assets and *Windows Credential Manager*
* Gets transaction data from Orchestrator queue and updates back status
* Takes screenshots in case of system exceptions


### How It Works ###

1. **INITIALIZE PROCESS**
 + ./Framework/*InitiAllSettings* - Load configuration data from Config.xlsx file and from assets
 + ./Framework/*GetAppCredential* - Retrieve credentials from Orchestrator assets or local Windows Credential Manager
 + ./Framework/*InitiAllApplications* - Open and login to applications used throughout the process

2. **GET TRANSACTION DATA**
 + ./Framework/*GetTransactionData* - Fetches transactions from an Orchestrator queue defined by Config("OrchestratorQueueName") or any other configured data source

3. **PROCESS TRANSACTION**
 + *Process* - Process trasaction and invoke other workflows related to the process being automated 
 + ./Framework/*SetTransactionStatus* - Updates the status of the processed transaction (Orchestrator transactions by default): Success, Business Rule Exception or System Exception

4. **END PROCESS**
 + ./Framework/*CloseAllApplications* - Logs out and closes applications used throughout the process


### For New Project ###

1. Check the Config.xlsx file and add/customize any required fields and values
2. Implement InitiAllApplications.xaml and CloseAllApplicatoins.xaml workflows, linking them in the Config.xlsx fields
3. Implement GetTransactionData.xaml and SetTransactionStatus.xaml according to the transaction type being used (Orchestrator queues by default)
4. Implement Process.xaml workflow and invoke other workflows related to the process being automated
