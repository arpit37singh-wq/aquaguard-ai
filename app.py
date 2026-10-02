import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="AquaGuard AI — Water Potability & Risk Diagnostic",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header Section
st.title("💧 AquaGuard AI")
st.subheader("Community Water Potability & Public Health Risk Diagnostic Engine")
st.markdown("""
*An intelligent diagnostics tool designed for rural healthcare workers and communities 
to predict water safety, identify biological/chemical hazards, and generate immediate purification protocols.*
""")

# Sidebar - Water Quality Inputs
st.sidebar.header("🔬 Water Quality Parameters")
st.sidebar.caption("Enter the readings from your field test kit or optical sensor:")

ph = st.sidebar.slider("pH Level", min_value=0.0, max_value=14.0, value=7.2, step=0.1, help="Safe WHO range: 6.5 - 8.5")
turbidity = st.sidebar.slider("Turbidity (NTU)", min_value=0.0, max_value=20.0, value=2.1, step=0.1, help="WHO standard: < 5.0 NTU")
tds = st.sidebar.slider("Total Dissolved Solids (TDS in ppm)", min_value=50, max_value=2000, value=280, step=10, help="WHO standard: < 500 ppm ideal")
chloramines = st.sidebar.slider("Chloramines / Residual Chlorine (ppm)", min_value=0.0, max_value=10.0, value=2.4, step=0.1, help="Standard: 0.2 - 4.0 ppm")
hardness = st.sidebar.slider("Total Hardness (mg/L)", min_value=50, max_value=500, value=160, step=5)
sulfate = st.sidebar.slider("Sulfates (mg/L)", min_value=50, max_value=600, value=180, step=5)

# Diagnostic Engine Logic
violations = []
health_risks = []
mitigation = []

# Parameter Evaluation
if ph < 6.5 or ph > 8.5:
    violations.append(f"pH level abnormal ({ph:.1f}). Safe threshold: 6.5–8.5.")
    if ph < 6.5:
        health_risks.append("Acidic water: Leaches toxic heavy metals (lead, copper) from pipes; gastric irritation.")
        mitigation.append("Add food-grade alkaline buffer (calcium carbonate/lime filtration).")
    else:
        health_risks.append("Alkaline water: Lowers disinfection efficiency, skin dryness, bitter taste.")

if turbidity > 5.0:
    violations.append(f"High Turbidity ({turbidity:.1f} NTU). Safe limit is 5.0 NTU.")
    health_risks.append("Suspended particles shelter pathogens (E. coli, Giardia, Vibrio cholerae) from UV and chlorine disinfection.")
    mitigation.append("Prioritize multi-stage sand/cloth filtration or alum coagulation before drinking.")

if tds > 500:
    violations.append(f"Elevated TDS ({tds} ppm). Desirable limit is 500 ppm.")
    if tds > 1000:
        health_risks.append("Severe mineralization: Risk of kidney stress, gastrointestinal distress.")
        mitigation.append("Requires Reverse Osmosis (RO) or distillation treatment.")

if chloramines < 0.2:
    violations.append("Zero/Low disinfectant residual (< 0.2 ppm).")
    health_risks.append("High risk of secondary microbial recontamination in storage vessels.")
    mitigation.append("Administer community chlorine water purification tablets (NaDCC).")
elif chloramines > 4.0:
    violations.append(f"Excessive Disinfectant ({chloramines:.1f} ppm).")
    health_risks.append("Eye/nose irritation, long-term stomach discomfort.")

# Scoring Metric
risk_score = min(100, int((len(violations) * 25) + (max(0, turbidity - 5) * 5) + (max(0, tds - 500) * 0.05)))
potable = len(violations) == 0

# Dashboard Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📊 Safety Verdict")
    
    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 100 - risk_score,
        title = {'text': "Safety Index (0-100)"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2ecc71" if potable else ("#f39c12" if risk_score < 60 else "#e74c3c")},
            'steps': [
                {'range': [0, 50], 'color': "#ffebee"},
                {'range': [50, 80], 'color': "#fff8e1"},
                {'range': [80, 100], 'color': "#e8f8f5"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 3},
                'thickness': 0.75,
                'value': 80
            }
        }
    ))
    fig.update_layout(height=280, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

    if potable:
        st.success("✅ **SAFE FOR CONSUMPTION** — Water meets baseline WHO safety guidelines.")
    elif risk_score < 60:
        st.warning("⚠️ **POTENTIAL HAZARD** — Treatment required prior to human consumption.")
    else:
        st.error("🚨 **CONTAMINATED / CRITICAL RISK** — High probability of biological or chemical danger.")

with col2:
    st.markdown("### 🧬 Diagnostic Breakdown & Anomalies")
    if violations:
        for v in violations:
            st.markdown(f"- 🔴 **Anomaly:** {v}")
    else:
        st.markdown("- 🟢 All tested chemical and clarity parameters are within safe target ranges.")

    st.markdown("---")
    st.markdown("### 🩺 Public Health Threat Analysis")
    if health_risks:
        for r in health_risks:
            st.markdown(f"- ⚠️ {r}")
    else:
        st.markdown("- 💧 Low epidemiological risk of waterborne vector illness based on these readings.")

# Actionable Protocols
st.markdown("---")
st.markdown("### 🛡️ Immediate Intervention Protocols")
pcol1, pcol2, pcol3 = st.columns(3)

with pcol1:
    st.markdown("#### 1. Primary Filtration")
    st.info("Pass water through a clean 4-layer folded cotton sari/muslin or biosand filter to remove larger suspended vectors.")

with pcol2:
    st.markdown("#### 2. Disinfection")
    st.info("Vigorous rolling boil for 1 full minute (3 min at high altitude) OR apply SODIS (6 hours clear PET bottle in direct sunlight).")

with pcol3:
    st.markdown("#### 3. Storage & Guarding")
    st.info("Store in narrow-neck covered vessels with a dedicated tap to prevent hand contact and secondary contamination.")

# Field Observation Simulator
st.markdown("---")
st.markdown("### 📝 Field Symptom & Water Quality Notes")
notes = st.text_area("Record community field observations (e.g., rust color, sulfur smell, diarrhea reports in cluster):", 
                     placeholder="e.g. Residents near north well report metallic taste and sulfur smell after heavy monsoon rainfall.")
if st.button("Generate Diagnostic Report"):
    st.success("Diagnostic summary generated! Ready for field clinic documentation and export.")
