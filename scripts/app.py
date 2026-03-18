import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial KPI Dashboard", layout="wide")

st.title("Financial KPI Dashboard")
st.write("Upload a CSV file to explore KPIs, trends, and filtered financial data.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully.")

        st.subheader("Data Preview")
        st.dataframe(df.head())

        st.subheader("Column Selection")

        columns = df.columns.tolist()

        date_col = st.selectbox("Select date column", ["None"] + columns)
        category_col = st.selectbox("Select category column", ["None"] + columns)
        value_col = st.selectbox("Select KPI/value column", columns)

        if date_col != "None":
            df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

        # Sidebar filters
        st.sidebar.header("Filters")

        filtered_df = df.copy()

        if category_col != "None":
            category_options = df[category_col].dropna().unique().tolist()
            selected_categories = st.sidebar.multiselect(
                "Filter by category",
                options=category_options,
                default=category_options
            )
            filtered_df = filtered_df[filtered_df[category_col].isin(selected_categories)]

        # Remove missing values in KPI column
        filtered_df = filtered_df.dropna(subset=[value_col])

        st.subheader("KPI Summary")

        total_value = filtered_df[value_col].sum()
        avg_value = filtered_df[value_col].mean()
        row_count = len(filtered_df)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total", f"{total_value:,.2f}")
        col2.metric("Average", f"{avg_value:,.2f}")
        col3.metric("Rows", f"{row_count:,}")

        # Trend chart
        if date_col != "None" and pd.api.types.is_datetime64_any_dtype(filtered_df[date_col]):
            st.subheader("Trend Over Time")

            trend_df = (
                filtered_df.dropna(subset=[date_col])
                .groupby(date_col, as_index=False)[value_col]
                .sum()
                .sort_values(date_col)
            )

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(trend_df[date_col], trend_df[value_col])
            ax.set_title(f"{value_col} Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel(value_col)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Category summary
        if category_col != "None":
            st.subheader("Category Breakdown")
            category_summary = (
                filtered_df.groupby(category_col, as_index=False)[value_col]
                .sum()
                .sort_values(value_col, ascending=False)
            )
            st.dataframe(category_summary)

        st.subheader("Filtered Data")
        st.dataframe(filtered_df)

        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download filtered data as CSV",
            data=csv,
            file_name="filtered_financial_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Error processing file: {e}")

else:
    st.info("Please upload a CSV file to begin.")