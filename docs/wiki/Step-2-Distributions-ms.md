[English](Step-2-Distributions) · [Dansk](Step-2-Distributions-da) · **Bahasa Malaysia**

# Langkah 2: Taburan ciri

**Soalan:** Bagaimana harga, perjalanan, bilik dan akses lebuh raya tertabur, dan berapa banyak rumah bersebelahan sungai?

![Langkah 2: taburan harga, jarak, bilik dan akses lebuh raya](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-2-distributions.png)

## Apa yang dikatakan kuliah

Sebelum membina sebarang model, buku nota meminta anda melihat ciri satu demi satu. Harga, jarak ke lima pusat pekerjaan dan bilangan bilik mendapat histogram dengan lengkung licin di atasnya (Kernel Density Estimate, KDE) daripada Seaborn, dan purata diletakkan dalam tajuk. Akses lebuh raya ialah histogram Matplotlib biasa, dan pemboleh ubah dummy sungai ialah carta bar Plotly dengan label No dan Yes. Tujuannya ialah melihat bentuk data: di mana kebanyakan rumah berada, di mana ekornya dan sama ada ada sesuatu yang kelihatan ganjil.

## Apa yang dilakukan kod

- `price_distribution_figure` melukis harga dengan KDE, 50 bin dan bentuk lebar (`aspect=2`); `price_title` meletakkan purata, 22.53 ribu dolar, dalam tajuk.
- `distance_distribution_figure` dan `rooms_distribution_figure` melakukan perkara yang sama untuk `DIS` (purata 3.80) dan `RM` (purata 6.28); `average_distance` dan `average_rooms` mengira purata dalam lapisan domain.
- `highway_access_figure` ialah histogram Matplotlib bagi `RAD` dengan 24 bin, tepi hitam dan bar sempit; `highway_access_counts` memberi kiraan di belakangnya.
- `river_bar_chart` memulangkan rajah Plotly dengan dua bar No (471 rumah) dan Yes (35 rumah); `river_counts_by_label` memberi kiraan dengan label tersebut.
- `distribution_panel_figure` meletakkan harga, jarak, bilik dan akses lebuh raya dalam gambar di atas.

## Apa yang anda perolehi

- Harga condong ke kanan: kebanyakan rumah berharga sekitar 21 ribu dolar (median 21.2), beberapa buah jauh lebih mahal, dan 16 kawasan berada tepat pada had 50.
- Jarak ke pusat pekerjaan juga condong ke kanan; bilik hampir berbentuk loceng sekitar 6.3.
- Akses lebuh raya bukan pemboleh ubah yang licin: ia mengambil nilai 1 hingga 8 kemudian melompat ke 24, yang mengandungi 132 daripada 506 kawasan. Histogram dengan bin lebar akan menyembunyikan jurang itu.
- Hanya 35 daripada 506 kawasan bersempadan dengan sungai, jadi carta bar pemboleh ubah dummy memberitahu dengan cepat betapa jarangnya kumpulan itu.
- Lengkung KDE membantu anda menilai bentuk, tetapi hanya bar menunjukkan kiraan sebenar; gunakan kedua-duanya.

Sebelumnya: [Step-1-Goals-And-Data-ms](Step-1-Goals-And-Data-ms)
