import streamlit as st

st.title("Webapp per matematica finanziaria")

# --- Scelta tasso ---
tipo_tasso = st.selectbox(
    "Tipo di tasso",
    ["Effettivo (i già noto)", "Nominale (calcolo i effettivo)"]
)

if tipo_tasso == "Effettivo (i già noto)":
    i = st.number_input("Inserisci tasso effettivo i", value=0.05)
else:
    r = st.number_input("Tasso nominale r", value=0.05)
    m = st.number_input("Numero di composizioni", value=1)
    I = st.number_input("Durata periodo (anni)", value=1.0)
    i = (1 + r/m)**(m*I) - 1
    st.write(f"Tasso effettivo calcolato: {i:.4f}")

# --- Orizzonte ---
n = st.number_input("Orizzonte investimento (n)", value=1)

# --- Fattori ---
F_P = (1 + i)**n
P_F = 1 / (1 + i)**n
A_P = (i * (1 + i)**n) / ((1 + i)**n - 1) if i != 0 else 0
P_A = ((1 + i)**n - 1) / (i * (1 + i)**n) if i != 0 else 0
F_A = ((1 + i)**n - 1) / i if i != 0 else 0
A_F = i / ((1 + i)**n - 1) if i != 0 else 0

st.subheader("Fattori")
st.write(f"F/P = {F_P:.4f}")
st.write(f"P/F = {P_F:.4f}")
st.write(f"A/P = {A_P:.4f}")
st.write(f"P/A = {P_A:.4f}")
st.write(f"F/A = {F_A:.4f}")
st.write(f"A/F = {A_F:.4f}")

# --- Scelte ---
inc = st.selectbox("Grandezza da calcolare", ["P", "F", "A"])
nota = st.selectbox("Grandezza nota", ["P", "F", "A"])

if inc == nota:
    st.error("Non puoi scegliere la stessa variabile!")
else:
    val = st.number_input(f"Inserisci valore di {nota}", value=100.0)

    risultato = None
    formula = ""

    if inc == "F":
        if nota == "P":
            risultato = val * F_P
            formula = "F = P * (F/P)"
        elif nota == "A":
            risultato = val * F_A
            formula = "F = A * (F/A)"

    elif inc == "P":
        if nota == "F":
            risultato = val * P_F
            formula = "P = F * (P/F)"
        elif nota == "A":
            risultato = val * P_A
            formula = "P = A * (P/A)"

    elif inc == "A":
        if nota == "P":
            risultato = val * A_P
            formula = "A = P * (A/P)"
        elif nota == "F":
            risultato = val * A_F
            formula = "A = F * (A/F)"

    if risultato is not None:
        st.subheader("Risultato")
        st.write(formula)
        st.success(f"{inc} = {risultato:.4f}")