import pandas as pd
import streamlit as st
import numpy as np
#st.title("Largest Number Searching App")
#st.latex(''' This\ app\ help\ you\ to\ find\ largest \ Number ''')
#st.markdown(""" 
### Enter First Number
### Enter Second Number
### Enter Third Number
#:moon:<br>
#:sunglasses: """, True)
#def Find_largest_Number(numbers):
def find_largest_number(Numbers):
    if len(Numbers)==0:
        return None
    else:
        return max(Numbers)
    
def main():
    st.title("Largest Number Searching App")
    st.latex(''' This\ app\ help\ you\ to\ find\ largest \ Number ''')

    num_count = st.number_input("How many number do you want to enter?" , min_value= 1,step = 1)

    Numbers=[]
    for i in range (num_count):
        number = st.number_input(f" Enter the Number {i+1} : ")
        Numbers.append(number)
    if len(Numbers)> 0:
        largest_number = find_largest_number(Numbers)
        st.latex(f"The \ Largest \ Number \ is : {largest_number}")
        st.markdown('''
         ### Absolutly correct <br> :sunglasses:
        ''' ,True)
    else:
        st.write('''Please Enter Valid Number.''')

if __name__ == "__main__":
    main()

