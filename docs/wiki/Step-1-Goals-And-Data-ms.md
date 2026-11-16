[English](Step-1-Goals-And-Data) · [Dansk](Step-1-Goals-And-Data-da) · **Bahasa Malaysia**

# Langkah 1: Matlamat dan penerokaan data

**Soalan:** Apakah tugasnya, apa yang ada dalam data harga rumah Boston, adakah ia bersih, dan apa kata statistik deskriptif?

![Langkah 1: statistik deskriptif data harga rumah Boston](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model/raw/branch/main/docs/images/step-1-goals.png)

## Apa yang dikatakan kuliah

Kuliah 597, "Day 81 Goals", meletakkan anda di Boston pada tahun 1970-an. Sebuah syarikat pembangunan hartanah mahu menilai projek kediaman sebelum ia bermula, dan anda membina modelnya: daripada bilangan bilik, jarak ke pusat pekerjaan, betapa kaya atau miskin kawasan itu, bilangan pelajar bagi setiap guru dan ciri yang serupa kepada anggaran harga. Rancangan hari ini ialah meneroka data, membahagikannya kepada data latihan dan data ujian, menjalankan regresi berbilang pemboleh ubah, menilai pekali dan reja, memperbaik model dengan penjelmaan data dan menilai sebuah hartanah.

## Apa yang dilakukan kod

- `load_data` membaca `boston.csv`; lajur pertama mengandungi nombor baris, jadi ia menjadi indeks.
- `table_shape`, `column_names`, `has_nan_values` dan `has_duplicates` menjawab soalan awal: 506 baris dan 14 lajur (13 ciri dan sasaran `PRICE`), tiada nilai `NaN` dan tiada pendua.
- `average_students_per_teacher` memberi kira-kira 18.46 pelajar bagi setiap guru (`PTRATIO`), dan `average_price` kira-kira 22.53, iaitu kira-kira $22,533, kerana `PRICE` dalam ribuan dolar.
- `river_value_range` menunjukkan bahawa `CHAS` hanya mengandungi 0 dan 1: ia pemboleh ubah dummy yang bernilai 1 apabila kawasan bersempadan dengan Sungai Charles. `river_counts` menunjukkan 471 rumah jauh dari sungai dan 35 bersebelahan sungai.
- `room_range` memberi bilangan bilik terkecil dan terbesar bagi setiap kediaman: kira-kira 3.56 dan 8.78.
- `descriptive_table_figure` melukis jadual statistik deskriptif dalam gambar di atas.

## Apa yang anda perolehi

- `.shape`, `.head()`, `.tail()`, `.info()`, `.isna()` dan `.duplicated()` memberi gambaran pertama tentang mana-mana DataFrame sebelum anda membina model.
- `.describe()` menunjukkan kiraan, purata, serakan dan kuartil setiap lajur sekali gus; nilai minimum dan maksimum sudah memberitahu apa itu pemboleh ubah dummy.
- Model memerlukan data yang bersih dan sasaran yang jelas: di sini sasarannya `PRICE` dan yang lain ialah ciri.

Sebelumnya: [Getting-Started-ms](Getting-Started-ms)
