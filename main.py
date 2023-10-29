import streamlit
import paginas.alunos.incluir as incluirPaginaAluno
import paginas.alunos.consultar as consultarAlunos

streamlit.sidebar.title('Menu')
pagina_aluno = streamlit.sidebar.selectbox('Aluno', ['Incluir', 'Consultar'])

if pagina_aluno == 'Consultar':
    consultarAlunos.consultar()

if pagina_aluno == 'Incluir':
    streamlit.experimental_set_query_params()
    incluirPaginaAluno.Incluir()
