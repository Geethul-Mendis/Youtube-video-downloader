import tkinter
import customtkinter
from pytube import YouTube
import threading

def start_download():
    """Function to handle the download process in a separate thread."""
    try:
        # Fetch the link from the entry widget
        youtube_link = link.get().strip()
        if not youtube_link:
            progressbar.configure(text="Please enter a YouTube link.", text_color="red")
            return
        # Create YouTube object
        youtube_object = YouTube(youtube_link)

        # Fetch the highest resolution stream available
        video_resolution = youtube_object.streams.filter(progressive=True).get_highest_resolution()

        # Update the title label with the video's title
        title.configure(text=youtube_object.title, text_color="white")
        progressbar.configure(text="Downloading...", text_color="yellow")
        progressbar.update_idletasks()  # Update the label to show downloading status
        
        # Download the video
        video_resolution.download()

        # Update the progress bar label on successful download
        progressbar.configure(text="Downloaded 🎉", text_color="green")
    except Exception as e:
        # Update the progress bar label if there is an error
        progressbar.configure(text="Download Error: " + str(e), text_color="red")

def on_download_button_click():
    """Handles the click event of the download button."""
    # Create a new thread to run the download process to keep the UI responsive
    download_thread = threading.Thread(target=start_download)
    download_thread.start()

# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Main application frame
app = customtkinter.CTk()
app.geometry("720x420")
app.title("YouTube Video Downloader")

# Title Label
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=30, pady=30)

# StringVar for Entry
url_variable = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_variable)
link.pack(pady=20)  # Added some padding for better UI layout

# Progress bar label to display messages
progressbar = customtkinter.CTkLabel(app, text="")
progressbar.pack(pady=20)

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=on_download_button_click)
download_button.pack(padx=50, pady=50)

# Run the app
app.mainloop()
