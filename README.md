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
```

### 4. Verificar instalação
```powershell
python -c "import pynput; print('pynput instalado com sucesso!')"
```

## 🚀 Como Usar

### Executar o Keylogger
```powershell
# Com o ambiente virtual ativado
python keylogger.py
```

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
├── .venv/                 # Ambiente virtual Python
├── .github/               # Configurações do GitHub
├── keylogger.py           # Script principal
├── log.txt                # Arquivo de logs (criado automaticamente)
└── README.md              # Este arquivo
```

## 🔧 Funcionalidades

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

## 🐛 Solução de Problemas

### Python não encontrado
```powershell
# Verificar se Python está instalado
python --version

# Se não estiver, baixe em: https://python.org/downloads/
```

### Erro de permissão de scripts
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Biblioteca pynput não funciona
```powershell
# Reinstalar a biblioteca
pip uninstall pynput
pip install pynput
```

### Keylogger não captura teclas
- Execute como administrador
- Verifique antivírus (pode bloquear)
- Confirme se o ambiente virtual está ativado


**Lembre-se**: Com grandes poderes vêm grandes responsabilidades. Use este conhecimento de forma ética e responsável! 🛡️