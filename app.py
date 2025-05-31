import streamlit as st
import json

# Load roadmap data
with open("building_services_roadmap.json", "r") as f:
    data = json.load(f)

st.title("Building Services Operational Roadmap (2025–2030)")
st.markdown("This interactive dashboard presents strategic initiatives, goals, and KPIs.")

# Build year selection from all start/end years
years = sorted({yr for item in data["initiatives"] for yr in [item["start_year"], item["end_year"]]})
selected_year = st.selectbox("Select a Year", years)

# Filter initiatives by selected year
filtered = [i for i in data["initiatives"] if i["start_year"] <= selected_year <= i["end_year"]]

# Display each filtered initiative
for i in filtered:
    st.subheader(i["initiative"])
    st.markdown(f"**Category:** {i['category']}")

    st.markdown("**Goals:**")
    for g in i["goals"]:
        st.markdown(f"- {g}")

    st.markdown("**KPIs:**")
    for k in i["kpis"]:
        st.markdown(f"- {k}")

    st.markdown("**Why It Matters**")

    # Get 'why_it_matters' safely
    why = i.get("why_it_matters", {})

    # Print summary if it exists
    if "summary" in why:
        st.markdown(f"- **Summary:** {why['summary']}")

    # Get nested 'details' safely
    details = why.get("details", {})

    # Print each section if it exists
    if details.get("financial_responsibility"):
        st.markdown(f"- **Financial Responsibility:** {details['financial_responsibility']}")

    if details.get("workflow_efficiency"):
        st.markdown(f"- **Workflow Efficiency:** {details['workflow_efficiency']}")

    if details.get("safety_standardization"):
        st.markdown(f"- **Safety Standardization:** {details['safety_standardization']}")

    if details.get("regulatory_readiness"):
        st.markdown(f"- **Regulatory Readiness:** {details['regulatory_readiness']}")

    if details.get("space_utilization"):
        st.markdown(f"- **Space Utilization:** {details['space_utilization']}")

    if details.get("strategic_alignment"):
        st.markdown(f"- **Strategic Alignment:** {details['strategic_alignment']}")

    st.markdown("**Strategic Alignment:**")
    for s in i["strategic_alignment"]:
        st.markdown(f"- {s}")

    st.markdown("---")


