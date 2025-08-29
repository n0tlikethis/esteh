import streamlit as st

st.set_page_config(layout="centered", page_icon="🧮", page_title="Calc-a-lator")

st.title("🧮 Calc-a-lator")

st.markdown("Kalkulator sederhana yang menerima 2 operand & dapat dipilih operatornya lalu dapat menampilkan hasil perhitungannya.")

operators = {
    0: ":material/add:",
    1: ":material/remove:",
    2: ":material/close:",
    3: ":material/go_to_line:",
}

operator_funcs = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: x / y,
}

col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input("Angka pertama", value=0, step=1)

with col2:
    n2 = st.number_input("Angka kedua", value=0, step=1)

selection = st.segmented_control(
        "Operator",
        options=operators.keys(),
        format_func=lambda option: operators[option],
        selection_mode="single",
        default=0,
    )

if selection is None:
    st.info("Pilih operator terlebih dahulu!", icon=":material/info:")
elif selection == 3 and n2 == 0:
    st.info("Angka tidak bisa dibagi dengan nol!", icon=":material/info:")
elif n1 is not None or n2 is not None:
    result = operator_funcs.get(selection)(n1, n2)
    # st.number_input("Hasil", value=result, disabled=True)
    st.success(f"Hasilnya adalah {result}", icon=":material/arrow_circle_right:")

