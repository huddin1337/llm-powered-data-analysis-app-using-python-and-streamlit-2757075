import streamlit as st
import pandas as pd

st.set_page_config (
  page_title="Ask-Bot",
  page_icon="❓",
  layout="wide"
)

# Session state 
#storeing messages in a list
if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("🖥️ Huddin1337 CSV Bot")
st.markdown("Upload your CSV file and ask questions about your data in plain English! Powered by OpenAI's GPT-4.")

## Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload Your CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    

    if uploaded_file:
      df = pd.read_csv(uploaded_file)
      st.session_state.df = df  # Store the DataFrame in session state for later use

      st.success(f"✅ {uploaded_file.name} uploaded successfully!")
      # Here you would add code to read the CSV and prepare it for analysis

      ##Data Preview
      with st.expander(f"📊 {uploaded_file.name}"):
         st.dataframe(df)  

      with st.expander("💡Data Properties"):
        col1, col2 = st.columns(2)
        with col1:
              st.metric("Rows", df.shape[0])  
              st.metric("Columns", df.shape[1])
        with col2:
              st.metric("Missing Values", df.isnull().sum().sum())  
              st.metric("Unique Values", df.nunique().sum())
      
    else:
      st.info("👆 Please upload a CSV file to get started.")


#main chat interface
if st.session_state.df is not None:
    # display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    #chat input
    st.chat_input("Ask a question about your data...")

    
else:
    #no data uploaded
