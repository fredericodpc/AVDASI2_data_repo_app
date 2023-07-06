import numpy                as np
import datetime
import streamlit            as st
import base64
# import pandas               as pd
# import plotly.express       as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
from PIL import Image
from streamlit_option_menu import option_menu



# ############################################################################
# ############################################################################
# ############################################################################


with st.sidebar:
    choose = option_menu("AVDASI 2", ["Version Control", "Company A", "Company B"],
                         icons=['git', 'airplane-engines', 'airplane-engines-fill'],
                         menu_icon="app-indicator", default_index=0,
                        )     
                         
                         # styles={
        # "container": {"padding": "5!important", "background-color": "#fafafa"},
        # "icon": {"color": "orange", "font-size": "25px"}, 
        # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        # "nav-link-selected": {"background-color": "#02ab21"},
    # }

    
    
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# # ############################################################################
# # ############################################################################
# # ############################################################################


if choose == "Version Control":
    st.title("AVDASI 2 Version Control System")    
    
    st.header("How to submit your files")
    st.info("")
    st.header("GIT cheat sheet")
    st.info("Copy your company's repository to your local machine.")
    st.code('''git clone <repo name>''', language='c')
    st.info("Check which files exist in your remote repository.")
    st.code('''git status''', language='c')
    st.info("Add a file to the staging area.")
    st.code('''git add <file name>''', language='c')
    st.info("Commit the changes existing in files sent to the stage area.")
    st.code('''git commit -m "<message>"''', language='c')
    st.info("Create a new branch (tab)")
    st.code('''git branch <branch name>''', language='c')
    st.info("Switch to a different branch (tab)")
    st.code('''git checkout <branch name>''', language='c')
    st.info("Send the committed changes to the respective branch in the remote repository.")
    st.code('''git push''', language='c')




    
    
    st.info("Accepted file types: .csv, .txt., .png/.jpeg, .pdf")

    
    
    
    
    
    
elif choose == "Company A":
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Aerodynamics", "Structures", "Avionics", "Testing", "Project Management", "Reports", "CAD/Drafts/Prototypes"])
    
    with tab4:
        st.subheader("Port Wing Assembly")
        st.divider()
        st.subheader("Starboard Wing Assembly")
        st.divider()
        st.subheader("Fuselage Assembly")
        st.divider()
        st.subheader("Wing Bench Test")
        st.divider()
        st.subheader("Fuselage Bench Test")
        st.divider()
        st.subheader("UAV Bench Test")
        st.divider()
        st.subheader("Wind Tunnel Test")
        st.divider()
        st.subheader("Dynamics Test Test")
        st.divider()
    
    # column1, column2 = st.columns([1,1])
    
    




elif choose == "Company B":
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Aerodynamics", "Structures", "Avionics", "Testing", "Project Management", "Reports", "CAD/Drafts/Prototypes"])
    
    with tab1:
        show_pdf('pdf_example.pdf')
    
    with tab3: 
        image = Image.open('teaching_support_team.png')
        st.image(image, caption='Teaching Support Team')


    with tab4:
        st.subheader("Port Wing Assembly")
        st.divider()
        st.subheader("Starboard Wing Assembly")
        st.divider()
        st.subheader("Fuselage Assembly")
        st.divider()
        st.subheader("Wing Bench Test")
        st.divider()
        st.subheader("Fuselage Bench Test")
        st.divider()
        st.subheader("UAV Bench Test")
        st.divider()
        st.subheader("Wind Tunnel Test")
        st.divider()
        st.subheader("Dynamics Test Test")
        st.divider()





    






