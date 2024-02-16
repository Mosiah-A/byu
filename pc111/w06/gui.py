import tkinter as tk
from tkinter import Frame, Label, Button
from math import pi

from number_entry import IntEntry  # Certifique-se de que o nome do arquivo está correto

def main():
    root = tk.Tk()

    frm_main = Frame(root)
    frm_main.master.title('Área de um Círculo')
    frm_main.pack(padx=320, pady=200, fill=tk.BOTH, expand=10)

    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    lbl_radius = Label(frm_main, text="Insira o Raio: ")
    ent_radius = IntEntry(frm_main, lower_bound=0)
    lbl_area = Label(frm_main, text="Área do Círculo é ")

    lbl_result = Label(frm_main, width=0)

    btn_calculate = Button(frm_main, text='Calcular')
    btn_calculate.bind('<Button-1>', lambda event: calculate(event, ent_radius, lbl_result))
    ent_radius.bind('<Return>', lambda event: calculate(event, ent_radius, lbl_result))


    lbl_radius.grid(   row=0, column=0, padx=3, pady=3)
    ent_radius.grid(   row=0, column=1, padx=3, pady=3, sticky='w')
    lbl_area.grid(     row=1, column=0, padx=3, pady=3)
    lbl_result.grid(   row=1, column=1, padx=(5,3), pady=3, sticky='w')
    btn_calculate.grid(row=0, column=2, padx=3, pady=3)

def calculate(event, ent_radius, lbl_result):
    try:
        radius_str = ent_radius.get()
        radius = float(radius_str)
        
        if radius < 0:
            raise ValueError("O raio não pode ser negativo")

        area = pi * radius**2
        lbl_result.config(text=f'{area:.2f}')
        
    except ValueError as e:
        lbl_result.config(text=str(e))

if __name__ == "__main__":
    main()
