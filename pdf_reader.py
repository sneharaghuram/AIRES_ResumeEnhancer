import streamlit as st 
import fitz
    

def main(): 
    st.title("Upload PDF") 
    pdf = st.file_uploader("Upload your PDF", type="pdf") 
    if pdf: 
        doc = fitz.open(stream=pdf.read(), filetype="pdf")
        st.write(doc) 
        doc.close()
            
if __name__ == '__main__': 
    main() 