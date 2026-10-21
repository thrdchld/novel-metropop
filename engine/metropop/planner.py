"""Story planner: turns data banks into a coherent, reproducible blueprint."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from . import data
from .rng import Rng
from .text import folder_name, slugify, truncate

MIN_CHAPTERS = 30
MAX_CHAPTERS = 40

PHASE_LABELS = {
    "setup": "Babak 1 — Setup",
    "escalation": "Babak 2A — Eskalasi",
    "midpoint": "Titik Tengah",
    "fallout": "Babak 2B — Kejatuhan",
    "act3": "Babak 3 — Resolusi",
}

PHASE_ORDER = ["setup", "escalation", "midpoint", "fallout", "act3"]

LOGLINES = {
    "salah-kirim": (
        "{protagonis}, {protagonist_job} di {company}, tanpa sengaja mengirim "
        "{draft_kind} soal {problem} ke {audience}. Alih-alih "
        "dipecat, ia dianggap {misread} dan dipaksa memimpin {movement}—selagi "
        "menyembunyikan bahwa semuanya kecelakaan."
    ),
    "pura-pura-pacar": (
        "{protagonis} dan {love} sepakat berpura-pura pacaran untuk {event}. "
        "Kesepakatan itu berjalan rapi, sampai batas waktu yang seharusnya singkat "
        "mulai terasa terlalu nyata."
    ),
    "proyek-bersama": (
        "{protagonis}, {protagonist_job} di {company}, dipaksa bekerja dengan "
        "{love}, {love_job} dari {klien}, untuk {project}. Masalahnya, mereka "
        "punya sejarah: {conflict_history}."
    ),
    "identitas-salah": (
        "Di hari pertama di {company}, {protagonis} disangka {wrong_identity}. "
        "Ia tidak membetulkannya, dan setiap hari kebohongan itu memberinya "
        "{benefit}—sampai orang yang sebenarnya muncul."
    ),
    "warisan": (
        "{protagonis} mewarisi {inheritance} dari {benefactor}, dengan syarat "
        "{condition}. {love} punya rencana lain untuk tempat itu, dan "
        "{protagonis} harus memilih antara menyelamatkan warisan atau dirinya sendiri."
    ),
    "viral": (
        "{protagonis}, {protagonist_job} di {company}, menjadi viral karena "
        "{viral_trigger}. Ia menikmati {benefit} sampai {backlash} membongkar "
        "bahwa {secret}."
    ),
}

DRAMATIC_QUESTIONS = {
    "salah-kirim": (
        "Apakah {protagonis} akan mengaku bahwa semuanya kecelakaan sebelum "
        "orang-orang yang mulai percaya padanya tahu sendiri?"
    ),
    "pura-pura-pacar": (
        "Apakah {protagonis} dan {love} berani mengakhiri sandiwara sebelum "
        "salah satu dari mereka benar-benar terluka?"
    ),
    "proyek-bersama": (
        "Apakah {protagonis} bisa menyelamatkan proyek dan kepercayaan {love} "
        "tanpa mengorbankan salah satunya?"
    ),
    "identitas-salah": (
        "Apakah {protagonis} akan berhenti memakai nama orang lain sebelum "
        "kebohongan itu menghancurkan orang yang ia sayangi?"
    ),
    "warisan": (
        "Apakah {protagonis} mampu menjaga {inheritance} tanpa kehilangan "
        "dirinya sendiri?"
    ),
    "viral": (
        "Apakah {protagonis} bisa mengambil kembali hidupnya setelah seluruh "
        "dunia merasa berhak menilainya?"
    ),
}

EXTRA_COMPLICATIONS = [
    "Seseorang yang seharusnya diam justru berbicara di tempat yang salah.",
    "Keputusan kecil dari minggu lalu kembali menagih sekarang.",
    "Uang yang dijanjikan tidak pernah datang.",
    "Sebuah janji lama harus ditepati di waktu yang paling buruk.",
    "Orang tua {protagonis} datang tanpa memberi kabar.",
    "Rekaman percakapan diputar di depan orang yang tidak seharusnya mendengarnya.",
    "Salah satu sekutu menerima tawaran dari pihak lain.",
    "Dokumen penting tertinggal di tempat yang tidak aman.",
    "Jadwal yang sudah disepakati diubah tanpa memberi tahu {protagonis}.",
    "Seseorang memakai nama {protagonis} untuk kepentingannya sendiri.",
    "Kabar baik datang, tapi harganya terlalu mahal.",
    "Sebuah kebetulan membuat dua orang yang seharusnya tidak bertemu akhirnya bertemu.",
]

EXTRA_TURNS = [
    "Yang selama ini terlihat seperti kebetulan ternyata disusun dengan rapi.",
    "Seseorang memilih diam, dan diamnya lebih berbahaya dari tuduhan.",
    "Bantuan datang dengan syarat yang tidak bisa ditolak.",
    "Kemenangan kecil justru mempercepat masalah besar.",
    "Kesalahan yang sama terulang, tapi kali ini ada saksi.",
    "Rencana yang paling aman ternyata yang paling merugikan.",
    "Untuk pertama kalinya, {protagonis} melihat ketakutan di mata {antagonis}.",
    "Seseorang yang selama ini dianggap lemah ternyata menyimpan bukti.",
    "Pilihan yang benar tetap terasa seperti pengkhianatan.",
    "Semua orang setuju, dan justru itu yang membuat {protagonis} curiga.",
]

CHANGE_BANK = {
    "setup": "Taruhan naik: makin banyak orang percaya pada versi yang salah, dan protagonis makin sulit mundur.",
    "escalation": "Tekanan bertambah: satu orang mulai curiga, dan hubungan pribadi mulai mengganggu keputusan.",
    "midpoint": "Tujuan protagonis berubah: dari bertahan menjadi melawan.",
    "fallout": "Sekutu retak dan pilihan menyempit; protagonis kehilangan jalan aman.",
    "act3": "Keputusan diambil, dan konsekuensinya tidak bisa ditarik.",
}

GOAL_BANK = {
    "Pemicu": "Menunjukkan kesalahan atau kesepakatan yang tidak bisa ditarik, beserta akibat awalnya.",
    "Reaksi": "Menunjukkan konsekuensi pertama dan aturan main yang membuat protagonis terjebak.",
    "Sekutu pertama": "Memperkenalkan bantuan yang punya syarat dan taruhan sendiri.",
    "Tekanan antagonis": "Membuat antagonis mengubah situasi menjadi keuntungan.",
    "Kemenangan palsu": "Memberi harapan yang justru memperbesar risiko.",
    "Komitmen": "Membuat protagonis menerima peran atau risiko yang tidak ia minta.",
    "Hambatan": "Menutup jalan keluar paling mudah.",
    "Rahasia menekan": "Membuat kebohongan makin mahal untuk dipertahankan.",
    "Konsekuensi": "Menunjukkan biaya pertama dari pilihan protagonis.",
    "Kedekatan": "Mendekatkan protagonis dan love interest dengan konsekuensi profesional.",
    "Serangan balik": "Membuat antagonis bergerak memakai aturan, bukan kekerasan.",
    "Adegan besar": "Menaikkan taruhan di depan publik.",
    "Peringatan": "Membuat sekutu meragukan protagonis.",
    "Titik tengah": "Mengubah pemahaman protagonis dan arah tujuannya.",
    "Retak": "Membuat sekutu merasa dibohongi.",
    "Pengkhianatan": "Memindahkan dukungan atau membocorkan rahasia.",
    "Bukti": "Memberi bukti dengan harga mahal.",
    "Titik terendah": "Menutup semua jalan aman.",
    "Keputusan": "Membuat protagonis memilih melawan.",
    "Persiapan": "Menyusun rencana dengan informasi yang belum lengkap.",
    "Rencana": "Menetapkan langkah konkret menuju konfrontasi.",
    "Konfrontasi": "Membenturkan rencana dengan kenyataan.",
    "Semua hilang": "Membuat satu elemen rencana gagal.",
    "Pengakuan": "Membuat protagonis mengatakan kebenaran tentang dirinya.",
    "Klimaks": "Membuka konfrontasi publik dan pembalikan fakta.",
    "Resolusi": "Menunjukkan konsekuensi nyata, tidak semua baik.",
    "Citra akhir": "Menunjukkan perubahan lewat pilihan kecil.",
    "Eskalasi awal": "Memperbesar masalah tanpa memberi jalan keluar.",
    "Kehidupan pribadi": "Menunjukkan taruhan personal yang membuat protagonis tidak bisa berhenti.",
    "Tekanan kecil": "Menambah satu komplikasi yang membuat situasi lebih sempit.",
    "Petunjuk": "Menanam detail yang akan dipakai kemudian.",
    "Kedekatan": "Mendekatkan dua tokoh dengan konsekuensi yang tidak mereka rencanakan.",
    "Konsekuensi baru": "Menagih pilihan dari bab-bab sebelumnya.",
    "Adegan besar": "Membawa konflik ke ruang publik.",
    "Persiapan akhir": "Menyiapkan konfrontasi dengan risiko yang jelas.",
    "Akselerasi": "Mempercepat menuju klimaks.",
}

READER_QUESTIONS = {
    "setup": "Apakah protagonis akan membetulkan kesalahannya sebelum makin banyak orang percaya?",
    "escalation": "Siapa yang akan tahu lebih dulu, dan apa yang ia lakukan dengan informasi itu?",
    "midpoint": "Apakah tujuan protagonis berubah setelah bukti ini?",
    "fallout": "Apakah protagonis masih punya sekutu yang bisa dipercaya?",
    "act3": "Apakah protagonis akan mengaku, dan apa harganya?",
}

NOT_HAPPENING = {
    "setup": "Tidak ada tokoh baru; belum ada pengakuan; rahasia utama belum terbuka; antagonis belum menyerang terbuka.",
    "escalation": "Tidak ada tokoh baru; belum ada bukti yang dibuka ke publik; hubungan romansa belum resmi.",
    "midpoint": "Tidak ada tokoh baru; belum ada keputusan final; antagonis belum tahu protagonis punya bukti.",
    "fallout": "Tidak ada tokoh baru; belum ada klimaks; belum ada pengakuan di depan publik.",
    "act3": "Tidak ada tokoh baru; tidak ada penyelesaian ajaib; tidak semua masalah selesai.",
}

TECHNIQUE_BANK = {
    "setup": ["dramatic irony", "foreshadowing", "action beats", "show, don't tell", "motif"],
    "escalation": ["dramatic irony", "pacing", "motif", "action beats", "foreshadowing"],
    "midpoint": ["plot twist", "dramatic irony", "reveal"],
    "fallout": ["flashback", "stream of consciousness", "red herring", "show, don't tell"],
    "act3": ["payoff", "motif", "climax", "cliffhanger", "dramatic irony"],
}

HOOK_TYPE_WORDS = [
    ("Pesan", ("pesan", "notifikasi", "telepon", "chat", "surat", "email")),
    ("Kedatangan", ("pintu", "masuk", "datang", "muncul", "tiba")),
    ("Pengungkapan", ("ternyata", "menemukan", "tahu", "bukti", "nama", "layar", "konfirmasi", "terkirim", "tombol", "mewarisi")),
    ("Keputusan", ("memilih", "menekan", "setuju", "memutuskan", "berdiri")),
    ("Ancaman", ("jangan", "tidak akan", "habis", "ancam")),
    ("Objek", ("amplop", "berkas", "dokumen", "kotak", "map")),
]

MOTIVES = {
    "protagonis": "membuktikan bahwa ia bisa aman tanpa harus menyenangkan semua orang",
    "love": "menjaga hidupnya tetap terpisah dari pekerjaan",
    "antagonis": "mempertahankan posisi dan citra yang ia bangun bertahun-tahun",
    "sekutu": "melindungi pekerjaan dan orang-orang yang bergantung padanya",
    "mentor": "mewariskan cara kerja yang lebih baik sebelum ia pergi",
    "keluarga": "memastikan anaknya tidak mengulangi kesulitan yang ia alami",
}

EMOTIONAL_BEATS = [
    "Momen tulus: protagonis mengakui satu hal kecil yang selama ini ia tahan.",
    "Momen tulus: seseorang menolong tanpa meminta imbalan.",
    "Momen tulus: protagonis dan love interest bicara tanpa kepentingan pekerjaan.",
    "Momen tulus: keluarga menunjukkan kasih dengan cara yang tidak sempurna.",
    "Momen tulus: sekutu memilih tetap tinggal meski tahu risikonya.",
    "Momen tulus: antagonis menunjukkan satu keretakan yang membuatnya manusiawi.",
]

FILLER_FUNCTIONS = {
    "setup": ["Eskalasi awal", "Kehidupan pribadi", "Tekanan kecil", "Petunjuk"],
    "escalation": ["Konsekuensi baru", "Kedekatan", "Tekanan", "Adegan besar", "Peringatan"],
    "fallout": ["Retak", "Bukti", "Pengkhianatan", "Keputusan", "Konsekuensi"],
    "act3": ["Persiapan akhir", "Tekanan", "Akselerasi"],
}

CONFESSION_EVENTS = [
    "{protagonis} berdiri dan mengatakan hal yang sebenarnya, tanpa menyiapkan kalimat penutup.",
    "{protagonis} mengaku kepada {sekutu} lebih dulu, lalu kepada semua orang.",
    "{protagonis} menyerahkan bukti sambil mengakui bagiannya sendiri.",
    "{protagonis} berhenti membela diri dan membiarkan ruangan menilai apa yang ia lakukan.",
]

SPECIAL_HOOKS = {
    "Pembuka": [
        "Hari itu dimulai seperti biasa, dan justru itu masalahnya.",
        "Belum ada yang tahu bahwa minggu ini akan berakhir berbeda.",
        "Rutinitas berjalan rapi, seperti sesuatu yang tinggal menunggu retak.",
        "Ia sudah hafal setiap sudut tempatnya bekerja, termasuk sudut tempat ia bersembunyi.",
    ],
    "Pemicu": [
        "Kata 'ya' keluar sebelum ia sempat menghitung risikonya.",
        "Malam itu, keputusan kecil berubah menjadi sesuatu yang tidak bisa dibatalkan.",
        "Tidak ada tombol undo untuk apa yang baru saja ia setujui.",
        "Ia keluar dari percakapan itu dengan satu kesepakatan yang tidak bisa ditarik.",
    ],
    "Komitmen": [
        "Ia mengangguk, dan kata 'siap' keluar sebelum otaknya sempat protes.",
        "Pengumuman itu muncul di grup kantor sebelum ia sempat meninggalkan ruangan.",
        "Ia sudah bilang ya. Dan semua orang mendengarnya.",
        "Pintu ditutup, tetapi perannya sudah diumumkan ke seluruh lantai.",
    ],
    "Titik tengah": [
        "Semua potongan cerita menyatu, dan jawabannya jauh lebih buruk dari yang ia bayangkan.",
        "Ia menemukan namanya di dokumen yang seharusnya tidak boleh ia lihat.",
        "Orang yang selama ini ia percaya ternyata ada di ruangan itu sejak awal.",
        "Layar menunjukkan bukti yang tidak bisa dibantah lagi.",
    ],
    "Semua hilang": [
        "Sekutu yang paling setia berdiri, lalu pergi tanpa menoleh.",
        "Semua orang sudah tahu, dan tidak ada yang mau duduk di sebelahnya.",
        "Pintu ruang rapat terbuka. Ia masuk sendirian.",
        "Telepon dari Mama. Kali ini ia mengangkat.",
    ],
    "Klimaks": [
        "Ia berdiri, dan untuk pertama kalinya tidak meminta maaf.",
        "Suaranya memenuhi ruangan. Tidak ada yang bertepuk tangan.",
        "Tangannya gemetar, tetapi jarinya tetap menekan tombol itu.",
        "Tidak ada jalan kembali setelah kalimat itu keluar.",
    ],
    "Resolusi": [
        "Tidak semua orang memaafkannya. Tetapi cukup banyak yang bertahan.",
        "Untuk pertama kalinya, ia pulang tanpa membawa pekerjaan.",
        "Ia menandatangani dokumen itu, lalu meletakkan pena dengan tenang.",
        "Ia mengembalikan kartu akses, dan tidak ada yang mencoba menahannya.",
    ],
    "Citra akhir": [
        "Di luar jendela, Jakarta masih berjalan seperti tidak terjadi apa-apa.",
        "Ia menutup pintu, tetapi kali ini bukan untuk bersembunyi.",
        "Ia meletakkan ponselnya menghadap ke bawah, lalu kembali ke meja.",
        "Untuk pertama kalinya, ia tidak menunggu izin untuk pulang.",
    ],
}

EARLY_COMPLICATIONS = [
    "Pekerjaan yang seharusnya selesai hari ini bertambah satu lagi.",
    "Atasan mengubah prioritas tanpa bertanya.",
    "Rapat yang dijadwalkan lima belas menit berjalan hampir satu jam.",
    "Ia harus memilih antara pulang tepat waktu atau menyelesaikan laporan.",
    "Ponselnya penuh pesan yang tidak sempat ia balas.",
    "Seseorang meminta tolong dengan cara yang sulit ditolak.",
    "Kopi terakhir di pantry sudah habis.",
    "Ia lupa membalas pesan keluarga sejak pagi.",
    "Jadwal yang sudah disusun rapi diubah di menit terakhir.",
    "Ia diminta mewakili tim di rapat yang tidak ia pahami.",
]

ACCIDENT_COMPLICATIONS = [
    "Tidak ada tombol undo yang cukup cepat.",
    "Terlalu banyak orang yang sudah tahu.",
    "Keputusan itu tidak bisa ditarik tanpa kehilangan sesuatu.",
    "Ia tidak punya jalan mundur yang rapi.",
]

EARLY_TURNS = [
    "Ia menyadari bahwa masalahnya tidak akan selesai hanya dengan pulang.",
    "Ia menghitung berapa lama ia bisa bertahan tanpa pekerjaan ini.",
    "Seseorang menawarkan bantuan, dan ia tidak tahu apakah itu tulus.",
    "Ia membaca ulang pesannya dan menemukan satu kalimat yang terlalu jujur.",
    "Dunia luar tetap berjalan seperti biasa, dan itu terasa lebih menakutkan.",
    "Ia menyadari tidak ada satu orang pun yang bisa ia hubungi malam ini.",
    "Rencana sederhananya berubah sebelum sempat dimulai.",
    "Ia melihat reaksi orang lain, dan reaksinya tidak seperti yang ia bayangkan.",
    "Sebuah detail kecil membuatnya curiga bahwa ini bukan kebetulan.",
    "Ia menyimpan satu informasi untuk dirinya sendiri, dan langsung menyesalinya.",
]


def setup_function(raw: str) -> str:
    lower = raw.lower()
    if "berbohong" in lower or "kebohongan" in lower:
        return "Rahasia menekan"
    if "{sekutu}" in raw:
        return "Sekutu pertama"
    if " IT" in raw or "menarik" in lower or "persetujuan" in lower:
        return "Hambatan"
    if "{antagonis}" in raw:
        return "Tekanan antagonis"
    if any(word in lower for word in ("pujian", "berhasil", "diterima", "forum")):
        return "Kemenangan palsu"
    return "Reaksi"

TIME_HINTS = [
    ("jumat", "Jumat malam"),
    ("sabtu pagi", "Sabtu pagi"),
    ("lembur", "malam"),
    ("malam", "malam"),
    ("pagi", "pagi"),
    ("siang", "siang"),
    ("sore", "sore"),
    ("akhir pekan", "akhir pekan"),
]

PLACE_HINTS = [
    ("ruang rapat", "ruang rapat"),
    ("forum", "aula serbaguna"),
    ("presentasi", "ruang rapat"),
    ("rapat", "ruang rapat"),
    ("pantry", "pantry"),
    ("lift", "lift"),
    ("parkir", "tempat parkir basement"),
    ("halte", "halte dekat kantor"),
    ("kafe", "kafe dekat kantor"),
    ("kesepakatan", "kafe dekat kantor"),
    ("reuni", "aula serbaguna"),
    ("restoran", "restoran klien"),
    ("dinner", "restoran klien"),
    ("notaris", "kantor notaris"),
    ("kontrakan", "rumah kontrakan"),
    ("rumah", "rumah Mama"),
    ("kamar", "kamar kos {protagonis}"),
    ("kos", "kamar kos {protagonis}"),
    ("menulis", "meja kerja {protagonis}"),
    ("membaca", "meja kerja {protagonis}"),
    ("meja kerja", "meja kerja {protagonis}"),
    ("redaksi", "kantor {company}"),
    ("email", "kantor {company}"),
    ("terkirim", "kantor {company}"),
    ("pesan", "kantor {company}"),
    ("lobi", "lobi"),
    ("acara", "aula serbaguna"),
    ("undangan", "rumah Mama"),
    ("kantor", "kantor {company}"),
]


def infer_time(scene: str, fallback: str) -> str:
    lower = scene.lower()
    if "jumat" in lower and ("malam" in lower or "lembur" in lower):
        return "Jumat malam"
    for keyword, value in TIME_HINTS:
        if keyword in lower:
            return value
    return fallback


def infer_place(scene: str, context: dict[str, Any]) -> str | None:
    lower = scene.lower()
    for keyword, template in PLACE_HINTS:
        if keyword in lower:
            return fill(template, context)
    return None


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def fill(template: str, context: dict[str, Any]) -> str:
    return template.format_map(_SafeDict(context))


def _name(rng: Rng, gender: str, used_first: set[str], used_surnames: set[str]) -> tuple[str, str]:
    first_pool = data.FEMALE_NAMES if gender == "female" else data.MALE_NAMES
    for _ in range(300):
        first = rng.pick(first_pool)
        surname = rng.pick(data.SURNAMES)
        if first not in used_first and surname not in used_surnames:
            used_first.add(first)
            used_surnames.add(surname)
            return first, f"{first} {surname}"
    first = rng.pick(first_pool)
    return first, f"{first} {rng.pick(data.SURNAMES)}"


def _phase_counts(total: int) -> tuple[int, int, int, int, int]:
    if not MIN_CHAPTERS <= total <= MAX_CHAPTERS:
        raise ValueError(f"MetroPop harus 30–40 bab, bukan {total}.")
    setup = max(7, round(total * 0.25))
    escalation = max(6, round(total * 0.23))
    midpoint = 1
    fallout = max(6, round(total * 0.22))
    act3 = total - setup - escalation - midpoint - fallout
    while act3 < 7:
        if setup > 8:
            setup -= 1
        elif fallout > 7:
            fallout -= 1
        elif escalation > 7:
            escalation -= 1
        else:
            break
        act3 += 1
    if act3 < 7:
        raise ValueError("Jumlah bab terlalu kecil untuk struktur tiga babak.")
    return setup, escalation, midpoint, fallout, act3


def _extras(rng: Rng, engine: dict[str, Any]) -> dict[str, str]:
    key = engine["key"]
    if key == "salah-kirim":
        return {
            "draft_kind": rng.pick(engine["draft_kind"]),
            "audience": rng.pick(engine["audience"]),
            "problem": rng.pick(engine["problem"]),
            "misread": rng.pick(engine["misread"]),
            "movement": rng.pick(engine["movement"]),
        }
    if key == "pura-pura-pacar":
        return {
            "plus_one_reason": rng.pick(engine["plus_one_reason"]),
            "love_reason": rng.pick(engine["love_reason"]),
            "event": rng.pick(engine["event"]),
            "duration": rng.pick(engine["duration"]),
        }
    if key == "proyek-bersama":
        return {"conflict_history": rng.pick(engine["conflict_history"])}
    if key == "identitas-salah":
        return {
            "wrong_identity": rng.pick(engine["wrong_identity"]),
            "benefit": rng.pick(engine["benefit"]),
        }
    if key == "warisan":
        return {
            "inheritance": rng.pick(engine["inheritance"]),
            "benefactor": rng.pick(engine["benefactor"]),
            "condition": rng.pick(engine["condition"]),
            "task": rng.pick(engine["task"]),
            "conflict_with_love": rng.pick(engine["conflict_with_love"]),
        }
    if key == "viral":
        return {
            "viral_trigger": rng.pick(engine["viral_trigger"]),
            "benefit": rng.pick(engine["benefit"]),
            "backlash": rng.pick(engine["backlash"]),
        }
    return {}


def _cast(rng: Rng, engine: dict[str, Any], world: dict[str, Any]) -> dict[str, dict[str, Any]]:
    used: set[str] = set()
    used_surnames: set[str] = set()

    protagonist_first, protagonist_full = _name(rng, "female", used, used_surnames)
    love_first, love_full = _name(rng, "male", used, used_surnames)
    antagonist_gender = "female" if rng.chance(0.35) else "male"
    antagonist_first, antagonist_full = _name(rng, antagonist_gender, used, used_surnames)
    ally_gender = "female" if rng.chance(0.55) else "male"
    ally_first, ally_full = _name(rng, ally_gender, used, used_surnames)
    mentor_gender = "female" if rng.chance(0.45) else "male"
    mentor_first, mentor_full = _name(rng, mentor_gender, used, used_surnames)

    antagonist_title = "Bu" if antagonist_gender == "female" else "Pak"
    mentor_title = "Bu" if mentor_gender == "female" else "Pak"
    family_name = f"Ibu {rng.pick(data.FAMILY_NAMES)}"

    want = rng.pick(data.WANTS)
    need = rng.pick(data.NEEDS)
    flaw = rng.pick(data.FLAWS)
    tactic = rng.pick(data.ANTAGONIST_TACTICS)
    stake = rng.pick(data.ALLY_STAKES)
    charm = rng.pick(data.LOVE_CHARMS)
    ally_job = rng.pick(["staf finance", "analis data", "staf legal", "admin HR", "tim operasional", "staf customer support", "desainer"])
    mentor_job = rng.pick(data.MENTOR_ROLES)

    def sheet(role_key: str, call: str) -> dict[str, Any]:
        return {
            "appearance": rng.sample(data.APPEARANCES, rng.integer(2, 3)),
            "tells": rng.sample(data.TELLS, 4),
            "signature_object": rng.pick(data.SIGNATURE_OBJECTS),
            "emotional_tell": rng.pick(data.EMOTIONAL_TELLS),
            "lie": rng.pick(data.LIES),
            "never_do": rng.pick(data.NEVER_DO),
            "motive": MOTIVES[role_key],
            "address": data.ADDRESS_STYLES[role_key],
            "dialogue_sample": [
                fill(sample, {"call": call})
                for sample in data.DIALOGUE_SAMPLES[role_key]
            ],
        }

    cast = {
        "protagonis": {
            "name": protagonist_full,
            "call": protagonist_first,
            "role": "Protagonis",
            "age": rng.integer(24, 30),
            "job": world["job"],
            "want": want,
            "need": need,
            "flaw": flaw,
            "wound": rng.pick(data.WOUNDS),
            "arc": "belajar memilih dengan sadar, bukan karena terpaksa",
            "voice": data.VOICES["protagonis"],
            "family_pressure": rng.pick(data.FAMILY_PRESSURES),
            "function": f"ingin {want}; butuh {need}",
            **sheet("protagonis", protagonist_first),
        },
        "love": {
            "name": love_full,
            "call": love_first,
            "role": "Love interest",
            "age": rng.integer(26, 36),
            "job": "",
            "charm": charm,
            "boundary": rng.pick(data.LOVE_BOUNDARIES),
            "secret": rng.pick(data.LOVE_SECRETS),
            "arc": "belajar membuka batas tanpa kehilangan prinsip",
            "voice": data.VOICES["love"],
            "function": f"membuat {protagonist_first} memilih antara aman dan jujur",
            **sheet("love", love_first),
        },
        "antagonis": {
            "name": antagonist_full,
            "call": f"{antagonist_title} {antagonist_first}",
            "role": "Antagonis",
            "age": rng.integer(38, 55),
            "job": "",
            "tactic": tactic,
            "vulnerability": rng.pick(data.ANTAGONIST_VULNERABILITIES),
            "rationale": rng.pick(data.ANTAGONIST_RATIONALES),
            "voice": data.VOICES["antagonis"],
            "function": f"menekan lewat: {tactic}",
            **sheet("antagonis", f"{antagonist_title} {antagonist_first}"),
        },
        "sekutu": {
            "name": ally_full,
            "call": ally_first,
            "role": "Sekutu",
            "age": rng.integer(23, 40),
            "job": ally_job,
            "stake": stake,
            "condition": rng.pick(data.ALLY_CONDITIONS),
            "voice": data.VOICES["sekutu"],
            "function": f"taruhan: {stake}",
            **sheet("sekutu", ally_first),
        },
        "mentor": {
            "name": mentor_full,
            "call": f"{mentor_title} {mentor_first}",
            "role": "Mentor",
            "age": rng.integer(45, 65),
            "job": mentor_job,
            "voice": data.VOICES["mentor"],
            "function": "memberi perspektif tanpa mengambil alih keputusan",
            **sheet("mentor", f"{mentor_title} {mentor_first}"),
        },
        "keluarga": {
            "name": family_name,
            "call": "Mama",
            "role": "Ibu protagonis",
            "age": rng.integer(48, 62),
            "job": "",
            "pressure": "",
            "voice": data.VOICES["ibu"],
            "function": "tekanan dan alasan emosional protagonis",
            **sheet("keluarga", "Mama"),
        },
    }
    return cast


def plan_story(
    title: str | None = None,
    engine_key: str | None = None,
    seed: int | None = None,
    chapters: int = 40,
    target_words: int = 750,
) -> dict[str, Any]:
    rng = Rng(seed)
    if engine_key:
        if engine_key not in data.ENGINE_BY_KEY:
            raise ValueError(f"Mesin tidak dikenal: {engine_key}")
        engine = data.ENGINE_BY_KEY[engine_key]
    else:
        engine = rng.pick(data.ENGINES)

    world = dict(rng.pick(engine["worlds"]))
    world.setdefault("client", "klien utama")
    world.setdefault("project", "proyek utama")
    world.setdefault("city", "Jakarta")
    world.setdefault("channel", "grup kantor")

    story_title = (title or rng.pick(engine["titles"])).strip()

    cast = _cast(rng, engine, world)
    protagonist = cast["protagonis"]
    love = cast["love"]
    antagonist = cast["antagonis"]
    ally = cast["sekutu"]
    mentor = cast["mentor"]
    family = cast["keluarga"]
    family["pressure"] = protagonist["family_pressure"]

    extras = _extras(rng, engine)

    context: dict[str, Any] = {
        # names used in prose templates
        "protagonis": protagonist["call"],
        "love": love["call"],
        "antagonis": antagonist["call"],
        "sekutu": ally["call"],
        "mentor": mentor["call"],
        "mama": family["call"],
        "protagonist_full": protagonist["name"],
        "love_full": love["name"],
        "antagonist_full": antagonist["name"],
        "ally_full": ally["name"],
        # world
        "company": world["company"],
        "sector": world["sector"],
        "job": world["job"],
        "protagonist_job": world["job"],
        "project": world["project"],
        "client": world["client"],
        "klien": world["client"],
        "city": world["city"],
        "channel": world["channel"],
        "love_job": "",
        "antagonist_role": "",
        **data.CONTEXT_DEFAULTS,
        **extras,
    }

    love["job"] = fill(rng.pick(engine["love_jobs"]), context)
    context["love_job"] = love["job"]

    # Extras may themselves contain placeholders (e.g. "mantan {protagonis}").
    for key, value in list(extras.items()):
        extras[key] = fill(value, context)
        context[key] = extras[key]

    antagonist_position = fill(rng.pick(engine["antagonist_roles"]), context)
    antagonist["job"] = antagonist_position
    context["antagonist_role"] = antagonist_position

    family["function"] = f"tekanan: {family['pressure']}" if family.get("pressure") else "alasan emosional protagonis"

    raw_secret = engine["secret"]
    if isinstance(raw_secret, list):
        raw_secret = rng.pick(raw_secret)
    context["secret"] = fill(raw_secret, context)

    theme = rng.pick(engine["themes"])
    context["theme"] = theme

    logline = fill(LOGLINES[engine["key"]], context)
    dramatic_question = fill(DRAMATIC_QUESTIONS[engine["key"]], context)
    ending_direction = fill(rng.pick(engine["resolutions"]), context)
    midpoint_text = fill(engine["midpoint"], context)
    crisis_text = fill(engine["crisis"], context)

    setup_n, escalation_n, midpoint_n, fallout_n, act3_n = _phase_counts(chapters)

    midpoint_chapter = setup_n + escalation_n + midpoint_n
    act3_start = setup_n + escalation_n + midpoint_n + fallout_n + 1
    climax_chapter = act3_start + (act3_n - 3)
    crisis_chapter = act3_start + 2
    act_break_chapter = setup_n
    turning_points = sorted({act_break_chapter, midpoint_chapter, act3_start, climax_chapter})

    threads = [
        {
            "name": "Refleks khas protagonis",
            "plant": 1,
            "pay": climax_chapter,
            "desc": f"Refleks '{protagonist['flaw']}' muncul pertama kali.",
        },
        {
            "name": "Objek khas protagonis",
            "plant": min(3, setup_n),
            "pay": midpoint_chapter,
            "desc": f"Objek {protagonist['signature_object']} diperkenalkan.",
        },
        {
            "name": "Aturan mekanisme",
            "plant": 2,
            "pay": act3_start + 2,
            "desc": engine["logic_rules"][0],
        },
        {
            "name": "Rahasia love interest",
            "plant": max(5, midpoint_chapter - 2),
            "pay": act3_start - 1,
            "desc": f"Rahasia {love['call']}: {love['secret']}",
        },
        {
            "name": "Bukti utama",
            "plant": max(4, midpoint_chapter - 1),
            "pay": climax_chapter - 1,
            "desc": "Bukti yang nanti dipakai di klimaks.",
        },
        {
            "name": "Tekanan keluarga",
            "plant": max(6, setup_n - 1),
            "pay": min(chapters, act3_start + 2),
            "desc": f"Tekanan keluarga: {protagonist['family_pressure']}",
        },
    ]
    setup_map: dict[int, list[str]] = {number: [] for number in range(1, chapters + 1)}
    payoff_map: dict[int, list[str]] = {number: [] for number in range(1, chapters + 1)}
    for thread in threads:
        setup_map[thread["plant"]].append(f"{thread['name']} — {thread['desc']}")
        payoff_map[thread["pay"]].append(f"{thread['name']} — dibayar atau diubah maknanya.")

    humor_chapters: set[int] = set()
    cursor = 2
    while cursor <= chapters:
        humor_chapters.add(cursor)
        cursor += rng.integer(2, 3)
    emotional_chapters = set(range(5, chapters + 1, 5))
    humor_pool = rng.cycle(engine.get("humor", ["Momen canggung di ruang publik."]), len(humor_chapters))
    emotional_pool = rng.cycle(EMOTIONAL_BEATS, len(emotional_chapters))
    humor_map = {
        number: humor_pool[index]
        for index, number in enumerate(sorted(humor_chapters))
    }
    emotional_map = {
        number: emotional_pool[index]
        for index, number in enumerate(sorted(emotional_chapters))
    }

    phases = [
        {"key": "setup", "label": PHASE_LABELS["setup"], "count": setup_n},
        {"key": "escalation", "label": PHASE_LABELS["escalation"], "count": escalation_n},
        {"key": "midpoint", "label": PHASE_LABELS["midpoint"], "count": midpoint_n},
        {"key": "fallout", "label": PHASE_LABELS["fallout"], "count": fallout_n},
        {"key": "act3", "label": PHASE_LABELS["act3"], "count": act3_n},
    ]
    start = 1
    for phase in phases:
        phase["start"] = start
        phase["end"] = start + phase["count"] - 1
        start = phase["end"] + 1

    title_pool = [
        t for t in data.CHAPTER_TITLES
        if 2 <= len(t.split()) <= 5 and t.lower() != story_title.lower()
    ]
    title_pool = rng.shuffled(list(dict.fromkeys(title_pool)))
    hook_pools = {phase: rng.shuffled(data.HOOKS[phase]) for phase in PHASE_ORDER}
    special_hook_pools: dict[str, list[str]] = {}
    complication_pool = rng.shuffled(data.COMPLICATIONS + EXTRA_COMPLICATIONS)
    turn_pool = rng.shuffled(data.TURNS + EXTRA_TURNS)
    early_complications = rng.shuffled(EARLY_COMPLICATIONS)
    accident_complications = rng.shuffled(
        engine.get("pemicu_complications", ACCIDENT_COMPLICATIONS)
    )
    early_turns = rng.shuffled(EARLY_TURNS)
    complication_index = 0
    turn_index = 0
    last_place = ""
    last_time = ""

    def next_title() -> str:
        if title_pool:
            return title_pool.pop()
        return f"Bab {len(chapters_out) + 1} Tanpa Judul"

    def next_hook(phase: str, function: str | None = None) -> str:
        source: list[str] | None = None
        if function == "Pemicu" and engine.get("pemicu_hooks"):
            source = engine["pemicu_hooks"]
        elif function in SPECIAL_HOOKS:
            source = SPECIAL_HOOKS[function]
        if source is not None:
            pool = special_hook_pools.setdefault(function, rng.shuffled(source))
            if not pool:
                pool.extend(rng.shuffled(source))
            return fill(pool.pop(), context)
        pool = hook_pools[phase]
        if not pool:
            pool.extend(rng.shuffled(data.HOOKS[phase]))
        return fill(pool.pop(), context)

    def next_complication(phase: str, function: str) -> str:
        nonlocal complication_index
        if phase == "setup":
            if function == "Pemicu":
                source = engine.get("pemicu_complications", ACCIDENT_COMPLICATIONS)
                if not accident_complications:
                    accident_complications.extend(rng.shuffled(source))
                return fill(accident_complications.pop(), context)
            if not early_complications:
                early_complications.extend(rng.shuffled(EARLY_COMPLICATIONS))
            return fill(early_complications.pop(), context)
        value = complication_pool[complication_index % len(complication_pool)]
        complication_index += 1
        return fill(value, context)

    def next_turn(phase: str, function: str) -> str:
        nonlocal turn_index
        if phase == "setup":
            if not early_turns:
                early_turns.extend(rng.shuffled(EARLY_TURNS))
            return fill(early_turns.pop(), context)
        value = turn_pool[turn_index % len(turn_pool)]
        turn_index += 1
        return fill(value, context)

    def next_place(scene: str) -> str:
        nonlocal last_place
        inferred = infer_place(scene, context)
        if inferred:
            last_place = inferred
            return inferred
        place = fill(rng.pick(data.LOCATIONS), context)
        if place == last_place:
            place = fill(rng.pick(data.LOCATIONS), context)
        last_place = place
        return place

    def next_time() -> str:
        nonlocal last_time
        value = rng.pick(data.TIMES)
        if value == last_time:
            value = rng.pick(data.TIMES)
        last_time = value
        return value

    def day_label(number: int) -> str:
        return f"Hari {(number - 1) // 2 + 1}"

    def hook_type(hook: str) -> str:
        lower = hook.lower()
        for label, words in HOOK_TYPE_WORDS:
            if any(word in lower for word in words):
                return label
        return "Pertanyaan"

    def present_characters(scene: str, pov: str) -> list[str]:
        people = [pov]
        for person in cast.values():
            for name in (person.get("call"), person.get("name")):
                if name and name in scene and name not in people:
                    people.append(name)
        return people

    def technique_for(phase: str, number: int) -> str:
        if number == 1:
            return "in medias res; dramatic irony; action beats"
        bank = TECHNIQUE_BANK[phase]
        picks = rng.sample(bank, 2)
        return "; ".join(picks)

    chapters_out: list[dict[str, Any]] = []

    def add(
        phase: str,
        function: str,
        scene: str,
        hook: str,
        target: int | None = None,
    ) -> None:
        number = len(chapters_out) + 1
        side_chapter = False
        pov = protagonist["call"]
        if phase in {"escalation", "fallout"} and 1 < number < chapters:
            if rng.chance(0.14):
                pov = love["call"]
                side_chapter = True
            elif rng.chance(0.07):
                pov = ally["call"]
                side_chapter = True

        chapter_time = infer_time(scene, next_time())
        chapter_place = next_place(scene)
        conflict = next_complication(phase, function)
        turn = next_turn(phase, function)
        people = present_characters(scene, pov)
        turning = number in turning_points
        chapter_target = target or (
            900 if turning or function in {"Komitmen", "Titik tengah", "Klimaks"} else target_words
        )
        setup_text = "; ".join(setup_map.get(number, [])) or "—"
        payoff_text = "; ".join(payoff_map.get(number, [])) or "—"
        beats = [
            f"Buka: {truncate(scene, 180)}",
            f"Tekanan: {conflict}",
            f"Informasi baru: {turn}",
            f"Tutup dengan hook: {hook}",
        ]

        chapters_out.append({
            "number": number,
            "title": next_title(),
            "phase": phase,
            "phase_label": PHASE_LABELS[phase],
            "function": function,
            "scene": scene,
            "goal": GOAL_BANK.get(function, f"Menjalankan beat '{function}'."),
            "conflict": conflict,
            "turn": turn,
            "change": CHANGE_BANK[phase],
            "knowledge": f"Yang menyaksikan: {', '.join(people)}. Fakta baru: {turn}",
            "setup": setup_text,
            "payoff": payoff_text,
            "humor_beat": humor_map.get(number, "—"),
            "emotional_beat": emotional_map.get(number, "—"),
            "technique": technique_for(phase, number),
            "hook": hook,
            "hook_type": hook_type(hook),
            "logic": engine["logic_rules"][(number - 1) % len(engine["logic_rules"])],
            "reader_question": READER_QUESTIONS[phase],
            "not_happening": NOT_HAPPENING[phase],
            "beats": beats,
            "pov": pov,
            "day": day_label(number),
            "time": chapter_time,
            "place": chapter_place,
            "target_words": chapter_target,
            "turning_point": turning,
            "side_chapter": side_chapter,
        })

    setup_raw = [(engine["inciting"], "Pemicu")] + [
        (raw, setup_function(raw)) for raw in engine["setup_events"]
    ]
    setup_slots = setup_n - 1
    fixed_for_setup = setup_raw[:setup_slots]
    leftover_setup = setup_raw[setup_slots:]
    setup_filler_pool = [raw for raw, _ in leftover_setup] + list(data.GENERIC_FILLERS["setup"])
    setup_fillers_needed = max(0, setup_slots - len(fixed_for_setup))
    setup_fillers = rng.cycle(setup_filler_pool, setup_fillers_needed)

    for raw, function in fixed_for_setup:
        add("setup", function, fill(raw, context), next_hook("setup", function))
    for index in range(setup_fillers_needed):
        function = FILLER_FUNCTIONS["setup"][index % len(FILLER_FUNCTIONS["setup"])]
        add("setup", function, fill(setup_fillers[index], context), next_hook("setup", function))
    add("setup", "Komitmen", fill(engine["act_break"], context), next_hook("setup", "Komitmen"))

    escalation_events = list(engine["escalation_events"])
    add("escalation", "Konsekuensi", fill(escalation_events[0], context), next_hook("escalation"))
    escalation_fillers_needed = escalation_n - 2
    escalation_pool = escalation_events[1:-1] + list(data.GENERIC_FILLERS["escalation"])
    escalation_fillers = rng.cycle(escalation_pool, escalation_fillers_needed)
    for index in range(escalation_fillers_needed):
        function = FILLER_FUNCTIONS["escalation"][index % len(FILLER_FUNCTIONS["escalation"])]
        add("escalation", function, fill(escalation_fillers[index], context), next_hook("escalation"))
    add("escalation", "Peringatan", fill(escalation_events[-1], context), next_hook("escalation"))

    add("midpoint", "Titik tengah", fill(engine["midpoint"], context), next_hook("midpoint", "Titik tengah"))

    fallout_events = list(engine["fallout_events"])
    add("fallout", "Retak", fill(fallout_events[0], context), next_hook("fallout"))
    fallout_fillers_needed = fallout_n - 3
    fallout_pool = fallout_events[1:-1] + list(data.GENERIC_FILLERS["fallout"])
    fallout_fillers = rng.cycle(fallout_pool, fallout_fillers_needed)
    for index in range(fallout_fillers_needed):
        function = FILLER_FUNCTIONS["fallout"][index % len(FILLER_FUNCTIONS["fallout"])]
        add("fallout", function, fill(fallout_fillers[index], context), next_hook("fallout"))
    add("fallout", "Titik terendah", fill(fallout_events[-2] if len(fallout_events) > 1 else engine["crisis"], context), next_hook("fallout"))
    add("fallout", "Persiapan", fill(fallout_events[-1], context), next_hook("fallout"))

    act3_events = list(engine["act3_events"])
    add("act3", "Rencana", fill(act3_events[0], context), next_hook("act3"))
    add("act3", "Konfrontasi", fill(act3_events[1], context), next_hook("act3"))
    add("act3", "Semua hilang", fill(engine["crisis"], context), next_hook("act3", "Semua hilang"))
    add("act3", "Pengakuan", fill(rng.pick(CONFESSION_EVENTS), context), next_hook("act3"))
    act3_fillers_needed = act3_n - 7
    act3_pool = act3_events[2:] + list(data.GENERIC_FILLERS["act3"])
    act3_fillers = rng.cycle(act3_pool, act3_fillers_needed)
    for index in range(act3_fillers_needed):
        function = FILLER_FUNCTIONS["act3"][index % len(FILLER_FUNCTIONS["act3"])]
        add("act3", function, fill(act3_fillers[index], context), next_hook("act3"))
    add("act3", "Klimaks", fill(engine["climax"], context), next_hook("act3", "Klimaks"))
    add("act3", "Resolusi", ending_direction, next_hook("act3", "Resolusi"))
    add("act3", "Citra akhir", fill(engine["final_image"], context), next_hook("act3", "Citra akhir"))

    # Safety: the composed slots must match the requested chapter count.
    while len(chapters_out) > chapters:
        chapters_out.pop()
    while len(chapters_out) < chapters:
        add("act3", "Akselerasi", fill(rng.pick(data.GENERIC_FILLERS["act3"]), context), next_hook("act3"))

    for index, chapter in enumerate(chapters_out, start=1):
        chapter["number"] = index

    story = {
        "version": 1,
        "title": story_title,
        "slug": slugify(story_title),
        "folder": folder_name(story_title),
        "engine": engine["key"],
        "engine_label": engine["label"],
        "promise": engine["promise"],
        "seed": rng.seed,
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "chapter_count": chapters,
        "target_words": target_words,
        "logline": logline,
        "blurb": f"{logline} {protagonist['call']} pikir ia bisa menunggu sampai semuanya reda. Tapi setiap hari, harga untuk mengaku makin mahal. {dramatic_question}",
        "premise": " ".join([
            logline,
            midpoint_text,
            "Konflik memuncak ketika " + crisis_text,
        ]),
        "theme": theme,
        "dramatic_question": dramatic_question,
        "ending_direction": ending_direction,
        "secret": context["secret"],
        "midpoint_text": midpoint_text,
        "crisis_text": crisis_text,
        "outline": {"version": "0.1", "status": "draft", "locked_at": None},
        "format": {
            "heading": "## Bab N: Judul",
            "chat": "**Nama:** *isi pesan*",
            "email": "teks email atau surat ditulis miring",
            "emoji": "dilarang",
        },
        "release_plan": "3–5 bab per minggu",
        "calendar": {
            "start": "Jumat",
            "note": "Dua bab per hari naratif; sesuaikan hari dan jam saat menulis.",
        },
        "turning_points": turning_points,
        "knowledge_facts": engine.get("knowledge_facts", []),
        "logic_rules": engine.get("logic_rules", []),
        "humor": engine.get("humor", []),
        "midpoint_chapter": midpoint_chapter,
        "climax_chapter": climax_chapter,
        "crisis_chapter": crisis_chapter,
        "act_break_chapter": act_break_chapter,
        "world": world,
        "extras": extras,
        "cast": cast,
        "glossary": engine["glossary"],
        "phases": phases,
        "chapters": chapters_out,
    }
    return story


def propose_ideas(
    seed: int | None = None,
    engine_key: str | None = None,
    count: int = 3,
) -> list[dict[str, Any]]:
    """Return 3 premise options as required by the writing guide."""
    rng = Rng(seed)
    count = max(1, min(count, 6))
    if engine_key:
        pool = [data.ENGINE_BY_KEY[engine_key]]
    else:
        pool = rng.shuffled(data.ENGINES)
    engines = [pool[index % len(pool)] for index in range(count)]

    ideas: list[dict[str, Any]] = []
    for engine in engines:
        story = plan_story(
            engine_key=engine["key"],
            seed=rng.integer(1, 999_999_999),
            chapters=30,
        )
        cast = story["cast"]
        ideas.append({
            "title": story["title"],
            "engine": engine["label"],
            "engine_key": engine["key"],
            "logline": story["logline"],
            "theme": story["theme"],
            "dramatic_question": story["dramatic_question"],
            "humor": story.get("humor", []),
            "cast": {
                "protagonis": f"{cast['protagonis']['name']} — {cast['protagonis']['job']}; cacat: {cast['protagonis']['flaw']}",
                "love": f"{cast['love']['name']} — {cast['love']['job']}",
                "antagonis": f"{cast['antagonis']['name']} — {cast['antagonis']['job'] or cast['antagonis']['role']}",
                "sekutu": f"{cast['sekutu']['name']} — {cast['sekutu']['job']}",
            },
        })
    return ideas
