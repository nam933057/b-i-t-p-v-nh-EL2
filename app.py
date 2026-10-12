#1. Tạo DataFrame
"Ho_va_ten':['Ngô Hoài An', 'Cao Nguyên Khang', 'Phạm Kha Quan', 'Phạm Anh Quan', 'Lê Việt Hoàng', 'Lê Quân', 'Nguyễn Quý', 'Nguyễn Trung Hậu', 'Nguyễn Minh Chiến', 'Lê Sơn Huớng'] ,
"Diem_chuyen_can':[6.0, 6.0, 8.0, 7.0, 9.0, 5.0, 7.0, 10.0, 8,5, 7.5] ,
"Diem_giua_ky':[6.5, 5.5, 8.5, 8.0, 6.5, 6.0, 7.5, 10.0, 8.0, 7.0],
"Diem_cuoi_ky':[7.0, 4.5, 8.0, 8.0, 7.0, 6.5, 7.0, 9.0, 7.5, 7,0] ,
df=pd.DataFrame(data)
# Hiển thị bản giữ liệu 
   print("df")
 #2. Tính điểm tổng kết
 # công thức: điểm tổng kết=0.2*chuyen_can+0.3*giua_ky+0.5*cuoi_ky
df['Tong_ket']=(0.2*df['chuyen_can']+0.3*df['giua_ky']+0.5*df['cuoi_ky']).round(2)
#thêm kết quả vào cột Tong_ket của DataFrame
print(df[[' Ho_va_ten','Tong_ket']])
#3. Xếp loại sinh viên
if:  diem_tong_ket  >=8.5 :
	print("Giỏi")
if: diem_tong_ket   >=7.0 :
	print("Khá")
if: diem_tong_ket.  >=5.0:
	print("Trung bình")
else:
	print("Yếu")
	df['Xep_loai']=df['Tong_ket'].apply(xep_loai) 	print("--- BẢNG ÐIỂM ÐẦY ÐỦ VÀ XẾP LOẠI -----")
	print("df")
	#4 Thống Kê
	#điểm tổng kết trung bình của lớp
	dtb_lop = df['Tong_ket'].mean()
	# sinh viên có điểm tổng kết cao nhất và thấp nhất 
	sv_max =df.loc[df["Tong_ket"].idmax()]
	sv_min  =df.loc[df["Tong_ket"].idmin()]
	# số sinh viên đạt(điểm tổng kết >=5)
	so_sv_dat =(df['Tong_ket']>=5.0.sum())
	print(f"điểm tổng kết trung bình của lớp:{dtb_lop:.2f}")
	print(f"Sinh viên cao điểm nhất: {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']})")
	print(f"Sinh viên thấp điểm nhất: {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']})")
print(f"Số sinh viên đạt: {so_sv_dat}")
#5. Trực quan hóa
plt.figure(figsize=(10, 5))
plt.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue')
plt.xlabel('Tên sinh viên')
plt.ylabel('Điểm tổng kết')
plt.title('Biểu đồ thể hiện điểm tổng kết của 10 sinh viên')
plt.ylim(0, 10)
for i, v in enumerate(df['diem_tong_ket']):
    plt.text(i, v + 0.1, str(v), ha='center')
plt.show()
# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu
data = {
    'Ho_va_ten': ['Ngô Hoài An', 'Cao Nguyên Khang', 'Phạm Kha Quan', 'Phạm Anh Quan', 'Lê Việt Hoàng', 'Lê Quân', 'Nguyễn Quý', 'Nguyễn Trung Hậu', 'Nguyễn Minh Chiến', 'Lê Sơn Huớng'],
    'Diem_chuyen_can': [6.0, 6.0, 8.0, 7.0, 9.0, 5.0, 7.0, 10.0, 8,5, 7.5],
    'Diem_giua_ky': [6.5, 5.5, 8.5, 8.0, 6.5, 6.0, 7.5, 10.0, 8.0, 7.0],
    'Diem_cuoi_ky': [7.0, 4.5, 8.0, 8.0, 7.0, 6.5, 7.0, 9.0, 7.5, 7,0]
}

df = pd.DataFrame(data)
df['Diem_tong_ket'] = (0.2 * df['diem_chuyen_can']) + (0.3 * df['diem_giua_ky']) + (0.5 * df['diem_cuoi_ky'])

def xep_loai(dtk):
    if diem_tong_ket >= 8.5:
        return 'Giỏi'
    elif diem_tong_ket >= 7.0:
        return 'Khá'
    elif diem_tong_ket >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Hiển thị bảng điểm
st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# Hiển thị thống kê
st.subheader("Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5).sum()

st.write(f"- **Điểm trung bình của lớp:** {dtb_lop:.2f}")
st.write(f"- **Sinh viên cao điểm nhất:** {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']:.2f})")
st.write(f"- **Sinh viên thấp điểm nhất:** {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']:.2f})")
st.write(f"- **Số sinh viên đạt ($\ge 5$ điểm):** {so_sv_dat}")

# Danh sách chọn sinh viên (Selectbox)
st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])

student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]
st.write(f"**Họ và tên:** {student_info['Ho_va_ten']}")
st.write(f"- Điểm chuyên cần: {student_info['diem_chuyen_can']}")
st.write(f"- Điểm giữa kỳ: {student_info['diem_giua_ky']}")
st.write(f"- Điểm cuối kỳ: {student_info['diem_cuoi_ky']}")
st.write(f"- **Điểm tổng kết:** {student_info['diem_tong_ket']:.2f}")
st.write(f"- **Xếp loại:** {student_info['Xep_loai']}")

# Biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết lớp học")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='royalblue')
ax.set_xlabel('Họ tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
st.pyplot(fig)

# Thông tin người tạo (chữ nhỏ ở cuối trang)
st.markdown("---")
st.markdown("<p style='font-size: small; color: gray;'>Họ tên: [Ðinh Hoàng Nam] - MSSV: [036208001031]</p>", unsafe_allow_html=True)
