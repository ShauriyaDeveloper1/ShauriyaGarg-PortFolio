from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    projects = [

        {
            "title": "Aadhaar Enrollment Analytics Dashboard",
            "description": "Interactive analytics dashboard with charts and KPI metrics.",
            "tech": ["FastAPI", "React", "Plotly"],
            "github": "https://github.com/ShauriyaDeveloper1/Adhaar-Enrollment-Dashboard",
            "demo": "https://adhaar-enrollment-dashboard-jkkj.vercel.app/",
            "image": "aadhaar.png"
        },

        {
            "title": "AI-Powered Interview Coach",
            "description": "AI platform using NLP, RL, speech analysis and posture tracking.",
            "tech": ["Python", "Flask", "OpenCV", "PyTorch"],
            "github": "https://github.com/ShauriyaDeveloper1/AI-Powered-Interview-Coach",
            "demo": "https://huggingface.co/spaces/Shauriya24/AI-Powered-Interview-Coach",
            "image": "ai.png"
        },

        {
            "title": "VoiceShield - AI Voice Deepfake Detection",
            "description": "Real-time AI voice deepfake detection and call security platform with AASIST neural networks.",
            "tech": ["Python", "FastAPI", "React", "Kotlin", "PyTorch", "Supabase"],
            "github": "https://github.com/ShauriyaDeveloper1/voice-shield",
            "demo": None,
            "image": "voiceshield.jpeg",
            "portrait": True
        }
    ]

    # Skills grouped per user's resume categories
    skills = {
        "Languages": ["C++", "Python", "Java", "SQL"],
        "Frameworks": ["Flask", "FastAPI", "Streamlit"],
        "Tools/Platforms": ["Git", "GitHub", "MySQL", "Firebase", "Power BI"],
        "Core CS": ["Data Structures & Algorithms", "OOP", "DBMS", "Operating Systems", "Computer Networks"]
    }

    # Material icon mapping for skill categories
    skill_category_icons = {
        "Languages": "code",
        "Frameworks": "layers",
        "Tools/Platforms": "build",
        "Core CS": "developer_board"
    }

    # Color accents for skill categories
    skill_category_colors = {
        "Languages": "accent-cyan",
        "Frameworks": "secondary",
        "Tools/Platforms": "primary",
        "Core CS": "tertiary"
    }

    achievements = [
        {
            "title": "Meta PyTorch OpenEnv Hackathon",
            "badge": "Top 2.5% Nationwide",
            "description": "Selected among the top 800 teams from 31,000+ registered teams nationwide.",
            "stat": "Scale: 31,000+ Competitors",
            "icon": "military_tech",
            "color": "accent-cyan"
        },
        {
            "title": "Smart BU Hackathon",
            "badge": "Rank 256 Placement",
            "description": "Secured Rank 256 among 600+ participating university teams.",
            "stat": "Cohort: 600+ Teams",
            "icon": "trophy",
            "color": "secondary"
        },
        {
            "title": "LeetCode Mastery",
            "badge": "Data Structures & Algos",
            "description": "Solved 300+ DSA problems across arrays, linked lists, trees and graphs.",
            "stat": "Focus: Dynamic Programming & Graphs",
            "icon": "terminal",
            "color": "primary"
        }
    ]

    certifications = [
        {
            "issuer": "NPTEL",
            "title": "Software Engineering",
            "description": "Foundations of lifecycle design & architecture.",
            "icon": "workspace_premium",
            "color": "primary"
        },
        {
            "issuer": "Microsoft",
            "title": "Azure AI Fundamentals",
            "description": "Cloud AI workloads & Azure ML compute.",
            "icon": "cloud",
            "color": "accent-cyan"
        },
        {
            "issuer": "Microsoft",
            "title": "Fabric Data Engineer Associate",
            "description": "Enterprise data analytics & warehousing pipelines.",
            "icon": "dataset",
            "color": "secondary"
        },
        {
            "issuer": "Google",
            "title": "Bits & Bytes of Networking",
            "description": "TCP/IP protocols, routing, & network security.",
            "icon": "lan",
            "color": "tertiary"
        }
    ]

    experience = [
        {
            "role": "AI Web Development Intern",
            "company": "InAmigos Foundation",
            "location": "Remote",
            "date": "June 2026",
            "description": "Developed AI-powered solutions and contributed to NGO website enhancement by analyzing existing platforms, designing new features, and creating responsive web interfaces using modern development tools.",
            "tools": ["Python", "AI APIs", "Responsive UI"]
        }
    ]

    education = [
        {
            "role": "Bachelor of Technology - Computer Science and Engineering",
            "company": "Bennett University",
            "location": "Uttar Pradesh, India",
            "date": "Aug 2024 – May 2028",
            "description": "Specialization in Data Science. Favorite Courses: Object Oriented Programming, Data Structures, Analysis of Algorithms, Data Science.",
            "highlight": "CGPA: 9.43"
        },
        {
            "role": "Intermediate",
            "company": "Renaissance School",
            "location": "Bulandshahr",
            "date": "Apr 2022 – Mar 2024",
            "description": "Curriculum Focus: Physics, Chemistry, Mathematics, Computer Science.",
            "highlight": "Aggregate: 89.4%"
        },
        {
            "role": "Matriculation",
            "company": "Sunrise Public School",
            "location": "Siyana, Bulandshahr",
            "date": "Apr 2020 – Mar 2022",
            "description": "Foundational general sciences and quantitative mathematics.",
            "highlight": "Percentage: 87%"
        }
    ]

    return render_template(
        "index.html",
        projects=projects,
        skills=skills,
        skill_category_icons=skill_category_icons,
        skill_category_colors=skill_category_colors,
        achievements=achievements,
        certifications=certifications,
        experience=experience,
        education=education
    )


if __name__ == "__main__":
    app.run(debug=True)