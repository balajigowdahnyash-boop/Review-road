import streamlit as st
import pandas as pd

st.set_page_config(page_title="REVIVE ROAD", page_icon="🛣️", layout="wide")

st.title("🛣️ REVIVE ROAD")
st.subheader("ONE ROAD, MULTIPLE ROLES")
st.write("AI-powered adaptive road infrastructure")
st.warning("Demo mode: These are sample values, not live road measurements.")

data = {
    "Road": ["Road A", "Road B", "Road C", "Road D"],
    "Road Health": [85, 45, 92, 35],
    "Potholes": [1, 6, 0, 8],
    "Waterlogging": ["No", "Yes", "No", "Yes"],
    "Priority": ["Low", "High", "Low", "Critical"]
}

df = pd.DataFrame(data)

col1, col2, col3 = st.columns(3)
col1.metric("Roads Monitored", len(df))
col2.metric("Average Road Health", f"{df['Road Health'].mean():.0f}/100")
col3.metric("Total Sample Potholes", int(df["Potholes"].sum()))

st.subheader("Road Health Dashboard")
st.bar_chart(df.set_index("Road")["Road Health"])

st.subheader("Road Condition Details")
st.dataframe(df, use_container_width=True)

st.subheader("Report a Road Issue")
with st.form("report_form"):
    road = st.text_input("Road name")
    issue = st.selectbox(
        "Issue type",
        ["Pothole", "Cracked Road", "Waterlogging", "Damaged Road"]
    )
    details = st.text_area("Describe the issue")
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        if road.strip() and details.strip():
            st.success(f"Demo report recorded for {road}: {issue}")
            st.write(details)
            st.caption("This report is not permanently stored or sent to authorities.")
        else:
            st.error("Please enter the road name and issue description.")

st.caption("REVIVE ROAD | Sense → Analyze → Predict → Adapt → Respond")
