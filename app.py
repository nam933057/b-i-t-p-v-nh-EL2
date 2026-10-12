import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng[span_9](start_span)[span_9](end_span)
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu mẫu[span_10](start_span)[span_10](end_span)
data = {
    'Ho_va_ten': ['Ngô Hoài An', 'Cao Nguyên Khang', 'Phạm Khả Quân', 'Phạm Anh Quân', 'Lê Việt Hoàng', 'Lê Quân', 'Nguyễn Quý', 'Nguyễn Trung Hậu', 'Nguyễn Minh', 'Trần Văn An'],
    'Chuyen_can': [8.0, 9.0, 7.0, 9.5, 7.5, 6.0, 9.0, 7.0, 7.5, 9.5]
    'Giua_ky': [7.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuoi_ky': [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.5, 7.5, 9.0]
}
df = pd.DataFrame(data)

# Tính tổng kết và xếp loại[span_11](start_span)[span_11](end_span)
df['Tong_ket'] = 0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 1. Hiển thị bảng điểm[span_12](start_span)[span_12](end_span)
st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 2. Hiển thị thông tin thống kê[span_13](start_span)[span_13](end_span)
st.subheader("Thống kê chung")
diem_tb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- **Điểm trung bình của lớp:** {diem_tb_lop:.2f}")
st.write(f"- **Sinh viên điểm cao nhất:** {sv_max['Ho_va_ten']} (Điểm: {sv_max['Tong_ket']})")
st.write(f"- **Sinh viên điểm thấp nhất:** {sv_min['Ho_va_ten']} (Điểm: {sv_min['Tong_ket']})")
st.write(f"- **Số sinh viên đạt (≥ 5.0):** {so_sv_dat}")

# 3. Selectbox chọn sinh viên[span_14](start_span)[span_14](end_span)
st.subheader("Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

st.write(f"**Họ và tên:** {student_info['Ho_va_ten']}")
st.write(f"- Điểm chuyên cần: {student_info['Chuyen_can']}")
st.write(f"- Điểm giữa kỳ: {student_info['Giua_ky']}")
st.write(f"- Điểm cuối kỳ: {student_info['Cuoi_ky']}")
st.write(f"- Điểm tổng kết: **{student_info['Tong_ket']:.2f}**")
st.write(f"- Xếp loại: **{student_info['Xep_loai']}**")

# 4. Hiển thị biểu đồ cột[span_15](start_span)[span_15](end_span)
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Sinh viên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
st.pyplot(fig)

# 5. Thông tin người tạo (chữ nhỏ ở cuối trang)[span_16](start_span)[span_16](end_span)
st.markdown("---")
st.markdown("<p style='font-size: small; color: gray;'>Họ và tên: [Đinh Hoàng Nam] - MSSV: [036208001031]</p>", unsafe_allow_html=True)
