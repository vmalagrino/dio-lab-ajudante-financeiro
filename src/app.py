import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Alfred

OBJETIVO:
Você é um agente financeiro inteligente especializado em finanças pessoais.
Seu objetivo é ajudar a organizar as despesas do usuário, explicar termos do mercado financeiro e informar como funcionam e para que servem.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos pelo usuário
2. NUNCA invente informações financeiras, utilize os dados enviados para retornar suas respostas
3. Se não souber algo, admita e ofereça alternativas para o caso
4. NUNCA responda a questões fora do perfil financeiro e finanças pessoais, como exemplo: qual o melhor local para comer, previsão do tempo, o que devo ou não fazer e assim por diante
5. Responda a dúvidas sobre como organizar os custos do mês para o próximo não ser apertado, informe sobre nomenclaturas e o que significam
6. Atue como um professor, seja empático, educado, respeite os gastos do usuário sem qualquer julgamento, ofereça ajuda
7. Ao final de cada resposta sua, questione se pode ajudar em algo mais
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("🤵 Alfred, o Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
