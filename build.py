"""Builds the Tajer download site (ar at /, fr at /fr/, en at /en/). Run: python build.py <github-owner>."""
import io
import os
import sys

OWNER = sys.argv[1] if len(sys.argv) > 1 else "OWNER"
VERSION = "1.4.0-beta.1"
REL = f"https://github.com/{OWNER}/tajer-site/releases/download/v{VERSION}/"
FILES = {
    "win64": ("Tajer-1.4-beta-win64.exe", "92 MB"),
    "win32": ("Tajer-1.4-beta-win32.exe", "91 MB"),
    "apk": ("Tajer-1.4-beta.apk", "10 MB"),
}

T = {
    "ar": dict(
        dir="rtl", lang="ar", title="تاجر — برنامج نقطة البيع للمحلات",
        tag="برنامج بيع ومخزون وديون لكل محل، يعمل بلا إنترنت.",
        lead="البيع بالباركود، ودفتر الديون، والمخزون بتاريخ الصلاحية، والمشتريات، والتقارير، والنسخ الاحتياطي. على الحاسوب وعلى الهاتف، بالعربية والفرنسية والإنجليزية والإسبانية والإيطالية والألمانية.",
        beta="نسخة تجريبية (Beta): للتجربة فقط، وقد تتغير البيانات بين النسخ. احتفظ بنسخة احتياطية.",
        dl="التحميل", win64="ويندوز 64 بت", win64n="لأغلب الحواسيب (ويندوز 7 فما فوق)",
        win32="ويندوز 32 بت", win32n="للحواسيب القديمة", apk="أندرويد", apkn="أندرويد 5 فما فوق — اسمح بالتثبيت من مصادر غير معروفة",
        feat="ما يقدمه", f=[
            ("سريع عند الصندوق", "مسح بالباركود بقارئ مخصص أو بكاميرا الهاتف، أزرار سريعة، وكل شيء بلوحة المفاتيح."),
            ("دفتر الديون", "رصيد كل زبون، سقف دين، كشف حساب مطبوع، وإيصال عند كل تسديد. بلا فوائد."),
            ("المخزون بالصلاحية", "دفعات بتواريخ صلاحية، منع بيع المنتهي، جرد، ومشتريات من الموردين."),
            ("يعمل بلا إنترنت", "بياناتك في محلك فقط. لا سحابة ولا تتبع. عدة صناديق عبر الشبكة المحلية."),
            ("الهاتف كقارئ", "اربط الهاتف بالحاسوب عبر شبكة المحل ليصبح قارئ باركود، أو استعمله صندوقًا مستقلًا."),
            ("وثائق نظامية", "NIF وRC وNIS وAI على الإيصال والفاتورة، إغلاق يومي، وتقارير PDF."),
        ],
        req="المتطلبات", reqs=["حاسوب بويندوز 7 أو أحدث، ذاكرة 2 جيغابايت، أي معالج ثنائي النواة.", "طابعة إيصالات ESC/POS بعرض 58 أو 80 مم (اختياري).", "قارئ باركود USB أو كاميرا الهاتف (اختياري).", "هاتف أندرويد 5 أو أحدث (اختياري)."],
        how="التثبيت", hows=["شغّل ملف التثبيت واترك المجلد الافتراضي C:\\RetailPOS (اسم بأحرف لاتينية).", "وافق على قاعدة جدار الحماية إن أردت ربط الهاتف.", "في أول تشغيل: اختر اللغة، أدخل بيانات المحل ورقمي NIF وRC، كلمة مرور النسخ الاحتياطي، والمدير."],
        shots="لقطات", legal="التراخيص والمصدر",
        legaltxt="تاجر مبني على Floreant POS (ترخيص MRPL 1.2). كود الأجزاء المرخصة متاح عند الطلب حسب عرض المصدر.",
        l1="عرض المصدر", l2="ترخيص MRPL", l3="تراخيص المكتبات", other="Français", other2="English",
    ),
    "fr": dict(
        dir="ltr", lang="fr", title="Tajer — logiciel de caisse pour commerces",
        tag="Caisse, stock et crédit clients pour tout commerce, sans Internet.",
        lead="Vente au code-barres, carnet de crédit, stock avec dates de péremption, achats, rapports et sauvegardes. Sur ordinateur et sur téléphone, en arabe, français, anglais, espagnol, italien et allemand.",
        beta="Version d'essai (bêta) : pour tester uniquement, les données peuvent changer d'une version à l'autre. Faites une sauvegarde.",
        dl="Télécharger", win64="Windows 64 bits", win64n="La plupart des PC (Windows 7 et plus)",
        win32="Windows 32 bits", win32n="Anciens PC", apk="Android", apkn="Android 5 et plus — autorisez les sources inconnues",
        feat="Ce qu'il fait", f=[
            ("Rapide en caisse", "Lecteur code-barres ou caméra du téléphone, touches rapides, tout au clavier."),
            ("Carnet de crédit", "Solde par client, plafond, relevé imprimé, reçu à chaque paiement. Sans intérêts."),
            ("Stock et péremption", "Lots datés, vente des produits périmés bloquée, inventaire, achats fournisseurs."),
            ("Sans Internet", "Vos données restent dans votre magasin. Ni cloud ni pistage. Plusieurs caisses en réseau local."),
            ("Le téléphone comme lecteur", "Reliez le téléphone au PC par le Wi-Fi du magasin, ou utilisez-le comme caisse."),
            ("Documents conformes", "NIF, RC, NIS et AI sur ticket et facture, clôture journalière, rapports PDF."),
        ],
        req="Configuration", reqs=["PC Windows 7 ou plus récent, 2 Go de RAM, processeur double cœur.", "Imprimante ticket ESC/POS 58 ou 80 mm (optionnel).", "Lecteur code-barres USB ou caméra du téléphone (optionnel).", "Téléphone Android 5 ou plus (optionnel)."],
        how="Installation", hows=["Lancez l'installateur et gardez le dossier C:\\RetailPOS (nom en lettres latines).", "Acceptez la règle du pare-feu pour relier le téléphone.", "Au premier démarrage : langue, magasin avec NIF et RC, mot de passe des sauvegardes, administrateur."],
        shots="Captures", legal="Licences et source",
        legaltxt="Tajer est basé sur Floreant POS (licence MRPL 1.2). Le code des parties sous licence est disponible sur demande selon l'offre de source.",
        l1="Offre de source", l2="Licence MRPL", l3="Licences tierces", other="العربية", other2="English",
    ),
    "en": dict(
        dir="ltr", lang="en", title="Tajer — point of sale for shops",
        tag="Sales, stock and customer credit for any shop, offline.",
        lead="Barcode sales, credit book, stock with expiry dates, purchases, reports and backups. On desktop and on the phone, in Arabic, French, English, Spanish, Italian and German.",
        beta="Beta version: for testing only; data may change between versions. Keep a backup.",
        dl="Download", win64="Windows 64-bit", win64n="Most PCs (Windows 7 and later)",
        win32="Windows 32-bit", win32n="Older PCs", apk="Android", apkn="Android 5 and later — allow unknown sources",
        feat="What it does", f=[
            ("Fast at the till", "Barcode scanner or phone camera, quick keys, everything on the keyboard."),
            ("Credit book", "Balance per customer, limit, printed statement, receipt for every payment. No interest."),
            ("Stock with expiry", "Dated lots, expired items blocked at sale, stock count, supplier purchases."),
            ("Works offline", "Your data stays in your shop. No cloud, no tracking. Several tills on the local network."),
            ("Phone as scanner", "Pair the phone with the PC over the shop Wi-Fi, or use it as a till on its own."),
            ("Proper documents", "NIF, RC, NIS and AI on receipt and invoice, daily close, PDF reports."),
        ],
        req="Requirements", reqs=["Windows 7 or later PC, 2 GB RAM, any dual-core CPU.", "ESC/POS receipt printer, 58 or 80 mm (optional).", "USB barcode scanner or phone camera (optional).", "Android 5 or later phone (optional)."],
        how="Install", hows=["Run the installer and keep the folder C:\\RetailPOS (a name in Latin letters).", "Allow the firewall rule if you want to pair a phone.", "On first start: language, shop with NIF and RC, backup password, administrator."],
        shots="Screenshots", legal="Licences and source",
        legaltxt="Tajer is based on Floreant POS (MRPL 1.2 licence). The source of the licensed parts is available on request under the source offer.",
        l1="Source offer", l2="MRPL licence", l3="Third-party licences", other="العربية", other2="Français",
    ),
}
LINKS = {"ar": ("fr/", "en/"), "fr": ("../", "../en/"), "en": ("../", "../fr/")}
SHOTS = {"ar": ["desktop-checkout-ar.png", "desktop-home-ar.png"], "fr": ["desktop-checkout-fr.png", "desktop-home-fr.png"],
         "en": ["desktop-checkout-fr.png", "desktop-home-fr.png"]}

def page(k):
    t = T[k]
    root = "" if k == "ar" else "../"
    feats = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in t["f"])
    reqs = "".join(f"<li>{r}</li>" for r in t["reqs"])
    hows = "".join(f"<li>{r}</li>" for r in t["hows"])
    shots = "".join(f'<img src="{root}assets/img/{s}" alt="" loading="lazy" width="2049" height="1152">' for s in SHOTS[k])
    def dl(key, name, note):
        f, size = FILES[key]
        return (f'<a class="dl" href="{REL}{f}"><span class="dl-name">{t[name]}</span>'
                f'<span class="dl-note">{t[note]}</span><span class="dl-meta">{f} · {size}</span></a>')
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['tag']}">
<link rel="icon" href="{root}assets/img/tajer-tile-32.png">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="bar"><div class="wrap bar-in">
  <a class="brand" href="{root}"><img src="{root}assets/img/tajer-tile.svg" alt="" width="36" height="36"><span>{'تاجر' if k == 'ar' else 'Tajer'}</span></a>
  <nav><a href="{LINKS[k][0]}">{t['other']}</a><a href="{LINKS[k][1]}">{t['other2']}</a></nav>
</div></header>
<main>
<section class="hero wrap">
  <h1>{t['tag']}</h1>
  <p class="lead">{t['lead']}</p>
  <p class="beta">{t['beta']}</p>
  <h2 id="download">{t['dl']} <small>v{VERSION}</small></h2>
  <div class="dls">{dl('win64', 'win64', 'win64n')}{dl('win32', 'win32', 'win32n')}{dl('apk', 'apk', 'apkn')}</div>
</section>
<section class="shots wrap"><h2>{t['shots']}</h2><div class="shot-row">{shots}<img class="phone" src="{root}assets/img/android-checkout-api34.png" alt="" loading="lazy" width="1080" height="2340"></div></section>
<section class="wrap"><h2>{t['feat']}</h2><ul class="feats">{feats}</ul></section>
<section class="wrap two"><div><h2>{t['req']}</h2><ul class="list">{reqs}</ul></div><div><h2>{t['how']}</h2><ol class="list">{hows}</ol></div></section>
<section class="wrap legal"><h2>{t['legal']}</h2><p>{t['legaltxt']}</p>
<p class="links"><a href="{root}legal/SOURCE_OFFER.txt">{t['l1']}</a><a href="{root}legal/LICENSE-MRPL.txt">{t['l2']}</a><a href="{root}legal/THIRD_PARTY_LICENSES.md">{t['l3']}</a></p></section>
</main>
<footer class="wrap foot">Tajer · تاجر — v{VERSION}</footer>
</body>
</html>
"""

here = os.path.dirname(os.path.abspath(__file__))
for k, sub in (("ar", ""), ("fr", "fr"), ("en", "en")):
    d = os.path.join(here, sub)
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(page(k))
print("built for", OWNER)
