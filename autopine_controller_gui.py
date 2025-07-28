# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import subprocess
import signal
import os

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Autopine Controller GUI")
        # Double the default size (you can tweak 400x200 as needed)
        master.geometry("400x200")
        master.minsize(300, 150)

        self.proc = None
        self.btn_run = tk.Button(self, text="RUN", width=20, height=2, command=self.do_run)
        self.btn_stop = tk.Button(self, text="STOP", width=20, height=2, command=self.do_kill)
        self.btn_run.pack(pady=10)
        self.btn_stop.pack(pady=10)
        self.pack(expand=True, fill="both")

    def do_run(self):
        # Launch the orchestrator in the same folder
        self.proc = subprocess.Popen(
            ["python", "autopine_full_orchestrator.py"],
            cwd=os.path.dirname(__file__)
        )
        messagebox.showinfo("Started", f"PID {self.proc.pid}")

    def do_kill(self):
        if self.proc and self.proc.poll() is None:
            # terminate the subprocess
            os.kill(self.proc.pid, signal.SIGTERM)
            messagebox.showinfo("Stopped", f"Killed PID {self.proc.pid}")
        else:
            messagebox.showwarning("Nothing to stop", "No running process found.")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
