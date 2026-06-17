import streamlit as st
import streamlit.components.v1 as components
import graphviz
import os

# Configuração da Página
st.set_page_config(page_title="Master Lógica Matemática", page_icon="🧠", layout="wide")

# Função para carregar o CSS externo
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# --- NAVEGAÇÃO NA ESQUERDA (SIDEBAR) ---
with st.sidebar:
    st.title("📂 Navegação")
    opcao = st.radio(
        "Escolha o tópico:",
        ["Tabela Verdade", "FND e FNC", "Negação de Proposições", "Lei de Morgan", "Exercícios", "Mapa Mental"]
    )

st.title(f"🧠 {opcao}")

# --- CONTEÚDO ---

if opcao == "Tabela Verdade":
    st.markdown("""
    <div class="resumo-box">
        <div class="resumo-title">Resumo: Tabela-Verdade</div>
        <p>A Tabela-Verdade é a ferramenta fundamental para determinar a validade de argumentos lógicos. 
        Ela mapeia todas as combinações de valores (V ou F) e os resultados de conectivos como:</p>
        <ul>
            <li><b>Conjunção (∧):</b> Verdade apenas se ambos forem verdade.</li>
            <li><b>Disjunção (∨):</b> Falso apenas se ambos forem falsos.</li>
            <li><b>Condicional (→):</b> Falso apenas no caso "Vera Fischer" (V seguido de F).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="video-header">🎬 Aula Completa</p>', unsafe_allow_html=True)
        st.video("https://youtu.be/KXm8Hi-I_G0")
    with col2:
        st.markdown('<p class="video-header">📱 Dica Rápida (Shorts)</p>', unsafe_allow_html=True)
        # Shorts renderizado perfeitamente em formato vertical
        components.iframe("https://www.youtube.com/embed/GDJeWM3skG0", width=315, height=560)

elif opcao == "FND e FNC":
    st.markdown("""
    <div class="resumo-box">
        <div class="resumo-title">Resumo: FND e FNC</div>
        <p>As formas normais servem para padronizar qualquer expressão lógica. É essencial para simplificação de circuitos e modelos de dados.</p>
        <ul>
            <li><b>FND (Forma Normal Disjuntiva):</b> Focada nos resultados 1 (Verdadeiros) da tabela.</li>
            <li><b>FNC (Forma Normal Conjuntiva):</b> Focada nos resultados 0 (Falsos) da tabela.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1: st.video("https://youtu.be/FVL1NDmT_jQ")
    with col2: st.video("https://youtube.com/watch?v=tqqwAmOx_IE")

elif opcao == "Negação de Proposições":
    st.markdown("""
    <div class="resumo-box">
        <div class="resumo-title">Resumo: Negação</div>
        <p>Negar uma proposição é inverter seu valor lógico. Na lógica proposicional, as negações mais importantes são:</p>
        <ul>
            <li><b>Negação do SE...ENTÃO:</b> P ∧ ~Q (Mantenha a primeira E negue a segunda).</li>
            <li><b>Negação do Bicondicional:</b> Transforma em Ou Exclusivo (XOR).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="video-header">🎬 Vídeo 1</p>', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=TVjzslm2QO4")
    with col2:
        st.markdown('<p class="video-header">🎬 Vídeo 2</p>', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=iOh0GEryCdE")

elif opcao == "Lei de Morgan":
    st.markdown("""
    <div class="resumo-box">
        <div class="resumo-title">Resumo: Leis de Morgan</div>
        <p>Augustus De Morgan criou regras para negar conjunções e disjunções:</p>
        <ol>
            <li>~(P ∧ Q) ≡ ~P ∨ ~Q</li>
            <li>~(P ∨ Q) ≡ ~P ∧ ~Q</li>
        </ol>
        <p>Em suma: Nega tudo e inverte o símbolo (E vira OU / OU vira E).</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="video-header">📱 Shorts: Lei de Morgan</p>', unsafe_allow_html=True)
    components.iframe("https://www.youtube.com/embed/wQLZuA0pY8I", width=315, height=560)

elif opcao == "Exercícios":
    st.markdown("### Resoluções Práticas")
    # Resumo retirado conforme solicitado
    col1, col2 = st.columns(2)
    with col1: 
        st.markdown('<p class="video-header">📱 Exercício 1</p>', unsafe_allow_html=True)
        components.iframe("https://www.youtube.com/embed/ddt3z6wuQXI", width=315, height=560)
    with col2: 
        st.markdown('<p class="video-header">📱 Exercício 2</p>', unsafe_allow_html=True)
        components.iframe("https://www.youtube.com/embed/pL9daiFc47Q", width=315, height=560)

elif opcao == "Mapa Mental":
    st.subheader("Visualização Estruturada da Matéria")
    
    # Criando duas colunas: Mapa (maior, peso 2) e Menu Interativo (menor, peso 1)
    col_mapa, col_info = st.columns([2, 1])
    
    with col_mapa:
        # Renderizando o Mapa Mental
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB') # Removidos os atributos de tamanho fixo para não bugar a tela
        
        # Nós do mapa
        dot.node('A', 'Lógica de\nCiência de Dados', shape='box', style='filled', fillcolor='#1f77b4', fontcolor='white')
        dot.node('B', 'Tabelas Verdade', shape='ellipse', style='filled', fillcolor='#aec7e8')
        dot.node('C', 'Formas Normais\n(FND e FNC)', shape='ellipse', style='filled', fillcolor='#ffbb78')
        dot.node('D', 'Negações e\nEquivalências', shape='ellipse', style='filled', fillcolor='#98df8a')
        dot.node('E', 'Leis de Morgan', shape='ellipse', style='filled', fillcolor='#ff9896')
        
        # Arestas
        dot.edge('A', 'B')
        dot.edge('A', 'C')
        dot.edge('A', 'D')
        dot.edge('D', 'E', label=' Derivadas')
        dot.edge('B', 'C', label=' Tabelas viram Fórmulas')
        
        # Exibição responsiva
        st.graphviz_chart(dot, use_container_width=True)

    with col_info:
        st.markdown("### 🔍 Detalhes do Mapa")
        st.write("Clique nas categorias abaixo para ler o resumo:")
        
        # Sistema interativo lateral com Expander
        with st.expander("📊 Tabelas Verdade", expanded=True):
            st.info("Estrutura base que analisa as combinações de Verdadeiro/Falso de proposições utilizando conectivos (E, OU, SE, SE E SOMENTE SE). Essencial para identificar Tautologias e Contradições.")
            
        with st.expander("📝 Formas Normais (FND e FNC)"):
            st.info("Formas padronizadas de escrever fórmulas. FND é focada em somar os produtos das linhas verdadeiras, enquanto FNC foca em multiplicar as somas das linhas falsas.")
            
        with st.expander("⚖️ Negações e Equivalências"):
            st.info("Regras de manipulação algébrica (como a contraposição e a simplificação de proposições compostas) usadas para provar argumentos sem precisar montar toda a tabela-verdade.")
            
        with st.expander("🔄 Leis de Morgan"):
            st.info("Regra específica de negação para conjunções e disjunções. Quando negamos uma estrutura com 'E' ou 'OU', negamos todos os componentes individuais e invertemos o conectivo central.")