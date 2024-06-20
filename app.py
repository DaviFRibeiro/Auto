import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyautogui as py
import time
import threading

def start_code():
    # Esconde a janela principal
    root.withdraw()
    
    countdown_window = tk.Toplevel()
    countdown_window.title("Contagem Regressiva")
    countdown_window.geometry("400x100")

    countdown_label = tk.Label(countdown_window, text="", fg='black', font=('Helvetica', 18))
    countdown_label.pack(expand=True)
    
    def countdown_and_automation():
        countdown_time = 5
        
        for i in range(countdown_time, 0, -1):
            countdown_label.config(text=f"Iniciará em {i}...")
            countdown_window.update()
            time.sleep(1)
        
        countdown_window.destroy()
        
        def automation():
            try:
                py.press('winleft')
                time.sleep(0.5)
                py.write('ICUE')
                time.sleep(0.5)  
                py.press('enter')
                time.sleep(5)

                py.press('winleft')
                time.sleep(0.5)
                py.write('WhatsApp')
                time.sleep(0.5)
                py.press('enter')
                time.sleep(5)

                py.press('winleft')
                time.sleep(0.5)
                py.write('Opera')
                time.sleep(0.5)
                py.press('enter')
                time.sleep(5)

                py.press('winleft')
                time.sleep(0.5)
                py.write('Terminal')
                time.sleep(0.5)
                py.press('enter')
                time.sleep(5)
                
                # Mostrar a tela de finalização
                show_completion_screen()

            except Exception as e:
                print(f"Erro durante a automação: {e}")

        automation()

    countdown_thread = threading.Thread(target=countdown_and_automation)
    countdown_thread.start()

    def show_completion_screen():
        completion_window = tk.Toplevel()
        completion_window.title("Finalização")
        completion_window.geometry("400x100")
        
        completion_label = tk.Label(completion_window, text="Código finalizado. Pressione Enter para encerrar.", fg='black', font=('Helvetica', 12))
        completion_label.pack(expand=True)
        
        completion_window.bind('<Return>', lambda event: root.quit())
    
    def stop_code(event):
        messagebox.showinfo("Aviso", "Interrompendo o código...")
        root.quit()
    
    root.bind_all('<KeyPress>', stop_code)
    root.bind_all('<Button>', stop_code)

root = tk.Tk()
root.title("Aviso")
root.geometry("400x200")

# Estilizar o texto
label = tk.Label(root, text="Iniciará em...", fg='black', font=('Helvetica', 12))
label.pack(pady=10)

# Adicionar imagem abaixo do texto
background_image = Image.open("logo.png")
background_photo = ImageTk.PhotoImage(background_image)

# Frame para agrupar o texto e a imagem
frame = tk.Frame(root)
frame.pack()

image_label = tk.Label(frame, image=background_photo)
image_label.pack(side='left', padx=10)

# Inicia o código automaticamente
start_code()

root.mainloop()
