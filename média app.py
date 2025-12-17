import streamlit as st

# 1. Configuração da Página (Título na aba e ícone)
st.set_page_config(
    page_title="Calculadora UNAMA",
    page_icon="⚖️",  # Ícone de balança (Direito)
    layout="centered"
)

# --- BARRA LATERAL (MENU) ---
with st.sidebar:
    st.header("Sobre")
    st.write("Esta calculadora segue o sistema de avaliação oficial (Regra dos 8 pontos de corte).")
    st.markdown("---")
    # AQUI: Coloque seu nome abaixo
    st.write("👨‍💻 **Desenvolvido por:**")
    st.write("Henrique Brito") 
    st.write("Estudante de Direito")

# --- CABEÇALHO COM LOGO ---
# Tenta usar uma logo da internet. Se o link quebrar um dia, ele apenas ignora.
try:
    # Link público da logo da UNAMA ou Grupo Ser
    st.image("https://logo.unama.br/img/png/unama.png", width=200)
except:
    st.header("UNAMA")

# Título colorido (Verde estilo UNAMA)
st.markdown("<h1 style='color: #006633;'>Calculadora de Notas</h1>", unsafe_allow_html=True)
st.write("Insira suas notas abaixo para verificar sua situação.")

st.divider()

# --- ENTRADA DE DADOS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 1ª Avaliação")
    nota1 = st.number_input("Nota AV1", min_value=0.0, max_value=10.0, step=0.1, key="n1")

with col2:
    st.markdown("#### 2ª Avaliação")
    nota2 = st.number_input("Nota AV2", min_value=0.0, max_value=10.0, step=0.1, key="n2")

# --- CÁLCULOS ---
if st.button("Calcular Minha Situação", type="primary"):
    
    soma = nota1 + nota2
    media = soma / 2
    
    st.markdown("---")
    
    # Mostrador de métricas grande
    c_soma, c_media = st.columns(2)
    c_soma.metric("Soma Total", f"{soma:.1f}")
    c_media.metric("Média Semestral", f"{media:.1f}")
    
    # --- REGRAS DE NEGÓCIO ---
    
    # 1. Reprovação Direta (Soma < 8)
    if soma < 8.0:
        st.error("❌ **REPROVADO POR NOTA (CORTE)**")
        st.write(f"Sua soma foi **{soma:.1f}**. A regra exige soma mínima de **8.0** para ir à final.")
        
    # 2. Aprovado Direto (Média >= 7)
    elif media >= 7.0:
        st.success("✅ **APROVADO DIRETO! PARABÉNS!**")
        st.balloons()
        
    # 3. Prova Final
    else:
        st.warning("⚠️ **VOCÊ ESTÁ NA PROVA FINAL**")
        nota_necessaria = 10 - media
        
        st.markdown(f"""
        ### Precisa tirar na Final: <span style='color:red'>{nota_necessaria:.1f}</span>
        """, unsafe_allow_html=True)
        
        st.info(f"Cálculo da faculdade: 10 - {media:.1f} (Média) = {nota_necessaria:.1f}")

# Rodapé simples
st.markdown("---")
st.caption("Ferramenta não oficial para auxílio estudantil.")

