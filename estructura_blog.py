#Diccionario
perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programacion",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}

#Tupla
estados_post = ("borrador", "publicado", "archivado")

#Set
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

#Lista con diccionarios
posts = [{
    "id": 1,
    "titulo": "Primeros pasos con Python",
    "autor": perfil_autor,
    "tags": ["Python", "Principiantes"],
    "estado": "publicado"
},
  {
      "id": 2,
      "titulo": "Que es Django",
      "autor": perfil_autor,
      "tags": ["Python", "Django", "Web"],
      "estado": "borrador"
},
  {
      "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
 }      
  ]
print("Autor del segundo post: ", posts[1]["autor"]["nombre"])
print("Lista de posts guardados: ")
print(posts)
