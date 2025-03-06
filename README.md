Aquí tienes un README profesional para tu proyecto Streamlit:

```markdown
# Quiz App - Aplicación Interactiva de Preguntas y Respuestas

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://typetest.streamlit.app/)

Aplicación web interactiva para crear y resolver cuestionarios personalizados, con seguimiento de progreso y repaso de preguntas fallidas.

## Características Principales 🚀

- **Subida de archivos TXT** con formato personalizado
- **Navegación entre páginas** (Inicio/Quiz)
- **Sistema de puntuación en tiempo real**
- **Repaso de preguntas fallidas**
- **Interfaz intuitiva** con sidebar de progreso
- **Modo de reinicio configurable** (Completo/Solo errores)
- **Validación automática** de respuestas
- **Feedback inmediato** con explicaciones

## Formato del Archivo de Preguntas 📝

Crea un archivo `.txt` con este formato:

```
¿Cuál es la capital de Francia?
a) Lyon
b) Marsella
c) París
d) Burdeos
e) Toulouse
-C

¿2 + 2 = ?
a) 1
b) 3
c) 4
d) 5
e) 6
-C
```

## Instalación y Uso ⚙️

1. **Clona el repositorio**:
```
git clone https://github.com/Mirgc/typetest.git
cd quiz-app
```

2. **Instala dependencias**:
```
pip install -r requirements.txt
```

3. **Ejecuta la aplicación**:
```
streamlit run app.py
```

4. **Sube tu archivo TXT** y ¡comienza el quiz!

## Estructura del Proyecto 📂
```
.
├── app.py             # Código principal de la aplicación
├── requirements.txt   # Dependencias del proyecto
├── README.md          # Documentación
└── examples/          # Ejemplos de cuestionarios
    └── sample_quiz.txt
```

## Tecnologías Utilizadas 💻
- **Python 3.9+**
- **Streamlit** (Interfaz web)
- **Re** (Procesamiento de texto)
- **OS** (Gestión de archivos)

## Licencia 📄
Este proyecto está bajo licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

```