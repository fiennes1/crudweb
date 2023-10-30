import streamlit as st
import paginas.alunos.incluir as incluirPaginaAluno
import paginas.alunos.consultar as consultarAlunos
import pyodbc

st.sidebar.title('Menu')
pagina_aluno = st.sidebar.selectbox('Aluno', ['Incluir', 'Consultar'])

if pagina_aluno == 'Consultar':
    consultarAlunos.consultar()

if pagina_aluno == 'Incluir':
    st.experimental_set_query_params()
    incluirPaginaAluno.Incluir()
