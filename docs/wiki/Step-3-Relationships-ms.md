[English](Step-3-Relationships) · [Dansk](Step-3-Relationships-da) · **Bahasa Malaysia**

# Langkah 3: Hubungan dalam data

**Soalan:** Ciri manakah bergerak bersama, dan apa yang anda jangka sebelum membina model?

![Langkah 3: lima hubungan dan korelasi setiap ciri dengan harga](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-3-relationships.png)

## Apa yang dikatakan kuliah

Sebelum model, buku nota meminta anda membuat ramalan kemudian menyemaknya. Adakah anda menjangka pencemaran lebih tinggi atau lebih rendah jauh dari pusat pekerjaan? Apakah yang patut dilakukan oleh bilangan bilik kepada harga, dan apakah yang patut dilakukan oleh peratusan penduduk berpendapatan rendah? Plot pasangan (pair plot) Seaborn melukis setiap ciri terhadap yang lain sekali gus (ia boleh mengambil seminit dua dengan semua 14 lajur), dan lima plot sendi (joint plot) kemudian meneliti hubungan tunggal dengan lebih terperinci: jarak melawan pencemaran, industri melawan pencemaran, kemiskinan melawan bilik, kemiskinan melawan harga dan bilik melawan harga. Plot serakan menggunakan sedikit ketelusan (`alpha=0.5`) supaya titik yang bertindih dapat dibezakan.

## Apa yang dilakukan kod

- `pair_plot_figure` melukis plot pasangan, dengan pilihan garis regresi dan pilihan subset lajur, supaya ujian dan percubaan kekal pantas.
- `joint_plot_figure` ialah satu fungsi pembantu di belakang `distance_pollution_figure`, `pollution_industry_figure`, `poverty_rooms_figure`, `poverty_price_figure` dan `rooms_price_figure`; setiap satu menetapkan warna, saiz dan `alpha` tugasan.
- `correlation` memulangkan korelasi dua ciri, dan fungsi pembantu bernama bagi setiap pemerhatian menyokongnya dengan angka: jarak dan pencemaran -0.77, pencemaran dan industri 0.76, kemiskinan dan bilik -0.61, kemiskinan dan harga -0.74, bilik dan harga 0.70.
- `correlation_with_price` menyusun semua ciri mengikut kekuatan hubungannya dengan harga; `step_3_relationships` melukis gambar di atas daripada angka ini.

## Apa yang anda perolehi

- Pencemaran menurun apabila jarak ke pusat pekerjaan bertambah dan meningkat dengan bahagian industri: kilang dan pencemaran berkait rapat.
- Rumah di kawasan yang lebih miskin (`LSTAT` tinggi) mempunyai lebih sedikit bilik dan harga lebih rendah, dan lebih banyak bilik bermakna harga lebih tinggi. Inilah tanda yang anda jangka daripada regresi.
- Ciri boleh berkait antara satu sama lain dan bukan hanya dengan harga (`RAD` dan `TAX` mempunyai korelasi 0.91). Ini dipanggil multikolineariti dan merupakan sebab untuk berhati-hati apabila anda membaca pekali kemudian.
- Korelasi hanyalah satu angka untuk hubungan garis lurus; plot serakan menunjukkan sama ada bentuknya benar-benar garis, jadi lihat kedua-duanya.

Sebelumnya: [Step-2-Distributions-ms](Step-2-Distributions-ms)
