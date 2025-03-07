from .models import Book

books = [
    {
        "title": "O'tkan kunlar",
        "author": "Abdulla Qodiriy",
        "genre": "Tarixiy roman",
        "publisher": "Sharq nashriyoti",
        "price": 50000,
        "quantity": 20,
        "description": "O'zbek adabiyotidagi birinchi tarixiy roman bo'lib, unda XIX asr oxiridagi Buxoro va Qo'qon xonliklarining ijtimoiy hayoti tasvirlangan.",
        "image": "books/otkan_kunlar.jpg"
    },
    {
        "title": " Mehrobdanchayon",    
        "author": "Abdulla Qodiriy",
        "genre": "Tarixiy roman",
        "publisher": "Adabiyot nashriyoti",
        "price": 48000,
        "quantity": 15,
        "description": "Bu roman XIX asr oxirida Buxoroda kechgan voqealarni aks ettirib, millatparvarlik va sevgi mavzularini yoritadi.",
        "image": "books/mehrobdan_chayon.jpg"
    },
    {
        "title": "Kecha va kunduz",
        "author": "Cho'lpon",
        "genre": "Tarixiy roman",
        "publisher": "Sharq nashriyoti",
        "price": 55000,
        "quantity": 10,
        "description": "Ushbu roman jadidchilik harakati, mustamlakachilik va ozodlik yo'lida kurash mavzularini yoritadi.",
        "image": "books/kecha_va_kunduz.jpg"
    },
    {
        "title": "Farg'ona tong otguncha",
        "author": "Odil Yoqubov",
        "genre": "Tarixiy roman",
        "publisher": "O'zbekiston nashriyoti",
        "price": 60000,
        "quantity": 12,
        "description": "Roman jadidlarning ozodlik yo'lidagi kurashi haqida hikoya qiladi.",
        "image": "books/fargona_tong_otguncha.jpg"
    },
    {
        "title": "Ulug'bek xazinasi",
        "author": "Odil Yoqubov",
        "genre": "Tarixiy roman",
        "publisher": "Sharq nashriyoti",
        "price": 58000,
        "quantity": 14,
        "description": "Buyuk alloma Mirzo Ulug'bekning ilmiy merosi va unga qarshi fitnalar tasvirlangan roman.",
        "image": "books/ulugbek_xazinasi.jpg"
    },
    {
        "title": "Bobur",
        "author": "Mirmuhsin",
        "genre": "Tarixiy-biografik roman",
        "publisher": "O'zbekiston nashriyoti",
        "price": 62000,
        "quantity": 18,
        "description": "Buyuk sarkarda va shoir Zahiriddin Muhammad Boburning hayoti va faoliyatini aks ettirgan roman.",
        "image": "books/bobur.jpg"
    },
    {
        "title": "Ikki eshik orasi",
        "author": "O'ybek",
        "genre": "Badiiy roman",
        "publisher": "Yangi asr nashriyoti",
        "price": 45000,
        "quantity": 10,
        "description": "Ijtimoiy hayot va odamlarning o'zaro munosabatlarini yoritgan mashhur roman.",
        "image": "books/ikki_eshik_orasi.jpg"
    },
    {
        "title": "Shum bola",
        "author": "G'afur G'ulom",
        "genre": "Satirik roman",
        "publisher": "O'zbekiston nashriyoti",
        "price": 40000,
        "quantity": 30,
        "description": "Bir bola obrazida xalqning sho'x, qiziqarli hayot tarzi aks ettirilgan kulgili asar.",
        "image": "books/shum_bola.jpg"
    },
    {
        "title": "Odam bo'lish qiyin",
        "author": "Shukur Xolmirzayev",
        "genre": "Badiiy roman",
        "publisher": "Yangi asr nashriyoti",
        "price": 52000,
        "quantity": 17,
        "description": "Yosh qahramonning hayot yo'lida uchraydigan qiyinchiliklar tasvirlangan asar.",
        "image": "books/odam_bolish_qiyin.jpg"
    },
    {
        "title": "Ko'hna dunyo",
        "author": "O'tkir Hoshimov",
        "genre": "Dramatik roman",
        "publisher": "Sharq nashriyoti",
        "price": 57000,
        "quantity": 25,
        "description": "O'tgan asrning ijtimoiy muammolari va insoniy qadriyatlari haqida hikoya qiluvchi asar.",
        "image": "books/kohna_dunyo.jpg"
    }
]

for book in books:
    Book.objects.create(
        title=book["title"],
        author=book["author"],
        genre=book["genre"],
        publisher=book["publisher"],
        price=book["price"],
        quantity=book["quantity"],
        description=book["description"],
        image=book["image"]
    )
