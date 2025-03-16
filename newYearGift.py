import tkinter as tk
from tkinter import Label, Button, CENTER
from PIL import Image, ImageTk  # Import PIL to handle JPG images


# Function to display the greeting message with an image
def show_greeting():
    # Create a new full-screen window for the greeting
    greeting_window = tk.Toplevel()
    greeting_window.title("New Year 2025 Greeting")
    greeting_window.attributes('-fullscreen', True)
    greeting_window.configure(bg="#1e1e2f")

    # Main frame to center everything
    main_frame = tk.Frame(greeting_window, bg="#1e1e2f", padx=30, pady=30)
    main_frame.pack(expand=True)

    # Load and display multiple images in a decorative manner
    images_frame = tk.Frame(main_frame, bg="#1e1e2f")
    images_frame.pack()

    image_paths = ["friend1.jpg", "friend2.jpg", "friend3.jpg", "friend4.jpg"]  # Update with real paths
    image_labels = []

    for img_path in image_paths:
        try:
            img = Image.open(img_path)
            img = img.resize((210, 180))  # Resize for a greeting card look
            img_tk = ImageTk.PhotoImage(img)

            img_label = Label(images_frame, image=img_tk, bg="#1e1e2f", bd=5, relief="ridge")
            img_label.image = img_tk  # Keep reference
            img_label.pack(side="left", padx=15, pady=10)
            image_labels.append(img_label)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

    # Greeting text
    greeting_text = Label(
        main_frame,
        text=(
            "\ud83c\udf1f Happy New Year 2025 \ud83c\udf1f\n\n"
            "Dear Arpita,\n\n"
            "I just wanted to take a moment to say thank you. Though we’ve known each other for only a short time since August, "
            "you’ve already become someone very special to me. Your presence has been a blessing, and I’m so grateful that life brought us together as friends.\n\n"
            "As we approach a new year, my heartfelt wishes are with you. May God fulfill all your dreams and aspirations, "
            "and may 2025 bring you immense joy, success, and countless reasons to smile. You deserve nothing but the best!\n\n"
            "Here’s a little shayari to express: \n\n"
            "“Zindagi ke safar mein kuch humsafar khaas hote hain,\n"
            "Jo waqt ke saath aur bhi aas paas hote hain.\n"
            "Shukriya un yaadon ka jo aapne diye,\n"
            "Dua hai har khushi aapke paas hote hain.”\n\n"
            "Thank you for coming into my life and making it brighter with your friendship. Here's to creating more wonderful memories together in the days ahead.\n\n"
            "Stay blessed, stay amazing, and always keep smiling! \ud83d\ude0a"
        ),
        font=("Georgia", 16, "italic"),
        bg="#1e1e2f", fg="#ffffff",
        justify="center", wraplength=900
    )
    greeting_text.pack(pady=20)

    # Additional images at the bottom for a greeting card effect
    bottom_images_frame = tk.Frame(main_frame, bg="#1e1e2f")
    bottom_images_frame.pack()

    for img_path in reversed(image_paths):
        try:
            img = Image.open(img_path)
            img = img.resize((180, 180))  # Resize for uniformity
            img_tk = ImageTk.PhotoImage(img)

            img_label = Label(bottom_images_frame, image=img_tk, bg="#1e1e2f", bd=5, relief="ridge")
            img_label.image = img_tk  # Keep reference
            img_label.pack(side="left", padx=15, pady=10)
            image_labels.append(img_label)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")

    # Close button
    close_button = Button(
        main_frame,
        text="Close Greeting",
        command=greeting_window.destroy,
        font=("Arial", 14, "bold"),
        bg="#ff4757", fg="#ffffff",
        relief="flat", padx=20, pady=10,
        bd=5, activebackground="#ff6b81", activeforeground="#ffffff",
    )
    close_button.pack(pady=20)


# Function to show an additional inspirational message
def show_inspiration():
    inspiration_window = tk.Toplevel(app)
    inspiration_window.title("Inspiration")
    inspiration_window.attributes('-fullscreen', False)
    inspiration_window.configure(bg="#34495e")

    inspiration_label = Label(
        inspiration_window,
        text=(
            "\u2728 \u201cBelieve in yourself and all that you are. "
            "Know that there is something inside you that is greater than any obstacle.\u201d \u2728\n\n"
            "Keep shining,✨ ARPITA! ✨ Your future is as bright as your smile."
        ),
        font=("Verdana", 16, "bold"),
        bg="#34495e",
        fg="#ecf0f1",
        justify="center",
        wraplength=800
    )
    inspiration_label.pack(pady=50)

    close_button = Button(
        inspiration_window,
        text="Close",
        command=inspiration_window.destroy,
        font=("Arial", 14, "bold"),
        bg="#e74c3c",
        fg="#ffffff",
        relief="flat",
        padx=20,
        pady=10,
        bd=5,
        activebackground="#e74c3c",
        activeforeground="#ffffff",
    )
    close_button.pack(pady=20)


# Function to show jokes about friendship and New Year
def show_jokes():
    jokes_window = tk.Toplevel(app)
    jokes_window.title("Friendship & New Year Jokes")
    jokes_window.attributes('-fullscreen', False)
    jokes_window.configure(bg="#2c3e50")

    jokes_text = (
        "1. 🎉 New Year's Eve is like a good friend... both show up just when you need them most! 😂\n\n"
        "2. What did one friend say to the other on New Year's Eve? 'Let’s make this year so awesome that even our memories will need a year to catch up!' 😂\n\n"
        "3. A good friend is like a New Year’s resolution: they may be hard to keep sometimes, but they make life a lot more fun! 😂\n\n"
        "4. New Year’s Eve is the perfect time to raise a toast to friendship – because let’s face it, friends are the ones who keep us laughing through every calendar year! 😂\n\n"
        "5. Why did the friends bring a ladder to the New Year party? They wanted to ring in the new year on a high note! 😂\n\n"
        "6. New Year’s Eve is the time to count your blessings... and the best blessing is always a friend who never forgets to text 'Happy New Year'! 😂\n\n"
        "7. Cheers to the friends who make the journey through the year more memorable – let’s raise a glass to lasting friendships and unforgettable New Year’s celebrations! 😂\n\n"
        "8. True friendship is like a great New Year’s resolution – tough to stick with, but worth the effort! 😂\n\n"
        "9. Here’s to another year of awkward selfies, unforgettable memories, and the friends who make everything fun – Happy New Year! 😂\n\n"
        "10. May this year bring you as much happiness as a New Year's Eve countdown with your best friend. Nothing beats those moments! 😂"
    )

    jokes_label = Label(
        jokes_window,
        text=jokes_text,
        font=("Arial", 14),
        bg="#2c3e50",
        fg="#f39c12",
        justify="left",
        wraplength=1000
    )
    jokes_label.pack(pady=50)

    close_button = Button(
        jokes_window,
        text="Close Jokes",
        command=jokes_window.destroy,
        font=("Arial", 14, "bold"),
        bg="#e74c3c",
        fg="#ffffff",
        relief="flat",
        padx=20,
        pady=10,
        bd=5,
        activebackground="#e74c3c",
        activeforeground="#ffffff",
    )
    close_button.pack(pady=20)


# Function to exit the application
def exit_app(event=None):
    app.quit()


# Main application window
app = tk.Tk()
app.title("Greeting App for Arpita")
app.attributes('-fullscreen', True)  # Set the window to fullscreen mode

# Set the background color for the window (no background image)
app.configure(bg="#2b2b3d")

# Add a welcome message
welcome_label = Label(
    app,
    text="\ud83c\udf1f  Welcome to the New Year 2025 Greeting 😊\ud83c\udf1f",
    font=("Georgia", 34, "bold"),
    bg="#2b2b3d",
    fg="#f1c40f",  # Highlighted text color
    wraplength=1200,
    anchor=CENTER
)
welcome_label.pack(pady=50)

# Add a description with "Arpita" styled attractively
description_label = Label(
    app,
    text="Wishing you a wonderful year ahead filled with happiness and success! \n\n"
    ,
    font=("Arial", 20),
    bg="#2b2b3d",
    fg="#ffffff",  # Color for general text
    wraplength=1200,
    anchor=CENTER
)
description_label.pack(pady=8)

# Add a bold and colorful label for ARPITA
arpita_label = Label(
    app,
    text="✨ ARPITA ✨",  # Making ARPITA bold and distinct
    font=("Arial", 24, "bold"),
    fg="#FF69B4",  # A bright color for Arpita to make it stand out
    bg="#2b2b3d",  # Background of the main window for consistency
)
arpita_label.pack(pady=10)

# Add a button to open the greeting
greeting_button = Button(
    app,
    text="\ud83c\udf89 Show New Year Greeting \ud83c\udf89",
    command=show_greeting,
    font=("Arial", 18, "bold"),
    bg="#27ae60",
    fg="#ffffff",
    relief="groove",
    padx=30,
    pady=15,
    bd=5,
    activebackground="#2ecc71",
    activeforeground="#ffffff",
)
greeting_button.pack(pady=20)

# Add a button to open the inspiration
inspiration_button = Button(
    app,
    text="\ud83c\udf1f Show Inspiration \ud83c\udf1f",
    command=show_inspiration,
    font=("Arial", 18, "bold"),
    bg="#2980b9",
    fg="#ffffff",
    relief="raised",
    padx=30,
    pady=15,
    bd=5,
    activebackground="#3498db",
    activeforeground="#ffffff",
)
inspiration_button.pack(pady=20)

# Add a button to show jokes
jokes_button = Button(
    app,
    text="\ud83d\ude02 Show Friendship Jokes \ud83d\ude02",
    command=show_jokes,
    font=("Arial", 18, "bold"),
    bg="#e67e22",
    fg="#ffffff",
    relief="ridge",
    padx=30,
    pady=15,
    bd=5,
    activebackground="#f39c12",
    activeforeground="#ffffff",
)
jokes_button.pack(pady=20)

# Bind the "Esc" key to exit the app
app.bind("<Escape>", exit_app)

# Run the main application
app.mainloop()
