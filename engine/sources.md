# Sumber, Hierarki Rujukan, dan Riset Internet

> **File Pemilik Tunggal:** File ini mengatur **Hierarki Rujukan (Repo sebagai Rujukan Utama vs Internet sebagai Tambahan), Protokol Riset Berkelanjutan Anti-Halusinasi & Anti-AI Slop, serta Katalog Referensi Novel Teruji**.

---

## 1. Hierarki Rujukan Mutlak (Prinsip Repo-First)

AI **WAJIB menjadikan repositori ini sebagai rujukan utama dan pertama** sebelum mengandalkan opini bawaan model atau mencari teori dari internet. Seluruh teori penulisan premis, 8 kerangka plot, rumus ABCD, penutupan jalan mudah, psikologi karakter, gaya bahasa (`acuan-bahasa.docx`), dan kontinuitas sudah lengkap di dalam `engine/`.

### Urutan Prioritas Rujukan:
1. **Instruksi langsung pengguna** pada sesi berjalan.
2. **Dokumen cerita aktif (`canon.md`, `outline.md`, `state.md`, `ledger.md`)** untuk fakta cerita.
3. **`acuan-bahasa.docx` dan `engine/05-style.md`** untuk gaya bahasa, diksi, nada bercerita (acuan utama: *Resign!* karya Almira Bastari), dan eliminasi AI slop.
4. **Panduan `engine/00-workflow.md` s.d. `11-worldbuilding.md`** untuk seluruh teori premis, kerangka plot, karakter, bab, kontinuitas, dan kualitas.
5. **Pencarian Internet (Hanya sebagai Tambahan Spesifik — Lihat Bagian 2).**

> **LARANGAN KERAS:** AI dilarang mengabaikan aturan di `engine/` dan menggantinya dengan opini atau kebiasaan generik AI sendiri.

---

## 2. Kapan dan Untuk Apa Mencari di Internet

Pencarian internet **BUKAN** untuk mencari teori plot dasar (karena sudah ada di `engine/02-premise.md` dan `03-structure.md`), melainkan hanya untuk **dua fungsi berikut**:

### A. Info Faktual Dunia Nyata & Kosakata Terbaru (Pelengkap Cerita)
Gunakan pencarian web saat membutuhkan fakta yang belum tercatat di repo:
- Prosedur administrasi atau cara kerja lembaga/layanan publik di Indonesia (misal: syarat mengurus BPKB/sertifikat hilang, aturan klaim ekspedisi, SOP HRD/pengadaan kantor) untuk menutup label `"perlu dicek"`;
- Kisaran harga barang, biaya sewa, atau tarif layanan terkini di Jakarta/kota Indonesia;
- Rute jalan, jarak tempuh, dan detail lokasi geografis nyata;
- Kosakata gaul, istilah dunia kerja, atau tren media sosial terbaru di Indonesia.

### B. Riset Berkelanjutan Anti-Halusinasi & Anti-AI Slop (Wajib Terus Diperbarui)
Karena pola tulisan AI (*AI slop*) dan celah halusinasi model bahasa terus berkembang, AI dan pengguna secara berkala mencari referensi terbaru di internet/riset akademik mengenai:
1. **Cara mendeteksi dan menghilangkan *AI slop* (baik di level kalimat/diksi maupun di level perilaku tokoh/plot):**
   - Kata, frasa klise, atau struktur kalimat yang paling sering diulang LLM terbaru;
   - Pola dialog atau monolog batin yang terasa buatan mesin vs tulisan penulis manusia;
   - Teknik terbaru membuat prosa bahasa Indonesia terasa alami, lisan, dan hidup.
2. **Cara mencegah halusinasi & amnesia kontinuitas AI dalam penulisan fiksi panjang:**
   - Metode *state tracking*, pelacakan objek fisik (*object permanence*), asimetri pengetahuan tokoh, dan pemeriksaan silang (*linting*) deterministik.

Setiap kali ditemukan pola *AI slop* baru atau teknik anti-halusinasi baru dari riset internet, **tambahkan temuannya ke `engine/05-style.md` (untuk gaya/kalimat), `engine/02-premise.md` / `08-quality.md` (untuk logika plot), dan `scripts/analyze-prose.py` (untuk deteksi otomatis)**.

---

## 3. Jika Pengguna Memberi PDF / Teks / URL Referensi Baru

1. Baca dan ekstrak isinya.
2. Ringkas 5-10 poin prinsip yang berguna dan bisa diuji.
3. Jangan menyalin kalimat atau adegan berhak cipta ke dalam novel.
4. Tanyakan apakah temuan tersebut mau dilebur ke file pemilik di `engine/` atau hanya dijadikan referensi proyek.

---

## 4. Katalog Referensi Novel Teruji (Inspirasi Pola & Gaya)

Judul-judul berikut dikelompokkan dengan pola yang sama seperti 16 studi kasus di `engine/03-structure.md`:

- **Tenggat, taruhan, komunitas:** *Around the World in Eighty Days* (Jules Verne); *A Christmas Carol* (Charles Dickens); *Laskar Pelangi*, *Sang Pemimpi*, *Orang-Orang Biasa* (Andrea Hirata); *Charlotte's Web* (E. B. White); *The Guernsey Literary and Potato Peel Pie Society* (Mary Ann Shaffer & Annie Barrows); *Little Women* (Louisa May Alcott); *Anne of Green Gables* (L. M. Montgomery); *Negeri 5 Menara* (A. Fuadi); *5 cm* (Donny Dhirgantoro).
- **Salah paham dan rahasia:** *Pride and Prejudice*, *Emma*, *Persuasion*, *Sense and Sensibility*, *Northanger Abbey* (Jane Austen); *Jane Eyre* (Charlotte Brontë); *Rebecca* (Daphne du Maurier); *Where'd You Go, Bernadette* (Maria Semple); *Salah Asuhan* (Abdoel Moeis); *Tenggelamnya Kapal Van der Wijck* (Hamka).
- **Perubahan diri dan kehidupan urban:** *Resign!* (Almira Bastari - di `acuan-bahasa.docx`); *Great Expectations*, *David Copperfield* (Charles Dickens); *The Devil Wears Prada* (Lauren Weisberger); *The Rosie Project* (Graeme Simsion); *Eleanor Oliphant Is Completely Fine* (Gail Honeyman); *The Secret Garden* (Frances Hodgson Burnett); *Pollyanna* (Eleanor H. Porter); *Confessions of a Shopaholic* (Sophie Kinsella); *The Alchemist* (Paulo Coelho); *Convenience Store Woman* (Sayaka Murata); *Kitchen* (Banana Yoshimoto); *A Man Called Ove* (Fredrik Backman); *The Midnight Library* (Matt Haig); *The Unlikely Pilgrimage of Harold Fry* (Rachel Joyce); *Hector and the Search for Happiness* (François Lelord); *Imperfect: Karier, Cinta & Timbangan* (Meira Anastasia).
- **Rantai peristiwa dan komedi:** *The Hundred-Year-Old Man Who Climbed Out the Window and Disappeared* (Jonas Jonasson); *Three Men in a Boat* (Jerome K. Jerome); *The Hitchhiker's Guide to the Galaxy* (Douglas Adams); *Good Omens* (Terry Pratchett & Neil Gaiman); *A Series of Unfortunate Events* (Lemony Snicket); *The Princess Bride* (William Goldman); *Bridget Jones: The Edge of Reason* (Helen Fielding); *Marmut Merah Jambu* (Raditya Dika).
- **Misteri dan planting:** *Harry Potter and the Philosopher's Stone*, *The Prisoner of Azkaban* (J. K. Rowling); *The Curious Incident of the Dog in the Night-Time* (Mark Haddon); *Holes* (Louis Sachar); *And Then There Were None*, *The Murder of Roger Ackroyd* (Agatha Christie); *The Hound of the Baskervilles* (Arthur Conan Doyle); *The Westing Game* (Ellen Raskin); *Where the Crawdads Sing* (Delia Owens); *The Thursday Murder Club* (Richard Osman); *Big Little Lies* (Liane Moriarty); *Gadis Kretek* (Ratih Kumala); *Aroma Karsa* (Dee Lestari).
- **Romance modern:** *Critical Eleven*, *Divortiare*, *A Very Yuppy Wedding*, *Antologi Rasa*, *The Architecture of Love* (Ika Natassa); *Perahu Kertas* (Dee Lestari); *Bridget Jones's Diary* (Helen Fielding); *Crazy Rich Asians* (Kevin Kwan); *Me Before You* (Jojo Moyes); *One Day* (David Nicholls); *The Hating Game* (Sally Thorne); *Love, Rosie*, *P.S. I Love You* (Cecelia Ahern); *Normal People* (Sally Rooney); *The Kiss Quotient* (Helen Hoang); *Beach Read* (Emily Henry); *Refrain* (Winna Efendi); *Dilan: Dia Adalah Dilanku Tahun 1990* (Pidi Baiq); *Ayat-Ayat Cinta* (Habiburrahman El Shirazy).
- **Bentuk naratif khusus (surat, diari, dua garis waktu):** *Daddy-Long-Legs* (Jean Webster); *The Perks of Being a Wallflower* (Stephen Chbosky); *Flowers for Algernon* (Daniel Keyes); *The Time Traveler's Wife* (Audrey Niffenegger).
