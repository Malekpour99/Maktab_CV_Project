from django.shortcuts import render

# Create your views here.


def index_view(request):
    resume = {
        "area_skills": [
            {
                "area": "Front-End",
                "skill_level": 98
            },
            {
                "area": "Back-End",
                "skill_level": 76
            },
            {
                "area": "Databases",
                "skill_level": 63
            },
        ],
        "programming_skills": [
            {
                "language": "Python",
                "skill_level": 96
            },
            {
                "language": "Vue-JS / Vuex / VueRouter",
                "skill_level": 90
            },
            {
                "language": "Django",
                "skill_level": 70
            },
            {
                "language": "JavaScript / TypeScript",
                "skill_level": 86
            },
            {
                "language": "HTML5",
                "skill_level": 100
            },
            {
                "language": "CSS / SCSS / SASS",
                "skill_level": 94
            },
        ],
        "language_skills": [
            {
                "language": "Persian",
                "lang_level": 100
            },
            {
                "language": "English",
                "lang_level": 100
            },
            {
                "language": "Deutsch",
                "lang_level": 45
            },
        ]
    }
    return render(request, "website\index.html", {"resume": resume})
