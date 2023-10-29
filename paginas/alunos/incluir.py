import streamlit
import controllers.alunocontrol as alunocontrol
import models.Aluno as Aluno


def Incluir():
    idAlteracao = streamlit.experimental_get_query_params()
    # limpar url
    streamlit.experimental_set_query_params()
    alunoRecuperado = None
    if idAlteracao.get('id') is not None:
        idAlteracao = idAlteracao.get('id')[0]
        alunoRecuperado = alunocontrol.selecionarId(idAlteracao)
        streamlit.experimental_set_query_params(
            id=[alunoRecuperado.id]
        )
        streamlit.title('Alterar notas')
    else:
        streamlit.title('Incluir notas')

    with streamlit.form(key='incluir_nota'):
        listaMaterias = ['Matemática', 'Física', 'Química', 'História', 'Português']
        if alunoRecuperado is None:
            input_nome = streamlit.text_input(label='Nome')
            input_materia = streamlit.selectbox('Matéria', options=listaMaterias)
            input_n1 = streamlit.number_input(label='Nota 1')
            input_n2 = streamlit.number_input(label='Nota 2')
            media = (input_n1 + input_n2) / 2
            if media >= 6:
                situacao = 'Aprovado'
            elif 4 <= media <= 5.9:
                situacao = 'Recuperação'
            else:
                situacao = 'Reprovado'
        else:
            input_nome = streamlit.text_input(label='Nome', value=alunoRecuperado.nome)
            input_materia = streamlit.selectbox('Matéria', options=listaMaterias, index=listaMaterias.index(alunoRecuperado.materia))
            input_n1 = streamlit.number_input(label='Nota 1', value=alunoRecuperado.n1)
            input_n2 = streamlit.number_input(label='Nota 2', value=alunoRecuperado.n2)
            media = (input_n1 + input_n2) / 2
            if media >= 6:
                situacao = 'Aprovado'
            elif 4 <= media <= 5.9:
                situacao = 'Recuperação'
            else:
                situacao = 'Reprovado'
        input_button_submit = streamlit.form_submit_button('Enviar')

    if input_button_submit:
        if alunoRecuperado is None:
            alunocontrol.incluir(Aluno.Aluno(0, input_nome, input_materia, input_n1, input_n2, media, situacao))
            streamlit.success('Nota incluída com sucesso!')
        else:
            alunocontrol.alterar(Aluno.Aluno(0, input_nome, input_materia, input_n1, input_n2, media, situacao))
            streamlit.success('Nota alterada com sucesso!')
            streamlit.experimental_set_query_params()

