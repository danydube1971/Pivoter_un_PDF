"""Voici un exemple de script Python 3 pour faire pivoter un fichier PDF vers la droite ou la gauche, en utilisant la bibliothèque PyPDF2."""

import PyPDF2
import os

# Fonction pour faire pivoter un fichier PDF
def rotate_pdf(input_path, output_path, rotation_angle):
    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        # Ouvre le fichier PDF en mode binaire (rb) pour la lecture et en mode binaire (wb) pour l'écriture
        pdf_reader = PyPDF2.PdfFileReader(input_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Parcourt chaque page du fichier PDF
        for page_num in range(pdf_reader.numPages):
            # Récupère la page courante
            page = pdf_reader.getPage(page_num)

            # Fait pivoter la page dans la direction souhaitée
            if rotation_angle == 'droite':
                page.rotateClockwise(90)
            elif rotation_angle == 'gauche':
                page.rotateCounterClockwise(90)
            else:
                print("L'angle de rotation doit être 'droite' ou 'gauche'.")
                return

            # Ajoute la page modifiée à l'écrivain PDF
            pdf_writer.addPage(page)

        # Écrit le contenu de l'écrivain PDF dans le fichier de sortie
        pdf_writer.write(output_file)

# Demande à l'utilisateur le chemin d'accès au fichier d'entrée
input_path = input("Entrez le chemin d'accès au fichier PDF à pivoter : ")

# Vérifie que le fichier existe
if not os.path.isfile(input_path):
    print("Le fichier spécifié n'existe pas.")
    exit()

# Demande à l'utilisateur la direction de rotation
rotation_angle = input("Faire pivoter le fichier vers la droite ou vers la gauche ? (droite/gauche) : ")

# Vérifie que l'angle de rotation est valide
if rotation_angle != 'droite' and rotation_angle != 'gauche':
    print("L'angle de rotation doit être 'droite' ou 'gauche'.")
    exit()

# Demande à l'utilisateur le chemin d'accès au fichier de sortie
output_path = input("Entrez le chemin d'accès au fichier de sortie : ")

# Appelle la fonction de rotation du fichier PDF
rotate_pdf(input_path, output_path, rotation_angle)

# Confirme la fin du processus
print("Le fichier a été pivoté avec succès.")

