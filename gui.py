import tkinter as tk
from tkinter import messagebox, ttk
from scraper import scrape_data
from saver import create_project_folder, save_text, save_images
import os
from pathlib import Path

def start():
    url = url_entry.get().strip()
    choice = data_type.get()

    if not url:
        messagebox.showerror("Error", "Enter a URL")
        return

    # Save in Downloads/Web_Scraped_Data
    folder = create_project_folder("Web_Scraped_Data")

    try:
        if choice == "All":
            result = scrape_data(url, "All")

            save_text(result["Title"], folder, "title.txt")
            save_text(result["Headings"], folder, "headings.txt")
            save_text(result["Links"], folder, "links.txt")
            save_images(result["Images"], folder)

        else:
            data = scrape_data(url, choice)

            if choice == "Images":
                save_images(data, folder)
            else:
                save_text(data, folder, f"{choice.lower()}.txt")

        messagebox.showinfo(
            "Success",
            f"Data saved in:\n{folder}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------- UI -------------------

root = tk.Tk()
root.title("Web Scraper")
root.geometry("460x260")
root.resizable(False, False)

tk.Label(root, text="Enter URL", font=("Arial", 11)).pack(pady=5)
url_entry = tk.Entry(root, width=55)
url_entry.pack()

tk.Label(root, text="Select data type", font=("Arial", 11)).pack(pady=10)

data_type = ttk.Combobox(
    root,
    values=["Title", "Headings", "Links", "Images", "All"],
    state="readonly"
)
data_type.current(0)
data_type.pack()

tk.Button(
    root,
    text="Scrape & Download",
    command=start,
    bg="#16a34a",
    fg="white",
    width=25
).pack(pady=25)

root.mainloop()
