[English](Step-7-Summary) · [Dansk](Step-7-Summary-da) · **Bahasa Malaysia**

# Langkah 7: Pengajaran dan ringkasan

**Soalan:** Apakah yang diajar oleh hari ke-81, dan di mana setiap pengajaran berada dalam kod?

![Langkah 7: r-kuasa dua kedua-dua model pada data latihan dan data ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-7-summary.png)

## Apa yang dikatakan kuliah

Kuliah 598, "Solution & Learning Points", memberi buku nota yang lengkap dan tujuh pengajaran. Setiap satu ialah kemahiran yang boleh anda guna semula pada set data seterusnya. Jadual menunjukkan di mana projek ini mengajarnya.

| # | Pengajaran | Langkah | Di mana dalam kod |
| --- | --- | --- | --- |
| 1 | Kesan hubungan dalam data dengan plot pasangan | [Langkah 3](Step-3-Relationships-ms) | `pair_plot_figure`, `correlation` |
| 2 | Bahagikan data untuk menilai model pada data yang belum dilihatnya | [Langkah 4](Step-4-Regression-ms) | `split_train_test` |
| 3 | Jalankan regresi berbilang pemboleh ubah | [Langkah 4](Step-4-Regression-ms) | `fit_linear_regression`, `r_squared` |
| 4 | Semak bahawa pekali mempunyai tanda yang anda jangka | [Langkah 4](Step-4-Regression-ms) dan [Langkah 5](Step-5-Log-Model-ms) | `coefficient_table`, `has_expected_signs` |
| 5 | Analisis reja: min, kepencongan dan plot | [Langkah 4](Step-4-Regression-ms) | `residuals`, `residual_mean`, `residual_skew` |
| 6 | Perbaiki model dengan penjelmaan log pada sasaran | [Langkah 5](Step-5-Log-Model-ms) | `fit_log_model`, `compare_test_r_squared` |
| 7 | Gunakan model untuk meramal harga bagi ciri yang dipilih | [Langkah 6](Step-6-Valuation-ms) | `value_property` |

## Apa yang dilakukan kod

`model_scores_figure` melukis gambar di atas daripada kod: r-kuasa dua model linear (0.75 pada data latihan, 0.67 pada data ujian) dan model log (0.79 dan 0.74). Model log menang pada kedua-duanya, dan kedua-duanya kehilangan sedikit padanan pada rumah yang belum dilihat. `value_property` menutup hari ini: hartanah yang dihuraikan bernilai kira-kira $25,792 berbanding $20,703 bagi yang purata. Buku nota `notebooks/boston_valuation.ipynb` menelusuri kesemua enam langkah dan disimpan bersama outputnya.

## Apa yang anda perolehi

- Aliran kerja penuh daripada soalan kepada jawapan: teroka, visualkan, bahagi, padankan, semak, perbaiki dan guna. Setiap peringkat ialah fungsi kecil dengan ujian, jadi anda boleh mengubah satu dan melihat apa yang rosak.
- Tabiat yang lebih penting daripada sebarang nombor tunggal: nilai model pada data yang belum dilihat, baca pekalinya dan lihat rejanya sebelum anda mempercayai ramalan.
- Had yang patut anda ketahui. Data ini dari tahun 1970-an dan daripada 506 kawasan, satu ciri (`B`) mengekod perkadaran kaum, dan regresi menunjukkan perkaitan, bukan sebab. Anggap penilaian itu sebagai latihan.
- Ke mana seterusnya: cuba lebih banyak atau lebih sedikit ciri, pembahagian lain, pengesahan silang, regularisasi (Ridge atau Lasso) atau model berasaskan pokok, dan bandingkannya pada data ujian dengan cara yang sama.

Sebelumnya: [Step-6-Valuation-ms](Step-6-Valuation-ms)
