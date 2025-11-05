import streamlit as st
import time
import os

# 1.Buttons
# Judul Aplikasi
st.title("Demo Tombol di Streamlit")

# Membuat Tombol
if st.button("Klik di Sini"):
    st.success("Kamu telah menekan tombol ✅")
else:
    st.info("Kamu belum menekan tombol.")

# 2. Radio Buttons
st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others')
)

if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

# 3. Check Boxes
st.title('Creating Checkboxes')
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# 4. Drop-Downs
st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
                     ('Books', 'Movies', 'Sports'))

# 5. Multiselects
st.title('Multi-Select')

# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

# 6. Download Buttons
st.title("Download Button Example")

# Pastikan file yang akan diunduh ada dan memiliki path yang benar
file_path = os.path.join(os.path.dirname(__file__), "files/avocado.csv")

try:
    # Buka file dalam mode 'read binary' ("rb") dan gunakan dalam tombol
    with open(file_path, "rb") as file:
        st.download_button(
            label="Download CSV Data",
            data=file,
            file_name='data_avocado.csv',
            mime='text/csv',  # MIME type untuk CSV
        )
except FileNotFoundError:
    st.error(f"File tidak ditemukan di: {file_path}. Pastikan struktur folder sudah benar.")

# 7. Progress Bars
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

# 8. Spinners
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')