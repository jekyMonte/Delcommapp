import shutil
import tkinter as tk
from tkinter import filedialog
import os
import customtkinter as Ctk

if not os.path.exists('target'):
    os.mkdir('target')
def upload_file():
    text_widget.configure(state='normal')
    filepath = filedialog.askopenfilename()
    print("Uploaded: ", filepath)
    filename = os.path.basename(filepath)
    text_widget.insert('1.0', filename)
    
    try:
        shutil.copy(filepath, "target/"+filename)
    except:
        print("close")
        pass
    text_widget.configure(state='disabled')
    
def delete_file():
    text_widget.configure(state='normal')
    filepath = os.getcwd()
    files = os.listdir("target")
    for file in files:
        filepath = os.path.join("target", file)
        if os.path.isfile(filepath):
            os.remove(filepath)
    text_widget.delete('1.0', tk.END)
    text_widget.configure(state='disabled')

def download_file():
    folder_selected = filedialog.askdirectory()
    # mengambil semua file yang ada dalam folder "hasil"
    for file_name in os.listdir("target"):
        file_path = os.path.join("target", file_name)
        if os.path.isfile(file_path):
            # menyalin file dari folder "hasil" ke folder yang dipilih
            shutil.copy(file_path, folder_selected)
    download_button.config(state='normal')
def generate_file():
    download_button.configure(state='disabled')
    # clear_button.configure(state='disabled')
    current_folder = os.getcwd()

    dirhasil = os.listdir(current_folder+'/target')
    
    pilihan = isi1.get()
    print(pilihan)
    # akhir = isi2.get('1.0', tk.END)
    print("\n")
    print("Processing...")
    print("Mohon tunggu...")
    for file in dirhasil:
        text_widget.configure(state='normal')
        process.configure(state='normal')
        with open(f'{current_folder}/target/{file}', 'r') as f:
            lines = f.readlines()
        lines_env  = []
        read_file_logic_check = False
        count_read_file = 0
        linekena = []
        for enum, line in enumerate(lines):
            
            if read_file_logic_check == True and '#show' in line:
                
                break
            elif read_file_logic_check == True and 'show' in line and lines[count_read_file+1] == '\n':
                print(lines[count_read_file])
                
                break
            if read_file_logic_check == True:
                lines_env.append(line)
                linekena.append(count_read_file)
            
            if pilihan in line and lines[count_read_file-1] != '!\n' or '#'+pilihan+'\n' in line and lines[count_read_file-1] != '!\n':
                read_file_logic_check = True
                
            count_read_file+=1
          
        total = len(linekena)
        kalian = []
        for persen in range(1,101):
            hasil = total/100 * persen
            kalian.append(int(hasil))
        hehe = 0
        hoho = 0
        for i in linekena:
            
            lines[i] = lines[i].replace(lines[i], '')
            hoho += 1
            # for hitung in kalian:
            #     if hitung == hoho:
            #         hehe += 1
            #         process.delete('1.0', tk.END)
            #         print("Processing file "+file+" ...")
            #         print("Mohon tunggu... "+str(hehe)+'%')
            #         output = str(hehe)+'%\n'
            #         process.insert(tk.END, output)

          
        delname = pilihan.split('\n')[0] 
        delfile = file.split('.txt')[0] 
        text_widget.delete('1.0', tk.END)
        process.delete('1.0', tk.END)
        with open(f'{current_folder}/target/{delfile}-delete {delname}.txt', 'w') as f:

            f.writelines(lines)
            print("File "+file+" Done !!!")
            output = "File "+file+" Done !!!"
            process.insert(tk.END, output)
            download_button.configure(state='normal')
            # clear_button.config(state='normal')
        os.remove(f'{current_folder}/target/{file}')
        text_widget.insert('1.0', f'{delfile}-delete {delname}.txt')
        text_widget.configure(state='disabled')
        process.configure(state='disabled')

Ctk.set_appearance_mode("Dark")
Ctk.set_default_color_theme("green")

root = Ctk.CTk()
root.wm_title("Delete Command App")
root.wm_iconbitmap("ikon.ico")
root.geometry("700x600")
frame = Ctk.CTkFrame(root)
frame.pack(fill="both", expand=True)

label = Ctk.CTkLabel(frame, text="Delete Command App", font=("Roboto", 24))
label.pack(pady=12, padx=10)

text_widget = Ctk.CTkTextbox(frame, state='disabled')
text_widget.configure(height=60, width=400)
upload_button = Ctk.CTkButton(frame, text="Upload File", command=upload_file)
upload_button.pack(pady=12, padx=10)

delete_button = Ctk.CTkButton(frame, text="Delete File", command=delete_file)
for file in os.listdir("target"):
    print(file)
    text_widget.configure(state='normal')
    text_widget.insert("1.0", file+ "\n")
    text_widget.configure(state='disabled')
text_widget.pack()

delete_button.pack(pady=12, padx=10)
text_delete = Ctk.CTkLabel(frame, text="Masukan command yang akan dihapus")
text_delete.pack(pady=12, padx=10)

isi1 = Ctk.CTkEntry(frame)
isi1.pack(pady=12, padx=10)
generate_button = Ctk.CTkButton(frame, text="Generate", command=generate_file)
generate_button.pack(pady=12, padx=10)
process = Ctk.CTkTextbox(frame, state='disabled')
process.configure(height=60, width=400)
process.pack(pady=12, padx=10)
download_button = Ctk.CTkButton(frame, text="Download Files", command=download_file, state='disabled')
download_button.pack(pady=12, padx=10)
label = Ctk.CTkLabel(frame, text="v1.0.0")
label.place(relx=1, rely=1, x=0, y=0, anchor='se')
label2 = Ctk.CTkLabel(frame, text="Copyright (c) 2023 - By Jeky")
label2.place(relx=0, rely=1, x=0, y=0, anchor='sw')
root.mainloop()
