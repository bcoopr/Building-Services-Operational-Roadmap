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
   # Print summary if present
if "summary" in why:
    st.markdown(f"- **Summary:** {why['summary']}")

# Define ordered display labels
details_labels = {
    "strategic_alignment": "Strategic Alignment",
    "staff_experience": "Staff Experience",
    "patient_impact": "Patient Impact",
    "operational_efficiency": "Operational Efficiency",
    "regulatory_readiness": "Regulatory Readiness",
    "financial_responsibility": "Financial Responsibility",
    "workflow_efficiency": "Workflow Efficiency",
    "safety_standardization": "Safety Standardization",
    "space_utilization": "Space Utilization"
}

# Get details section safely
details = why.get("details", {})

# Print in the preferred order using friendly names
for key in details_labels:
    if key in details:
        label = details_labels[key]
        st.markdown(f"- **{label}:** {details[key]}")
