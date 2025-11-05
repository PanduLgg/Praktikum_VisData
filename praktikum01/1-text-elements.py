import streamlit as st
st.title("Text Elements in Streamlit")
st.header("Text Elements Header in Streamlit")
st.subheader("This is a Subheader")
st.text("This is a simple text element.")
st.markdown("### This is a Markdown Header")
st.markdown("You can also use **Bold** and *Italic*")
st.caption("This is a caption text.")

# MANDIRI
st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 1: Text Elements")
st.markdown("""
1. Pandu Linggar - 0110220217
2. Rizky Amalia - 0110220218
3. Salsabila Putri - 0110220222
""")

#Rumus LaTeX
st.header("Rumus LaTeX")
st.latex(r'''a^2 + b^2 = c^2''')
st.latex(r'''e^{i\pi} + 1 = 0''')
st.latex(r'''\frac{d}{dx}e^x = e^x''')
st.latex(r'''\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}''')
st.latex(r'''\lim_{x \to 0} \frac{\sin x}{x} = 1''')
st.latex(r'''\sqrt{a^2 + b^2} = c''')
st.latex(r'''\cos^2 \theta + \sin^2 \theta = 1''')
st.latex(r'''E = mc^2''')
st.latex(r'''\int_a^b f(x)dx = F(b) - F(a)''')

#Menampilkan kode Program
st.header("Menampilkan Kode Program")
st.subheader("Kode Python Sederhana")

code = '''
def hello():
    print("Hello, Streamlit!")
'''

st.code(code, language='python')

st.subheader("Kode JavaScript Sederhana")
js_code = '''
function greet() {
    console.log("Hello, Streamlit!");
}
greet();
'''
st.code(js_code, language='javascript')

st.subheader("Kode HTML Sederhana")
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Hello Streamlit</title>
</head>
<body>
    <h1>Hello, Streamlit!</h1>
</body>'''

st.code(html_code, language='html')

st.subheader("Kode Java Sederhana")
st.code("""
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Streamlit!");
    }
}
""", language='java')
