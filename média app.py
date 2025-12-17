import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Calculadora UNAMA",
    page_icon="⚖️",
    layout="centered"
)

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Sobre")
    st.write("Calculadora acadêmica não oficial baseada nas regras de avaliação (Média 7.0 / Corte Soma 8.0).")
    st.markdown("---")
    st.write("👨‍💻 **Desenvolvido por:**")
    st.write("Henrique Brito") 
    st.write("Estudante de Direito")
    st.markdown("---")
    st.info("Dica: Use a aba 'Quanto preciso?' para planejar sua AV2.")

# --- CABEÇALHO ---
try:
    st.image("https://logo.unama.br/img/png/unama.png", width=200)
except:
    st.header("UNAMA")

st.markdown("<h1 style='color: #006633;'>Calculadora de Notas</h1>", unsafe_allow_html=True)

# --- CRIAÇÃO DAS ABAS ---
tab1, tab2 = st.tabs(["🧮 Calcular Minha Média", "🔮 Quanto preciso na AV2?"])

# === ABA 1: CALCULADORA PADRÃO (A que já existia) ===
with tab1:
    st.write("Já tem as duas notas? Veja sua situação final.")
    
    col1, col2 = st.columns(2)
    with col1:
        t1_nota1 = st.number_input("Nota da 1ª Avaliação", 0.0, 10.0, step=0.1, key="t1_n1")
    with col2:
        t1_nota2 = st.number_input("Nota da 2ª Avaliação", 0.0, 10.0, step=0.1, key="t1_n2")

    if st.button("Calcular Resultado", type="primary", key="btn_calc"):
        soma = t1_nota1 + t1_nota2
        media = soma / 2
        
        st.markdown("---")
        c_soma, c_media = st.columns(2)
        c_soma.metric("Soma Total", f"{soma:.1f}")
        c_media.metric("Média Semestral", f"{media:.1f}")
        
        if soma < 8.0:
            st.error("❌ **REPROVADO POR NOTA** (Soma < 8.0)")
            st.caption("Você não atingiu a pontuação mínima para ir à final.")
        elif media >= 7.0:
            st.success("✅ **APROVADO DIRETO!**")
            st.balloons()
        else:
            st.warning("⚠️ **PROVA FINAL**")
            nec_final = 10 - media
            st.markdown(f"Você precisa de **{nec_final:.1f}** na prova final para passar.")

# === ABA 2: PREVISÃO (NOVIDADE) ===
with tab2:
    st.write("Fez a 1ª prova e quer saber o alvo para a 2ª?")
    
    t2_nota1 = st.number_input("Quanto você tirou na 1ª Avaliação?", 0.0, 10.0, step=0.1, key="t2_n1")
    
    if st.button("Simular Cenários", key="btn_sim"):
        st.markdown("---")
        
        # Meta 1: Não reprovar direto (Soma deve ser 8.0)
        # n1 + n2 = 8  -> n2 = 8 - n1
        meta_corte = 8.0 - t2_nota1
        if meta_corte < 0: meta_corte = 0.0 # Se já tirou 8 na primeira, precisa de 0
        
        # Meta 2: Passar direto (Média deve ser 7.0, ou seja, Soma 14.0)
        # n1 + n2 = 14 -> n2 = 14 - n1
        meta_aprovacao = 14.0 - t2_nota1
        
        # ANÁLISE DOS CENÁRIOS
        
        # Cenário A: Impossível passar direto (precisaria de mais de 10)
        if meta_aprovacao > 10.0:
            st.warning(f"⚠️ **Atenção:** Com a nota {t2_nota1} na primeira prova, matematicamente **não é possível passar direto**, pois você precisaria de {meta_aprovacao:.1f} na segunda prova.")
            st.info(f"🎯 Seu foco agora é garantir a Final. Para não reprovar direto, tire pelo menos **{meta_corte:.1f}**.")
            
        # Cenário B: Possível passar direto
        else:
            st.success("✅ Ainda é possível passar direto!")
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.metric("Para Passar Direto", f"{meta_aprovacao:.1f}", delta="Meta Ouro")
                st.caption("Se tirar isso, está de férias.")
                
            with col_b:
                st.metric("Para ir pra Final", f"{meta_corte:.1f}", delta="Meta Mínima", delta_color="off")
                st.caption("Mínimo para não reprovar direto.")

st.markdown("---")
st.caption("Ferramenta desenvolvida para fins acadêmicos.")
