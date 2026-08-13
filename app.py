from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    projects = [

        {
            "title": "SMS Spam Detector",

            "description":
            "NLP-based spam classification system with 96% accuracy.",

            "tech":
            "Scikit-learn, Streamlit",

            "github":
            "https://github.com/ShauriyaDeveloper1/SMS-Spam-Detector",

            "demo":
            "https://shauriyadeveloper1-sms-spam-detector-app-sqhwfy.streamlit.app/",
            "image": "sms.png"
        },

        {
            "title": "Aadhaar Enrollment Analytics Dashboard",

            "description":
            "Interactive analytics dashboard with charts and KPI metrics.",

            "tech":
            "FastAPI, React, Plotly",

            "github":
            "https://github.com/ShauriyaDeveloper1/Adhaar-Enrollment-Dashboard",

            "demo":
            "https://adhaar-enrollment-dashboard-jkkj.vercel.app/",
            "image": "aadhaar.png"
        },

        {
            "title": "AI-Powered Interview Coach",

            "description":
            "AI platform using NLP, RL, speech analysis and posture tracking.",

            "tech":
            "Python, Flask, OpenCV, PyTorch",

            "github":
            "https://github.com/ShauriyaDeveloper1/AI-Powered-Interview-Coach",

            "demo":
            "https://huggingface.co/spaces/Shauriya24/AI-Powered-Interview-Coach",
            "image": "ai.png"
        }
    ]

    # Skills grouped per user's resume categories
    skills = {
        "Languages": ["C++", "Python", "Java", "SQL"],
        "Frameworks": ["Flask", "FastAPI", "Streamlit"],
        "Tools/Platforms": ["Git", "GitHub", "MySQL", "Firebase", "Power BI"],
        "Core CS": ["Data Structures & Algorithms", "OOP", "DBMS", "Operating Systems", "Computer Networks"]
    }
    # Simple SVG initials generator for skill 'logos'
    def svg_initials(label, size=28):
        # pick a deterministic color from a palette
        palette = ["#06b6d4", "#7c5cff", "#38bdf8", "#2563eb", "#14b8a6", "#fb7185"]
        key = sum(ord(c) for c in label) % len(palette)
        color = palette[key]
        # initials: take up to 2 characters
        clean = ''.join(ch for ch in label if ch.isalnum())
        initials = (clean[:2] or label[:2]).upper()
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}" aria-hidden="true"><circle cx="{size/2}" cy="{size/2}" r="{size/2}" fill="{color}" opacity="0.14"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Poppins, sans-serif" font-size="10" fill="{color}" font-weight="600">{initials}</text></svg>'''
        return svg

    # build icon map for all skills
    # try to use brand logos from Simple Icons CDN for known skills, else fallback to initials
    slug_map = {
        "Python": "python",
        "C++": "cplusplus",
        "Java": "java",
        "SQL": "mysql",
        "Flask": "flask",
        "FastAPI": "fastapi",
        "Streamlit": "streamlit",
        "Git": "git",
        "GitHub": "github",
        "MySQL": "mysql",
        "Firebase": "firebase",
        "Power BI": "powerbi"
    }

    skill_icons = {}
    base = "https://cdn.jsdelivr.net/npm/simple-icons@v7/icons/{slug}.svg"
    flat_skills = []
    for cat, items in skills.items():
        for s in items:
            slug = slug_map.get(s)
            url = base.format(slug=slug) if slug else ""
            if slug:
                # use <img> so the SVG loads as an image; fallback to initials if loading blocked
                skill_icons[s] = f'<img src="{url}" alt="{s} logo" class="skill-logo"/>'
                flat_skills.append({"name": s, "icon": url})
            else:
                skill_icons[s] = svg_initials(s)
                # Note: For Matter.js we need a solid image, since SVG string might not load directly into canvas easily.
                # But we can try to use a data URI for the SVG!
                svg_string = skill_icons[s].replace('"', "'")
                data_uri = f"data:image/svg+xml;utf8,{svg_string}"
                flat_skills.append({"name": s, "icon": data_uri})

    achievements = [
        "Meta PyTorch OpenEnv Hackathon: Selected among the top 800 teams from 31,000+ registered teams nationwide.",
        "Smart BU Hackathon: Secured Rank 256 among 600+ participating teams.",
        "LeetCode: Solved 300+ DSA problems across arrays, linked lists, trees and graphs."
    ]

    certifications = [
        "Certification of Software Engineering by NPTEL.",
        "Certificate of Operating Systems and You: Becoming a Power User by Google",
        "Certification for Data Structure and Algorithm by Infosys Springboard",
        "Certification for The Bits and Bytes of Computing Networking by Google"
    ]

    experience = [
        {
            "role": "AI Web Development Intern",
            "company": "InAmigos Foundation",
            "location": "Remote",
            "date": "June 2026",
            "description": "Developed AI-powered solutions and contributed to NGO website enhancement by analyzing existing platforms, designing new features, and creating responsive web interfaces using modern development tools."
        }
    ]

    education = [
        {
            "role": "Bachelor of Technology - Computer Science and Engineering",
            "company": "Bennett University",
            "location": "Uttar Pradesh, India",
            "date": "August 2024 - May 2028",
            "description": "CGPA: 9.43. Favorite Courses: Object Oriented Programming, Data Structures, Analysis Of Algorithms, Data Science."
        },
        {
            "role": "Intermediate",
            "company": "Renaissance School",
            "location": "Bulandshahr",
            "date": "April 2022 - March 2024",
            "description": "Percentage: 89.4%. Favorite Courses: Physics, Chemistry, Mathematics, Computer Science."
        },
        {
            "role": "Matriculation",
            "company": "Sunrise Public School",
            "location": "Siyana, Bulandshahr",
            "date": "April 2020 - March 2022",
            "description": "Percentage: 87%."
        }
    ]

    import json

    return render_template(
        "index.html",
        projects=projects,
        skills=skills,
        skill_icons=skill_icons,
        flat_skills=json.dumps(flat_skills),
        achievements=achievements,
        certifications=certifications,
        experience=experience,
        education=education
    )


if __name__ == "__main__":
    app.run(debug=True)