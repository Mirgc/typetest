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

def main():
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
        quiz = parse_quiz(uploaded_file)
        total_questions = len(quiz)

        current_index = st.session_state.get("current_index", 0)
        correct_answers = st.session_state.get("correct_answers", 0)
        wrong_answers = st.session_state.get("wrong_answers", 0)

        if current_index < total_questions:
            st.write(f"Pregunta {current_index + 1} de {total_questions}")
            st.write(f"✅ Correctas: {correct_answers}")
            st.write(f"❌ Incorrectas: {wrong_answers}")

            q = quiz[current_index]
            st.subheader(f"{q['id']}. {q['question']}")

            selected_option = st.radio("Opciones:", q["options"], key=f"q{current_index}")

            if st.button("Comprobar"):
                # Extraer la letra de la opción seleccionada
                selected_letter = re.match(r"([a-eA-E])\)", selected_option).group(1).upper() if selected_option else ""

                if selected_letter == q["answer"]:
                    st.success("¡Correcto!")
                    correct_answers += 1

                else:
                    st.error("Incorrecto")
                    st.info(f"La respuesta correcta es: {q['answer']}")
                    wrong_answers += 1

                st.session_state.correct_answers = correct_answers
                st.session_state.wrong_answers = wrong_answers

            if st.button("Siguiente"):
                st.session_state.current_index = current_index + 1
                st.rerun()

        else:
            st.write("### Resumen del Test")
            st.write(f"✅ Correctas: {correct_answers}")
            st.write(f"❌ Incorrectas: {wrong_answers}")

            if wrong_answers:
                if st.button("Repetir Fallidas"):
                    st.session_state.current_index = 0
                    st.session_state.correct_answers = 0
                    st.session_state.wrong_answers = 0 
                    st.rerun()

if __name__ == "__main__":
    main()
