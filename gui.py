import tkinter as tk #tkinter to create gui
from tkinter import messagebox #messagebox for pop-up messages
from network_scanner import scan_network, save_to_csv, save_to_json
from db_handler import save_to_postgresql

def scan():
    network = entry.get()
    if not network:
        messagebox.showerror("Error", "Please enter a network range")
        return

    results = scan_network(network) #Running scan
    save_to_csv(results)
    save_to_json(results)
    save_to_postgresql(results)
    
    text.delete("1.0", tk.END) #clearing text box
    for device in results:
        text.insert(tk.END, f"IP: {device['IP']} - MAC: {device['MAC']}\n")
    messagebox.showinfo("Success", "Scan complete and results saved!")

app = tk.Tk()
app.title("Network scanner")

tk.Label(app, text="Enter network (e.g., 192.168.1.0/24):").pack()
entry = tk.Entry(app)
entry.pack()

scan_button = tk.Button(app, text="Scan Network", command=scan)
scan_button.pack()

text = tk.Text(app, height=10, width=50)
text.pack()

app.mainloop()
