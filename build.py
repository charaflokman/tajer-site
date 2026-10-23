"""Builds the Tajer download site (ar at /, fr at /fr/, en at /en/). Run: python build.py <github-owner>."""
import io
import os
import sys

OWNER = sys.argv[1] if len(sys.argv) > 1 else "OWNER"
DESKTOP_VERSION = "1.0.8"  # change here to switch the Windows download names
ANDROID_VERSION = "1.0.7"  # change here to switch the Android download name
VERSION = DESKTOP_VERSION
# Windows installers are too big to push through git from the shop line: they live on the GitHub release
RELEASE_URL = f"https://github.com/charaflokman/tajer-site/releases/download/v{DESKTOP_VERSION}/"
FILES = {
    "win64": (f"Tajer-{DESKTOP_VERSION}-win64.exe", "99 MB"),
    "win32": (f"Tajer-{DESKTOP_VERSION}-win32.exe", "98 MB"),
    "apk": (f"Tajer-{ANDROID_VERSION}.apk", "7 MB"),
}


def load_sums():
    out = {}
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads", "SHA256SUMS.txt")
    if os.path.exists(p):
        for line in io.open(p, encoding="utf-8"):
            parts = line.strip().split(None, 1)
            if len(parts) == 2 and len(parts[0]) == 64:
                out[parts[1].lstrip("*").strip()] = parts[0].lower()
    return out


SUMS = load_sums()

T = {
    "ar": dict(
        dir="rtl", lang="ar", title="تاجر — برنامج نقطة البيع للمحلات",
        tag="برنامج بيع ومخزون وديون لكل محل، يعمل بلا إنترنت.",
        lead="البيع بالباركود، ودفتر الديون، والمخزون بتاريخ الصلاحية، والمشتريات، والتقارير، والنسخ الاحتياطي. على الحاسوب وعلى الهاتف، بالعربية والفرنسية والإنجليزية والإسبانية والإيطالية والألمانية.",
        beta="النسخة @V. احتفظ دائما بنسخة احتياطية من بياناتك.",
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
        beta="Version @V. Faites toujours une sauvegarde de vos données.",
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
        beta="Version @V. Always keep a backup of your data.",
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
BL = {
 "ar": dict(nav="ويندوز حظر الملف؟", title="ويندوز حظر الملف — تاجر", h="ويندوز حظر الملف؟ لا تقلق",
  intro="تاجر برنامج سليم، لكنه جديد وغير موقّع رقميا بعد، فيظنه ويندوز أو مضاد الفيروسات مجهولا. إليك الحلول الثلاثة، ثم طريقة التأكد أن الملف سليم.",
  s1="1) رسالة زرقاء «Windows protected your PC»", s1t="اضغط «More info» (معلومات إضافية)، ثم يظهر زر «Run anyway» (تشغيل على أي حال). اضغطه.",
  s2="2) الملف لا يفتح أو يرفض التشغيل", s2t="اضغط بالزر الأيمن على الملف، اختر «Properties» (خصائص). أسفل النافذة ضع علامة على «Unblock» (إلغاء الحظر)، ثم «OK». شغّل الملف من جديد.",
  s3="3) مضاد الفيروسات حذف الملف أو أنذر", s3t="هذا إنذار خاطئ شائع للبرامج الجديدة. تأكد من البصمة (القسم التالي)، فإن تطابقت اسمح بالملف من «Allowed threats» أو أضفه للاستثناءات في مضاد الفيروسات ثم حمّله من جديد.",
  sh="كيف أتأكد أن الملف سليم؟ (SHA256)", sht=["افتح مجلد التحميلات، اضغط على شريط العنوان واكتب cmd ثم Enter.", "اكتب الأمر التالي (غيّر اسم الملف) ثم Enter:", "قارن الأرقام والحروف الطويلة مع المكتوبة بجانب زر التحميل في الموقع (أو في ملف SHA256SUMS.txt). إن تطابقت كلها فالملف سليم. إن اختلفت فلا تشغله وأعد التحميل."],
  mi="More info", ra="Run anyway", un="Unblock", back="رجوع إلى التحميل", pic="صورة توضيحية مبسطة"),
 "fr": dict(nav="Windows a bloqué le fichier ?", title="Windows a bloqué le fichier — Tajer", h="Windows a bloqué le fichier ? Pas de panique",
  intro="Tajer est sain, mais il est récent et pas encore signé numériquement : Windows ou l'antivirus le croit inconnu. Voici trois solutions, puis comment vérifier que le fichier est intact.",
  s1="1) Message bleu « Windows protected your PC »", s1t="Cliquez « More info » (Informations complémentaires), puis le bouton « Run anyway » (Exécuter quand même) apparaît. Cliquez dessus.",
  s2="2) Le fichier ne s'ouvre pas", s2t="Clic droit sur le fichier, « Properties » (Propriétés). En bas, cochez « Unblock » (Débloquer), puis « OK ». Relancez le fichier.",
  s3="3) L'antivirus a supprimé le fichier ou donne une alerte", s3t="C'est une fausse alerte fréquente pour les logiciels récents. Vérifiez l'empreinte (section suivante) ; si elle correspond, autorisez le fichier dans « Menaces autorisées » ou ajoutez-le aux exclusions de l'antivirus, puis retéléchargez.",
  sh="Comment vérifier le fichier ? (SHA256)", sht=["Ouvrez le dossier Téléchargements, cliquez dans la barre d'adresse, tapez cmd puis Entrée.", "Tapez la commande suivante (changez le nom du fichier) puis Entrée :", "Comparez la longue suite de chiffres et lettres avec celle affichée près du bouton de téléchargement (ou dans SHA256SUMS.txt). Si tout correspond, le fichier est intact. Sinon, ne le lancez pas et retéléchargez."],
  mi="More info", ra="Run anyway", un="Unblock", back="Retour au téléchargement", pic="Image explicative simplifiée"),
 "en": dict(nav="Windows blocked the file?", title="Windows blocked the file — Tajer", h="Windows blocked the file? Don't worry",
  intro="Tajer is safe, but it is new and not digitally signed yet, so Windows or your antivirus treats it as unknown. Here are three fixes, then how to check the file is genuine.",
  s1="1) Blue message \"Windows protected your PC\"", s1t="Click \"More info\", then the \"Run anyway\" button appears. Click it.",
  s2="2) The file will not open", s2t="Right-click the file, choose \"Properties\". At the bottom tick \"Unblock\", then \"OK\". Run the file again.",
  s3="3) The antivirus deleted the file or warned you", s3t="This is a common false alarm for new software. Check the fingerprint (next section); if it matches, allow the file in the antivirus \"Allowed threats\" or add it to the exclusions, then download again.",
  sh="How do I check the file is genuine? (SHA256)", sht=["Open the Downloads folder, click the address bar, type cmd and press Enter.", "Type this command (change the file name) and press Enter:", "Compare the long string with the one shown next to the download button (or in SHA256SUMS.txt). If all of it matches, the file is genuine. If not, do not run it and download again."],
  mi="More info", ra="Run anyway", un="Unblock", back="Back to download", pic="Simplified illustration"),
}
CP = {"ar": "نسخ الكامل", "fr": "Copier tout", "en": "Copy full"}
VIDEOS = [
    ("01-sell-cash", "البيع نقدا"), ("02-sell-credit", "البيع بالدين"), ("03-return", "إرجاع بضاعة"),
    ("04-receive-goods", "استلام بضاعة من المورد"), ("05-import-pdf-invoice", "استيراد فاتورة PDF"),
    ("06-record-loss", "تسجيل تالف أو ضائع"), ("07-stock-count", "جرد المخزون"), ("08-print-labels", "طباعة ملصقات الأسعار"),
    ("09-close-day", "إغلاق اليوم"), ("10-backup", "النسخ الاحتياطي"), ("11-link-device", "ربط جهاز آخر"),
    ("12-themes", "تغيير المظهر"),
]
VID_LINK = {"ar": "videos/", "fr": "../videos/", "en": "../videos/"}
VID_LABEL = {"ar": "فيديوهات الشرح", "fr": "Vidéos (arabe)", "en": "Videos (Arabic)"}

def videos_page():
    cards = "".join(
        f'<li><a href="ar/{n}.mp4"><img src="ar/{n}.png" alt="" loading="lazy" width="640" height="360">'
        f'<span>{i:02d}. {t}</span></a></li>' for i, (n, t) in enumerate(VIDEOS, 1))
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>فيديوهات الشرح — تاجر</title>
<meta name="description" content="فيديوهات قصيرة بالعربية تشرح استعمال تاجر خطوة بخطوة.">
<link rel="icon" href="../assets/img/tajer-tile-32.png">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body>
<header class="bar"><div class="wrap bar-in">
  <a class="brand" href="../"><img src="../assets/img/tajer-tile.svg" alt="" width="36" height="36"><span>تاجر</span></a>
  <nav><a href="../">الرئيسية</a></nav>
</div></header>
<main class="wrap">
  <h1>فيديوهات الشرح</h1>
  <p class="lead">فيديوهات قصيرة بالعربية، كل واحد يشرح مهمة من يوم المحل. تحتاج إلى الإنترنت لمشاهدتها.</p>
  <ul class="vids">{cards}</ul>
</main>
<footer class="wrap foot">Tajer · تاجر — v{VERSION}</footer>
</body>
</html>
"""

def blocked_page(k):
    b = BL[k]
    t = T[k]
    root = "../" if k == "ar" else "../../"
    home = "../"
    fn = FILES["win64"][0]

    def fig(inner):
        return f'<figure class="mock" dir="ltr">{inner}<figcaption>{b["pic"]}</figcaption></figure>'
    f1 = fig(f'<div class="win"><div class="wt">Windows protected your PC</div><p>SmartScreen prevented an unrecognized app from starting.</p><p><u class="hl">{b["mi"]}</u></p><div class="btns"><span class="btn hl">{b["ra"]}</span><span class="btn">Don&#39;t run</span></div></div>')
    f2 = fig(f'<div class="win"><div class="wt">{fn} - Properties</div><p>Security: this file came from another computer and might be blocked.</p><p><span class="chk hl">&#10003;</span> <b class="hl">{b["un"]}</b></p><div class="btns"><span class="btn hl">OK</span><span class="btn">Cancel</span></div></div>')
    h = SUMS.get(fn)
    shown = (h[:12] + "...") if h else "a1b2c3d4e5f6..."
    f3 = fig(f'<div class="win term"><div class="wt">cmd</div><pre>C:\\Users\\you\\Downloads&gt;certutil -hashfile {fn} SHA256\nSHA256 hash of {fn}:\n<span class="hl">{shown}</span>\nCertUtil: -hashfile command completed successfully.</pre></div>')
    cmd = f'<pre class="cmd" dir="ltr">certutil -hashfile {fn} SHA256</pre>'
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{b['title']}</title>
<meta name="description" content="{b['intro']}">
<link rel="icon" href="{root}assets/img/tajer-tile-32.png">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="bar"><div class="wrap bar-in">
  <a class="brand" href="{home}"><img src="{root}assets/img/tajer-tile.svg" alt="" width="36" height="36"><span>{'تاجر' if k == 'ar' else 'Tajer'}</span></a>
  <nav><a href="{home}#download">{b['back']}</a></nav>
</div></header>
<main class="wrap help">
  <h1>{b['h']}</h1>
  <p class="lead">{b['intro']}</p>
  <h2>{b['s1']}</h2><p>{b['s1t']}</p>{f1}
  <h2>{b['s2']}</h2><p>{b['s2t']}</p>{f2}
  <h2>{b['s3']}</h2><p>{b['s3t']}</p>
  <h2>{b['sh']}</h2>
  <ol class="list"><li>{b['sht'][0]}</li><li>{b['sht'][1]}{cmd}</li><li>{b['sht'][2]}</li></ol>{f3}
  <p><a href="{home}#download">{b['back']}</a></p>
</main>
<footer class="wrap foot">Tajer · تاجر — v{VERSION}</footer>
<script>document.addEventListener("click",function(e){{var b=e.target.closest(".cp");if(!b)return;var h=b.dataset.h,o=b.textContent;function ok(){{b.textContent="OK";setTimeout(function(){{b.textContent=o}},1500)}}if(navigator.clipboard){{navigator.clipboard.writeText(h).then(ok,function(){{prompt("SHA256",h)}})}}else{{prompt("SHA256",h)}}}});</script>
</body>
</html>
"""


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
        h = SUMS.get(f)
        sha = (f'<div class="sha" dir="ltr">SHA256: <code>{h[:16]}</code> <button type="button" class="cp" data-h="{h}">{CP[k]}</button></div>') if h else ""
        return (f'<div class="dlbox"><a class="dl" href="{(RELEASE_URL if f.endswith('.exe') else root + 'downloads/') + f}" download><span class="dl-name">{t[name]}</span>'
                f'<span class="dl-note">{t[note]}</span><span class="dl-meta">{f} · {size}</span></a>{sha}</div>')
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
  <nav><a href="blocked/">{BL[k]['nav']}</a><a href="{LINKS[k][0]}">{t['other']}</a><a href="{LINKS[k][1]}">{t['other2']}</a></nav>
</div></header>
<main>
<section class="hero wrap">
  <h1>{t['tag']}</h1>
  <p class="lead">{t['lead']}</p>
  <p class="beta">{t['beta'].replace('@V', VERSION)}</p>
  <h2 id="download">{t['dl']} <small>v{VERSION}</small></h2>
  <div class="dls">{dl('win64', 'win64', 'win64n')}{dl('win32', 'win32', 'win32n')}{dl('apk', 'apk', 'apkn')}</div>
  <p class="blk"><a href="blocked/">{BL[k]['nav']}</a></p>
</section>
<section class="shots wrap"><h2>{t['shots']}</h2><div class="shot-row">{shots}<img class="phone" src="{root}assets/img/android-checkout-api34.png" alt="" loading="lazy" width="1080" height="2340"></div></section>
<section class="wrap"><h2>{t['feat']}</h2><ul class="feats">{feats}</ul></section>
<section class="wrap two"><div><h2>{t['req']}</h2><ul class="list">{reqs}</ul></div><div><h2>{t['how']}</h2><ol class="list">{hows}</ol></div></section>
<section class="wrap legal"><h2>{t['legal']}</h2><p>{t['legaltxt']}</p>
<p class="links"><a href="{root}legal/SOURCE_OFFER.txt">{t['l1']}</a><a href="{root}legal/LICENSE-MRPL.txt">{t['l2']}</a><a href="{root}legal/THIRD_PARTY_LICENSES.md">{t['l3']}</a></p></section>
</main>
<footer class="wrap foot">Tajer · تاجر — v{VERSION}</footer>
<script>document.addEventListener("click",function(e){{var b=e.target.closest(".cp");if(!b)return;var h=b.dataset.h,o=b.textContent;function ok(){{b.textContent="OK";setTimeout(function(){{b.textContent=o}},1500)}}if(navigator.clipboard){{navigator.clipboard.writeText(h).then(ok,function(){{prompt("SHA256",h)}})}}else{{prompt("SHA256",h)}}}});</script>
</body>
</html>
"""

here = os.path.dirname(os.path.abspath(__file__))
for k, sub in (("ar", ""), ("fr", "fr"), ("en", "en")):
    d = os.path.join(here, sub)
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(page(k))
for k, sub in (("ar", "blocked"), ("fr", "fr/blocked"), ("en", "en/blocked")):
    d = os.path.join(here, sub)
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(blocked_page(k))
os.makedirs(os.path.join(here, "videos"), exist_ok=True)
io.open(os.path.join(here, "videos", "index.html"), "w", encoding="utf-8", newline=chr(10)).write(videos_page())
print("built for", OWNER)
