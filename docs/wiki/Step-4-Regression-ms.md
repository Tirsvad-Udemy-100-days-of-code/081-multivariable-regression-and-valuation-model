[English](Step-4-Regression) · [Dansk](Step-4-Regression-da) · **Bahasa Malaysia**

# Langkah 4: Pembahagian dan regresi berbilang pemboleh ubah

**Soalan:** Mengapa kita membahagi data, bagaimana kita memadankan regresi, dan bagaimana kita membaca pekali serta reja?

![Langkah 4: harga sebenar melawan harga ramalan, reja melawan harga ramalan dan taburan reja](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-4-regression.png)

## Apa yang dikatakan kuliah

Kuliah memberi pengajaran pertama tentang model: ketepikan sebahagian data sebelum memadankan, supaya anda boleh menilai model pada rumah yang tidak pernah dilihatnya. Buku nota membahagi jadual 80/20 dengan keadaan rawak (random state) tetap, jadi rumah yang sama sentiasa jatuh dalam bahagian yang sama: 404 untuk latihan dan 102 untuk ujian (79.8 % dan 20.2 %). Regresi berbilang pemboleh ubah kemudian memadankan satu pekali bagi setiap ciri, dan kuliah membaca hasilnya dalam tiga cara: r-kuasa dua 0.75 pada data latihan, tanda setiap pekali berbanding apa yang anda jangka, dan reja, iaitu jurang antara harga sebenar dan harga ramalan.

## Apa yang dilakukan kod

- `split_features_and_target` memisahkan 13 ciri daripada `PRICE`, `split_train_test` membuat pembahagian 80/20 dengan `random_state=10`, dan `split_percentages` melaporkan bahagiannya.
- `fit_linear_regression` memadankan `LinearRegression` pada data latihan dan `r_squared` menilainya: 0.75 pada data latihan (dan 0.67 pada data ujian, yang dibandingkan oleh langkah 5 dengan model log).
- `coefficient_table` memberi satu pekali bagi setiap ciri. `room_premium` mendarab pekali `RM` (3.11) dengan 1000: satu bilik tambahan menambah kira-kira $3,108.5 pada harga.
- `predictions`, `residuals`, `residual_mean` dan `residual_skew` melakukan analisis reja: puratanya hampir 0 dan kepencongannya 1.46.
- `actual_vs_predicted_figure`, `residuals_vs_predicted_figure` dan `residual_distribution_figure` melukis carta dalam warna indigo dengan garis cyan di mana ramalan sama dengan sebenar; `regression_panel_figure` meletakkannya dalam gambar di atas.

## Apa yang anda perolehi

- Model mesti dinilai pada data yang belum dilihatnya. `random_state` tetap menjadikan pembahagian boleh diulang, dan bahagian yang ditahan ialah pilihan yang boleh anda pertahankan.
- Pekali bercerita yang boleh anda semak: `RM` positif (+3.11, lebih banyak bilik lebih mahal), `CHAS` positif (+1.98, sungai menambah nilai), manakala `LSTAT` (-0.58), `NOX` (-16.27), `DIS` (-1.48) dan `PTRATIO` (-0.82) negatif. Pekali berada dalam unit cirinya sendiri, jadi bandingkan tanda sebelum saiz.
- Reja sepatutnya kelihatan seperti hingar rawak di sekitar sifar. Di sini ia berpusat pada 0 tetapi condong ke kanan: model memandang rendah beberapa rumah mahal, dan harga yang dihadkan pada 50 kelihatan sebagai satu baris titik dalam carta pertama. Itu petunjuk bahawa harga mungkin boleh diubah, iaitu langkah seterusnya.

Sebelumnya: [Step-3-Relationships-ms](Step-3-Relationships-ms)
