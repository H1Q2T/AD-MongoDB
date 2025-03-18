import tkinter as tk
from tkinter import ttk, messagebox
import database

# Crear ventana principal
root = tk.Tk()
root.title("MongoDB Movie & Series Manager")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# ---- Configurar Estilos ----
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", padding=5)
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

# ---- Scroll Global ----
canvas = tk.Canvas(root, bg="#f0f0f0")
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame_main = tk.Frame(canvas, bg="#f0f0f0")

frame_main.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame_main, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# ---- Función para mostrar resultados ----
def display_results(results):
    tree.delete(*tree.get_children())  # Borra contenido anterior
    if not results:
        messagebox.showinfo("Info", "No results found.")
    else:
        for result in results:
            values = [result.get("title", ""), result.get("year", ""), result.get("director", "")]
            tree.insert("", tk.END, values=values)

# ---- Funciones para consultas ----
def show_titles_and_directors():
    results = database.list_titles_and_directors()
    display_results(results)

def show_titles_and_years():
    results = database.list_titles_and_years_sorted()
    display_results(results)

def show_professor_search():
    results = database.search_by_professor()
    display_results(results)

def show_recent_titles():
    results = database.list_recent_titles()
    display_results(results)

def add_new_entry():
    title = entry_title.get().strip()
    year = entry_year.get().strip()
    director = entry_director.get().strip()
    cast = entry_cast.get().strip()
    summary = entry_summary.get().strip()

    if not title or not year or not director or not cast or not summary:
        messagebox.showerror("Error", "All fields are required.")
        return

    cast_list = [name.strip() for name in cast.split(",")]
    message = database.add_new_entry(title, year, director, cast_list, summary)
    messagebox.showinfo("Success", message)

# ---- Sección de botones de consulta ----
frame_buttons = tk.LabelFrame(frame_main, text="Queries", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
frame_buttons.pack(pady=10, fill="x", padx=20)

btn1 = ttk.Button(frame_buttons, text="List Titles & Directors", command=show_titles_and_directors)
btn2 = ttk.Button(frame_buttons, text="List Titles & Years", command=show_titles_and_years)
btn3 = ttk.Button(frame_buttons, text="Search 'Professor'", command=show_professor_search)
btn4 = ttk.Button(frame_buttons, text="List Titles After 2018", command=show_recent_titles)

btn1.grid(row=0, column=0, padx=10, pady=5)
btn2.grid(row=0, column=1, padx=10, pady=5)
btn3.grid(row=1, column=0, padx=10, pady=5)
btn4.grid(row=1, column=1, padx=10, pady=5)

# ---- Sección de Resultados ----
frame_table = tk.LabelFrame(frame_main, text="Results", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
frame_table.pack(pady=10, fill="both", expand=True, padx=20)

columns = ("Title", "Year", "Director")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=8)
tree.column("Title", width=300)
tree.column("Year", width=100, anchor="center")
tree.column("Director", width=200)

for col in columns:
    tree.heading(col, text=col)

scrollbar_tree = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar_tree.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar_tree.pack(side="right", fill="y")

# ---- Sección para agregar nueva película/serie ----
frame_add = tk.LabelFrame(frame_main, text="Add New Entry", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
frame_add.pack(pady=10, fill="x", padx=20)

tk.Label(frame_add, text="Title:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_title = ttk.Entry(frame_add, width=50)
entry_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_add, text="Year:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_year = ttk.Entry(frame_add, width=50)
entry_year.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_add, text="Director:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_director = ttk.Entry(frame_add, width=50)
entry_director.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_add, text="Cast (comma separated):", font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_cast = ttk.Entry(frame_add, width=50)
entry_cast.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_add, text="Summary:", font=("Arial", 10)).grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_summary = ttk.Entry(frame_add, width=50)
entry_summary.grid(row=4, column=1, padx=5, pady=5)

btn_add = ttk.Button(frame_add, text="Add Entry", command=add_new_entry)
btn_add.grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar ventana
root.mainloop()
