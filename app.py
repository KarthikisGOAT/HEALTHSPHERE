import streamlit as st
from datetime import datetime
import random

# ============================================================
# HEALTHSPHERE
# A medical information & health education website
# ============================================================

st.set_page_config(
    page_title="HealthSphere | Health & Disease Information",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #f7f9fb;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main content */
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #123b5d;
        line-height: 1.1;
        margin-bottom: 12px;
    }

    .subtitle {
        font-size: 19px;
        color: #536575;
        line-height: 1.6;
        margin-bottom: 25px;
    }

    .hero {
        background: linear-gradient(135deg, #e9f6fb 0%, #ffffff 55%, #edf8f4 100%);
        padding: 55px 45px;
        border-radius: 24px;
        border: 1px solid #dce9ef;
        margin-bottom: 30px;
    }

    .hero-badge {
        display: inline-block;
        background: #dff3f6;
        color: #126276;
        padding: 7px 14px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    .section-title {
        color: #123b5d;
        font-size: 30px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 18px;
    }

    .card {
        background: white;
        border: 1px solid #e2e9ee;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 15px;
        box-shadow: 0 3px 12px rgba(20, 50, 70, 0.04);
    }

    .card h3 {
        color: #123b5d;
        margin-top: 0;
    }

    .card p {
        color: #566773;
        line-height: 1.6;
    }

    .disease-header {
        background: linear-gradient(135deg, #123b5d, #176b83);
        color: white;
        padding: 35px;
        border-radius: 20px;
        margin-bottom: 25px;
    }

    .disease-header h1 {
        color: white;
        font-size: 40px;
        margin-bottom: 8px;
    }

    .disease-header p {
        color: #e5f4f7;
        font-size: 17px;
        line-height: 1.6;
    }

    .tag {
        display: inline-block;
        padding: 5px 11px;
        margin: 3px;
        border-radius: 15px;
        background: #e8f2f6;
        color: #19546c;
        font-size: 12px;
        font-weight: 600;
    }

    .warning {
        background: #fff7e5;
        border-left: 5px solid #e8a317;
        padding: 18px;
        border-radius: 10px;
        color: #62480b;
        margin: 20px 0;
    }

    .info {
        background: #eaf6f8;
        border-left: 5px solid #2c91a3;
        padding: 18px;
        border-radius: 10px;
        color: #174c58;
        margin: 20px 0;
    }

    .emergency {
        background: #fff0f0;
        border-left: 5px solid #d94848;
        padding: 20px;
        border-radius: 10px;
        color: #6b2020;
        margin: 20px 0;
    }

    .stat-card {
        background: white;
        border-radius: 18px;
        border: 1px solid #e2e9ee;
        padding: 24px;
        text-align: center;
    }

    .stat-number {
        font-size: 32px;
        font-weight: 800;
        color: #176b83;
    }

    .stat-label {
        color: #667781;
        font-size: 14px;
    }

    .source {
        background: white;
        border: 1px solid #e0e7eb;
        padding: 15px 18px;
        border-radius: 12px;
        margin: 8px 0;
    }

    .small-text {
        color: #73828b;
        font-size: 13px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e4eaee;
    }

    section[data-testid="stSidebar"] h1 {
        color: #123b5d;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }

    /* Search box */
    .search-help {
        color: #687983;
        font-size: 13px;
        margin-top: -10px;
        margin-bottom: 20px;
    }

    /* Mobile */
    @media (max-width: 768px) {
        .main-title {
            font-size: 34px;
        }

        .hero {
            padding: 30px 22px;
        }

        .disease-header h1 {
            font-size: 30px;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA
# Educational content only
# ============================================================

DISEASES = {
    "Asthma": {
        "category": "Respiratory",
        "summary": "Asthma is a condition in which the airways can become inflamed and narrowed, sometimes making breathing difficult.",
        "symptoms": [
            "Wheezing",
            "Coughing",
            "Shortness of breath",
            "Chest tightness"
        ],
        "causes": [
            "Airway inflammation and sensitivity",
            "Allergens",
            "Respiratory infections",
            "Smoke and air pollution",
            "Exercise or cold air in some people"
        ],
        "risk_factors": [
            "Family history",
            "Allergies",
            "Exposure to tobacco smoke",
            "Air pollution",
            "Certain occupational exposures"
        ],
        "complications": [
            "Severe asthma attacks",
            "Sleep disturbance",
            "Reduced activity",
            "Emergency medical care in severe cases"
        ],
        "prevention": [
            "Avoid known triggers when possible",
            "Follow an asthma management plan from a healthcare professional",
            "Avoid tobacco smoke",
            "Keep recommended vaccinations up to date"
        ],
        "diagnosis": "Healthcare professionals may use medical history, physical examination and breathing tests such as spirometry.",
        "treatment": "Management may include avoiding triggers, inhaled medicines and an individualized asthma action plan.",
        "when_to_seek": "Seek urgent medical attention for severe or rapidly worsening breathing difficulty.",
    },

    "Type 2 Diabetes": {
        "category": "Endocrine & Metabolic",
        "summary": "Type 2 diabetes is a condition in which the body does not use insulin effectively and blood glucose levels become too high.",
        "symptoms": [
            "Increased thirst",
            "Frequent urination",
            "Increased hunger",
            "Fatigue",
            "Blurred vision",
            "Slow-healing wounds"
        ],
        "causes": [
            "Insulin resistance",
            "Reduced insulin production over time",
            "Genetic factors",
            "Multiple environmental and lifestyle factors"
        ],
        "risk_factors": [
            "Family history",
            "Increasing age",
            "Physical inactivity",
            "Certain patterns of body fat distribution",
            "History of prediabetes"
        ],
        "complications": [
            "Heart and blood vessel disease",
            "Kidney disease",
            "Nerve damage",
            "Eye problems",
            "Foot problems"
        ],
        "prevention": [
            "Regular physical activity",
            "Balanced eating habits",
            "Regular health checkups",
            "Maintaining healthy habits over time"
        ],
        "diagnosis": "Diagnosis generally uses blood glucose testing, including tests such as A1C or fasting blood glucose.",
        "treatment": "Treatment can include lifestyle changes, blood-glucose monitoring and medicines when prescribed by a healthcare professional.",
        "when_to_seek": "Seek medical advice for persistent symptoms such as excessive thirst, frequent urination or unexplained fatigue.",
    },

    "Hypertension": {
        "category": "Heart & Blood Vessels",
        "summary": "Hypertension, or high blood pressure, occurs when blood pressure remains higher than recommended over time.",
        "symptoms": [
            "Often no noticeable symptoms",
            "Headache can occur in some situations",
            "Dizziness may occur",
            "Vision changes can occur in severe situations"
        ],
        "causes": [
            "Multiple genetic factors",
            "Age-related changes",
            "Lifestyle factors",
            "Certain medical conditions",
            "Some medicines"
        ],
        "risk_factors": [
            "Family history",
            "Increasing age",
            "High-sodium dietary patterns",
            "Physical inactivity",
            "Tobacco use",
            "Excess alcohol use"
        ],
        "complications": [
            "Heart disease",
            "Stroke",
            "Kidney problems",
            "Vision problems"
        ],
        "prevention": [
            "Regular blood pressure checks",
            "Regular physical activity",
            "Balanced eating habits",
            "Limiting excess sodium",
            "Avoiding tobacco"
        ],
        "diagnosis": "Blood pressure is measured using a blood pressure cuff. Repeated measurements may be needed.",
        "treatment": "Treatment can involve lifestyle changes and prescription medicines depending on the person's situation.",
        "when_to_seek": "Very high blood pressure accompanied by concerning symptoms such as chest pain, severe headache, confusion or difficulty breathing requires urgent medical attention.",
    },

    "Migraine": {
        "category": "Neurological",
        "summary": "Migraine is a neurological condition that can cause recurring headaches and other symptoms.",
        "symptoms": [
            "Moderate to severe headache",
            "Nausea",
            "Sensitivity to light",
            "Sensitivity to sound",
            "Visual changes in some people"
        ],
        "causes": [
            "Changes in brain activity",
            "Genetic factors",
            "Various environmental triggers"
        ],
        "risk_factors": [
            "Family history",
            "Hormonal changes",
            "Stress",
            "Sleep disruption",
            "Certain foods or environmental triggers"
        ],
        "complications": [
            "Reduced daily activity",
            "Missed school or work",
            "Frequent headaches",
            "Medication-overuse headaches in some situations"
        ],
        "prevention": [
            "Regular sleep",
            "Regular meals",
            "Adequate hydration",
            "Identifying personal triggers",
            "Managing stress"
        ],
        "diagnosis": "Diagnosis is usually based on symptoms and medical history. Additional testing may be considered when symptoms suggest another condition.",
        "treatment": "Treatment may include medicines for attacks and, for some people, preventive treatment prescribed by a healthcare professional.",
        "when_to_seek": "A sudden, severe or unusual headache, especially with neurological symptoms, requires urgent medical evaluation.",
    },

    "Influenza (Flu)": {
        "category": "Infectious Diseases",
        "summary": "Influenza is a contagious respiratory infection caused by influenza viruses.",
        "symptoms": [
            "Fever or feeling feverish",
            "Cough",
            "Sore throat",
            "Muscle aches",
            "Fatigue",
            "Headache"
        ],
        "causes": [
            "Influenza A viruses",
            "Influenza B viruses"
        ],
        "risk_factors": [
            "Close contact with infected people",
            "Crowded environments",
            "Certain medical conditions",
            "Older age and very young age groups"
        ],
        "complications": [
            "Pneumonia",
            "Dehydration",
            "Worsening of underlying conditions",
            "Other complications in higher-risk people"
        ],
        "prevention": [
            "Seasonal influenza vaccination",
            "Hand hygiene",
            "Avoiding close contact when sick",
            "Covering coughs and sneezes"
        ],
        "diagnosis": "Diagnosis can be based on symptoms and, when needed, laboratory testing.",
        "treatment": "Rest, fluids and symptom care may help. Antiviral medicines may be appropriate for some people and are most effective when started early.",
        "when_to_seek": "Seek urgent care for serious breathing problems, persistent chest pain, confusion or significant deterioration.",
    },

    "Pneumonia": {
        "category": "Respiratory",
        "summary": "Pneumonia is an infection or inflammation of the lungs that can be caused by bacteria, viruses or other organisms.",
        "symptoms": [
            "Cough",
            "Fever",
            "Chills",
            "Shortness of breath",
            "Chest discomfort",
            "Fatigue"
        ],
        "causes": [
            "Bacteria",
            "Viruses",
            "Fungi in some cases",
            "Aspiration of material into the lungs"
        ],
        "risk_factors": [
            "Very young or older age",
            "Chronic medical conditions",
            "Weakened immune system",
            "Smoking",
            "Recent respiratory infection"
        ],
        "complications": [
            "Breathing difficulties",
            "Bloodstream infection",
            "Fluid around the lungs",
            "Respiratory failure in severe cases"
        ],
        "prevention": [
            "Recommended vaccinations",
            "Hand hygiene",
            "Avoid smoking",
            "Managing chronic conditions"
        ],
        "diagnosis": "Evaluation may include examination, oxygen measurement and sometimes chest imaging or laboratory tests.",
        "treatment": "Treatment depends on the cause and severity. Bacterial pneumonia may require antibiotics prescribed by a healthcare professional.",
        "when_to_seek": "Difficulty breathing, bluish lips or skin, confusion or severe chest symptoms require urgent medical attention.",
    },

    "Dengue": {
        "category": "Infectious Diseases",
        "summary": "Dengue is a viral infection mainly transmitted through the bites of infected Aedes mosquitoes.",
        "symptoms": [
            "High fever",
            "Headache",
            "Muscle and joint pain",
            "Nausea",
            "Rash"
        ],
        "causes": [
            "Dengue virus infection",
            "Transmission through infected mosquitoes"
        ],
        "risk_factors": [
            "Living in or traveling to areas where dengue occurs",
            "Mosquito exposure",
            "Previous dengue infection can affect risk of severe disease"
        ],
        "complications": [
            "Severe dengue",
            "Bleeding",
            "Shock",
            "Organ complications"
        ],
        "prevention": [
            "Avoid mosquito bites",
            "Use appropriate insect protection",
            "Remove standing water around homes",
            "Use screens where appropriate"
        ],
        "diagnosis": "Healthcare professionals may use symptoms, examination and blood tests.",
        "treatment": "Treatment focuses on supportive care and careful monitoring. Medical advice is important, particularly if warning signs appear.",
        "when_to_seek": "Severe abdominal pain, repeated vomiting, bleeding, extreme weakness or breathing difficulty can be warning signs requiring urgent care.",
    },

    "Anemia": {
        "category": "Blood Disorders",
        "summary": "Anemia occurs when the blood does not have enough healthy red blood cells or hemoglobin to carry oxygen effectively.",
        "symptoms": [
            "Fatigue",
            "Weakness",
            "Pale skin",
            "Shortness of breath",
            "Dizziness",
            "Headache"
        ],
        "causes": [
            "Iron deficiency",
            "Vitamin deficiencies",
            "Blood loss",
            "Chronic diseases",
            "Inherited blood disorders"
        ],
        "risk_factors": [
            "Nutritional deficiencies",
            "Heavy blood loss",
            "Certain chronic conditions",
            "Family history of inherited blood disorders"
        ],
        "complications": [
            "Severe fatigue",
            "Heart strain",
            "Pregnancy complications in some cases",
            "Problems related to the underlying cause"
        ],
        "prevention": [
            "Balanced nutrition",
            "Treating underlying conditions",
            "Following professional advice about supplementation when needed"
        ],
        "diagnosis": "A blood test such as a complete blood count can help identify anemia and may be followed by additional testing.",
        "treatment": "Treatment depends on the underlying cause and may include dietary changes, supplements or treatment of blood loss or another medical condition.",
        "when_to_seek": "Seek medical advice for unexplained or persistent fatigue, weakness or shortness of breath.",
    },

    "Hypothyroidism": {
        "category": "Endocrine & Metabolic",
        "summary": "Hypothyroidism occurs when the thyroid gland does not produce enough thyroid hormones.",
        "symptoms": [
            "Fatigue",
            "Feeling unusually cold",
            "Dry skin",
            "Constipation",
            "Changes in mood",
            "Difficulty concentrating"
        ],
        "causes": [
            "Autoimmune thyroid disease",
            "Certain treatments",
            "Some medicines",
            "Thyroid problems present from birth"
        ],
        "risk_factors": [
            "Family history",
            "Certain autoimmune conditions",
            "Increasing age",
            "Previous thyroid treatment"
        ],
        "complications": [
            "Heart problems",
            "Fertility problems",
            "Neurological symptoms",
            "Severe untreated hypothyroidism can become a medical emergency"
        ],
        "prevention": [
            "Some causes cannot be prevented",
            "Regular medical follow-up when at risk",
            "Following prescribed treatment"
        ],
        "diagnosis": "Blood tests measuring thyroid-related hormones are commonly used.",
        "treatment": "Treatment commonly involves thyroid hormone replacement prescribed and monitored by a healthcare professional.",
        "when_to_seek": "Severe weakness, confusion, difficulty breathing or significant deterioration requires urgent medical evaluation.",
    },

    "Osteoporosis": {
        "category": "Bones & Joints",
        "summary": "Osteoporosis is a condition that weakens bones and increases the risk of fractures.",
        "symptoms": [
            "Often no symptoms until a fracture occurs",
            "Back pain from vertebral fractures",
            "Loss of height",
            "Changes in posture"
        ],
        "causes": [
            "Bone loss over time",
            "Hormonal changes",
            "Age-related changes",
            "Certain medicines or medical conditions"
        ],
        "risk_factors": [
            "Increasing age",
            "Family history",
            "Low bone density",
            "Certain hormonal changes",
            "Long-term use of some medicines"
        ],
        "complications": [
            "Fractures",
            "Loss of mobility",
            "Chronic pain",
            "Reduced independence"
        ],
        "prevention": [
            "Adequate calcium and vitamin D intake",
            "Weight-bearing physical activity",
            "Avoiding tobacco",
            "Fall prevention",
            "Bone health screening when recommended"
        ],
        "diagnosis": "Bone density testing can help assess bone strength.",
        "treatment": "Treatment may include lifestyle measures and prescription medicines depending on fracture risk.",
        "when_to_seek": "A suspected fracture or sudden severe back pain should be medically evaluated.",
    },

    "Gastritis": {
        "category": "Digestive System",
        "summary": "Gastritis refers to inflammation of the stomach lining.",
        "symptoms": [
            "Upper abdominal discomfort",
            "Nausea",
            "Feeling full quickly",
            "Indigestion",
            "Reduced appetite"
        ],
        "causes": [
            "Helicobacter pylori infection",
            "Certain medicines",
            "Alcohol irritation",
            "Other conditions that affect the stomach lining"
        ],
        "risk_factors": [
            "H. pylori infection",
            "Frequent use of certain pain medicines",
            "Alcohol use",
            "Some chronic illnesses"
        ],
        "complications": [
            "Stomach ulcers",
            "Bleeding",
            "Iron deficiency",
            "Changes to the stomach lining in some cases"
        ],
        "prevention": [
            "Use medicines as directed",
            "Discuss frequent painkiller use with a healthcare professional",
            "Good food and hygiene practices"
        ],
        "diagnosis": "Evaluation may include medical history, testing for H. pylori, blood tests or other investigations.",
        "treatment": "Treatment depends on the cause and may involve medicines that reduce stomach acid or treatment for H. pylori infection.",
        "when_to_seek": "Vomiting blood, black stools, severe pain or fainting requires urgent medical attention.",
    },

    "Eczema": {
        "category": "Skin Conditions",
        "summary": "Eczema is a group of conditions that can cause itchy, inflamed and irritated skin.",
        "symptoms": [
            "Itchy skin",
            "Dry skin",
            "Red or inflamed skin",
            "Skin irritation",
            "Cracked skin"
        ],
        "causes": [
            "Skin barrier dysfunction",
            "Immune system activity",
            "Genetic factors",
            "Environmental triggers"
        ],
        "risk_factors": [
            "Family history",
            "Allergies",
            "Asthma or allergic conditions",
            "Certain environmental exposures"
        ],
        "complications": [
            "Skin infections",
            "Sleep disruption",
            "Skin thickening from repeated scratching"
        ],
        "prevention": [
            "Use recommended moisturizers",
            "Avoid known irritants",
            "Use gentle skin-care products",
            "Follow a healthcare professional's treatment plan"
        ],
        "diagnosis": "Diagnosis is often based on the appearance of the skin and medical history.",
        "treatment": "Treatment can include moisturizers, topical medicines and trigger management depending on severity.",
        "when_to_seek": "Rapidly worsening skin symptoms, signs of infection or extensive symptoms should be medically assessed.",
    },

    "Common Cold": {
        "category": "Infectious Diseases",
        "summary": "The common cold is a mild upper-respiratory infection caused by many different viruses.",
        "symptoms": [
            "Runny nose",
            "Nasal congestion",
            "Sneezing",
            "Sore throat",
            "Cough",
            "Mild fatigue"
        ],
        "causes": [
            "Many respiratory viruses",
            "Transmission through respiratory droplets and contaminated hands or surfaces"
        ],
        "risk_factors": [
            "Close contact with infected people",
            "Crowded environments",
            "Frequent exposure to respiratory viruses"
        ],
        "complications": [
            "Sinus infection",
            "Ear infection",
            "Worsening of asthma in some people"
        ],
        "prevention": [
            "Hand washing",
            "Avoid touching eyes, nose and mouth with unclean hands",
            "Avoid close contact with people who are sick"
        ],
        "diagnosis": "Usually diagnosed based on symptoms.",
        "treatment": "Rest, fluids and symptom relief may help. Antibiotics do not treat viral colds.",
        "when_to_seek": "Seek medical care for severe breathing difficulty, persistent high fever, dehydration or symptoms that significantly worsen.",
    },

    "Heart Disease": {
        "category": "Heart & Blood Vessels",
        "summary": "Heart disease refers to several conditions affecting the heart and blood vessels, including coronary artery disease.",
        "symptoms": [
            "Chest discomfort",
            "Shortness of breath",
            "Fatigue",
            "Palpitations",
            "Swelling of the legs in some conditions"
        ],
        "causes": [
            "Atherosclerosis",
            "High blood pressure",
            "Diabetes",
            "Inherited conditions",
            "Other cardiovascular conditions"
        ],
        "risk_factors": [
            "High blood pressure",
            "High cholesterol",
            "Diabetes",
            "Tobacco use",
            "Physical inactivity",
            "Family history"
        ],
        "complications": [
            "Heart attack",
            "Heart failure",
            "Stroke",
            "Abnormal heart rhythms"
        ],
        "prevention": [
            "Do not smoke",
            "Regular physical activity",
            "Balanced nutrition",
            "Manage blood pressure and cholesterol",
            "Regular health checkups"
        ],
        "diagnosis": "Depending on symptoms, evaluation can include blood tests, ECG, imaging and other cardiovascular tests.",
        "treatment": "Treatment depends on the specific condition and can include lifestyle changes, medicines or procedures.",
        "when_to_seek": "New or severe chest pressure, difficulty breathing, fainting or other signs of a possible heart emergency require emergency medical care.",
    },

    "Alzheimer's Disease": {
        "category": "Brain & Nervous System",
        "summary": "Alzheimer's disease is a progressive brain disorder that affects memory, thinking and eventually the ability to perform everyday activities.",
        "symptoms": [
            "Memory loss",
            "Difficulty finding words",
            "Problems with planning",
            "Confusion about time or place",
            "Changes in behavior"
        ],
        "causes": [
            "Complex changes in brain cells",
            "Genetic factors",
            "Age-related biological changes"
        ],
        "risk_factors": [
            "Increasing age",
            "Family history",
            "Certain genetic factors",
            "Cardiovascular health factors"
        ],
        "complications": [
            "Loss of independence",
            "Difficulty with communication",
            "Safety concerns",
            "Increased need for support"
        ],
        "prevention": [
            "Maintain cardiovascular health",
            "Regular physical activity",
            "Stay socially and mentally active",
            "Manage health conditions with professional guidance"
        ],
        "diagnosis": "Evaluation can include medical history, cognitive testing, physical examination and sometimes imaging or laboratory tests.",
        "treatment": "Some medicines may help manage symptoms for certain people. Supportive care and planning are also important.",
        "when_to_seek": "New or rapidly worsening confusion should be medically evaluated because several treatable conditions can cause it.",
    },

    "Kidney Stones": {
        "category": "Kidneys & Urinary System",
        "summary": "Kidney stones are hard deposits that form inside the kidneys and can sometimes travel through the urinary tract.",
        "symptoms": [
            "Sharp pain in the side or back",
            "Pain that may move toward the lower abdomen",
            "Pain during urination",
            "Blood in urine",
            "Nausea"
        ],
        "causes": [
            "High concentrations of certain minerals in urine",
            "Low fluid intake",
            "Some metabolic conditions",
            "Dietary and genetic factors"
        ],
        "risk_factors": [
            "Previous kidney stones",
            "Low fluid intake",
            "Family history",
            "Certain diets",
            "Some medical conditions"
        ],
        "complications": [
            "Urinary blockage",
            "Urinary infection",
            "Kidney problems in severe cases"
        ],
        "prevention": [
            "Adequate fluid intake",
            "Following dietary advice based on stone type",
            "Managing underlying conditions"
        ],
        "diagnosis": "Testing can include urine tests, blood tests and imaging.",
        "treatment": "Treatment depends on stone size and location and may range from monitoring to procedures.",
        "when_to_seek": "Severe pain with fever, chills, vomiting or difficulty urinating requires urgent medical attention.",
    },

    "Tuberculosis": {
        "category": "Infectious Diseases",
        "summary": "Tuberculosis (TB) is an infectious disease caused by bacteria that most commonly affect the lungs.",
        "symptoms": [
            "Persistent cough",
            "Fever",
            "Night sweats",
            "Weight loss",
            "Fatigue"
        ],
        "causes": [
            "Mycobacterium tuberculosis bacteria",
            "Spread through the air from people with certain forms of active TB"
        ],
        "risk_factors": [
            "Close contact with active TB",
            "Crowded living conditions",
            "Weakened immune system",
            "Certain medical conditions"
        ],
        "complications": [
            "Lung damage",
            "Spread to other organs",
            "Severe illness if untreated"
        ],
        "prevention": [
            "Early identification and treatment",
            "Appropriate infection-control measures",
            "Vaccination in countries where recommended"
        ],
        "diagnosis": "Testing can include TB blood tests or skin tests, chest imaging and laboratory examination of respiratory samples.",
        "treatment": "TB requires specific antibiotic treatment over an extended period under medical supervision.",
        "when_to_seek": "Persistent cough, coughing blood, unexplained fever or significant weight loss should be medically evaluated.",
    }
}

# ============================================================
# OTHER DATA
# ============================================================

CATEGORIES = sorted(set(d["category"] for d in DISEASES.values()))

SYMPTOM_MAP = {
    "Headache": ["Migraine", "Influenza (Flu)", "Anemia"],
    "Cough": ["Common Cold", "Influenza (Flu)", "Pneumonia", "Asthma", "Tuberculosis"],
    "Fever": ["Influenza (Flu)", "Dengue", "Pneumonia", "Tuberculosis"],
    "Fatigue": [
        "Anemia",
        "Influenza (Flu)",
        "Type 2 Diabetes",
        "Hypothyroidism",
        "Pneumonia"
    ],
    "Shortness of breath": [
        "Asthma",
        "Pneumonia",
        "Anemia",
        "Heart Disease"
    ],
    "Chest discomfort": ["Heart Disease", "Asthma"],
    "Nausea": ["Migraine", "Kidney Stones", "Gastritis", "Influenza (Flu)"],
    "Dizziness": ["Anemia", "Migraine"],
    "Frequent urination": ["Type 2 Diabetes"],
    "Increased thirst": ["Type 2 Diabetes"],
    "Skin itching": ["Eczema"],
    "Runny nose": ["Common Cold", "Influenza (Flu)"],
    "Abdominal pain": ["Gastritis", "Kidney Stones", "Dengue"]
}

HEALTH_TIPS = [
    "Regular physical activity supports cardiovascular and overall health.",
    "Getting enough sleep is an important part of maintaining health.",
    "Hand washing is one of the simplest ways to reduce the spread of many infections.",
    "Regular health checkups can help identify some health problems early.",
    "Avoiding tobacco products can substantially reduce health risks.",
    "A varied and balanced diet can provide important nutrients your body needs.",
    "Staying hydrated is important, especially during hot weather and physical activity.",
    "Wearing appropriate sun protection can help protect your skin from UV radiation.",
    "Keeping vaccinations up to date can help prevent several infectious diseases.",
    "Mental wellbeing is part of overall health; talking to a trusted person can help when things feel difficult."
]

QUIZ = [
    {
        "q": "Which organ pumps blood around the body?",
        "options": ["Liver", "Heart", "Lung", "Kidney"],
        "answer": "Heart"
    },
    {
        "q": "Which condition is associated with high blood glucose?",
        "options": ["Type 2 Diabetes", "Eczema", "Osteoporosis", "Migraine"],
        "answer": "Type 2 Diabetes"
    },
    {
        "q": "Which disease is caused by Mycobacterium tuberculosis?",
        "options": ["Dengue", "Tuberculosis", "Asthma", "Gastritis"],
        "answer": "Tuberculosis"
    },
    {
        "q": "Which condition affects bone strength?",
        "options": ["Osteoporosis", "Asthma", "Gastritis", "Influenza"],
        "answer": "Osteoporosis"
    },
    {
        "q": "Which illness is commonly transmitted by infected Aedes mosquitoes?",
        "options": ["Dengue", "Migraine", "Eczema", "Anemia"],
        "answer": "Dengue"
    }
]

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_disease" not in st.session_state:
    st.session_state.selected_disease = None

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None

# ============================================================
# FUNCTIONS
# ============================================================

def disease_card(name):
    data = DISEASES[name]

    st.markdown(
        f"""
        <div class="card">
            <h3>🩺 {name}</h3>
            <span class="tag">{data['category']}</span>
            <p>{data['summary']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(f"View information — {name}", key=f"view_{name}"):
        st.session_state.selected_disease = name
        st.session_state.page = "Disease Details"
        st.rerun()


def show_disease(name):
    data = DISEASES[name]

    st.markdown(
        f"""
        <div class="disease-header">
            <span>{data['category']}</span>
            <h1>{name}</h1>
            <p>{data['summary']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← Back to Disease Explorer"):
        st.session_state.page = "Disease Explorer"
        st.session_state.selected_disease = None
        st.rerun()

    st.markdown('<div class="section-title">Symptoms</div>', unsafe_allow_html=True)

    cols = st.columns(2)
    for i, symptom in enumerate(data["symptoms"]):
        with cols[i % 2]:
            st.markdown(f"• {symptom}")

    st.markdown('<div class="section-title">Causes</div>', unsafe_allow_html=True)
    for item in data["causes"]:
        st.markdown(f"• {item}")

    st.markdown('<div class="section-title">Risk factors</div>', unsafe_allow_html=True)
    for item in data["risk_factors"]:
        st.markdown(f"• {item}")

    st.markdown('<div class="section-title">Diagnosis</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info">{data["diagnosis"]}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Treatment & management</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="card">
            <p>{data["treatment"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Possible complications</div>', unsafe_allow_html=True)
    for item in data["complications"]:
        st.markdown(f"• {item}")

    st.markdown('<div class="section-title">Prevention & healthy habits</div>', unsafe_allow_html=True)
    for item in data["prevention"]:
        st.markdown(f"• {item}")

    st.markdown(
        f"""
        <div class="warning">
            <strong>When to seek medical care</strong><br><br>
            {data["when_to_seek"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="small-text">
        This page provides general educational information. It is not a diagnosis
        and should not replace advice from a qualified healthcare professional.
        </div>
        """,
        unsafe_allow_html=True
    )


def go_to(page):
    st.session_state.page = page
    st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;padding:10px 0 20px;">
            <div style="font-size:42px;">🩺</div>
            <h2 style="color:#123b5d;margin:0;">HealthSphere</h2>
            <p style="color:#71808a;font-size:12px;">Health information hub</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    pages = [
        "Home",
        "Disease Explorer",
        "Symptoms Guide",
        "Healthy Living",
        "Health Quiz",
        "Emergency Guide",
        "About"
    ]

    selected_page = st.radio(
        "Navigation",
        pages,
        index=pages.index(st.session_state.page)
        if st.session_state.page in pages else 0
    )

    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.session_state.selected_disease = None
        st.rerun()

    st.divider()

    st.markdown(
        """
        <div class="small-text">
        <strong>Important</strong><br>
        HealthSphere is an educational resource. It does not provide
        personalized diagnosis, treatment or medical advice.
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div style="display:flex;justify-content:space-between;align-items:center;
                padding:5px 0 20px;">
        <div>
            <span style="font-size:28px;font-weight:800;color:#123b5d;">
                HealthSphere
            </span>
            <span style="color:#82919a;font-size:13px;margin-left:10px;">
                Health & Disease Information
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HOME
# ============================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-badge">YOUR HEALTH INFORMATION HUB</div>
            <div class="main-title">
                Understand your health.<br>
                Make informed choices.
            </div>
            <div class="subtitle">
                Explore reliable, easy-to-understand information about diseases,
                symptoms, prevention, healthy living and medical topics.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    search = st.text_input(
        "🔎 Search HealthSphere",
        placeholder="Search diseases, symptoms or health topics..."
    )

    if search:
        query = search.lower().strip()

        results = []

        for name, data in DISEASES.items():
            searchable = (
                name + " " +
                data["category"] + " " +
                data["summary"] + " " +
                " ".join(data["symptoms"])
            ).lower()

            if query in searchable:
                results.append(name)

        if results:
            st.markdown(
                f'<div class="section-title">Search results ({len(results)})</div>',
                unsafe_allow_html=True
            )

            for name in results:
                disease_card(name)
        else:
            st.info("No matching health topics were found.")

    st.markdown(
        '<div class="section-title">Explore HealthSphere</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(3)

    cards = [
        ("🦠", "Diseases & Conditions",
         "Explore information about common diseases and health conditions.",
         "Disease Explorer"),
        ("🧠", "Symptoms",
         "Learn about symptoms and conditions that may be associated with them.",
         "Symptoms Guide"),
        ("🥗", "Healthy Living",
         "Explore general information about healthy habits and prevention.",
         "Healthy Living"),
        ("🧪", "Medical Topics",
         "Understand common tests, prevention and healthcare concepts.",
         "About"),
        ("📝", "Health Quiz",
         "Test your knowledge with a short educational quiz.",
         "Health Quiz"),
        ("🆘", "Emergency Guide",
         "Learn about situations where urgent medical help may be needed.",
         "Emergency Guide")
    ]

    for i, (icon, title, description, target) in enumerate(cards):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="card">
                    <div style="font-size:32px;">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(f"Explore →", key=f"home_{target}_{i}"):
                go_to(target)

    st.markdown(
        '<div class="section-title">Featured Conditions</div>',
        unsafe_allow_html=True
    )

    featured = [
        "Type 2 Diabetes",
        "Hypertension",
        "Asthma",
        "Dengue",
        "Migraine",
        "Heart Disease"
    ]

    cols = st.columns(3)

    for i, name in enumerate(featured):
        with cols[i % 3]:
            disease_card(name)

    tip = random.choice(HEALTH_TIPS)

    st.markdown(
        f"""
        <div class="info">
            <strong>💡 Health tip</strong><br><br>
            {tip}
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# DISEASE EXPLORER
# ============================================================

elif st.session_state.page == "Disease Explorer":

    st.markdown(
        '<div class="main-title">Diseases & Conditions</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Browse health conditions by category or search for a specific condition.</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "🔎 Search diseases",
        placeholder="Example: diabetes, asthma, dengue..."
    )

    category = st.selectbox(
        "Filter by category",
        ["All categories"] + CATEGORIES
    )

    filtered = []

    for name, data in DISEASES.items():

        matches_search = (
            not search or
            search.lower() in name.lower() or
            search.lower() in data["summary"].lower()
        )

        matches_category = (
            category == "All categories" or
            data["category"] == category
        )

        if matches_search and matches_category:
            filtered.append(name)

    st.markdown(
        f'<div class="section-title">{len(filtered)} conditions</div>',
        unsafe_allow_html=True
    )

    if filtered:
        cols = st.columns(2)

        for i, name in enumerate(filtered):
            with cols[i % 2]:
                disease_card(name)
    else:
        st.info("No conditions matched your search.")

# ============================================================
# DISEASE DETAILS
# ============================================================

elif st.session_state.page == "Disease Details":

    if st.session_state.selected_disease:
        show_disease(st.session_state.selected_disease)
    else:
        st.session_state.page = "Disease Explorer"
        st.rerun()

# ============================================================
# SYMPTOMS GUIDE
# ============================================================

elif st.session_state.page == "Symptoms Guide":

    st.markdown(
        '<div class="main-title">Symptoms Guide</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            Select a symptom to explore health conditions that can sometimes
            be associated with it.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="warning">
            <strong>Important:</strong>
            A symptom can have many possible causes. This guide is for
            education only and cannot determine what condition a person has.
        </div>
        """,
        unsafe_allow_html=True
    )

    symptom = st.selectbox(
        "Choose a symptom",
        sorted(SYMPTOM_MAP.keys())
    )

    st.markdown(
        f'<div class="section-title">Information about "{symptom}"</div>',
        unsafe_allow_html=True
    )

    possible = SYMPTOM_MAP[symptom]

    st.markdown(
        f"""
        <div class="card">
            <p>
            <strong>{symptom}</strong> can occur with many different health
            conditions. The conditions below are examples associated with
            this symptom and are not a diagnosis.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    for name in possible:
        data = DISEASES[name]

        st.markdown(
            f"""
            <div class="card">
                <h3>{name}</h3>
                <span class="tag">{data['category']}</span>
                <p>{data['summary']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(f"Read about {name}", key=f"symptom_{name}"):
            st.session_state.selected_disease = name
            st.session_state.page = "Disease Details"
            st.rerun()

# ============================================================
# HEALTHY LIVING
# ============================================================

elif st.session_state.page == "Healthy Living":

    st.markdown(
        '<div class="main-title">Healthy Living</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            General health information about everyday habits that can support
            wellbeing.
        </div>
        """,
        unsafe_allow_html=True
    )

 topics = [
    (
        "🥗 Nutrition",
        "A balanced eating pattern can include a variety of vegetables, "
        "fruits, whole grains, protein sources and other nutrient-rich foods. "
        "Individual nutritional needs vary."
    ),
    (
        "😴 Sleep",
        "Regular, sufficient sleep supports physical and mental health. "
        "Keeping a consistent sleep schedule and having a comfortable, "
        "quiet sleep environment can help."
    ),
    (
        "🏃 Physical Activity",
        "Regular physical activity can support heart health, bone health, "
        "strength, mobility and mental wellbeing. Activity should be "
        "appropriate for a person's age and abilities."
    ),
    (
        "🧼 Hygiene",
        "Hand hygiene, respiratory etiquette and appropriate food hygiene "
        "can reduce the spread of many infections."
    ),
    (
        "🧠 Mental Wellbeing",
        "Mental health is part of overall health. Staying connected with "
        "trusted people, maintaining healthy routines and seeking "
        "professional support when needed can be beneficial."
    ),
    (
        "☀️ Sun Protection",
        "Limiting excessive UV exposure, using appropriate protective "
        "clothing and following local sun-safety guidance can help protect "
        "skin."
    ),
    (
        "🚭 Tobacco",
        "Avoiding tobacco and exposure to tobacco smoke reduces the risk "
        "of many serious health conditions."
    ),
    (
        "💧 Hydration",
        "Fluid needs vary depending on age, activity, climate and health. "
        "Water is a common way to maintain hydration."
    )
]

    cols = st.columns(2)

    for i, (title, text) in enumerate(topics):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <h3>{title}</h3>
                    <p>{text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div class="info">
            Healthy living recommendations can differ depending on age,
            medical conditions, medications and individual circumstances.
            A healthcare professional can provide personalized guidance.
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# QUIZ
# ============================================================

elif st.session_state.page == "Health Quiz":

    st.markdown(
        '<div class="main-title">Health Knowledge Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Test your general health knowledge.</div>',
        unsafe_allow_html=True
    )

    answers = []

    for i, item in enumerate(QUIZ):

        st.markdown(
            f"""
            <div class="card">
                <h3>Question {i + 1}</h3>
                <p style="font-size:17px;color:#123b5d;">
                    <strong>{item["q"]}</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        answer = st.radio(
            "Choose an answer",
            item["options"],
            key=f"quiz_{i}",
            index=None
        )

        answers.append(answer)

    if st.button("Check my score", type="primary"):

        score = 0

        for i, item in enumerate(QUIZ):
            if answers[i] == item["answer"]:
                score += 1

        st.session_state.quiz_score = score

    if st.session_state.quiz_score is not None:

        score = st.session_state.quiz_score

        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:48px;">🎉</div>
                <h2 style="color:#123b5d;">
                    Your score: {score}/{len(QUIZ)}
                </h2>
                <p>
                    This quiz is for educational purposes and does not
                    assess your health.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Try again"):
            st.session_state.quiz_score = None
            st.rerun()

# ============================================================
# EMERGENCY GUIDE
# ============================================================

elif st.session_state.page == "Emergency Guide":

    st.markdown(
        '<div class="main-title">Emergency Guide</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            General information about situations that may require urgent
            medical attention.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="emergency">
            <strong>🚨 If someone may be experiencing a medical emergency,
            contact your local emergency service immediately.</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

    emergencies = [
        (
            "❤️ Possible heart emergency",
            "New or severe chest pressure or discomfort, especially when
            accompanied by difficulty breathing, fainting, sweating or other
            concerning symptoms, needs urgent medical evaluation."
        ),
        (
            "🧠 Possible stroke",
            "Sudden facial weakness, arm weakness, speech difficulty,
            confusion or other sudden neurological changes require emergency
            medical attention."
        ),
        (
            "🫁 Severe breathing difficulty",
            "Severe or rapidly worsening difficulty breathing can be an
            emergency."
        ),
        (
            "🩸 Severe bleeding",
            "Heavy or uncontrolled bleeding requires urgent medical attention."
        ),
        (
            "🧠 Sudden severe headache",
            "A sudden, extremely severe or unusual headache, particularly
            with neurological symptoms, needs urgent medical evaluation."
        ),
        (
            "⚠️ Severe allergic reaction",
            "Sudden difficulty breathing, swelling of the face or throat,
            fainting or rapidly worsening symptoms can indicate a serious
            allergic reaction."
        )
    ]

    for title, description in emergencies:
        st.markdown(
            f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="warning">
            <strong>Do not rely on HealthSphere during an emergency.</strong>
            This website cannot assess a person in real time. Contact your
            local emergency service or seek immediate professional medical care.
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# ABOUT
# ============================================================

elif st.session_state.page == "About":

    st.markdown(
        '<div class="main-title">About HealthSphere</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            A simple health-information project designed to make medical
            topics easier to explore.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <h3>🩺 Our purpose</h3>
            <p>
                HealthSphere is designed as an educational health-information
                website. It organizes general information about diseases,
                symptoms, prevention and healthy living into an easy-to-use
                interface.
            </p>
        </div>

        <div class="card">
            <h3>📚 Medical information</h3>
            <p>
                Medical information should be checked against authoritative
                sources and reviewed by qualified healthcare professionals.
                Content on this demonstration application should not be
                treated as personalized medical advice.
            </p>
        </div>

        <div class="card">
            <h3>🔒 Privacy</h3>
            <p>
                This demonstration application does not require users to
                create an account or enter personal medical information.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Recommended sources</div>',
        unsafe_allow_html=True
    )

    sources = [
        ("World Health Organization", "https://www.who.int/"),
        ("Centers for Disease Control and Prevention", "https://www.cdc.gov/"),
        ("National Institutes of Health", "https://www.nih.gov/"),
        ("MedlinePlus", "https://medlineplus.gov/"),
        ("NHS", "https://www.nhs.uk/")
    ]

    for name, url in sources:
        st.markdown(
            f"""
            <div class="source">
                <strong>{name}</strong><br>
                <a href="{url}" target="_blank">{url}</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    f"""
    <div style="text-align:center;padding:15px 0 25px;">
        <div style="font-size:20px;font-weight:700;color:#123b5d;">
            🩺 HealthSphere
        </div>
        <div class="small-text">
            Health information for educational purposes •
            Not a substitute for professional medical advice
        </div>
        <div class="small-text" style="margin-top:8px;">
            © {datetime.now().year} HealthSphere
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
