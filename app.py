from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fuzzy', methods=['GET'])
def fuzzy():
    return render_template('fuzzy.html')

@app.route('/pakar', methods=['GET'])
def pakar():
    return render_template('pakar.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    tipe = request.form.get('tipe')
    if tipe == 'fuzzy':
        return proses_fuzzy()
    elif tipe == 'pakar':
        return proses_pakar()
    else:
        return redirect(url_for('index'))

def proses_fuzzy():
    nama = request.form.get('nama', '').strip()
    nim = request.form.get('nim', '').strip()
    semester = request.form.get('semester', '').strip()
    tugas = request.form.get('tugas', type=int, default=5)
    stres = request.form.get('stres', type=int, default=5)
    motivasi = request.form.get('motivasi', type=int, default=5)
    tidur = request.form.get('tidur', type=int, default=5)

    if not nama or not nim or not semester:
        return render_template('fuzzy.html', error='Semua field harus diisi!')

    burnout = (tugas + stres + (11 - motivasi) + (11 - tidur)) / 40

    if burnout <= 0.39:
        kategori = 'Rendah'
        warna = '#10b981'
        icon = '😊'
        rekomendasi = 'Pertahankan pola hidup sehat Anda saat ini. Terus jaga keseimbangan antara akademik dan kehidupan pribadi.'
    elif burnout <= 0.69:
        kategori = 'Sedang'
        warna = '#f59e0b'
        icon = '😐'
        rekomendasi = 'Perbaiki manajemen waktu Anda. Buat jadwal yang terstruktur dan sisihkan waktu untuk istirahat dan relaksasi.'
    else:
        kategori = 'Tinggi'
        warna = '#ef4444'
        icon = '😰'
        rekomendasi = 'Segera istirahat dan kurangi beban. Pertimbangkan untuk berkonsultasi dengan konselor kampus.'

    data = {
        'tipe': 'fuzzy', 'nama': nama, 'nim': nim, 'semester': semester,
        'tugas': tugas, 'stres': stres, 'motivasi': motivasi, 'tidur': tidur,
        'burnout': round(burnout, 4), 'burnout_persen': round(burnout * 100, 1),
        'kategori': kategori, 'warna': warna, 'icon': icon, 'rekomendasi': rekomendasi
    }
    return render_template('hasil.html', data=data)

def proses_pakar():
    gejala = request.form.getlist('gejala')
    if not gejala:
        return render_template('pakar.html', error='Pilih minimal satu gejala!')

    diagnosa_list = []

    if 'mesin_sulit' in gejala and 'starter_rusak' in gejala:
        diagnosa_list.append({
            'diagnosa': 'Aki Lemah / Rusak', 'icon': '🔋', 'warna': '#ef4444',
            'penyebab': 'Aki melemah atau rusak sehingga tidak mampu menyuplai daya listrik yang cukup.',
            'solusi': 'Periksa kondisi aki, bersihkan terminal aki, dan ganti aki jika sudah tidak layak pakai.'
        })

    if 'mesin_mati' in gejala and 'tidak_bertenaga' in gejala:
        diagnosa_list.append({
            'diagnosa': 'Masalah Bahan Bakar', 'icon': '⛽', 'warna': '#f59e0b',
            'penyebab': 'Suplai bahan bakar ke mesin terganggu, bisa karena filter atau karburator/injektor kotor.',
            'solusi': 'Periksa dan bersihkan karburator atau injektor. Ganti filter bensin jika perlu.'
        })

    if 'asap_berlebihan' in gejala:
        diagnosa_list.append({
            'diagnosa': 'Pembakaran Tidak Sempurna', 'icon': '💨', 'warna': '#8b5cf6',
            'penyebab': 'Campuran udara dan bahan bakar tidak seimbang, atau busi sudah aus.',
            'solusi': 'Periksa dan ganti busi secara berkala. Setting ulang karburator.'
        })

    if 'suara_kasar' in gejala:
        diagnosa_list.append({
            'diagnosa': 'Masalah Oli atau Mesin', 'icon': '🔧', 'warna': '#06b6d4',
            'penyebab': 'Pelumasan mesin tidak optimal, oli kotor atau volume oli kurang.',
            'solusi': 'Ganti oli mesin secara rutin. Jika masih kasar, periksa komponen internal mesin.'
        })

    if not diagnosa_list:
        diagnosa_list.append({
            'diagnosa': 'Tidak Teridentifikasi', 'icon': '❓', 'warna': '#64748b',
            'penyebab': 'Kombinasi gejala tidak sesuai dengan rule dalam basis pengetahuan.',
            'solusi': 'Pilih kombinasi gejala yang lebih spesifik atau bawa ke bengkel resmi.'
        })

    gejala_teks = {
        'mesin_sulit': 'Mesin sulit dinyalakan', 'starter_rusak': 'Starter tidak berfungsi',
        'mesin_mati': 'Mesin mati mendadak', 'tidak_bertenaga': 'Motor tidak bertenaga',
        'asap_berlebihan': 'Asap knalpot berlebihan', 'suara_kasar': 'Suara mesin kasar'
    }
    gejala_dipilih = [gejala_teks.get(g, g) for g in gejala]

    data = {'tipe': 'pakar', 'gejala_dipilih': gejala_dipilih, 'diagnosa_list': diagnosa_list}
    return render_template('hasil.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
