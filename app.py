from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    projects = [

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
        }
    ]

    # Skills grouped per user's resume categories
    skills = {
        "Languages": ["Python", "C++", "Java"],
        "Libraries": ["Scikit-learn", "Pandas", "NumPy", "Matplotlib"],
        "Tools": ["Git", "GitHub", "Google Colab"],
        "Database": ["MySQL"]
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
        "Scikit-learn": "scikitlearn",
        "Pandas": "pandas",
        "NumPy": "numpy",
        "Matplotlib": "matplotlib",
        "Git": "git",
        "GitHub": "github",
        "Google Colab": "googlecolab",
        "MySQL": "mysql"
    }

    skill_icons = {}
    base = "https://cdn.jsdelivr.net/npm/simple-icons@v7/icons/{slug}.svg"
    for cat, items in skills.items():
        for s in items:
            slug = slug_map.get(s)
            if slug:
                url = base.format(slug=slug)
                # use <img> so the SVG loads as an image; fallback to initials if loading blocked
                skill_icons[s] = f'<img src="{url}" alt="{s} logo" class="skill-logo"/>'
            else:
                skill_icons[s] = svg_initials(s)

    achievements = [

        "Qualified Round 1 of Meta PyTorch OpenEnv Hackathon",
        "Ranked 256 out of 600+ participants in Smart BU Hackathon",
        "Solved 100+ problems on different platforms like LeetCode and GeeksforGeeks",
        "Participant at AMD AI Reinforcement Learning Hackathon, IIT Delhi"
    ]

    certifications = [

        "Google - The Bits and Bytes of Computer Networking",
        "Infosys Springboard - Data Structures and Algorithms",
        "IBM - Introduction to Data Analytics",
        "Google - Operating Systems and You: Becoming a Power User",
        "NPTEL - Software Engineering"
    ]

    return render_template(
        "index.html",
        projects=projects,
        skills=skills,
        skill_icons=skill_icons,
        achievements=achievements,
        certifications=certifications
    )


if __name__ == "__main__":
    app.run(debug=True)