import tkinter as tk
from tkinter import ttk
import requests

def send_request(module, entry, output):
    contract = entry.get()
    if not contract:
        return

    url = f"http://127.0.0.1:29373/aqt?module={module}&input={contract}"
    try:
        response = requests.get(url)
        output_text = response.text
    except requests.RequestException as e:
        output_text = f"Error: {str(e)}"

    output.config(state="normal")
    output.delete(1.0, tk.END)
    output.insert(tk.END, f"Module: {module}\nContract: {contract}\nResponse: {output_text}")
    output.config(state="disabled")
    entry.delete(0, tk.END)

def toggle_always_on_top():
    root.attributes("-topmost", always_on_top_var.get())

# GUI Setup
root = tk.Tk()
root.title("Contract Request GUI")
root.geometry("400x300")
root.configure(bg="#2e2e2e")
root.resizable(False, False)

# Always on top checkbox
always_on_top_var = tk.BooleanVar(value=False)
always_on_top_check = tk.Checkbutton(root, text="Always on Top", variable=always_on_top_var, command=toggle_always_on_top, bg="#2e2e2e", fg="#ffffff", selectcolor="#3e3e3e")
always_on_top_check.pack(anchor="ne", padx=5, pady=5)

# Contract Entry and Buttons
frame = ttk.Frame(root, style="TFrame")
frame.pack(pady=5, padx=10, fill="x")

modules = ["pumpfun", "moonshot", "raydiumsnipe"]
entries = {}

for module in modules:
    module_frame = ttk.Frame(frame, style="TFrame")
    module_frame.pack(fill="x", pady=2)

    label = ttk.Label(module_frame, text=module.capitalize() + ":", foreground="#ffffff", background="#2e2e2e")
    label.pack(side="left")

    entry = tk.Entry(module_frame, bg="#3e3e3e", fg="#00ff00", insertbackground="#00ff00", relief="flat")
    entry.pack(side="left", fill="x", expand=True, padx=5)
    entries[module] = entry

    button = ttk.Button(module_frame, text="Send", command=lambda m=module, e=entry: send_request(m, e, output))
    button.pack(side="right")

# Output Box
output = tk.Text(root, wrap="word", state="disabled", height=6, bg="#1e1e1e", fg="#00ff00", insertbackground="#00ff00")
output.pack(pady=5, padx=10, fill="both", expand=True)

# Styling
style = ttk.Style()
style.configure("TFrame", background="#2e2e2e")
style.configure("TLabel", background="#2e2e2e", foreground="#ffffff")
style.configure("TButton", background="#3e3e3e", foreground="#ffffff")

# Run the Application
root.mainloop()
