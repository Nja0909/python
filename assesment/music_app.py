import os
import tkinter as tk
from tkinter import messagebox, filedialog


if not os.path.exists("playlists"):
    os.makedirs("playlists")



class Playlist:
    def __init__(self, name, songs):
        self.name = name.strip()
        self.songs = [song.strip() for song in songs if song.strip()]

    def save(self):
        """Save playlist to file"""
        if not self.name:
            raise ValueError("Playlist name cannot be empty.")
        if not self.songs:
            raise ValueError("Playlist must have at least one song.")

        filename = f"playlists/playlist_{self.name}.txt"
        if os.path.exists(filename):
            raise FileExistsError("A playlist with this name already exists.")

        with open(filename, "w", encoding="utf-8") as f:
            for song in self.songs:
                f.write(song + "\n")



class MusicBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 MusicBox App")
        self.root.geometry("600x400")

        tk.Label(root, text="Playlist Name:").pack(anchor="w", padx=10, pady=2)
        self.entry_name = tk.Entry(root, width=40)
        self.entry_name.pack(padx=10, pady=2)

        tk.Label(root, text="Enter Songs (one per line):").pack(anchor="w", padx=10, pady=2)
        self.text_songs = tk.Text(root, height=6, width=60)
        self.text_songs.pack(padx=10, pady=2)

        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)
        tk.Button(frame_buttons, text="Save Playlist", command=self.save_playlist).pack(side="left", padx=5)
        tk.Button(frame_buttons, text="Load Playlists", command=self.load_playlists).pack(side="left", padx=5)

        tk.Label(root, text="Saved Playlists:").pack(anchor="w", padx=10, pady=2)
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(padx=10, pady=2)
        self.listbox.bind("<<ListboxSelect>>", self.show_playlist)

        tk.Label(root, text="Playlist Songs:").pack(anchor="w", padx=10, pady=2)
        self.text_display = tk.Text(root, height=6, width=60, state="disabled")
        self.text_display.pack(padx=10, pady=2)



    def save_playlist(self):
        name = self.entry_name.get().strip()
        songs = self.text_songs.get("1.0", tk.END).splitlines()

        try:
            playlist = Playlist(name, songs)
            playlist.save()
            messagebox.showinfo("Success", f"Playlist '{name}' saved successfully!")
            self.entry_name.delete(0, tk.END)
            self.text_songs.delete("1.0", tk.END)
            self.load_playlists()  # refresh list
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except FileExistsError as fe:
            messagebox.showerror("Error", str(fe))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    def load_playlists(self):
        self.listbox.delete(0, tk.END)
        try:
            for file in os.listdir("playlists"):
                if file.startswith("playlist_") and file.endswith(".txt"):
                    self.listbox.insert(tk.END, file)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load playlists: {e}")

    def show_playlist(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        filename = self.listbox.get(selection[0])

        try:
            with open(os.path.join("playlists", filename), "r", encoding="utf-8") as f:
                songs = f.read()
            self.text_display.config(state="normal")
            self.text_display.delete("1.0", tk.END)
            self.text_display.insert(tk.END, songs)
            self.text_display.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "Playlist file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open playlist: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicBoxApp(root)
    root.mainloop()
