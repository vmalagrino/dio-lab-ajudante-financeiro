# 🤵 Alfred, o agente Financeiro Inteligente com IA Generativa

## 1. Documentação do Agente

Um asisstente de IA criado para ajudar no dia-a-dia com dúvidas sobre conceitos, funcionalidades e as modalidades de investimento existentes, feito para educar e organizar sua vida financeira, pensado para ser o seu ajudante pessoal em finanças.

**O que o Alfred faz:**

- ✅ Explica conceitos financeiros de forma simples
- ✅ Usa dados do cliente como exemplos práticos
- ✅ Responde dúvidas sobre produtos financeiros
- ✅ Analisa padrões de gastos de forma educativa

**O que o Alfred NÃO faz:**

- ❌ Não recomenda investimentos
- ❌ Não acessa dados bancários sensíveis
- ❌ Não substitui um profissional certificado

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

## 2. Base de Conhecimento

| Arquivo | Formato | Descrição para o agente|
|---------|---------|-----------|
| `historico_atendimento.csv` | CSV | Interações anteriores, para dar continuidade ao atendimento de forma eficiente. |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre dúvudas e necessidades de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para serem explicados o funcionamento ao cliente. |
| `transacoes.csv` | CSV | Analisar padrões de gastos do cliente e usar estes dados de forma didática. |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

## 3. Prompts do Agente

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

## 4. Aplicação Funcional

### 4.1. Instalar Dependências

```python
pip install streamlit pandas requests
```

### 4.2. Executar o Alfred

```python
streamlit run src/app.py
```

### 4.3. Exemplo de uso




📁 **Pasta:** [`src/app.py`](./src/app.py)

---

## 5. Avaliação e Métricas

| teste | teste |
|-------|-------|
| valores| teste de valores|

**Métricas Sugeridas:**

- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

## 6. Pitch

### Qual problema seu agente resolve?

Muitas pessoas não tem noção do que são os investimentos e não tem ou não tiveram uma educação financeira que pudesse ajudar com assuntos como economia, redução de gastos. O Alfred tem o papel de esclarecer dúvidas e e ser o seu professor nessa jornada.

### Como ele funciona na prática?

Através da inclusão dos dados manualmente ou por meio de código ele ajuda e gera informações a respeito de suas finanças e dúvidas sobre investimentos, ou seja, ele não gera dados ou busca de novas fontes, ele apenas trabalha com o que foi informado.

### Por que essa solução é inovadora?

Através de conceitos simples e forma prática e didática ele vem para educar e ajudar os usuários sobre suas finanças e sobre o mundo dos investimentos, abrindo portas para novos conhecimentos.

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)