import os

from django.conf import settings
from django.http import FileResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PortfolioDataSerializer


@api_view(["GET"])
def get_portfolio_data(request):
    """
    API endpoint pour récupérer les données du portfolio
    Support multilingue via le paramètre ?lang=fr ou ?lang=en
    Langue par défaut : anglais (en)
    """
    lang = request.query_params.get("lang", "en")

    if lang == "fr":
        data = {
            "name": "Lylian Challier",
            "title": "Curieux & Passionné par les Maths, l'IA et la Science.",
            "description": "Étudiant en master à CentraleSupélec, spécialisé en mathématiques, IA, Machine Learning et Deep Learning, je suis à la recherche d'une expérience de 6 mois à partir de mars 2026. Après ce stage, il me restera une dernière année de master avant de me lancer dans une thèse CIFRE.",
            "current_work": "Cette année, j'ai été sélectionné pour participer au programme d'innovation Digital Tech Year et j'ai reçu la bourse MathTech Gap Year (4 lauréats, FMJH). Cette expérience fait le lien entre l'innovation en matière d'IA dans le monde réel et mes objectifs de recherche dans le cadre d'une thèse CIFRE.",
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
                "email": "lylian.challier@student-cs.fr",
                "linkedin": "https://linkedin.com/in/lylian-challier",
            },
            "tools": [
                {
                    "name": "CSS3",
                    "badge": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
                },
                {
                    "name": "Django",
                    "badge": "https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green",
                },
                {
                    "name": "Docker",
                    "badge": "https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white",
                },
                {
                    "name": "FastAPI",
                    "badge": "https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi",
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
                    "name": "React",
                    "badge": "https://camo.githubusercontent.com/3467eb8e0dc6bdaa8fa6e979185d371ab39c105ec7bd6a01048806b74378d24c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642",
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
    else:  # anglais par défaut
        data = {
            "name": "Lylian Challier",
            "title": "Curious & Passionate about Mathematics, AI, and Science.",
            "description": "MSc student at CentraleSupélec, specialized in mathematics, AI, machine learning and deep learning, applying for a 6 month experience starting March 2026. After this internship, I will have one final year of my master's degree left before starting an industrial PhD.",
            "current_work": "This year I was selected for the Digital Tech Year selective track, an innovation program, and awarded the MathTech Gap Year fellowship (4 laureates, FMJH). This experience bridges real-world AI innovation with my PhD-oriented research goals.",
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
                "email": "lylian.challier@student-cs.fr",
                "linkedin": "https://linkedin.com/in/lylian-challier",
            },
            "tools": [
                {
                    "name": "CSS3",
                    "badge": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
                },
                {
                    "name": "Django",
                    "badge": "https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green",
                },
                {
                    "name": "Docker",
                    "badge": "https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white",
                },
                {
                    "name": "FastAPI",
                    "badge": "https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi",
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
                    "name": "React",
                    "badge": "https://camo.githubusercontent.com/3467eb8e0dc6bdaa8fa6e979185d371ab39c105ec7bd6a01048806b74378d24c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742d3230323332413f7374796c653d666f722d7468652d6261646765266c6f676f3d7265616374266c6f676f436f6c6f723d363144414642",
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


def download_cv(request):
    """
    Vue pour télécharger le CV en PDF
    Force le téléchargement plutôt que l'ouverture dans le navigateur
    """
    cv_path = os.path.join(settings.BASE_DIR, "core", "static", "core", "pdf", "CV.pdf")

    if not os.path.exists(cv_path):
        raise Http404("CV not found")

    response = FileResponse(open(cv_path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="CV_Lylian_Challier.pdf"'
    return response
