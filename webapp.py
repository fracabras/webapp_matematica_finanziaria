import streamlit as st

st.title("Calcolatore di Matematica Finanziaria")

modalita = st.radio(
    "Modalità inserimento tasso",
    ["Decimale (0.05)", "Percentuale (5%)"]
)

usa_percentuale = modalita == "Percentuale (5%)"

tipo_tasso = st.selectbox(
    "Tipo di tasso",
    ["Effettivo", "Nominale"]
)

def converti(val):
    return val / 100 if usa_percentuale else val

if tipo_tasso == "Effettivo":
    i_input = st.number_input(
        "i effettivo nel periodo di composizione", 
        value=5.0 if usa_percentuale else 0.05,
        step=0.01 if usa_percentuale else 0.0001,
        format="%.4f"
    )
    i = converti(i_input)

else:
    r_input = st.number_input(
        "tasso nominale r", 
        value=5.0 if usa_percentuale else 0.05,
        step=0.01 if usa_percentuale else 0.0001,
        format="%.4f"
    )
    m = st.number_input("Numero di composizioni m", value=1, step=1)
    I = st.number_input("I durata periodo temporale", value=1.0, format="%.4f")

    r = converti(r_input)
    i = (1 + r/m)**(m*I) - 1

    if usa_percentuale:
        st.write(f"Tasso effettivo calcolato: **{i*100:.4f}%**")
    else:
        st.write(f"Tasso effettivo calcolato: **{i:.4f}**")

n = st.number_input("Orizzonte investimento (n)", value=1, step=1)

if i != 0:
    F_P = (1 + i)**n
    P_F = 1 / (1 + i)**n
    A_P = (i * (1 + i)**n) / ((1 + i)**n - 1) if n > 0 else 0
    P_A = ((1 + i)**n - 1) / (i * (1 + i)**n) if n > 0 else 0
    F_A = ((1 + i)**n - 1) / i if n > 0 else 0
    A_F = i / ((1 + i)**n - 1) if n > 0 else 0
else:
    F_P = P_F = A_P = P_A = F_A = A_F = 0

st.subheader("Fattori")
col1, col2 = st.columns(2)
with col1:
    st.write(f"F/P = **{F_P:.4f}**")
    st.write(f"P/F = **{P_F:.4f}**")
    st.write(f"A/P = **{A_P:.4f}**")
with col2:
    st.write(f"P/A = **{P_A:.4f}**")
    st.write(f"F/A = **{F_A:.4f}**")
    st.write(f"A/F = **{A_F:.4f}**")

st.divider()
inc = st.selectbox("Grandezza da calcolare", ["P", "F", "A"])
nota = st.selectbox("Grandezza nota", ["P", "F", "A"])

if inc == nota:
    st.error("La grandezza da calcolare deve essere diversa da quella nota.")
else:
    val = st.number_input(f"Inserisci valore di {nota}", value=100.0, format="%.4f")

    risultato = None
    formula = ""

    if inc == "F":
        if nota == "P":
            risultato = val * F_P
            formula = "F = P \\cdot (F/P,\\; i,\\; n)"
        elif nota == "A":
            risultato = val * F_A
            formula = "F = A \\cdot (F/A,\\; i,\\; n)"

    elif inc == "P":
        if nota == "F":
            risultato = val * P_F
            formula = "P = F \\cdot (P/F,\\; i,\\; n)"
        elif nota == "A":
            risultato = val * P_A
            formula = "P = A \\cdot (P/A,\\; i,\\; n)"

    elif inc == "A":
        if nota == "P":
            risultato = val * A_P
            formula = "A = P \\cdot (A/P,\\; i,\\; n)"
        elif nota == "F":
            risultato = val * A_F
            formula = "A = F \\cdot (A/F,\\; i,\\; n)"

    if risultato is not None:
        st.subheader("Risultato")
        st.latex(formula)
        st.success(f"**{inc} = {risultato:.4f}**")
