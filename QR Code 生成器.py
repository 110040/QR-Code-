import qrcode as qr
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as fd
from PIL import ImageTk

def generate():
    qr_label.qr_img = qr.make(encode_text.get())
    img_width, img_height = qr_label.qr_img.size
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img)
    qr_label.config(image=qr_label.tk_img, width=img_width, height=img_height)
    qr_label.pack()

    # 在生成成功後彈出成功的提示視窗
    messagebox.showinfo('操作順利完成', 'QR Code 生成完成!!!')

def save():
    filename = fd.asksaveasfilename(title='儲存檔案', initialfile='qrcode.png')
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

def exit_app():
    base.destroy()

def about():
    messagebox.showinfo("關於", "QR Code 生成器 v4.0\n\n作者：邱苡宬")

def story():
    story_window = tk.Toplevel()
    story_window.title("故事")

    # 在新視窗中添加 Label 顯示故事內容，設定字型大小為30
    story_label = tk.Label(story_window, text="這是宣傳標語的那個故事...\n\n今天是一年一度的貓狗對抗大賽，\n和往常一樣，每個人都有自己支持的對象\n老鼠小米更是前一天就請早起的貓咪叫他起床\n沒想到，貓咪居然沒有來叫他起床\n她氣死了，邊跺腳邊走到比賽現場\n走到比賽現場後，比賽都已經比完了\n主持人宣布:「小貓隊大敗小狗隊獲得本次冠軍」\n小米傷心極了，因為小貓對大敗\n坐在旁邊的小牛前來關心\n還順便告訴他:「這次小貓隊贏了呵」\n小米瞬間歡天喜地，嘴裡還喃喃自語的說著:「原來是聽錯了啊」", font=("微軟正黑體", 20))
    story_label.pack()


base = tk.Tk()
base.title('QR Code 生成器')

# 創建菜單
menu_bar = tk.Menu(base)
base.config(menu=menu_bar)

# 檔案選單
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="選單", menu=file_menu)
file_menu.add_command(label="關於", command=about)
file_menu.add_command(label="故事", command=story)
file_menu.add_separator()
file_menu.add_command(label="離開", command=exit_app)

input_area = tk.Frame(base, relief=tk.RAISED, bd=2)
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2)

encode_text = tk.StringVar()
entry = tk.Entry(input_area, textvariable=encode_text)
entry.pack(side=tk.LEFT)

qr_label = tk.Label(image_area)

encode_button = tk.Button(input_area, text='開始生成!', command=generate)
encode_button.pack(side=tk.LEFT)

input_area.pack(pady=5)
image_area.pack(padx=3, pady=1)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

context_menu = tk.Menu(base, tearoff=0)
context_menu.add_command(label="儲存此QR Code", command=save)

base.bind('<Button-3>', show_context_menu)

base.mainloop()
