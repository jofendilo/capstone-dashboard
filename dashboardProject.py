from email.policy import default
import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt

st.set_page_config(page_title="Perlahan Tapi Pasti: Perkembangan Proses Digitalisasi Indonesia", layout="wide")

with st.sidebar:
    st.image(Image.open('idnmap.png'), use_column_width=True)
    st.title("[Insight]: Proses Digitalisasi Indonesia")
    st.subheader("Daftar Isi")
    st.markdown('''
    - [Internet untuk Semua - Pembangunan Menara BTS](#internet-untuk-semua-pembangunan-menara-bts)
    - [Efek Ekspos Internet](#efek-ekspos-internet)
    - ['Buah' Hasil Digitalisasi](#buah-hasil-digitalisasi)
    ''',unsafe_allow_html=True)
    for i in range(2):
        st.write("")
    st.caption('''
        Created by: Jonathan Afendi\n   
        Capstone Project
        DQLab - Tetris Program Digitalent           
    ''')
    

    
st.title("Perlahan Tapi Pasti: Perkembangan Proses Digitalisasi Indonesia")
st.write("Perkembangan teknologi merupakan sesuatu yang pasti terjadi di dunia ini. Teknologi bisa dibilang sebagai tulang punggung bagi perkembangan dunia. Mereka dapat menghubungkan satu manusia dengan yang lain, memudahkan proses belajar, sampai mengefisiensi proses bisnis dan ekonomi secara digital. Oleh karena pengaruh yang luar biasa tersebut, sangatlah bijak bagi para pemimpin dunia untuk dapat melakukan proses digitalisasi, dimana proses tersebut dapat mempengaruhi perkembangan dan kesejahteraan dunia.\n \nIndonesia seperti yang kita ketahui, telah melakukan proses digitalisasi. Hal ini dapat dilihat penggunaan electronic money dan digital banking yang mencapai 4.314,3 Triliun rupiah tahun ini*. Lantas, apa sajakah yang sudah dilakukan oleh Indonesia?")

col1source, col2source = st.columns(2)

with col2source:
    st.caption("<p align=right>*source: https://www.bi.go.id/id/publikasi/ruang-media/cerita-bi/Pages/Pandemi-Pendorong-Digitalisasi.aspx</p>", unsafe_allow_html=True)

df1=pd.read_csv("btsfin.csv")

st.header("Internet untuk Semua - Pembangunan Menara BTS")

provinsi = st.selectbox(
    "Pilih provinsi:",
    df1['Provinsi'].unique()
)
df_selection1= df1[df1["Provinsi"]== provinsi]

col1,col2 = st.columns([3,1])
with col1:
    st.write("<p align=center><b>Total Menara BTS berdasarkan Provinsi</b></p>", unsafe_allow_html=True)
        
    line_chart = alt.Chart(df_selection1).mark_bar(binSpacing=0).encode(
        x=alt.X('Tahun',axis=alt.Axis(labelAngle=360)),
        y='Menara',
        color='Source'
    )

    text= line_chart.mark_text(dy=-5).encode(
        text='Menara'
    )

    linechart=line_chart+text
    st.altair_chart(linechart,use_container_width=True)

with col2:
    for i in range(10):
        st.write("")
    st.caption("<p align=justify><b>Catatan:</b> Interpolasi dilakukan secara linear pada tahun 2015-2017 yang disebabkan oleh ketiadaan data. Data diasumsikan berjalan stagnan.</p>", unsafe_allow_html=True)

st.caption("<p align=center><b>Sumber:</b> https://www.bps.go.id/indicator/2/1677/1/banyaknya-desa-kelurahan-yang-memiliki-menara-base-transceiver-station-bts-menurut-provinsi-dan-klasifikasi-daerah.html</p>", unsafe_allow_html=True)
st.write("Sampai dengan akhir 2021, Indonesia telah membangun lebih dari 39 ribu Menara BTS (Base Transceiver Station) yang berguna untuk menyambung peralatan elektronik ke jaringan internet. Hal ini merupakan tahap awal dari proses digitalisasi pemerintah dimana ekspos internet kepada masyarakat diperkuat. Dapat dilihat dari chart di atas bahwa peningkatan cenderung stabil dan mencapai persentase 44.2% dari tahun 2014 - 2021")

for i in range(2):
    st.write("") 

st.header("Efek Ekspos Internet")    
st.write("Dengan terjadinya ekspos dari layanan internet, masyarakat pun mulai memanfaatkan akses internet untuk kebutuhan sehari-hari. Hal ini dibuktikan dari penggunaan internet yang semakin meningkat sampai dengan tahun 2021. Berikut merupakan figur tampilan chart dari peningkatan penggunaan internet untuk kehidupan sehari-hari")

for i in range(2):
    st.write("") 

df2=pd.read_csv("bps-act.csv")

col1act,col2act = st.columns([1,2])
with col1act:
    provinsi2 = st.selectbox(
        "Pilih provinsi Aktivitas:",
        df2['Provinsi'].unique()
    )
    df_selection2= df2[df2["Provinsi"]==provinsi2]

with col2act:
    aktivitas = st.multiselect(
        "Pilih aktivitas:",
        df2['Aktivitas'].unique(),
        df2['Aktivitas'].unique()
    )
    df_selection2=df_selection2.query("Aktivitas == @aktivitas")
    

st.write("<p align=center><b>Aktivitas Penggunaan Internet (Remaja - Dewasa)</b></p>", unsafe_allow_html=True)

line_chart2 = alt.Chart(df_selection2).mark_line(point = True).encode(
    x=alt.X('Tahun',axis=alt.Axis(labelAngle=360)),
    y='Persentase',
    color='Aktivitas'
)
st.altair_chart(line_chart2,use_container_width=True)

col1sources, col2sources = st.columns(2)
with col1sources:
    st.caption("<p align=center><b>Catatan:</b><br>Persentase pada setiap kategori dihitung berdasarkan jumlah total penduduk di Indonesia. Perlu diketahui bahwa 1 orang bisa melakukan lebih dari 1 aktivitas seperti 'Bekerja' dan 'Sekolah'</p>", unsafe_allow_html=True)

with col2sources:
    st.caption("<p align=center><b>Sumber:</b><br>https://www.bps.go.id/indicator/2/425/1/persentase-penduduk-usia-10-tahun-ke-atas-yang-pernah-mengakses-internet-dalam-3-bulan-terakhir-menurut-provinsi-dan-jenis-kegiatan-utama.html</p>",unsafe_allow_html=True)    

st.write("Sampai dengan 2021, sudah terjadi peningkatan pada seluruh aktivitas yang ada. Menariknya, aktivitas Sekolah (Belajar) meningkat secara pesat di tahun 2017 sampai 2018. Apabila kita melihat pada chart pertama, pembangunan menara BTS mulai dicatat kembali di tahun 2018. Dapat diasumsikan bahwa Pemerintah memperhatikan seluruh aktivitas masyarakat yang ada. Dan ketika melihat adanya lonjakan untuk kegiatan positif seperti belajar, pembangunan fasilitas ditingkatkan kembali.")
st.write("Melihat antusiasme dan peningkatan aktivitas masyarakat melalui internet, pemerintah pun mulai melakukan proses digitalisasi pada bidang layanan lainnya. Dapat kita lihat sekarang bahwa pemerintah mengimplementasi program seperti Perpanjangan SIM Online, Passport Online sampai Pelatihan Digital secara Online yang bertujuan untuk meningkatkan kualitas SDM dan pelayanan kepada masyarakat")

st.header("'Buah' Hasil Digitalisasi")

for i in range(2):
    st.write("") 

df3=pd.read_csv("ketsu.csv")

provinsi3 = st.selectbox(
    "Pilih provinsi Keterampilan:",
    df3['Provinsi'].unique()
)
df_selection3= df3[df3["Provinsi"]==provinsi3]

st.write("<p align=center><b>Peningkatan Keterampilan TIK (Remaja - Dewasa)</b></p>", unsafe_allow_html=True)
bar_chart = alt.Chart(df_selection3).mark_bar().encode(
    x=alt.X('Tahun',axis=alt.Axis(labelAngle=360)),
    y='Persentase',
    color='Provinsi'
)

text2= bar_chart.mark_text(dy=-5).encode(
        text='Persentase'
    )

bar_charts=bar_chart+text2

st.altair_chart(bar_charts,use_container_width=True)
st.caption("<p align=center><b>Sumber:</b>https://www.bps.go.id/indicator/28/1447/1/proporsi-remaja-dan-dewasa-usia-15-59-tahun-dengan-keterampilan-teknologi-informasi-dan-komputer-tik-menurut-provinsi.html</p>",unsafe_allow_html=True) 
st.write("Dari proses digitalisasi yang telah dilakukan, dapat terlihat bahwa terjadi peningkatan impresif untuk keterampilan TIK masyarakat dari tahun 2015 ke 2021. Per tahun 2021, lebih dari 70% masyarakat di Indonesia dinilai sudah melewati batas keterampilan minimal di bidang Teknologi dan Informatika. Dari sini dapat kita simpulkan bahwa, proses digitalisasi dan penambahan fasilitas internet sangat berkolerasi dengan tingkat keterampilan Teknologi Informatika SDM Indonesia.")
st.write("Antusiasme masyarakat untuk mempelajari hal-hal baru disertai dengan fasilitas digital saat ini, sudah meningkatkan daya saing SDM kita dengan negara lainnya. Dengan adanya kelanjutan pengembangan proses digitalisasi, diharapkan kompetensi SDM Indonesia semakin berkembang dan mengungguli negara-negara lainnya.")
