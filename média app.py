import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Notas", page_icon="🎓")

st.title("🎓 Calculadora de Notas")
st.write("Baseada nas regras de aprovação (Média 7.0 / Corte 8.0 na soma)")

st.divider() # Linha divisória

# 1. Entrada de dados (usamos number_input em vez de input)
col1, col2 = st.columns(2) # Cria duas colunas para ficar bonito visualmente

with col1:
    nota1 = st.number_input("Nota da 1ª Avaliação", min_value=0.0, max_value=10.0, step=0.1)

with col2:
    nota2 = st.number_input("Nota da 2ª Avaliação", min_value=0.0, max_value=10.0, step=0.1)

# Botão para calcular
if st.button("Calcular Resultado"):
    
    # 2. Cálculos
    soma = nota1 + nota2
    media = soma / 2
    
    # Mostra os resultados matemáticos
    st.info(f"📊 **Soma:** {soma:.1f} | **Média:** {media:.1f}")
    
    # 3. Regras de Negócio (A mesma lógica anterior)
    
    # CASO 1: Reprovação Automática pela Soma
    if soma < 8.0:
        st.error("❌ **REPROVADO AUTOMATICAMENTE**")
        st.write(f"A soma das notas ({soma:.1f}) é inferior a 8.0.")
        st.warning("Você **não** tem direito a fazer a prova final.")
        
    # CASO 2: Aprovado Direto
    elif media >= 7.0:
        st.success("✅ **APROVADO DIRETO!**")
        st.balloons() # Solta balões na tela
        
    # CASO 3: Prova Final
    else:
        st.warning("⚠️ **EM PROVA FINAL**")
        
        # Cálculo: 10 - média
        nota_necessaria = 10 - media
        st.markdown(f"### Você precisa tirar na Final: **{nota_necessaria:.1f}**")
        
        # Explicação visual da conta
        st.caption(f"Cálculo: 10 - {media:.1f} (Sua média) = {nota_necessaria:.1f}")