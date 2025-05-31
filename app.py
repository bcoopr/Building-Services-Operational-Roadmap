import streamlit as st
import json

# Load roadmap data
with open("building_services_roadmap.json", "r") as f:
    data = json.load(f)

st.title("Building Services Operational Roadmap (2025–2030)")
st.markdown("This interactive dashboard presents strategic initiatives, goals, timelines, and KPIs.")

# Build year selection from all start/end years
years = sorted({yr for item in data["initiatives"] for yr in [item["start_year"], item["end_year"]]})
selected_year = st.selectbox("Select a Year", years)

# Filter initiatives by selected year
filtered = [i for i in data["initiatives"] if i["start_year"] <= selected_year <= i["end_year"]]

# Define principle display labels
principles = {
    "fiduciary_responsibility": "Financial Responsibility",
    "staff_experience": "Staff Experience",
    "member_experience": "Member Experience",
    "regulatory_compliance": "Regulatory Compliance"
}

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
    why = i.get("why_it_matters", {})
    if "summary" in why:
        st.markdown(f"- **Summary:** {why['summary']}")

    details = why.get("details", {})
    for key, label in principles.items():
        if key in details:
            st.markdown(f"- **{label}:** {details[key]}")

    st.markdown("**Strategic Alignment:**")
    for s in i.get("strategic_alignment", []):
        st.markdown(f"- {s}")

    # Display Timeline
    timeline = i.get("timeline", {})
    if timeline:
        st.markdown("**Timeline:**")
        for year in sorted(timeline):
            st.markdown(f"- **{year}**")
            for item in timeline[year]:
                st.markdown(f"  - {item}")

    st.markdown("---")
