import streamlit as st

st.title('Simple Streamlit App')
st.write('Hello, welcome to my first Streamlit app!')

if st.button('Click me'):
    st.write('Button clicked!')
    
    
selectbox = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])