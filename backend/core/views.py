from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PortfolioDataSerializer


@api_view(["GET"])
def get_portfolio_data(request):
    """
    API endpoint pour récupérer les données du portfolio
    Support multilingue via le paramètre ?lang=fr ou ?lang=en
    """
    lang = request.query_params.get("lang", "fr")

    if lang == "en":
        data = {
            "name": "Lylian Challier",
            "title": "Curious & Passionate about Mathematics, AI, and Science.",
            "description": "Master's student in Applied Mathematics & Artificial Intelligence at Institut de Mathématiques d'Orsay, Université Paris-Saclay. I love to explore how math can solve real-world problems.",
            "current_work": "Currently interning at LISN/CNRS, working on symbolic regression to model turbulent convection near walls. I'm focusing on three main methods: SINDy, Gene Expression Programming (GEP), and Kolmogorov-Arnold Network (KAN).",
            "projects": [
                {
                    "title": "Variational Auto-Encoders",
                    "description": "implementation & Streamlit app",
                    "link": "https://lylianchallier-vae.streamlit.app/",
                },
                {
                    "title": "Electricity demand forecasting",
                    "description": "using Deep Learning",
                },
                {"title": "Net-Load Forecasting", "description": "in R"},
                {
                    "title": "Movie recommendation system",
                    "description": "using unsupervised learning",
                },
            ],
            "contact": {
                "email": "lylian.challier@universite-paris-saclay.fr",
                "linkedin": "https://linkedin.com/in/lylian-challier",
            },
            "tools": [
                {
                    "name": "CSS3",
                    "badge": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
                },
                {
                    "name": "Git",
                    "badge": "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
                },
                {
                    "name": "HTML5",
                    "badge": "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
                },
                {
                    "name": "LaTeX",
                    "badge": "https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white",
                },
                {
                    "name": "NumPy",
                    "badge": "https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white",
                },
                {
                    "name": "Pandas",
                    "badge": "https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white",
                },
                {
                    "name": "Python",
                    "badge": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
                },
                {
                    "name": "PyTorch",
                    "badge": "https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white",
                },
                {
                    "name": "R",
                    "badge": "https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white",
                },
                {
                    "name": "Scikit-learn",
                    "badge": "https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white",
                },
                {
                    "name": "Streamlit",
                    "badge": "https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white",
                },
                {
                    "name": "SQL",
                    "badge": "https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white",
                },
            ],
        }
    else:  # français par défaut
        data = {
            "name": "Lylian Challier",
            "title": "Curieux & Passionné par les Maths, l'IA et la Science.",
            "description": "Étudiant en Master Mathématiques et Intelligence Artificielle à l'Institut de Mathématiques d'Orsay, Université Paris-Saclay. J'aime voir comment les mathématiques peuvent résoudre des problèmes concrets.",
            "current_work": "Je suis actuellement en stage au LISN/CNRS pour explorer la régression symbolique afin de modéliser la convection turbulente près des parois. J'étudie trois méthodes principales : SINDy (Sparse Identification of Nonlinear Dynamics), la Gene Expression Programming (GEP), et les Kolmogorov-Arnold Networks (KANs).",
            "projects": [
                {
                    "title": "Auto-Encodeurs Variationnels",
                    "description": "implémentation & application Streamlit",
                    "link": "https://lylianchallier-vae.streamlit.app/",
                },
                {
                    "title": "Prévision de la demande électrique",
                    "description": "avec du Deep Learning",
                },
                {"title": "Prévision de la charge nette", "description": "en R"},
                {
                    "title": "Recommandation de films",
                    "description": "par apprentissage non supervisé",
                },
            ],
            "contact": {
                "email": "lylian.challier@universite-paris-saclay.fr",
                "linkedin": "https://linkedin.com/in/lylian-challier",
            },
            "tools": [
                {
                    "name": "CSS3",
                    "badge": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
                },
                {
                    "name": "Git",
                    "badge": "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
                },
                {
                    "name": "HTML5",
                    "badge": "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
                },
                {
                    "name": "LaTeX",
                    "badge": "https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white",
                },
                {
                    "name": "NumPy",
                    "badge": "https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white",
                },
                {
                    "name": "Pandas",
                    "badge": "https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white",
                },
                {
                    "name": "Python",
                    "badge": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
                },
                {
                    "name": "PyTorch",
                    "badge": "https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white",
                },
                {
                    "name": "R",
                    "badge": "https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white",
                },
                {
                    "name": "Scikit-learn",
                    "badge": "https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white",
                },
                {
                    "name": "Streamlit",
                    "badge": "https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white",
                },
                {
                    "name": "SQL",
                    "badge": "https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white",
                },
            ],
        }

    serializer = PortfolioDataSerializer(data)
    return Response(serializer.data)
