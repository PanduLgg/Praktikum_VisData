import streamlit as st
import datetime
import pandas as pd

# 1. Text Box
st.title("Text Box")
# Creating Text box with 10 as character limit
name = st.text_input("Enter your Name", max_chars=10)
password = st.text_input("Enter your password", type='password')

# 2. Text Area
# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""",input_text)

# 3. Number Input
# Create number input
st.number_input("Enter your Number")
# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

# 4. Time
st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

# 5. Date
st.title("Date")
# Defining Date Function
st.date_input("Select Date")
st.title("Date")
# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

# 6. Color
st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

# 7. Dataset Upload
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# 8. Submit Button
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)