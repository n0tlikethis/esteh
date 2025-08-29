import streamlit as st

st.set_page_config(layout="centered", page_title="Fibonacci", page_icon="🧬")

st.title("🧬 Fibonacci")

st.markdown(
    "Masukkan nilai `n` untuk menghasilkan deret Fibonacci sebanyak `n` angka pertama."
)


def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


n = st.number_input("Nilai `n`", min_value=1, max_value=1000, value=10, step=1)

fibonacci_sequence = generate_fibonacci(n)

st.caption(f"Deret Fibonacci ({n} angka):")
st.code(", ".join(map(str, fibonacci_sequence)))
