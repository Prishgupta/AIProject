from dotenv import load_dotenv  
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


## configure API key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to load Google Gemini Model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retrive query from the SQL database 
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define the prompt for the Gemini model
prompt = [
    """
    You are an expert in converting English language queries into SQL queries. 
    Your task is to generate an SQL query based on the given English-language query.
    Also show the SQL quesry generate at the back end.
    
    **Database Schema:**
    The database contains a table named `student` with the following columns:
    - `name`
    - `class`
    - `section`
    - `roll_no`
    - `marks`
    
    **Examples:**  
    1. **Input:** "How many entries of records are present?"  
       **Output:** `SELECT COUNT(*) FROM student;`
       
    2. **Input:** "Tell me all the students studying in the Data Science class."  
       **Output:** `SELECT * FROM student WHERE class = 'Data Science';`
    
    **Instructions:**  
    - Generate only the SQL query as output.
    - Show the SQL query generated at the back end.
    - Do not include SQL syntax highlighting markers (e.g., triple backticks).
    - Do not include the word "SQL" in the output.
    """
]



## Streamlit app

st.set_page_config(page_title="SQL Query Generator")
st.header("SQL Query Generator")

question=st.text_input("Input:", key="input")
submit=st.button("Ask the question")

## Check if the submit button is clicked

if submit:
    response = get_gemini_response(question, prompt)  # Function to generate SQL query

    # Display the generated SQL query
    st.subheader("Generated SQL Query")
    st.code(response, language="sql")  

    # Fetch records from the database
    data = read_sql_query(response, "student.db")

    st.subheader("Retrieved Records")
    if data:
        for row in data:
            st.header(row)  # Displays each row properly
    else:
        st.header("No records found.")

    

    