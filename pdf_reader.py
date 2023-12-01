import streamlit as st 
import fitz

def main(): 
    st.title("Upload PDF") 
    pdf = st.file_uploader("Upload your PDF", type="pdf") 
    if pdf: 
        doc = fitz.open(stream=pdf.read(), filetype="pdf")

        for page_num in range(doc.page_count):
            page = doc[page_num]
            text_blocks = page.get_text("blocks")
            st.write(page.get_text("blocks"))
            # for block in text_blocks:
            #     if block != "":
            #         st.write(block)
            #st.write(text)

        doc.close()
            
if __name__ == '__main__': 
    main() 