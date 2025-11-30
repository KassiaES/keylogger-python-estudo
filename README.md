# Keylogger Python - Estudo de Segurança

⚠️ **AVISO IMPORTANTE**: Este projeto é destinado exclusivamente para **fins educacionais e de estudo de segurança cibernética**. Utilize apenas em sistemas próprios e com autorização explícita. O uso indevido pode violar leis de privacidade e segurança.

## 📋 Descrição

Este é um keylogger simples desenvolvido em Python usando a biblioteca `pynput`. O projeto captura teclas pressionadas e salva em um arquivo de log, sendo útil para:

- Estudos de segurança cibernética
- Compreensão de como funciona a captura de eventos de teclado
- Análise de comportamento de entrada do usuário
- Demonstração de conceitos de monitoramento de sistema

## 🛠️ Pré-requisitos

- Python 3.8+ instalado no sistema
- Windows (testado no Windows com PowerShell)
- Permissões administrativas podem ser necessárias

## ⚙️ Configuração do Ambiente

### 1. Clone ou baixe o projeto
```bash
git clone <url-do-repositorio>
cd Keylogger
```

### 2. Criar ambiente virtual (.venv)
```powershell
# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual no Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Se houver erro de execução de scripts, execute:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Instalar dependências
```powershell
# Com o ambiente virtual ativado
pip install pynput

# Para versão com envio de email (opcional)
pip install secure-smtplib
```

### 4. Verificar instalação
```powershell
python -c "import pynput; print('pynput instalado com sucesso!')"
```

## 🚀 Como Usar

### Executar o Keylogger Básico
```powershell
# Com o ambiente virtual ativado
python keylogger.py
```

### 📧 Executar o Keylogger com Envio de Email
```powershell
# 1. Configure suas credenciais de email
cp config_email.example.py config_email.py

# 2. Edite config_email.py com suas informações:
# - Seu email Gmail
# - App Password do Google (não a senha normal)
# - Intervalo de envio desejado

# 3. Execute o keylogger com email
python keylogger_email.py
```

### 🔍 Execução Invisível (Modo Stealth)
Para estudos avançados de segurança, você pode executar o keylogger de forma invisível:

```powershell
# 1. Renomear o arquivo para .pyw (Python Window - sem console)
ren .\keylogger.py .keylogger.pyw
# OU para a versão com email:
ren .\keylogger_email.py .keylogger_email.pyw

# 2. Executar de forma invisível (sem janela do terminal)
python .keylogger.pyw
# OU:
python .keylogger_email.pyw
```

**Como funciona:**
- **`.pyw`**: Extensão especial do Python que executa scripts sem mostrar janela do console
- **Processo em background**: O keylogger roda silenciosamente em segundo plano
- **Sem feedback visual**: Não há mensagens no terminal (mais realista para estudos de segurança)

**Para voltar ao modo normal:**
```powershell
# Renomear de volta para .py
ren .\.keylogger.pyw .\keylogger.py
ren .\.keylogger_email.pyw .\keylogger_email.py
```

⚠️ **Atenção**: Use o modo invisível apenas para:
- Estudos controlados de segurança
- Demonstrações educacionais autorizadas
- Testes em sistemas próprios

### Operação
1. **Início**: O programa exibe "Keylogger iniciado. Pressione ESC para parar."
2. **Captura**: Todas as teclas digitadas são capturadas e salvas em `log.txt`
3. **Parada**: Pressione a tecla `ESC` para encerrar o programa
4. **Finalização**: O programa exibe "Keylogger parado."

### Visualizar Resultados
- Os logs são salvos automaticamente no arquivo `log.txt`
- Abra o arquivo no VS Code ou qualquer editor de texto
- O arquivo é sobreescrito a cada nova execução

## 📁 Estrutura do Projeto

```
Keylogger/
├── .venv/                          # Ambiente virtual Python
├── .github/                        # Configurações do GitHub
├── keylogger.py                    # Script básico do keylogger
├── keylogger_email.py              # Keylogger com envio de email
├── config_email.example.py         # Exemplo de configuração de email
├── config_email.py                 # Suas credenciais (não incluído no Git)
├── log.txt                         # Arquivo de logs (criado automaticamente)
├── PROTECAO_CONTRA_KEYLOGGERS.txt  # Guia completo de proteção e sandboxing
└── README.md                       # Este arquivo
```

## 🔧 Funcionalidades

### Versão Básica (`keylogger.py`)
- ✅ Captura teclas em tempo real
- ✅ Salva em arquivo local (`log.txt`)
- ✅ Para com a tecla ESC
- ✅ Sobreescreve logs a cada execução

### Versão com Email (`keylogger_email.py`)
- ✅ Todas as funcionalidades da versão básica
- ✅ **Envio automático por email** a cada 5 minutos
- ✅ **Envio de logs finais** ao pressionar ESC
- ✅ **Timestamp** em cada email
- ✅ **Configuração segura** de credenciais
- ✅ **Suporte a App Passwords** do Google

### 📧 Configuração do Email (Gmail)

1. **Criar conta de teste:**
   - Crie um Gmail específico para testes (ex: `testkeylogger@gmail.com`)

2. **Habilitar verificação em duas etapas:**
   - Acesse: Google Account → Security → 2-Step Verification
   - Ative a verificação em duas etapas

3. **Gerar App Password:**
   - Acesse: https://myaccount.google.com/apppasswords
   - Crie uma senha de app para "Python Keylogger"
   - Use essa senha no arquivo `config_email.py`

4. **Configurar credenciais:**
   ```powershell
   cp config_email.example.py config_email.py
   # Edite config_email.py com suas informações
   ```

### Teclas Capturadas
- **Caracteres alfanuméricos**: a-z, A-Z, 0-9
- **Espaços**: Convertidos em espaços normais
- **Enter**: Convertido em quebra de linha
- **Tab**: Convertido em tabulação
- **Backspace**: Registrado como `[BACKSPACE]`
- **ESC**: Registrado como `[ESC]` e para o programa

### Teclas Ignoradas
- Shift (esquerdo e direito)
- Ctrl (esquerdo e direito)
- Alt (esquerdo e direito)
- Caps Lock
- Cmd/Windows Key

## ⚠️ Avisos Legais e Éticos

### 📜 Uso Responsável
- ✅ **Permitido**: Uso em sistemas próprios para aprendizado
- ✅ **Permitido**: Demonstrações educacionais com autorização
- ✅ **Permitido**: Pesquisa de segurança em ambiente controlado

### ❌ Uso Proibido
- ❌ **Proibido**: Uso sem consentimento em sistemas de terceiros
- ❌ **Proibido**: Captura de dados pessoais sem autorização
- ❌ **Proibido**: Uso para atividades maliciosas ou ilegais

### 🔒 Considerações de Segurança
- O arquivo `log.txt` contém dados sensíveis
- Sempre delete os logs após o estudo
- Use apenas em redes seguras e isoladas
- Considere as implicações de privacidade


## 🎓 Objetivos Educacionais

- Compreender como funciona a captura de entrada do usuário
- Aprender sobre bibliotecas de monitoramento em Python
- **Estudar protocolos de email (SMTP) em Python**
- **Entender autenticação segura em aplicações**
- **Praticar envio automatizado de dados**
- Desenvolver consciência sobre segurança e privacidade
- Praticar boas práticas de desenvolvimento em Python

---

**Lembre-se**: Com grandes poderes vêm grandes responsabilidades. Use este conhecimento de forma ética e responsável! 🛡️