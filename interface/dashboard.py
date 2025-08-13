import streamlit as st
from src.main import PinCode, RandomPassword, MemorablePasswordGenarator

st.image('./image/banner.jpeg', width=400)
st.title(":zap: Password Generator")


option=st.radio(
    'Select a password generator',  
    ('Pin Code', 'Random Password', 'Memorable Password')
)

if option ==('Pin Code'):
    length = st.slider('please select the lengt of your pincode', 8, 32, 0)

    genarator = PinCode(length)
elif option == ('Random Password'):
     length = st.slider('please select the lengt of your pincode', 8, 32, 0)
     symbol = st.toggle('Include Symbols:')
     number = st.toggle("Include Numbers") 
     genarator = RandomPassword(length, symbol, number)

else:
      num_of_word = st.slider('please select the lengt of your pincode', 4, 8)
      capital = st.toggle('Capitalized')
      separator = st.selectbox('seperator', ['-', ',', '|'])

      genarator=MemorablePasswordGenarator(num_of_word, capital, separator, codex=None)
     
if st.button('`show me my password`'):
    password = genarator.generate()
    st.write(f'your password is `{password}`')

