[English](Step-6-Valuation) · [Dansk](Step-6-Valuation-da) · **Bahasa Malaysia**

# Langkah 6: Menilai sebuah hartanah

**Soalan:** Bagaimana anda menggunakan model untuk menilai rumah purata dan rumah yang anda huraikan?

![Langkah 6: nilai anggaran hartanah purata dan hartanah yang dihuraikan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-6-valuation.png)

## Apa yang dikatakan kuliah

Sekarang model menjawab soalan perniagaan. Buku nota bermula dengan hartanah purata, satu baris yang mengandungi min setiap ciri, dan meminta model log memberi anggaran: harga log 3.03. Fungsi eksponen menukarkannya kembali kepada harga dalam ribuan dolar, dan didarab 1000 ia kira-kira $20,703. Kemudian buku nota menghuraikan sebuah hartanah: bersebelahan sungai, 8 bilik, 20 pelajar bagi setiap guru, 5 unit dari pusat pekerjaan, pencemaran tinggi (persentil ke-75 `NOX`) dan kemiskinan rendah (persentil ke-25 `LSTAT`). Semua ciri lain mengekalkan puratanya. Anggaran log ialah 3.25, iaitu kira-kira $25,792.

## Apa yang dilakukan kod

- `average_property` membina jadual satu baris dengan min 13 ciri.
- `estimate_value` meminta model memberi anggaran log dan menukarnya kepada dolar dengan `exp` dan faktor 1000; ia memulangkan kedua-dua nombor dalam `ValueEstimate`.
- `described_property` bermula daripada hartanah purata dan menetapkan enam ciri: sungai (`CHAS`), bilik (`RM`), pelajar bagi setiap guru (`PTRATIO`), jarak (`DIS`), pencemaran (`NOX`) dan kemiskinan (`LSTAT`).
- `value_property` ialah fungsi tugasan: ciri ialah parameter dengan nilai kuliah sebagai lalai, ia memadankan model log jika anda tidak memberikan satu, dan memulangkan anggaran. Ia menolak nilai yang tidak mungkin benar, seperti sifar bilik.
- `property_characteristics` menyenaraikan apa yang berubah berbanding purata, dan `valuation_figure` melukis gambar di atas.

## Apa yang anda perolehi

- Model hanya berguna apabila anda boleh bertanya soalan kepadanya: anda menghuraikan sebuah hartanah dalam lajur ciri dan mendapat harga kembali. Ciri yang anda tidak tahu kekal pada purata, iaitu lalai yang munasabah.
- Model log meramalkan harga log. Terbalikkan penjelmaan dengan `exp` sebelum bercakap tentang dolar, dan ingat unitnya: harga dalam ribuan.
- Hartanah yang dihuraikan bernilai kira-kira 25 % lebih daripada yang purata ($25,792 berbanding $20,703), kerana bilik tambahan, sungai dan kemiskinan rendah mengatasi pencemaran yang lebih tinggi dan kelas yang lebih besar.
- Dolar ini ialah dolar tahun 1970-an dan model dilatih pada 506 kawasan; anggaran ialah titik permulaan untuk perbincangan, bukan tag harga. Ingat juga bahawa lajur `B` mengekod perkadaran kaum, jadi model ini tidak sepatutnya digunakan dalam amalan.

Sebelumnya: [Step-5-Log-Model-ms](Step-5-Log-Model-ms)
