import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_NAME = "xemay.db"

# ==========================================
# DATABASE FUNCTIONS
# ==========================================
def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS xemay (
            MaXe INTEGER PRIMARY KEY,
            TenXe TEXT,
            HangXe TEXT,
            MauSac TEXT,
            GiaBan REAL,
            SoLuong INTEGER
        );
    """)

    cur.execute("DELETE FROM xemay")

    # Thêm dữ liệu mẫu
    sample_data = [
        (101, "Wave Alpha", "Honda", "Đỏ", 18600000, 20),
        (102, "Wave RSX", "Honda", "Đen", 24100000, 15),
        (103, "Future 125", "Honda", "Xanh", 31300000, 10),
        (104, "Vision 110", "Honda", "Trắng", 36900000, 25),
        (105, "Air Blade 125", "Honda", "Đỏ đen", 42200000, 12),
        (106, "Air Blade 160", "Honda", "Đen bạc", 56600000, 8),
        (107, "Winner X", "Honda", "Đen cam", 46800000, 7),

        (201, "Sirius FI", "Yamaha", "Đỏ", 21000000, 30),
        (202, "Jupiter FI", "Yamaha", "Xanh", 30000000, 18),
        (203, "Exciter 150", "Yamaha", "Xanh GP", 47500000, 14),
        (204, "Exciter 155 VVA", "Yamaha", "Xám", 51500000, 10),
        (205, "NVX 155", "Yamaha", "Xanh đen", 51500000, 9),

        (301, "Raider R150", "Suzuki", "Đen", 50800000, 6),
        (302, "Satria F150", "Suzuki", "Xanh GP", 53500000, 8),
        (303, "GD110", "Suzuki", "Đỏ đen", 28000000, 11),

        (401, "Elizabeth", "SYM", "Đỏ đô", 31000000, 17),
        (402, "Attila", "SYM", "Đen", 33500000, 13),
        (403, "Star SR", "SYM", "Xanh đen", 19500000, 20),

        (501, "Liberty 125 ABS", "Piaggio", "Trắng", 61000000, 7),
        (502, "Medley ABS", "Piaggio", "Xám", 75600000, 5),
        (503, "Vespa Primavera", "Piaggio", "Vàng", 85200000, 4)
    ]

    cur.executemany("""
        INSERT INTO xemay (MaXe, TenXe, HangXe, MauSac, GiaBan, SoLuong)
        VALUES (?, ?, ?, ?, ?, ?)
    """, sample_data)

    conn.commit()
    conn.close()



# ==========================================
# GUI APPLICATION
# ==========================================
class App(tk.Tk):
    
    
    def __init__(self):
        super().__init__()

        self.title("QUẢN LÝ XE MÁY")
        self.resizable(False, False)
        self.resizable(False, False)
        self.resizable(True, True)
        self.update_idletasks() 
        width = 950
        height = 630
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
        # ========== TIÊU ĐỀ ==========
        title = tk.Label(self, text="QUẢN LÝ XE MÁY", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # ========== FRAME NHẬP LIỆU ==========
        form_frame = tk.Frame(self)
        form_frame.pack(fill="x", padx=20)

        # Các nhãn – ô nhập
        labels = ["Mã Xe", "Tên Xe", "Hãng Xe", "Màu Sắc", "Giá Bán", "Số Lượng"]
        self.entries = {}

        # Dòng 1
        tk.Label(form_frame, text="Mã Xe").grid(row=0, column=0, sticky="w")
        self.entries["MaXe"] = tk.Entry(form_frame, width=20)
        self.entries["MaXe"].grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Hãng Xe").grid(row=0, column=2, sticky="w")
        self.entries["HangXe"] = ttk.Combobox(form_frame, width=18, values=[
            "Honda", "Yamaha", "Suzuki", "SYM", "Piaggio"
        ])
        self.entries["HangXe"].grid(row=0, column=3, padx=10, pady=5)

        # Dòng 2
        tk.Label(form_frame, text="Tên Xe").grid(row=1, column=0, sticky="w")
        self.entries["TenXe"] = tk.Entry(form_frame, width=20)
        self.entries["TenXe"].grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Màu Sắc").grid(row=1, column=2, sticky="w")
        self.entries["MauSac"] = tk.Entry(form_frame, width=20)
        self.entries["MauSac"].grid(row=1, column=3, padx=10, pady=5)

        # Dòng 3
        tk.Label(form_frame, text="Giá Bán").grid(row=2, column=0, sticky="w")
        self.entries["GiaBan"] = tk.Entry(form_frame, width=20)
        self.entries["GiaBan"].grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Số Lượng").grid(row=2, column=2, sticky="w")
        self.entries["SoLuong"] = tk.Entry(form_frame, width=20)
        self.entries["SoLuong"].grid(row=2, column=3, padx=10, pady=5)

        # ========== NÚT CHỨC NĂNG ==========
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Thêm", width=12, command=self.insert_record).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Lưu", width=12, command=self.update_record).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Sửa", width=12, command=self.edit_record).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Hủy", width=12, command=self.clear_inputs).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Xóa", width=12, command=self.delete_record).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Thoát", width=12, command=self.quit).grid(row=0, column=5, padx=5)

        # ========== DANH SÁCH XE ==========
        tk.Label(self, text="Danh sách xe máy", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)

        columns = ("MaXe", "TenXe", "HangXe", "MauSac", "GiaBan", "SoLuong")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=130)

        self.tree.pack(padx=20, fill="both")
        self.tree.bind("<ButtonRelease-1>", self.select_item)

        # Load dữ liệu từ DB
        create_tables()
        self.load_data()

    # =======================================
    # CHỨC NĂNG
    # =======================================
    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM xemay")

        for row in cur.fetchall():
           formatted_price = "{:,.0f}".format(row[4]).replace(",", ".")
           new_row = (row[0], row[1], row[2], row[3], formatted_price, row[5])
           self.tree.insert("", tk.END, values=new_row)

        conn.close()

    def insert_record(self):
        try:
            data = (
                int(self.entries["MaXe"].get()),
                self.entries["TenXe"].get(),
                self.entries["HangXe"].get(),
                self.entries["MauSac"].get(),
                float(self.entries["GiaBan"].get()),
                int(self.entries["SoLuong"].get())
            )
        except:
            messagebox.showerror("Lỗi", "Vui lòng nhập đúng dữ liệu!")
            return

        conn = connect_db()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO xemay VALUES (?, ?, ?, ?, ?, ?)", data)
            conn.commit()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
        conn.close()
        self.load_data()
        self.clear_inputs()

    def select_item(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        
        values = self.tree.item(selected[0], "values")
        keys = ["MaXe", "TenXe", "HangXe", "MauSac", "GiaBan", "SoLuong"]

        for i, key in enumerate(keys):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, values[i])

    def edit_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Hãy chọn xe để sửa")
            return
        self.select_item(None)

    def update_record(self):
        try:
            data = (
                self.entries["TenXe"].get(),
                self.entries["HangXe"].get(),
                self.entries["MauSac"].get(),
                float(self.entries["GiaBan"].get()),
                int(self.entries["SoLuong"].get()),
                int(self.entries["MaXe"].get())
            )
        except:
            messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")
            return

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("""
            UPDATE xemay SET TenXe=?, HangXe=?, MauSac=?, GiaBan=?, SoLuong=?
            WHERE MaXe=?
        """, data)

        conn.commit()
        conn.close()
        self.load_data()
        self.clear_inputs()

    def delete_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Chưa chọn", "Hãy chọn xe để xóa!")
            return

        maxe = self.tree.item(selected[0])["values"][0]

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM xemay WHERE MaXe=?", (maxe,))
        conn.commit()
        conn.close()

        self.load_data()
        self.clear_inputs()

    def clear_inputs(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


# ==========================================
# RUN APP
# ==========================================
if __name__ == "__main__":
    app = App()
    app.mainloop()
