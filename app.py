import streamlit as st
import time
import json
from agent import SupervisorAgent

# --- PAGE CONFIGURATION (The Foundation) ---
st.set_page_config(
    page_title="CareerAgent Pro",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (The "Polish") ---
# This removes the default "clunky" Streamlit look and adds a "Glassmorphism" effect.
st.markdown("""
<style>
    /* 1. Remove Top Padding (Golden Rule: Maximize Screen Real Estate) */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* 2. Global Dark Theme Adjustments */
    [data-testid="stAppViewContainer"] {
        background-color: #0E1117;
    }
    
    /* 3. Card Styling for Metrics (Golden Rule: Group Related Info) */
    .metric-card {
        background-color: #262730;
        border: 1px solid #41444C;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        text-align: center;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4CAF50;
    }
    .metric-label {
        font-size: 1rem;
        color: #FAFAFA;
        opacity: 0.8;
    }
    
    /* 4. AI Insight Box (Golden Rule: Highlight Key Feedback) */
    .ai-box {
        background-color: #1E293B; /* Slate Blue */
        border-left: 5px solid #3B82F6; /* Bright Blue Accent */
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    
    /* 5. Sidebar Polish */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZATION ---
if 'agent' not in st.session_state:
    st.session_state.agent = SupervisorAgent()

# --- SIDEBAR: CONTEXT & MEMORY ---
with st.sidebar:
    st.title("🧠 Agent Memory")
    st.markdown("---")
    
    # Visualizing Memory State
    st.caption("Live Cognitive State")
    try:
        with open("memory.json", "r") as f:
            data = json.load(f)
            # Just show the last log to keep it clean
            if data.get("logs"):
                st.json(data["logs"][-1], expanded=True)
            else:
                st.info("Memory Empty - Start a session.")
    except:
        st.text("Memory Initialize...")

    st.markdown("---")
    if st.button("🗑️ Hard Reset System", use_container_width=True):
        import os
        if os.path.exists("memory.json"):
            os.remove("memory.json")
            st.rerun()

# --- MAIN LAYOUT ---
# Header Section
c1, c2 = st.columns([3, 1])
with c1:
    st.title("🚀 CareerAgent OS")
    st.caption("Bloom's Taxonomy • Real-Time Velocity • Market Alignment")
with c2:
    # Just a visual badge
    st.markdown("""
    <div style="text-align: right; padding-top: 20px;">
        <span style="background-color:#4CAF50; padding: 5px 10px; border-radius: 15px; font-size: 12px; font-weight: bold;">● SYSTEM ONLINE</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Main Interaction Area (2 Columns)
col_plan, col_feedback = st.columns([1, 1], gap="large")

# === LEFT COLUMN: STRATEGY ENGINE ===
with col_plan:
    st.subheader("1. Strategic Planning")
    st.info("Define your target. The Agent scans 2025 market data.")
    
    role = st.text_input("Target Role", value="AI Engineer", placeholder="e.g., Full Stack Developer")
    
    if st.button("Generate Roadmap ➔", type="primary", use_container_width=True):
        with st.status("⚡ Agent Swarm Active...", expanded=True) as status:
            st.write("🌍 **Researcher:** Scanning DuckDuckGo (2025)...")
            time.sleep(0.8)
            st.write("📊 **Analyst:** Calculating Learning Velocity...")
            time.sleep(0.8)
            st.write("🤖 **Supervisor:** Synthesizing Bloom's Strategy...")
            
            roadmap = st.session_state.agent.create_roadmap(role)
            st.session_state.roadmap = roadmap
            status.update(label="✅ Strategy Locked", state="complete", expanded=False)
    
    # Display Roadmap in a clean container
    if 'roadmap' in st.session_state:
        with st.container(border=True):
            st.markdown(st.session_state.roadmap)

# === RIGHT COLUMN: ADAPTIVE FEEDBACK LOOP ===
with col_feedback:
    st.subheader("2. Weekly Feedback Loop")
    st.warning("Talk to the Agent. It listens for 'Gaps' (Recall vs. Concept).")
    
    user_log = st.text_area("Weekly Reflection", height=100, placeholder="e.g., 'I tried building the app but I kept forgetting the syntax for API calls.'")
    
    if st.button("Analyze Progress 🧠", use_container_width=True):
        if not user_log:
            st.error("Please write a reflection first.")
        else:
            with st.spinner("🔍 Diagnosing Cognitive State..."):
                # 1. Run Analysis
                adaptation = st.session_state.agent.run_adaptive_cycle(user_log)
                
                # 2. Fetch Data
                logs = st.session_state.agent.memory.get_context()["logs"]
                last_metric = logs[-1]["metrics"]
                
                # 3. Save to Session State (Persistence)
                st.session_state.feedback_result = {
                    "adaptation": adaptation,
                    "score": last_metric['score'],
                    "gap": last_metric['focus_gap'],
                    "reasoning": last_metric.get('reasoning', "Analysis Complete.")
                }
            st.rerun()

    # --- PERSISTENT RESULTS DASHBOARD (The "Golden" Part) ---
    if 'feedback_result' in st.session_state:
        res = st.session_state.feedback_result
        
        st.markdown("### 📊 Cognitive Diagnosis")
        
        # Custom HTML Cards for Metrics (Better than st.metric)
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{res['score']}</div>
                <div class="metric-label">Bloom's Score</div>
            </div>
            """, unsafe_allow_html=True)
        with m_col2:
            # Color code the gap type
            gap_color = "#FF5252" if "GAP" in res['gap'] else "#4CAF50"
            st.markdown(f"""
            <div class="metric-card" style="border-color: {gap_color};">
                <div class="metric-value" style="color: {gap_color}; font-size: 1.8rem;">{res['gap']}</div>
                <div class="metric-label">Detected State</div>
            </div>
            """, unsafe_allow_html=True)

        # AI Reasoning Box (The "Why")
        st.markdown(f"""
        <div class="ai-box">
            <b>💡 AI Reasoning:</b><br>
            <i>"{res['reasoning']}"</i>
        </div>
        """, unsafe_allow_html=True)
        
        # New Directive
        with st.expander("🛠️ View Adaptive Plan", expanded=True):
            st.write(res['adaptation'])