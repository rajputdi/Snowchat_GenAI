import streamlit as st
from db_team4 import snowflake as db
from db_team4.snowflake import *
from langchain_integration.query_generator import generate_sql_query


def main():
    display_snowflake_tables_tab()


def display_snowflake_tables_tab():
    st.title(":robot_face: SQL Query Chatbot-Snowflake :snowflake:")

    if "generated_sql" not in st.session_state:
        st.session_state["generated_sql"] = ""

    # Try to access a nested secret to see if it throws an error
    try:
        user = st.secrets["connections"]["snowpark"]["user"]
        # st.write("Successfully accessed secrets")
    except Exception as e:
        st.error(f"Error accessing secrets: {e}")

    # Button to retrieve table names from Snowflake
    if st.button("Retrieve Table Names :page_facing_up:"):
        try:
            # Access the Snowflake connection details directly here
            snowflake_secrets = st.secrets["connections"]["snowpark"]
            # Call the function and pass the retrieved secrets

            table_names = db.get_table_names(snowflake_secrets)

            st.session_state["table_names"] = table_names
            st.success("Table names retrieved!")
        except Exception as e:
            st.error(f"Error retrieving tables: {e}")

    if "table_names" in st.session_state:
        selected_tables = st.multiselect(
            "Select tables", st.session_state["table_names"]
        )
        st.session_state["selected_tables"] = selected_tables

        if st.button("Get Tables Schema"):
            if not selected_tables:  # Check if the list is empty
                st.warning("Please select at least one table.")
            else:
                try:
                    snowflake_secrets = st.secrets["connections"]["snowpark"]
                    print(selected_tables)
                    schema_details = db.get_table_schema(
                        snowflake_secrets, selected_tables
                    )
                    with st.expander("View Schema Details"):
                        st.text_area("Schema:", schema_details, height=300)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        if "sql_chat_messages" not in st.session_state:
            st.session_state["sql_chat_messages"] = [
                {"role": "assistant", "content": "How can I help you with SQL queries?"}
            ]

        # Display chat messages
        for msg in st.session_state["sql_chat_messages"]:
            role, content = msg["role"], msg["content"]
            st.chat_message(role).write(content)

        # User input for SQL query
        sql_query_input = st.chat_input("Enter your query to generate SQL")
        if sql_query_input:
            process_sql_query(sql_query_input)

        # Rest of the code for SQL query execution...
        user_sql_query = st.sidebar.text_area("Enter your SQL Query", height=100)

        # Button to execute the SQL query
        if st.sidebar.button("Execute SQL"):
            snowflake_secrets = st.secrets["connections"]["snowpark"]
            if user_sql_query:
                try:
                    # Execute the SQL query and get the results as a dataframe
                    df = execute_query(snowflake_secrets, user_sql_query)

                    # Display the results as a dataframe
                    st.sidebar.dataframe(df)
                except Exception as e:
                    st.error(f"An error occurred while executing SQL: {e}")
            else:
                st.warning("Please enter a SQL query first.")


def process_sql_query(user_input):
    """
    Process the user's input to generate SQL and update the chat history.
    """
    try:
        # Retrieve OpenAI API key from Streamlit's secrets
        openai_api_key = st.secrets["openai_api_key"]
        tables = st.session_state["selected_tables"]
        print(tables)
        # Generate SQL query
        generated_sql = generate_sql_query(user_input, tables)
        st.session_state["generated_sql"] = generated_sql

        # Update chat history with user query and generated SQL
        st.session_state["sql_chat_messages"].append(
            {"role": "user", "content": user_input}
        )
        st.session_state["sql_chat_messages"].append(
            {"role": "assistant", "content": f"Generated SQL: {generated_sql}"}
        )
        st.experimental_rerun()
    except Exception as e:
        st.session_state["sql_chat_messages"].append(
            {
                "role": "assistant",
                "content": f"Chatbot cannot help you. Reason: Asked Irrelevant Question/Tables not chosen/Token Length exceeded",
            }
        )
        st.experimental_rerun()


if __name__ == "__main__":
    main()
