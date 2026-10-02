# 💧 AquaGuard AI
### Community Water Potability & Public Health Risk Diagnostic Engine
**EurekaDev 2026 Submission | Coding Track: Biology/Medical & Environmental Science / Community Problem**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aquaguard-health.streamlit.app/)

---

## 📌 Executive Summary
Over 2 billion people worldwide live in water-stressed regions without immediate access to laboratory-grade water testing facilities. While physical field test strips and portable colorimeters provide basic parameter data (pH, turbidity, dissolved solids), local community health workers and rural populations frequently lack the clinical and chemical expertise required to interpret these multidimensional readings accurately. 

**AquaGuard AI** bridges this critical last-mile diagnostic gap. It serves as an accessible, real-time diagnostic engine that translates field water telemetry into:
1. Instant potability safety scores using WHO drinking-water quality thresholds.
2. Pathogen and chemical hazard classification (e.g., microbial vectors, heavy metal leaching, gastrointestinal risks).
3. Field-deployable, low-cost intervention protocols (multi-layer filtration, boiling standards, and solar disinfection dosages).

---

## 🚀 Live Demonstration
- **Live Interactive Dashboard:** [aquaguard-health.streamlit.app](https://aquaguard-health.streamlit.app/)
- **Target Platform:** Zero-install responsive web application optimized for mobile and desktop field diagnostics.

---

## 🔬 Core Features & Diagnostic Architecture

### 1. Multi-Parameter Chemical & Physical Telemetry Analysis
The engine evaluates key parameters based on empirical World Health Organization (WHO) Drinking Water Guidelines (4th Edition):
- **pH Level:** Gauges corrosive heavy-metal leaching ($< 6.5$) versus scale-forming/disinfection impedance ($> 8.5$).
- **Turbidity (NTU):** Flags suspended matter shielding biological vectors ($> 5.0\text{ NTU}$).
- **Total Dissolved Solids (TDS):** Evaluates mineralization and gastrointestinal distress indicators ($> 500\text{ ppm}$).
- **Chloramine / Disinfectant Residuals:** Assesses secondary bacterial re-growth risks in field storage vessels ($< 0.2\text{ ppm}$).
- **Hardness & Sulfates:** Evaluates long-term mineral burdens and acute osmotic laxative risks.

### 2. Algorithmic Risk & Safety Scoring
AquaGuard AI calculates a dynamic **Safety Index (0–100)**:
- Quantifies cumulative non-linear threshold violations.
- Renders an interactive visual gauge indicating real-time hazard severity:
  - **🟢 Safe for Consumption (80–100):** Meets baseline standard thresholds.
  - **🟡 Potential Hazard (50–79):** Requires active pre-treatment or secondary chlorination.
  - **🔴 Contaminated / Critical Danger (< 50):** High likelihood of pathogenic or chemical toxicity.

### 3. Community Mitigation & Intervention Engine
Generates actionable, decentralized public health countermeasures:
- **Primary Filtration:** Fabric/sari folded micro-filtration and biosand protocol guidance.
- **Microbial Inactivation:** Altitude-adjusted rolling boil parameters and SODIS (Solar Disinfection) solar UV exposure timelines.
- **Safe Storage Protocols:** Preventing vessel-based secondary microbial vectors.

---

## 🛠️️ Technology Stack
- **Framework:** Streamlit (Python 3.10+)
- **Data Computation:** NumPy, Pandas
- **Interactive Visualization:** Plotly Graph Objects Engine
- **Cloud Infrastructure:** Streamlit Community Cloud (Global Edge Deployment)

---

## 💻 Local Development Setup

To run AquaGuard AI locally on your machine:

```bash
# Clone the repository
git clone [https://github.com/arpit37singh-wq/aquaguard-ai.git](https://github.com/arpit37singh-wq/aquaguard-ai.git)
cd aquaguard-ai

# Install dependencies
pip install -r requirements.txt

# Launch application
streamlit run app.py
