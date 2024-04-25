import streamlit as st
from pathlib import Path
import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt
import squarify
import numpy as np


# Function to create a connection to Snowflake
def create_snowflake_connection():
    snowflake_credentials = st.secrets["connections"]["snowpark"]
    conn = snowflake.connector.connect(
        user=snowflake_credentials["user"],
        password=snowflake_credentials["password"],
        account=snowflake_credentials["account"],
        warehouse=snowflake_credentials["warehouse"],
        database=snowflake_credentials["database"],
        schema=snowflake_credentials["schema"],
        role=snowflake_credentials["role"],
    )
    return conn


# Function to execute a query in Snowflake
def query_snowflake(sql_query):
    conn = create_snowflake_connection()
    # print(conn)
    try:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result_set = cursor.fetchall()
        return result_set
    finally:
        cursor.close()
        conn.close()


# Function to convert query results to a Pandas DataFrame
def get_dataframe_from_query(sql_query):
    # print(sql_query)
    data = query_snowflake(sql_query)
    df = pd.DataFrame(data)
    return df


# Streamlit app
def main():
    st.title("OAG DATASET-Snowflake Data Analytics	:chart:")

    tab1, tab2, tab3 = st.tabs(
        [
            "Busiest Airport(Incoming Flights) :people_holding_hands:",
            "Top 5 Airports hourly analysis :airplane_arriving:",
            "Fuel Consumption- Aircraft Type :fuelpump:",
        ]
    )
    with tab1:
        # Sample SQL query - replace with your actual query
        sql_query = """SELECT
    AIRPORTCODE,
    ARRIVALFLIGHTCOUNT,
    DEPARTUREFLIGHTCOUNT,
    RANK
FROM (
    SELECT
        AIRPORTCODE,
        ARRIVALFLIGHTCOUNT,
        DEPARTUREFLIGHTCOUNT,
        RANK() OVER (ORDER BY (ARRIVALFLIGHTCOUNT + DEPARTUREFLIGHTCOUNT) DESC) AS RANK
    FROM
        HOL_DB.PUBLIC.RANKEDAIRPORTS
) AS RankedAirports
WHERE
    RANK <= 10;

                        """

        url3 = "https://www.afar.com/magazine/busiest-airports-in-the-us"
        st.markdown(f"[Busiest Airport in US]({url3})")

        # Fetch data and convert to DataFrame
        df = get_dataframe_from_query(sql_query)
        df.columns = [
            "Airport IATA Code",
            "Arrival Flight Count",
            "Departure Flight Count",
            "Rank",
        ]
        st.dataframe(df)
        # Number of bars
        n_bars = len(df)
        index = np.arange(n_bars)

        # Bar width
        bar_width = 0.35

        # Plotting
        plt.figure(figsize=(10, 8))

        # Creating bars for arrival and departure flight counts
        plt.barh(
            index,
            df["Arrival Flight Count"],
            bar_width,
            label="Arrival Flight Count",
            color="blue",
        )
        plt.barh(
            index + bar_width,
            df["Departure Flight Count"],
            bar_width,
            label="Departure Flight Count",
            color="green",
        )

        plt.ylabel("Airport IATA Code")  # Y-axis represents the airport codes
        plt.xlabel("Flight Count")  # X-axis represents the number of flights
        plt.title("Flight Counts by Airport (Arrivals and Departures)")
        plt.yticks(index + bar_width / 2, df["Airport IATA Code"])
        plt.legend()

        # Invert y-axis for better readability
        plt.gca().invert_yaxis()

        # Display the plot
        st.pyplot(plt)

    with tab2:
        st.title("Airport hourly analysis(Incoming Flights)")
        airport_codes = ["ATL", "ORD", "LAX", "JFK", "DFW"]
        # Create a dropdown menu for airport codes
        selected_airport = st.selectbox("Select an Airport:", airport_codes)

        if st.button("Get Analytics"):
            sql_query2 = f"""
                                select HOUROFDAY, ARRIVALFLIGHTCOUNT, DEPARTUREFLIGHTCOUNT    
            from rankedhours_dr where arrival_iata_airport_code = '{selected_airport}'
                                    """

            # # Fetch data and convert to DataFrame
            df2 = get_dataframe_from_query(sql_query2)
            df2.columns = [
                "Hour [0-23]",
                "Arrival Flight Count",
                "Departure Flight Count",
            ]
            st.dataframe(df2)
            # print(df2)

            # First, sort your DataFrame by hour
            df2 = df2.sort_values(by="Hour [0-23]")

            # Plot setup
            plt.figure(figsize=(12, 6))

            # Plotting the number of incoming flights
            plt.plot(
                df2["Hour [0-23]"],
                df2["Arrival Flight Count"],
                marker="o",
                linestyle="-",
                color="b",
                label="Incoming Flights",
            )

            # Plotting the number of departing flights
            plt.plot(
                df2["Hour [0-23]"],
                df2["Departure Flight Count"],
                marker="o",
                linestyle="-",
                color="r",
                label="Departing Flights",
            )

            # Setting x-axis labels for every hour
            plt.xticks(range(0, 24), [f"{i}" for i in range(24)])

            # Adding labels and title
            plt.xlabel("Hour of the Day")
            plt.ylabel("Number of Flights")
            plt.title("Hourly Traffic (Arrivals and Departures)")

            # Adding grid and legend
            plt.grid(True)
            plt.legend()

            # Display the plot in Streamlit
            st.pyplot(plt)

    with tab3:
        sql_query3 = """
                        SELECT
    EQUIPMENT_CD_ICAO,
    AVG(AVG_EMISSIONS_PER_SEAT) AS AVG_EMISSIONS_PER_GROUP
FROM
    HOL_DB.PUBLIC.EMISSIONPERSEAT
GROUP BY
    EQUIPMENT_CD_ICAO
ORDER BY
    AVG_EMISSIONS_PER_GROUP DESC
LIMIT 5;
                        
                        """
        df3 = get_dataframe_from_query(sql_query3)
        df3.columns = ["PLANE MODEL", "AVG EMISSIONS"]
        st.dataframe(df3)

        plt.figure(figsize=(10, 6))
        plt.bar(df3["PLANE MODEL"], df3["AVG EMISSIONS"], color="skyblue")
        plt.xlabel("Plane Model")
        plt.ylabel("Average Emissions")
        plt.title("Top 5 Plane Models by Average Emissions")
        plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

        # Display the plot in Streamlit
        st.pyplot(plt)

        st.write("Supporting Articles")
        url1 = "https://www.aeroinside.com/17523/lufthansa-a346-at-boston-on-nov-8th-2022-and-nov-9th-2022-returned-twice-due-to-engine-trouble"
        url2 = "https://www.google.com/search?q=a340+problem&sca_esv=583240805&rlz=1C1ONGR_enIN974IN974&sxsrf=AM9HkKk_usunicDN2tZeEu7Pd6Io23lZWQ%3A1700198819305&ei=o_lWZYWjEvKmptQP2dSu4AQ&ved=0ahUKEwjFgLCVpsqCAxVyk4kEHVmqC0wQ4dUDCBA&uact=5&oq=a340+problem&gs_lp=Egxnd3Mtd2l6LXNlcnAiDGEzNDAgcHJvYmxlbTIFEAAYgAQyBhAAGBYYHjIGEAAYFhgeMgsQABiABBiKBRiGAzILEAAYgAQYigUYhgMyCxAAGIAEGIoFGIYDMgsQABiABBiKBRiGAzILEAAYgAQYigUYhgNItzJQpgpYty9wAXgBkAEAmAHbAaABgAuqAQYxNS4xLjG4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIIEAAYgAQYogTCAgYQABgHGB7CAgQQABgewgIGEAAYBRgewgIKEAAYCBgHGB4YD8ICCxAAGIAEGIoFGJECwgIEECMYJ8ICChAAGIAEGBQYhwLCAgsQABiABBixAxiDAeIDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp"
        st.markdown(f"[A346 Engine Problem]({url1})")
        st.markdown(f"[A343 Fuel Consumption Problem]({url2})")


if __name__ == "__main__":
    main()
