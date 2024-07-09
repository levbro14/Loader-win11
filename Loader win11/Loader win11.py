import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
from threading import Thread
from PIL import ImageTk
import pathlib, os.path


root = tk.Tk()
root.geometry("500x500")
root.title("Loader win11")
root.resizable(False, False)

def disable_all_btn():
    btn_change_path.config(state="disable")
    btn_ds.config(state="disable")
    btn_epic.config(state="disable")
    btn_steam.config(state="disable")
    btn_VsCode.config(state="disable")
    btn_chrome.config(state="disable")
    btn_GPUZ.config(state="disable")
    btn_Telegram.config(state="disable")
    btn_OBS.config(state="disable")

def enable_all_btn():
    btn_change_path.config(state="normal")
    btn_ds.config(state="normal")
    btn_epic.config(state="normal")
    btn_steam.config(state="normal")
    btn_VsCode.config(state="normal")
    btn_chrome.config(state="normal")
    btn_GPUZ.config(state="normal")
    btn_Telegram.config(state="normal")
    btn_OBS.config(state="normal")


path = ""
def change_path():
    global path
    path = filedialog.askdirectory()
    if path == "":
        messagebox.showerror("Ошибка", "Выберите путь для сохранения")
        change_path()
    else:
        btn_change_path.config(text=path)


def download(url, file_name):
    try:
        if path != "":
            disable_all_btn()

            progress_var.set(0)
            with requests.get(url, stream=True) as r:
                total_length = int(r.headers.get('content-length'))
                with open(f"{path}/{file_name}", 'wb') as f:
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = (downloaded / total_length) * 100

                        progress_var.set(percent)
                        lbl_percent.config(text=f"{percent}%")

            messagebox.showinfo("Скачано!", f"Файл успешно скачан в {path}/{file_name}")
            enable_all_btn()


        else:
            messagebox.showerror("Ошибка", "Выберите путь для сохранения")

    except Exception as ex:
        messagebox.showerror("Ошибка", f"Причина ошибки: {ex}")
        enable_all_btn()


    


appdir = pathlib.Path(__file__).parent.resolve()
   
image = ImageTk.PhotoImage(file=os.path.join(appdir,'Discord.png'))
btn_ds = ttk.Button(text="Discord", image=image, command=lambda: Thread(target=download, kwargs={'url': "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64", 'file_name': "Discord.exe"}).start())
btn_ds.place(x=80, y=100, anchor="center", width=80, height=80)

image1 = ImageTk.PhotoImage(file=os.path.join(appdir,'EpicGames.png'))
btn_epic = ttk.Button(text="Epic Games", image=image1, command=lambda: Thread(target=download, kwargs={'url': "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=8f2e6a9865d44aa193bc0895fb4cb28d", 'file_name': "EpicGames.msi"}).start())
btn_epic.place(x=160, y=100, anchor="center", width=80, height=80)

image2 = ImageTk.PhotoImage(file=os.path.join(appdir,'Steam.png'))
btn_steam = ttk.Button(text="Steam", image=image2, command=lambda: Thread(target=download, kwargs={'url': "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe", 'file_name': "EpicGames.msi"}).start())
btn_steam.place(x=240, y=100, anchor="center", width=80, height=80)

image3 = ImageTk.PhotoImage(file=os.path.join(appdir,'VisualStudioCode.png'))
btn_VsCode = ttk.Button(text="Visual Studio Code", image=image3, command=lambda: Thread(target=download, kwargs={'url': "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", 'file_name': "Visual Studio Code.exe"}).start())
btn_VsCode.place(x=320, y=100, anchor="center", width=80, height=80)

image4 = ImageTk.PhotoImage(file=os.path.join(appdir,'Chrome.png'))
btn_chrome = ttk.Button(text="Chrome", image=image4, command=lambda: Thread(target=download, kwargs={'url': "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B598F532A-443B-37B1-14FE-DC1CE6816E0C%7D%26lang%3Dru%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe", 'file_name': "Chrome.exe"}).start())
btn_chrome.place(x=400, y=100, anchor="center", width=80, height=80)

image5 = ImageTk.PhotoImage(file=os.path.join(appdir,'GPU-Z.png'))
btn_GPUZ = ttk.Button(text="GPU-Z", image=image5, command=lambda: Thread(target=download, kwargs={'url': "https://9vp10r.spflare.com/b3/9/3/94369910912a7cd334e4458ad4618748/GPU-Z.2.59.0.exe", 'file_name': "GPU-Z.exe"}).start())
btn_GPUZ.place(x=80, y=200, anchor="center", width=80, height=80)

image6 = ImageTk.PhotoImage(file=os.path.join(appdir,'Telegram.png'))
btn_Telegram = ttk.Button(text="Telegram", image=image6, command=lambda: Thread(target=download, kwargs={'url': "https://telegram.org/dl/desktop/win64", 'file_name': "Telegram.exe"}).start())
btn_Telegram.place(x=160, y=200, anchor="center", width=80, height=80)

image7 = ImageTk.PhotoImage(file=os.path.join(appdir,'OBS.png'))
btn_OBS = ttk.Button(text="OBS-Studio", image=image7, command=lambda: Thread(target=download, kwargs={'url': "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-30.1.2-Full-Installer-x64.exe", 'file_name': "OBS-Studio.exe"}).start())
btn_OBS.place(x=240, y=200, anchor="center", width=80, height=80)


progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.place(x=50, y=420, width=350)

lbl_percent = ttk.Label(text="0%", font=("Arial", 12, "bold"))
lbl_percent.place(x=410, y=420)



btn_change_path = ttk.Button(text="Выбрать местоположение", command=change_path)
btn_change_path.place(x=50, y=450, width=350)

root.mainloop()