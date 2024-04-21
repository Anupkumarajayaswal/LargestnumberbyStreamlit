import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.latex("Find \the \Largest \ Number \Among \ Given \Three\ Number ")
    st.write(''' This app help you to find largest Number ftom 3 Number  ''')
    
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)
    
    if st.button("Find the largest number"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_number}")
        st.latex(f"The \ Largest \ Number \ is : {largest_number}")
        st.markdown('''
         ### Absolutly correct  you are Genious <br> :sunglasses:
        ''' ,True)

if __name__ == "__main__":
    main()
