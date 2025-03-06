import streamlit as st
import re

def mostrar_pregunta(q, idx):
    with st.form(key=f'form_{idx}'):
        st.markdown(f"**{idx+1}. {q['pregunta']}**")
        respuesta = st.radio(
            "Selecciona una opción:",
            options=[chr(65+i) for i in range(len(q['opciones']))],
            key=f"q{idx}",
            format_func=lambda x: f"{x}) {q['opciones'][ord(x)-65]}"
        )
        submitted = st.form_submit_button("Validar respuesta")
        
        if submitted:
            handle_answer(q, idx, respuesta)

def handle_answer(question, idx, selected):
    if selected == question['correcta']:
        st.success("¡Respuesta correcta!")
        st.session_state.respuestas[idx] = True
    else:
        st.error(f"Respuesta incorrecta. La correcta es: {question['correcta']})")
        st.session_state.respuestas[idx] = False

def mostrar_resultados():
    correctas = sum(st.session_state.respuestas.values())
    total = len(st.session_state.respuestas)
    
    st.subheader(f"Resultados: {correctas}/{total} correctas")
    
    if st.button("Repetir preguntas fallidas"):
        preguntas_fallidas = [
            q for idx, q in enumerate(st.session_state.questions)
            if not st.session_state.respuestas.get(idx, True)
        ]
        reiniciar_quiz(preguntas_fallidas)