"""
   Draw the flag of Morocco using the Turtle graphics library.

   Dessine le drapeau du Maroc en utilisant la bibliothèque Turtle.

   .رسم علم المغرب باستخدام مكتبة تيرتل

   param size: Size of the flag (dimension of the rectangle side)
   param color: Background color of the rectangle

   param size: Taille du drapeau (dimension du côté du rectangle)
   :aram color: Couleur de fond du rectangle

   param size: حجم العلم (بُعد جانب المستطيل)
   param color: لون خلفية المستطيل
"""

import turtle

def draw_morocco_flag(size, color):

    # Initialize a turtle named "pen"
    # Initialiser une tortue appelée "pen"
    # تهيئة السلحفاة بإسم "pen"
    pen = turtle.Turtle()

    # Set the shape of the turtle
    # Définir la forme de la tortue
    # تعيين شكل السلحفاة
    pen.shape("turtle")

    # Set the color of the turtle
    # Définir la couleur de la tortue
    # تعيين لون السلحفاة
    pen.color(color)

    # Set the speed of the turtle
    # Définir la vitesse de la tortue
    # تعيين سرعة السلحفاة
    pen.speed(1)

    # Set the width of the turtle's pen
    # Définir la largeur du trait de la tortue
    # تعيين عرض قلم السلحفاة
    pen.width(13)

    # Position the turtle to the initial position
    # Positionner la tortue à la position initiale
    # تحديد موقع السلحفاة في الوضع الأولي
    pen.goto(-150, 0)

    # Use a loop to draw the five stars
    # Utiliser une boucle pour dessiner les cinq étoiles
    # استخدام حلقة لرسم النجوم الخمس
    i = 0
    while i < 5:
        pen.forward(size)
        pen.right(180 * 4 / 5)  # pen.right(144)
        i += 1

    # Hide the turtle at the end of the drawing
    # Cacher la tortue à la fin du dessin
    # إخفاء السلحفاة في نهاية الرسم
    pen.hideturtle()

# Create a window for the flag
# Créer une fenêtre pour le drapeau
# إنشاء نافذة للعلم
window = turtle.Screen()

# Set the background color of the window
# Définir la couleur de fond de la fenêtre
# تعيين لون خلفية النافذة
window.bgcolor("red")

# Title of the window in different languages
# Titre de la fenêtre en différentes langues
# عنوان النافذة بلغات مختلفة
window.title("Kingdom of Morocco - المملكة المغربية - Kingdom of Morocco - Reino de Marruecos")

# Call the function to draw the flag with a size of 250 and a green color
# Appeler la fonction pour dessiner le drapeau avec une taille de 250 et une couleur verte
# استدعاء الدالة لرسم العلم بحجم 250 ولون أخضر
draw_morocco_flag(250, "green")

# Wait for the user to click to close the window
# Attendre que l'utilisateur clique pour fermer la fenêtre
# انتظر حتى ينقر المستخدم لإغلاق النافذة
window.exitonclick()
