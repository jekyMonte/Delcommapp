import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog
import os

if not os.path.exists('target'):
    os.mkdir('target')
def upload_file():
    filepath = filedialog.askopenfilename()
    print("Uploaded: ", filepath)
    filename = os.path.basename(filepath)
    text_widget.insert('1.0', filename)
    
    try:
        shutil.copy(filepath, "target/"+filename)
    except:
        print("close")
        pass

    
def delete_file():
    filepath = os.getcwd()
    files = os.listdir("target")
    for file in files:
        filepath = os.path.join("target", file)
        if os.path.isfile(filepath):
            os.remove(filepath)
    text_widget.delete('1.0', tk.END)

def download_file():
    folder_selected = filedialog.askdirectory()
    # mengambil semua file yang ada dalam folder "hasil"
    for file_name in os.listdir("target"):
        file_path = os.path.join("target", file_name)
        if os.path.isfile(file_path):
            # menyalin file dari folder "hasil" ke folder yang dipilih
            shutil.copy(file_path, folder_selected)
    download_button.config(state='normal')
    # clear_button.config(state='normal')
def generate_file():
    download_button.config(state='disabled')
    # clear_button.config(state='disabled')
    current_folder = os.getcwd()

    dirhasil = os.listdir(current_folder+'/target')
    
    pilihan = (isi1.get('1.0', tk.END))
    # akhir = isi2.get('1.0', tk.END)
    print("\n")
    print("Processing...")
    print("Mohon tunggu...")
    for file in dirhasil:
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
            download_button.config(state='normal')
            # clear_button.config(state='normal')
        os.remove(f'{current_folder}/target/{file}')
        text_widget.insert('1.0', f'{delfile}-delete {delname}.txt')
# def clearhasil():
#     filepath = os.getcwd()
#     files = os.listdir("hasil")
#     for file in files:
#         filepath = os.path.join("hasil", file)
#         if os.path.isfile(filepath):
#             os.remove(filepath)
#     process.delete('1.0', tk.END)
root = tk.Tk()
root.wm_title("Delete Command App")
root.wm_iconbitmap("ikon.ico")
root.geometry("500x500")
text_widget = tk.Text(root)
text_widget.config(height=3, width=60)
upload_button = tk.Button(text="Upload File", command=upload_file)
upload_button.pack()

delete_button = tk.Button(text="Delete File", command=delete_file)

text_widget.pack()
for file in os.listdir("target"):
    text_widget.insert(tk.END, file + "\n")
delete_button.pack()
text_delete = tk.Label(text="Masukan command yang akan dihapus")
text_delete.pack()

isi1 = tk.Text(root)
isi1.config(height=2, width=30)
isi1.pack()
# text_delete2 = tk.Label(text="Silahkan pilih batas akhir command yang ingin di hapus :")
# text_delete2.pack()
isi2 = tk.Text(root)
isi2.config(height=2, width=30)
# isi2.pack()
generate_button = tk.Button(text="Generate", command=generate_file)
generate_button.pack()
process = tk.Text(root)
process.config(height=5, width=60)
process.pack()
download_button = tk.Button(root, text="Download Files", command=download_file, state='disabled')
download_button.pack()
# clear_button = tk.Button(root, text="Delete All", command=clearhasil, state='disabled')
# clear_button.pack()
label = tk.Label(root, text="v1.0.0")
label.config(font=("Arial", 7))
label.place(relx=1, rely=1, x=0, y=0, anchor='se')
label2 = tk.Label(root, text="Copyright (c) 2023 - By Team Devnet Nusantara Compnet Integrator")
label2.config(font=("Arial", 8))
label2.place(relx=0, rely=1, x=0, y=0, anchor='sw')
root.mainloop()
