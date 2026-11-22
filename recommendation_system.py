courses_by_interest = {
    "redes": [
        "Fundamentos de redes de telecomunicaciones",
        "Enrutamiento y conmutación",
        "Diseño y administración de redes",
    ],
    "fibra": [
        "Introducción a la fibra óptica",
        "Instalación y certificación de redes de fibra",
        "Mantenimiento de sistemas de fibra óptica",
    ],
    "linux": [
        "Linux básico para telecomunicaciones",
        "Administración de servidores Linux",
        "Automatización de redes con Linux",
    ],
}

interest = input("Escribe un interés (redes, fibra o linux): ").strip().lower()

if not interest:
    print("La entrada está vacía. Escribe redes, fibra o linux.")
else:
    courses = courses_by_interest.get(interest, [])
    if courses:
        print(f"Cursos recomendados para {interest}:")
        for course in courses:
            print(f"- {course}")
    else:
        print(f"No hay cursos disponibles para el interés «{interest}».")