import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import time
from streamlit_lottie import st_lottie
import json
import base64

# ---- Futuristic Theme ----
def set_futuristic_theme():
    st.markdown(f"""
    <style>
        /* Main theme */
        .main {{
            background-color: #0f0e17;
            color: #fffffe;
        }}
        
        /* Sidebar */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #0f0e17 0%, #1a1a2e 100%) !important;
            border-right: 1px solid #4a4a8a;
        }}
        
        /* Buttons */
        .stButton>button {{
            background: linear-gradient(90deg, #6246ea 0%, #d16ba5 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        
        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(98, 70, 234, 0.4);
        }}
        
        /* Cards */
        .card {{
            background: rgba(30, 30, 60, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid #4a4a8a;
            transition: all 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(98, 70, 234, 0.3);
        }}
        
        /* Input fields */
        .stTextArea textarea, .stTextInput input {{
            background-color: rgba(15, 14, 23, 0.8) !important;
            color: #fffffe !important;
            border: 1px solid #4a4a8a !important;
            border-radius: 12px !important;
        }}
        
        /* Progress bars */
        .stProgress > div > div > div {{
            background: linear-gradient(90deg, #6246ea 0%, #d16ba5 100%);
        }}
        
        /* Custom animations */
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        
        .floating {{
            animation: float 6s ease-in-out infinite;
        }}
    </style>
    """, unsafe_allow_html=True)

# ---- App Layout ----
def main():
    set_futuristic_theme()
    
    # Sidebar Navigation
    with st.sidebar:
        st.title("🚀 Smart Revise")
        nav_option = st.radio(
            "Navigation",
            ["📚 My Notes", "🧠 Generate Quiz", "📊 Dashboard"],
            label_visibility="collapsed"
        )
        
        st.divider()
        
        # Futuristic user profile
        with stylable_container(
            key="profile",
            css_styles="""
                {{
                    background: rgba(30, 30, 60, 0.7);
                    border-radius: 16px;
                    padding: 15px;
                    margin: 10px 0;
                }}
            """
        ):
            st.markdown("👤 **User Profile**")
            st.markdown("🎯 **Level:** 5")
            st.markdown("⭐ **XP:** 1200/2000")
            st.progress(0.6)
    
    # Main Content
    if nav_option == "📚 My Notes":
        show_notes_page()
    elif nav_option == "🧠 Generate Quiz":
        show_quiz_page()
    elif nav_option == "📊 Dashboard":
        show_dashboard()

# ---- Pages ----
def show_notes_page():
    st.header("📚 Quantum Notes")
    
    # Futuristic file uploader
    with stylable_container(
        key="uploader",
        css_styles="""
            {{
                border: 2px dashed #4a4a8a;
                border-radius: 16px;
                padding: 30px;
                text-align: center;
                margin: 20px 0;
                transition: all 0.3s ease;
            }}
            :hover {{
                border-color: #6246ea;
                background: rgba(98, 70, 234, 0.1);
            }}
        """
    ):
        st.markdown("""<div class='floating'>📎</div>""", unsafe_allow_html=True)
        st.markdown("### Drag and drop files here")
        st.markdown("Or")
        uploaded_file = st.file_uploader(
            "Browse files", 
            type=["txt", "md", "pdf"],
            label_visibility="collapsed"
        )
    
    # Notes editor
    with stylable_container(
        key="editor",
        css_styles="""
            {{
                background: rgba(30, 30, 60, 0.7);
                border-radius: 16px;
                padding: 20px;
            }}
        """
    ):
        notes = st.text_area(
            "Create new notes",
            height=200,
            placeholder="Type or paste your notes here...",
            label_visibility="collapsed"
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("💾 Save Notes", use_container_width=True):
                st.success("Notes saved to quantum memory!")
        with col2:
            if st.button("⚡ Generate Quiz", use_container_width=True):
                st.session_state.page = "🧠 Generate Quiz"
                st.rerun()

def show_quiz_page():
    st.header("🧠 Neural Quiz Generator")
    
    # Quiz type selector
    with stylable_container(
        key="quiz_type",
        css_styles="""
            {{
                background: rgba(30, 30, 60, 0.7);
                border-radius: 16px;
                padding: 20px;
                margin-bottom: 20px;
            }}
        """
    ):
        quiz_type = st.radio(
            "Select quiz mode:",
            ["⚡ Flash Quiz", "🧠 Deep Recall", "📚 Comprehensive"],
            horizontal=True
        )
    
    # Generated questions
    with stylable_container(
        key="question_card",
        css_styles="""
            {{
                background: rgba(30, 30, 60, 0.7);
                border-radius: 16px;
                padding: 20px;
                margin: 10px 0;
            }}
        """
    ):
        st.markdown("### What is the primary purpose of photosynthesis?")
        
        # Answer options with hover effects
        options = [
            "Convert sunlight to chemical energy",
            "Absorb water from soil",
            "Regulate plant temperature",
            "Produce oxygen as byproduct"
        ]
        
        selected = st.radio(
            "Select your answer:",
            options,
            index=None,
            label_visibility="collapsed"
        )
        
        if selected:
            if selected == options[0]:
                st.success("✅ Correct! +10 XP")
            else:
                st.error("❌ Incorrect. The correct answer is: " + options[0])
    
    # Quiz controls
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🔄 New Question", use_container_width=True)
    with col2:
        st.button("📊 Show Explanation", use_container_width=True)
    with col3:
        st.button("🚀 Submit All", type="primary", use_container_width=True)

def show_dashboard():
    st.header("📊 Neuro Dashboard")
    
    # Stats cards
    col1, col2, col3 = st.columns(3)
    with col1:
        with stylable_container(
            key="stat1",
            css_styles="""
                {{
                    background: linear-gradient(135deg, #6246ea 0%, #d16ba5 100%);
                    border-radius: 16px;
                    padding: 20px;
                    color: white;
                }}
            """
        ):
            st.metric("🧠 Concepts Mastered", "24", "+3 this week")
    
    with col2:
        with stylable_container(
            key="stat2",
            css_styles="""
                {{
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    border-radius: 16px;
                    padding: 20px;
                    color: white;
                }}
            """
        ):
            st.metric("⏱️ Avg Response Time", "2.4s", "-0.3s")
    
    with col3:
        with stylable_container(
            key="stat3",
            css_styles="""
                {{
                    background: linear-gradient(135deg, #0f3460 0%, #533483 100%);
                    border-radius: 16px;
                    padding: 20px;
                    color: white;
                }}
            """
        ):
            st.metric("📅 Upcoming Reviews", "5", "2 due tomorrow")
    
    # Progress chart
    with stylable_container(
        key="progress",
        css_styles="""
            {{
                background: rgba(30, 30, 60, 0.7);
                border-radius: 16px;
                padding: 20px;
                margin-top: 20px;
            }}
        """
    ):
        st.markdown("### 🚀 Knowledge Growth")
        # Placeholder for chart with correct width parameter
        st.image("https://via.placeholder.com/800x400/1a1a2e/ffffff?text=Progress+Analytics", 
                use_container_width=True)  # Updated parameter here

if __name__ == "__main__":
    main()
