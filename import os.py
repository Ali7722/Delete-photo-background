import os
from tkinter import Tk, Button, filedialog, Label
from rembg import remove
from PIL import Image

def select_image():
    # فتح نافذة اختيار الملفات واختيار صورة
    file_path = filedialog.askopenfilename(
        title="اختر الصورة",
        filetypes=[("Image Files", "*.jpeg;*.jpg;*.png;*.bmp")]
    )
    
    if file_path:
        # تحميل الصورة وإزالة الخلفية
        inp = Image.open(file_path)
        output = remove(inp)

        # حفظ الصورة في نفس مسار الصورة الأصلية كملف PNG
        output_path = os.path.splitext(file_path)[0] + "_output.png"
        output.save(output_path)

        # تحديث النص لعرض رسالة النجاح
        result_label.config(text=f"تم حفظ الصورة المعدلة في:\n{output_path}")

# إعداد واجهة tkinter
root = Tk()
root.title("برنامج إزالة الخلفية")
root.geometry("400x200")

# زر لاختيار الصورة
select_button = Button(root, text="اختر الصورة", command=select_image, width=20, height=2)
select_button.pack(pady=20)

# تسمية لعرض الرسالة النهائية
result_label = Label(root, text="", wraplength=300)
result_label.pack()

# تشغيل واجهة tkinter
root.mainloop()
