import streamlit
import controllers.alunocontrol as alunocontrol
import paginas.alunos.incluir as criarPaginaAluno



def consultar():
    parametroId = streamlit.experimental_get_query_params()
    if parametroId == {}:
        streamlit.experimental_set_query_params()
        streamlit.title('Alunos')
        colunas = streamlit.columns((3, 4, 5, 3, 3, 3, 6, 5, 5))
        campos = ['N°', 'Nome', 'Matéria', 'Nota1', 'Nota 2', 'Média', 'Situação', 'Excluir', 'Alterar']
        for col, campos_nome in zip(colunas, campos):
            col.write(campos_nome)

        for item in alunocontrol.selecionarTodos():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = streamlit.columns((3, 4, 5, 3, 3, 3, 6, 5, 5))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.materia)
            col4.write(item.n1)
            col5.write(item.n2)
            col6.write(item.media)
            col7.write(item.situacao)
            button_space_excluir = col8.empty()
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
            button_space_alterar = col9.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.id))

            if on_click_excluir:
                alunocontrol.excluir(item.id)
                button_space_excluir.button('Excluído', 'btnExcluído' + str(item.id))

            if on_click_alterar:
                streamlit.experimental_set_query_params(
                    id=[item.id]
                )
                streamlit.experimental_rerun()

    else:
        on_click_voltar = streamlit.button('Voltar')
        if on_click_voltar:
            streamlit.experimental_set_query_params()
            streamlit.experimental_rerun()
        criarPaginaAluno.Incluir()





