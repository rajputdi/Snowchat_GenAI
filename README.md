# Assignment_04

# Part A:

1. Naman Gupta: [Github Link](https://github.com/naman02602/sfguide-data-engineering-with-snowpark-python)
2. Jagruti Agrawal: [Github Link](https://github.com/Jagruti1906/sfguide-data-engineering-with-snowpark-python)
3. Divyesh Rajput: [Github Link](https://github.com/rajputdi/sfguide-data-engineering-with-snowpark-python)

# Part B:

Link to the application:

[Streamlit](https://wasgwogpfkl5yto2awpmjd.streamlit.app/)

[Codelab](https://codelabs-preview.appspot.com/?file_id=1mfLS9nPQTpeH135d3CkisDhNd843zBflrGr8IP75V3c#0)

[Demo](https://youtu.be/QjffuiWDbpA)

# Problem Statement:

This data engineering project requires a comprehensive approach to effectively leverage Snowflake marketplace datasets for a meaningful use case. The primary challenge is to integrate diverse datasets cohesively. The team collaboratively developed a thematic story around these datasets, defining use cases that addresses a specific problem. This involves programming SQL processes and User Defined Functions to achieve use cases. Git actions has been used for deployment purposes introducing continuous integration and deployment (CI/CD).

The integration of Snowflake with Streamlit adds another layer for the user. The objective is to enable the creation of analytics based on processed data and develop a text-based SQL query feature capable of interpreting user natural language input. This involves retrieving table schema using the Langchain OpenAI service, integrating it into the query prompt for user-friendly interaction. The Streamlit application presents the generated raw SQL code to users, allowing for updates or feedback to the OpenAI API.

Testing the system is imperative, involving the creation of at various test cases. These tests covers scenarios where SQL code generation works seamlessly, where it fails initially but can be corrected with query prompt modifications, and where failures persist despite multiple attempts. The final deployment phase involves deploying the application to a public cloud platform, Streamlit Cloud, ensuring public access. This introduces challenges related to scalability, security, and reliability that need careful consideration to guarantee a successful and user-friendly deployment.

![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/assets/113845871/07555b00-6e04-4f5a-82e0-bcbb60e8f85b)
![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/assets/113845871/b7d7147e-5004-49ae-8551-3ab59a0da150)
![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/assets/113845871/6daa4aac-c6dd-433c-964a-a0a9b5d836bc)
![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/assets/113845871/16ac2730-56b4-4df3-bcc2-d0f7c207bf63)

# Architecture Diagram:

Streamlit Application Flow:
![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/blob/main/Diagrams/streamlit_app_1.png)

Snowflake Flow:
![image](https://github.com/BigDataIA-Fall2023-Team4/Assignment_04/blob/main/Diagrams/snowflake_flow.png)

# Technologies Used:

1. GitHub
2. Python
3. LangChain
4. OpenAI
5. Snowflake
6. Streamlit

# Data Source:
1. [OAG_FLIGHT_EMISSIONS_DATA_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ3D?originTab=databases&database=OAG_FLIGHT_EMISSIONS_DATA_SAMPLE)
2. [OAG_FLIGHT_STATUS_DATA_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ42?originTab=databases&database=OAG_FLIGHT_STATUS_DATA_SAMPLE)
3. [OAG_GLOBAL_AIRLINE_SCHEDULES_SAMPLE](https://app.snowflake.com/lhbewyp/ve70966/#/data/shared/SNOWFLAKE_DATA_MARKETPLACE/listing/GZ1M7Z2MQ39?originTab=databases&database=OAG_GLOBAL_AIRLINE_SCHEDULES_SAMPLE)

# Project Structure:

```
📦 
├─ .github
│  └─ workflows
│     └─ main.yml
├─ .gitignore
├─ README.md
├─ app.py
├─ db_team4
│  ├─ __init__.py
│  └─ snowflake.py
├─ deploy.py
├─ langchain_integration
│  ├─ __init__.py
│  └─ query_generator.py
├─ modules
│  ├─ airport_crowd.sql
│  ├─ carbon_footprint.sql
│  ├─ data_cleaning.sql
│  ├─ emissions_per_seat_udf
│  │  ├─ app.py
│  │  ├─ app.toml
│  │  └─ app.zip
│  ├─ hourly_crowd.sql
│  ├─ load_raw.sql
│  ├─ seat_occupancy.sql
│  ├─ seat_occupancy_udf
│  │  ├─ app.py
│  │  ├─ app.toml
│  │  └─ app.zip
│  ├─ setup_snow.sql
│  ├─ teardown.sql
│  └─ treating_nulls_udf
│     ├─ app.py
│     ├─ app.toml
│     ├─ app.zip
│     └─ requirements.txt
├─ requirements.txt
├─ runsql.py
├─ streamlit_ui
│  ├─ __init__.py
│  ├─ chatbot.py
│  ├─ home.py
│  └─ snowflake_conn.py
└─ utils
   ├─ __init__.py
   └─ snowpark_utils.py
```
©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

# Team Contribution:

| Name            | Contribution % | Contributions |
|-----------------|----------------|---------------|
| Naman Gupta     |     33.3%      |  Dataset Exploration, Use Case building, SQL Processes & UDF Creation, CI-CD pipeline     |
| Jagruti Agrawal |     33.3%      |  Dataset Exploration, Use Case building, SQL Processes & UDF Creation, Architecture development            |
| Divyesh Rajput  |     33.3%      |  Dataset Exploration, Use Case building, Chat-bot development with Langchain & OpenAI          |
