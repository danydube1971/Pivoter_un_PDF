# Pivoter_un_PDF
Permet de pivoter un fichier PDF à droite ou à gauche

Ce script utilise le module PyPDF2 pour faire pivoter un fichier PDF dans la direction spécifiée par l'utilisateur. 
Voici ce que fait chaque étape du script :

1. Définit une fonction "rotate_pdf" qui prend en entrée le chemin d'accès au fichier PDF d'entrée, 
le chemin d'accès au fichier de sortie, et l'angle de rotation (soit "droite", soit "gauche").
2. Ouvre le fichier PDF d'entrée en mode binaire pour la lecture et crée un écrivain PDF pour le fichier de sortie 
en mode binaire pour l'écriture en utilisant les méthodes PdfFileReader() et PdfFileWriter() de PyPDF2.
3. Parcourt chaque page du fichier PDF d'entrée en utilisant la méthode numPages de PdfFileReader.
4. Fait pivoter chaque page dans la direction spécifiée par l'utilisateur en utilisant les méthodes rotateClockwise() 
ou rotateCounterClockwise() de la classe PageObject de PyPDF2.
5. Ajoute chaque page modifiée à l'écrivain PDF en utilisant la méthode addPage() de PdfFileWriter.
6. Écrit le contenu de l'écrivain PDF dans le fichier de sortie en utilisant la méthode write().
7. Demande à l'utilisateur le chemin d'accès au fichier PDF d'entrée.
8. Vérifie que le fichier existe en utilisant la fonction isfile() de os.
9. Demande à l'utilisateur la direction de rotation (soit "droite", soit "gauche").
10. Vérifie que l'angle de rotation est valide.
11. Demande à l'utilisateur le chemin d'accès au fichier de sortie.
12. Appelle la fonction de rotation du fichier PDF en utilisant les entrées de l'utilisateur.
13. Affiche un message de confirmation indiquant que le fichier a été pivoté avec succès.

Ainsi, à la fin de l'exécution du script, le fichier PDF d'entrée aura été pivoté dans la direction spécifiée par l'utilisateur 
et sauvegardé dans le fichier de sortie spécifié.
