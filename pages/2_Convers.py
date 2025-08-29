import streamlit as st

st.set_page_config(layout="centered", page_icon="🪄", page_title="Convers")

st.title("🪄 Convers")

st.markdown(
    "Konversi suhu yang menerima suatu nilai dalam satuan Celsius, Reaumur, & Fahrenheit kemudian dapat dikonversi ke satuan yang berbeda."
)

units = {
    "°C": "Celsius",
    "°R": "Reaumur",
    "°F": "Fahrenheit",
}

def convert_temperature(value, from_unit, to_unit):
    from_unit = units[from_unit]
    to_unit = units[to_unit]

    if from_unit == to_unit:
        return value

    # convert to celcius first
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Reaumur":
        celsius = value * 5 / 4
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9

    # then convert to another
    if to_unit == "Celsius":
        return celsius
    elif to_unit == "Reaumur":
        return celsius * 4 / 5
    elif to_unit == "Fahrenheit":
        return celsius * 9 / 5 + 32

# state init
for key in ["unit_a", "unit_b", "temp_a", "temp_b"]:
    if key not in st.session_state:
        if key == "unit_a":
            st.session_state[key] = "°C"
        elif key == "unit_b":
            st.session_state[key] = "°R"
        else:
            st.session_state[key] = 0.0

# callback function
def update_val():
    try:
        st.session_state.temp_b = convert_temperature(
            st.session_state.temp_a,
            st.session_state.unit_a,
            st.session_state.unit_b
        )
    except Exception:
        pass

col1, col2 = st.columns(2)

with col1:
    st.number_input(
        "Nilai suhu awal",
        key="temp_a",
        on_change=update_val,
    )

    st.segmented_control(
        "Satuan awal",
        options=units.keys(),
        selection_mode="single",
        key="unit_a",
        on_change=update_val,
    )

with col2:
    st.number_input(
        "Nilai suhu akhir",
        key="temp_b",
        disabled=True,
    )

    st.segmented_control(
        "Satuan akhir",
        options=units.keys(),
        selection_mode="single",
        key="unit_b",
        on_change=update_val,
    )

if not st.session_state.unit_a or not st.session_state.unit_b:
    st.info("Pilih satuan terlebih dahulu!", icon=":material/info:")
