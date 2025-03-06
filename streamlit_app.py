import streamlit as st
import re

def parse_quiz(file):
    content = file.getvalue().decode("utf-8")
    questions = re.findall(r"(.*?)\n(a\).*?)\n-(\w)", content, re.S)
    quiz = []
    for question, options, answer in questions:
        options_list = options.strip().split("\n")
        quiz.append({
            "question": question.strip(),
            "options": options_list,
            "answer": answer.strip().upper()
        })
    return quiz

def main():
    st.title("Quiz App")

    uploaded_file = st.file_uploader("Sube tu archivo de preguntas", type=["txt"])

    if uploaded_file:
        quiz = parse_quiz(uploaded_file)
        total_questions = len(quiz)

        current_index = st.session_state.get("current_index", 0)
        correct_answers = st.session_state.get("correct_answers", 0)
        wrong_answers = st.session_state.get("wrong_answers", [])

        if current_index < total_questions:
            q = quiz[current_index]
            st.subheader(q["question"])

            selected_option = st.radio("Opciones:", q["options"], key=f"q{current_index}")
            st.text("answer")

            if st.button("Comprobar"):
                correct_option = next((opt for opt in q["options"] if opt.startswith(q["answer"] + ")")), None)

                if selected_option == correct_option:
                    st.success("¡Correcto!")
                    correct_answers += 1
                else:
                    st.error("Incorrecto")
                    st.info(f"La respuesta correcta es: {correct_option}")
                    wrong_answers.append(q)

                st.session_state.current_index = current_index + 1
                st.session_state.correct_answers = correct_answers
                st.session_state.wrong_answers = wrong_answers
                st.experimental_rerun()

        else:
            st.write("### Resumen del Test")
            st.write(f"✅ Correctas: {correct_answers}")
            st.write(f"❌ Incorrectas: {len(wrong_answers)}")

            if wrong_answers:
                if st.button("Repetir Fallidas"):
                    st.session_state.current_index = 0
                    st.session_state.correct_answers = 0
                    st.session_state.wrong_answers = []
                    st.experimental_rerun()

if __name__ == "__main__":
    main()
