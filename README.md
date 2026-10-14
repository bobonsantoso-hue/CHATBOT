# 📚 StudyBuddy - AI Learning Companion

StudyBuddy adalah chatbot berbasis AI yang dirancang untuk membantu mahasiswa dan pelajar dalam proses pembelajaran mereka. Dengan antarmuka yang ramah dan responsif, StudyBuddy siap menjadi teman belajar Anda 24/7!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Target Pengguna

StudyBuddy ditujukan untuk:
- **Mahasiswa** yang membutuhkan bantuan memahami materi kuliah
- **Pelajar SMA/SMP** yang ingin belajar dengan cara yang lebih interaktif
- **Siapa saja** yang ingin meningkatkan kemampuan belajar mereka

## 💡 Bagaimana StudyBuddy Membantu Pengguna?

StudyBuddy membantu pengguna dengan cara:

1. **Menjelaskan Konsep Sulit** 📖
   - Memecah topik kompleks menjadi penjelasan yang mudah dipahami
   - Menggunakan analogi dan contoh yang relevan
   - Menyesuaikan tingkat penjelasan dengan level pengguna

2. **Bantuan Pekerjaan Rumah** ✍️
   - Membimbing proses pemecahan masalah (bukan hanya memberi jawaban)
   - Mendorong pemikiran kritis
   - Memberikan langkah-langkah penyelesaian yang jelas

3. **Strategi Belajar** 🎯
   - Tips manajemen waktu
   - Teknik mencatat yang efektif
   - Strategi persiapan ujian

4. **Motivasi & Dukungan** 💪
   - Memberikan dorongan positif
   - Merayakan kemajuan kecil
   - Membantu mengatasi kesulitan belajar

5. **Tersedia 24/7** ⏰
   - Bantuan kapan saja Anda membutuhkannya
   - Tidak perlu menunggu jam belajar
   - Belajar sesuai ritme Anda sendiri

## ✨ Fitur Utama

- 💬 **Chat Interface yang Intuitif** - Percakapan natural seperti berbicara dengan teman
- 🤖 **AI Cerdas** - Powered by Google Gemini AI
- 🎨 **UI/UX Menarik** - Desain modern dan responsif
- 📊 **Statistik Sesi** - Pantau aktivitas belajar Anda
- 💾 **Riwayat Chat** - Simpan dan review percakapan sebelumnya
- 🌈 **Personalisasi** - Respon disesuaikan dengan kebutuhan Anda

## 🚀 Cara Install & Menjalankan

### Prasyarat

Pastikan Anda sudah menginstall:
- Python 3.8 atau lebih baru
- pip (Python package installer)

### Langkah-langkah Instalasi

1. **Clone atau Download Repository ini**
   ```bash
   git clone <repository-url>
   cd CHATBOT
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup API Key**
   
   a. Copy file `.env.example` menjadi `.env`:
   ```bash
   copy .env.example .env
   ```
   
   b. Dapatkan API Key gratis dari Google:
   - Kunjungi: https://makersuite.google.com/app/apikey
   - Login dengan akun Google Anda
   - Klik "Create API Key"
   - Copy API key yang dihasilkan
   
   c. Buka file `.env` dan ganti `your_api_key_here` dengan API key Anda:
   ```
   GEMINI_API_KEY=AIza...your_actual_key_here
   ```

4. **Jalankan Aplikasi**
   ```bash
   streamlit run app.py
   ```

5. **Buka Browser**
   - Aplikasi akan terbuka otomatis di browser
   - Atau buka manual: http://localhost:8501

## 📖 Cara Menggunakan

1. **Mulai Percakapan**
   - Ketik pertanyaan Anda di kolom input di bagian bawah
   - Tekan Enter atau klik tombol kirim

2. **Contoh Pertanyaan**
   - "Jelaskan tentang fotosintesis"
   - "Bagaimana cara menyelesaikan persamaan kuadrat?"
   - "Tips untuk mengingat materi lebih baik?"
   - "Apa perbedaan antara DNA dan RNA?"

3. **Tips Menggunakan StudyBuddy**
   - Berikan konteks yang jelas dalam pertanyaan Anda
   - Jangan ragu untuk bertanya follow-up jika kurang jelas
   - Gunakan StudyBuddy sebagai alat bantu belajar, bukan hanya untuk mencari jawaban
   - Sebutkan level pendidikan Anda untuk penjelasan yang lebih sesuai

## 🛠️ Teknologi yang Digunakan

- **Python** - Bahasa pemrograman utama
- **Streamlit** - Framework untuk web interface
- **Google Gemini AI** - Model AI untuk natural language processing
- **python-dotenv** - Manajemen environment variables

## 📂 Struktur Project

```
CHATBOT/
│
├── app.py                 # Aplikasi utama Streamlit
├── requirements.txt       # Dependencies Python
├── .env.example          # Template konfigurasi API
├── .gitignore           # File yang diabaikan Git
└── README.md            # Dokumentasi (file ini)
```

## 🎓 Pengembangan Lebih Lanjut

Beberapa ide untuk pengembangan:

- [ ] Tambah fitur export chat history ke PDF
- [ ] Integrasi dengan Google Calendar untuk study schedule
- [ ] Mode quiz interaktif untuk menguji pemahaman
- [ ] Multi-language support (Indonesia, Inggris, dll)
- [ ] Database untuk menyimpan riwayat chat permanen
- [ ] Fitur upload file (PDF, gambar) untuk dianalisis

## ⚠️ Troubleshooting

### Error: "Gemini API key not configured"
- Pastikan file `.env` sudah dibuat (bukan `.env.example`)
- Pastikan API key sudah diisi dengan benar
- Restart aplikasi setelah mengubah `.env`

### Error: "Module not found"
- Jalankan ulang: `pip install -r requirements.txt`
- Pastikan menggunakan Python 3.8+

### Aplikasi tidak terbuka di browser
- Buka manual: http://localhost:8501
- Cek apakah port 8501 sudah digunakan aplikasi lain
- Gunakan port lain: `streamlit run app.py --server.port 8502`

### Respon AI lambat atau error
- Cek koneksi internet Anda
- Verifikasi API key masih aktif di Google AI Studio
- Cek quota API key (gratis ada limitasi)

## 📝 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan portfolio.

## 👨‍💻 Author

Dibuat dengan ❤️ untuk Final Project Hacktiv8

---

## 📸 Screenshot

### Tampilan Awal
![Welcome Screen](screenshot-welcome.png)
*Tampilan welcome dengan fitur-fitur yang tersedia*

### Chat Interface
![Chat Interface](screenshot-chat.png)
*Contoh percakapan dengan StudyBuddy*

---

**Selamat Belajar dengan StudyBuddy! 📚✨**

Jika ada pertanyaan atau saran, jangan ragu untuk menghubungi atau membuat issue di repository ini.
