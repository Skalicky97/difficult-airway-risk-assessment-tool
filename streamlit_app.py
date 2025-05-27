import streamlit as st
import streamlit as st

st.set_page_config(page_title="Difficult Airway Risk Calculator", layout="centered")

st.title("🫁 Difficult Airway Risk Calculator")

# Define the scoring criteria
criteria = {
    "Mallampati": {"Class I": 0, "Class II": 0, "Class III": 5, "Class IV": 10},
    "Thyromental Distance": {"> 6 cm (3 fingers)": 0, "< 6 cm (3 fingers)": 5},
    "Mouth Opening": {"≥ 3 fingers": 0, "< 3 fingers": 5},
    "BMI": {
        "< 29.9": 0,
        "30 – 34.9 (Class I)": 5,
        "35 – 39.9 (Class II)": 10,
        "≥ 40 (Class III)": 15,
    },
    "Upper Lip Bite Test": {"Class I": 0, "Class II": 10, "Class III": 15},
    "Surgery/Radiation to Head/Neck": {"No": 0, "Yes": 10},
    "Previous Difficult Airway": {"No": 0, "Yes": 10},
    "Obstructive Sleep Apnea (OSA)": {"No": 0, "Yes or suspected": 5},
    "Cervical Spine Mobility": {"Full": 0, "Limited": 15},
    "ASA": {"1": 0, "2": 0, "3": 5, "4": 10},
}

scores = {}

st.subheader("📝 Select the appropriate options:")

# Render dropdowns for each criterion
for criterion, options in criteria.items():
    choice = st.selectbox(criterion, list(options.keys()))
    scores[criterion] = options[choice]

# Calculate total score
total_score = sum(scores.values())

# Determine risk level
if total_score <= 20:
    risk_level = "Low"
    risk_color = "green"
elif total_score <= 60:
    risk_level = "Moderate"
    risk_color = "orange"
else:
    risk_level = "High"
    risk_color = "red"

# Display results
st.markdown("---")
st.markdown(f"### 🧮 Total Risk Score: **{total_score}**")
st.markdown(
    f"### 📊 Risk Level: <span style='color:{risk_color}; font-weight:bold'>{risk_level}</span>",
    unsafe_allow_html=True
)
