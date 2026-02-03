import streamlit as st

st.title("Formulario de matricula estudiantil")

nombre = st.text_input("Nombre del estudiante")
cedula = st.text_input("Numero de cedula")

clase = st.selectbox(
    "Seleccione la clase",
    [
        "Seleccione una opcion",
        "Matematicas",
        "Programacion",
        "Base de datos",
        "Redes de computadoras",
        "Diseno web",
        "Ingles tecnico",
        "Sistemas operativos"
    ]
)

maestro = st.selectbox(
    "Seleccione maestro",
    [
        "Seleccione una opcion",
        "Carlos Perez",
        "Ana Rodriguez",
        "Norman Cubilla",
        "Jose Martinez",
        "Laura Gomez",
        "Miguel Sanchez",
        "Patricia Lopez",
        "Edwin Sanders"
    ]
)

aula = st.text_input("Numero de aula")

horario = st.selectbox(
    "Horario",
    ["Seleccione una opcion", "Manana", "Tarde", "Noche"]
)

creditos = st.number_input(
    "Numero de creditos",
    min_value=0,
    max_value=6,
    step=1
)

modalidad = st.selectbox(
    "Modalidad",
    ["Seleccione una opcion", "Presencial", "Virtual", "Hibrida"]
)

comentarios = st.text_area("Comentarios adicionales (opcional)")

if st.button("Registrar matricula"):

    if nombre == "":
        st.warning("Debe ingresar el nombre del estudiante")

    elif cedula == "":
        st.warning("Debe ingresar la cedula del estudiante")

    elif clase == "Seleccione una opcion":
        st.warning("Debe seleccionar una clase")

    elif maestro == "Seleccione una opcion":
        st.warning("Debe seleccionar un maestro")

    elif aula == "":
        st.warning("Debe ingresar el numero de aula")

    elif horario == "Seleccione una opcion":
        st.warning("Debe seleccionar un horario")

    elif creditos == 0:
        st.warning("Debe ingresar una cantidad de creditos valida")

    elif modalidad == "Seleccione una opcion":
        st.warning("Debe seleccionar una modalidad")

    else:
        st.write("### Datos de matricula registrados:")
        st.write(f"Estudiante: {nombre}")
        st.write(f"Cedula: {cedula}")
        st.write(f"Clase: {clase}")
        st.write(f"Maestro: {maestro}")
        st.write(f"Aula: {aula}")
        st.write(f"Horario: {horario}")
        st.write(f"Creditos: {creditos}")
        st.write(f"Modalidad: {modalidad}")

        if comentarios != "":
            st.write(f"Comentarios: {comentarios}")

        st.success("Matricula registrada con exito")
