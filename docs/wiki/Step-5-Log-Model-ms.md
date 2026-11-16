[English](Step-5-Log-Model) · [Dansk](Step-5-Log-Model-da) · **Bahasa Malaysia**

# Langkah 5: Penjelmaan log

**Soalan:** Bolehkah penjelmaan log harga memberi padanan yang lebih baik, dan bagaimana kita membandingkan model pada data yang belum dilihat?

![Langkah 5: model linear dan model harga log bersebelahan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-5-log-model.png)

## Apa yang dikatakan kuliah

Reja model pertama condong ke kanan, dan harga itu sendiri condong (1.11). Idea kuliah ialah mengubah sasaran: ambil logaritma tabii harga, padankan regresi yang sama padanya, dan lihat sama ada reja kelihatan lebih seperti hingar. Buku nota menunjukkan bagaimana log memampatkan harga yang besar, kemudian menggunakan semula pembahagian 80/20 yang sama supaya kedua-dua model dinilai pada rumah yang sama. Model log memadankan data latihan dengan lebih baik (r-kuasa dua 0.79 berbanding 0.75), dan rejanya hampir simetri. Semakan akhir ialah data ujian: kedua-dua model mendapat skor lebih rendah di situ berbanding data latihan, dan model log masih lebih baik.

## Apa yang dilakukan kod

- `price_skew`, `log_price` dan `log_price_skew` memberi kepencongan harga (1.11) dan harga log (-0.33). `price_skew_figure`, `log_price_skew_figure` dan `log_mapping_figure` melukis kedua-dua taburan dan lengkung yang memetakan harga kepada lognya.
- `fit_linear_model` dan `fit_log_model` memadankan kedua-dua model pada pembahagian yang sama (404 dan 102 baris yang sama kerana `random_state` tetap) dan menyimpan r-kuasa dua latihan dan ujian, ramalan serta reja bersama.
- `log_coefficient_table` memulangkan pekali model log, dan `has_expected_signs` menyemaknya: `CHAS` +0.080, `RM` +0.073, `PTRATIO` -0.035, `LSTAT` -0.031 dan `NOX` -0.704.
- `compare_test_r_squared` memulangkan r-kuasa dua set ujian bagi kedua-dua model: 0.67 untuk model linear dan 0.74 untuk model log.
- `log_actual_vs_predicted_figure`, `log_residuals_vs_predicted_figure` dan `log_residual_distribution_figure` melukis model log dalam biru laut; `model_comparison_panel_figure` meletakkan model linear indigo dan model log biru laut dalam gambar di atas.

## Apa yang anda perolehi

- Sasaran yang condong boleh diubah. Kepencongan harga turun daripada 1.11 kepada -0.33 dengan log, dan kepencongan reja turun daripada 1.46 kepada 0.09, jadi ralat jauh lebih hampir kepada lengkung loceng.
- Pekali model log ialah perubahan relatif: satu pelajar tambahan bagi setiap guru (`PTRATIO`, -0.035) menurunkan harga kira-kira 3.5 %, dan rumah bersebelahan sungai (`CHAS`, +0.080) bernilai kira-kira 8 % lebih, jika semua yang lain sama.
- R-kuasa dua latihan sentiasa kelihatan lebih baik daripada sepatutnya. Bandingkan model pada data ujian: di sini 0.67 berbanding 0.74, jadi padanan yang lebih baik bukan ilusi.
- Ramalan daripada model log ialah harga log. Tukarkannya semula kepada dolar dengan fungsi eksponen, yang dilakukan oleh langkah seterusnya.

Sebelumnya: [Step-4-Regression-ms](Step-4-Regression-ms)
