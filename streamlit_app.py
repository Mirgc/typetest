import streamlit as st
import re

def parse_quiz(file):
    content = file.getvalue().decode("utf-8")
    questions = re.findall(r"(.*?)\n((?:[a-e]\).*?\n?)+)-([a-eA-E])", content, re.S)
    quiz = []
    for i, (question, options, answer) in enumerate(questions):
        options_list = [opt.strip() for opt in options.strip().split("\n")]
        quiz.append({
            "id": i + 1,
            "question": question.strip(),
            "options": options_list,
            "answer": answer.strip().upper()
        })
    return quiz

def main_page():
    st.title("Quiz App")

    st.write("### Ejemplo de formato del archivo:")
    st.code("""
Cual es la capital de España?
a) Bilbao
b) Barcelona
c) Cadiz
d) Madrid
e) Burgos
-D

Cuanto es 5+2?
a) 7
b) 5
c) 3
d) 10
e) 15
-A
""", language="text")

    uploaded_file = st.file_uploader("Sube tu archivo de preguntas", type=["txt"])
    
    if uploaded_file:
        st.session_state.quiz = parse_quiz(uploaded_file)
        st.session_state.current_page = "quiz"
        st.session_state.current_index = 0
        st.session_state.correct_answers = 0
        st.session_state.wrong_answers = []
        st.rerun()


def quiz_page():
    st.title("Modo Quiz")
    
    # Menú de navegación en sidebar
    if st.sidebar.button("Volver al inicio"):
        st.session_state.current_page = "main"
        st.rerun()
    
    # Estadísticas en el sidebar
    st.sidebar.write("### Progreso")
    st.sidebar.write(f"✅ Correctas: {st.session_state.correct_answers}")
    st.sidebar.write(f"❌ Incorrectas: {len(st.session_state.wrong_answers)}")
    
    # Controles principales
    quiz = st.session_state.quiz
    total_questions = len(quiz)
    current_index = st.session_state.current_index
    
    # Encabezado con estadísticas
    display_index = min(current_index + 1, total_questions)
    st.write(f"**Pregunta {display_index} de {total_questions}**")
   
    st.markdown("---")
    
    # Mostrar pregunta actual
    if current_index < total_questions:
        q = quiz[current_index]
        st.subheader(f"{q['id']}. {q['question']}")
        
        selected_option = st.radio("Opciones:", q["options"], key=f"q{current_index}")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            if st.button("Comprobar"):
                selected_letter = re.match(r"([a-eA-E])\)", selected_option).group(1).upper()
                
                if selected_letter == q["answer"]:
                    st.success("¡Correcto!")
                    st.session_state.correct_answers += 1
                else:
                    st.error(f"Incorrecto. La respuesta es {q['answer']})")
                    st.session_state.wrong_answers.append(q)
                
                st.session_state.current_index = min(current_index + 1, total_questions)
                if st.session_state.current_index >= total_questions:
                    st.balloons()
                if st.button("Siguiente"):
                    st.rerun()
        
        with col2:
            if st.button("Saltar pregunta"):
                st.session_state.wrong_answers.append(q)
                st.session_state.current_index = min(current_index + 1, total_questions)
                if st.session_state.current_index >= total_questions:
                    st.balloons()
                st.rerun()
    else:
        st.write("🎉 ¡Quiz completado!")
        # Opciones de reinicio
        restart_mode = st.radio("Selecciona modo de reinicio:", 
                              ["Completo", "Solo preguntas fallidas"],
                              horizontal=True)
        
        if st.button(f"Reiniciar ({restart_mode})"):
            if restart_mode == "Solo preguntas fallidas" and st.session_state.wrong_answers:
                # Reiniciar solo con preguntas fallidas
                st.session_state.quiz = st.session_state.wrong_answers.copy()
                st.session_state.total_questions = len(st.session_state.quiz)
                # Resetear IDs de preguntas
                for i, q in enumerate(st.session_state.quiz):
                    q['id'] = i + 1
            
            st.session_state.current_index = 0
            st.session_state.correct_answers = 0
            st.session_state.wrong_answers = []
            st.rerun()

def main():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "main"
    
    if st.session_state.current_page == "main":
        main_page()
    elif st.session_state.current_page == "quiz":
        quiz_page()

if __name__ == "__main__":
    main()

