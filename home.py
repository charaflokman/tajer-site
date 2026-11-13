"""Home page of the Tajer site (redesign): texts and template. Used by build.py."""
import json

ICONS = ["scan", "credit", "stock", "backup", "phone", "printer"]

N = {
    "ar": dict(
        brand="تاجر", kicker="برنامج نقطة البيع للمحلات",
        h1=("محلك كله في ", "برنامج واحد", "."),
        cta1="حمّل لويندوز", cta2="للهاتف أندرويد",
        facts=["يعمل بلا إنترنت", "6 لغات", "النسخة @V"],
        again="اطبع وصلا آخر", videos="فيديوهات الشرح", dlnav="التحميل",
        strip=["البيع بالباركود", "دفتر الديون", "المخزون بالصلاحية", "المشتريات", "التقارير", "النسخ الاحتياطي", "عدة صناديق", "الهاتف كقارئ"],
        day_h="يوم في المحل", day_p="من فتح الباب إلى إغلاق الصندوق، تاجر معك في كل خطوة.",
        day=[
            ("08:00", "فتح الوردية", "عدّ نقود الصندوق واكتب المبلغ. البرنامج يحسب الباقي طول اليوم."),
            ("09:30", "وصلت البضاعة", "استلم بضاعة المورد من فاتورة PDF أو Excel، بالكميات وتواريخ الصلاحية."),
            ("11:00", "زحمة عند الصندوق", "امسح الباركود والسعر يظهر. كل شيء بلوحة المفاتيح، والوصل يطبع فورا."),
            ("13:00", "زبون يأخذ بالدين", "اختر الزبون والمبلغ يسجل في دفتره. لكل زبون سقف دين وكشف حساب مطبوع."),
            ("17:00", "زبون يرجع سلعة", "ابحث عن الوصل واختر السلعة. المخزون والصندوق يتعدلان وحدهما."),
            ("20:00", "إغلاق اليوم", "تقرير اليوم بضغطة: المبيعات، الديون، وما في الصندوق. ثم نسخة احتياطية."),
        ],
        show_h="شاشة واضحة، بلا شرح", show_p="أزرار كبيرة، كلمات بسيطة، وكل شيء بلوحة المفاتيح.",
        tabs=[("الصندوق", "desktop-checkout-ar.png"), ("الرئيسية", "desktop-home-ar.png"), ("التقارير", "desktop-reports-ar.png")],
        say=("بياناتك في محلك. ", "لا سحابة ولا تتبع."),
        keep_n="خصوصيتك",
        stats=[("0", "إنترنت مطلوب"), ("6", "لغات"), ("58/80", "مم، طابعة الوصل"), ("5+", "أندرويد على الهاتف")],
        dl_p="اختر جهازك. الملف يتحمل مباشرة.", get="تحميل",
        rc=[
            dict(shop="بقالة الأمل", meta="13/11/2026 10:42 · 000128", totalLabel="المجموع", total="1.345,00",
                 rows=[["حليب كامل 1 لتر", "240,00", "× 2"], ["خبز ماون", "40,00", ""], ["زيت زيتون 750 مل", "950,00", ""], ["سكر 1 كغ", "115,00", ""]],
                 after=[["نقدا", "1.500,00"], ["الباقي", "155,00"]], note="", thanks="شكرا لزيارتكم"),
            dict(shop="بقالة الأمل", meta="13/11/2026 13:05 · 000131", totalLabel="المجموع", total="1.570,00",
                 rows=[["سميد 10 كغ", "1.150,00", ""], ["قهوة 250 غ", "420,00", ""]],
                 after=[["رصيد الزبون بعد البيع", "4.320,00"]], note="على الدفتر: كريم بن علي", thanks="شكرا لزيارتكم"),
            dict(shop="بقالة الأمل", meta="13/11/2026 17:20 · 000139", totalLabel="أعيد نقدا", total="950,00",
                 rows=[["إرجاع: زيت زيتون 750 مل", "-950,00", ""]],
                 after=[], note="رجعت السلعة إلى المخزون", ok=True, thanks="الوصل الأصلي 000128"),
        ],
    ),
    "fr": dict(
        brand="Tajer", kicker="Logiciel de caisse pour commerces",
        h1=("Tout votre magasin dans ", "un seul logiciel", "."),
        cta1="Télécharger pour Windows", cta2="Pour téléphone Android",
        facts=["Fonctionne sans Internet", "6 langues", "Version @V"],
        again="Imprimer un autre ticket", videos="Vidéos (arabe)", dlnav="Télécharger",
        strip=["Vente au code-barres", "Carnet de crédit", "Stock et péremption", "Achats", "Rapports", "Sauvegardes", "Plusieurs caisses", "Téléphone comme lecteur"],
        day_h="Une journée au magasin", day_p="De l'ouverture à la clôture de caisse, Tajer vous suit à chaque étape.",
        day=[
            ("08:00", "Ouverture de la caisse", "Comptez le fond de caisse et saisissez le montant. Le logiciel calcule le reste toute la journée."),
            ("09:30", "La marchandise arrive", "Recevez la livraison depuis la facture PDF ou Excel, avec quantités et dates de péremption."),
            ("11:00", "Affluence en caisse", "Scannez le code-barres, le prix s'affiche. Tout au clavier, le ticket sort tout de suite."),
            ("13:00", "Un client achète à crédit", "Choisissez le client, le montant va dans son carnet. Plafond et relevé imprimé pour chacun."),
            ("17:00", "Un client rend un article", "Retrouvez le ticket, choisissez l'article. Le stock et la caisse se corrigent seuls."),
            ("20:00", "Clôture de la journée", "Le rapport du jour en une touche : ventes, crédits, caisse. Puis une sauvegarde."),
        ],
        show_h="Un écran clair, sans mode d'emploi", show_p="Grands boutons, mots simples, tout au clavier.",
        tabs=[("Caisse", "desktop-checkout-fr.png"), ("Accueil", "desktop-home-fr.png"), ("Rapports", "desktop-reports-fr.png")],
        say=("Vos données restent au magasin. ", "Ni cloud ni pistage."),
        keep_n="Vie privée",
        stats=[("0", "Internet requis"), ("6", "langues"), ("58/80", "mm, imprimante ticket"), ("5+", "Android sur téléphone")],
        dl_p="Choisissez votre appareil. Le fichier se télécharge directement.", get="Télécharger",
        rc=[
            dict(shop="Alimentation El Amel", meta="13/11/2026 10:42 · 000128", totalLabel="Total", total="1.345,00",
                 rows=[["Lait entier 1 L", "240,00", "× 2"], ["Pain", "40,00", ""], ["Huile d'olive 750 ml", "950,00", ""], ["Sucre 1 kg", "115,00", ""]],
                 after=[["Espèces", "1.500,00"], ["Rendu", "155,00"]], note="", thanks="Merci de votre visite"),
            dict(shop="Alimentation El Amel", meta="13/11/2026 13:05 · 000131", totalLabel="Total", total="1.570,00",
                 rows=[["Semoule 10 kg", "1.150,00", ""], ["Café 250 g", "420,00", ""]],
                 after=[["Solde client après la vente", "4.320,00"]], note="À crédit : Karim Benali", thanks="Merci de votre visite"),
            dict(shop="Alimentation El Amel", meta="13/11/2026 17:20 · 000139", totalLabel="Rendu en espèces", total="950,00",
                 rows=[["Retour : huile d'olive 750 ml", "-950,00", ""]],
                 after=[], note="Article remis en stock", ok=True, thanks="Ticket d'origine 000128"),
        ],
    ),
    "en": dict(
        brand="Tajer", kicker="Point of sale for shops",
        h1=("Your whole shop in ", "one program", "."),
        cta1="Download for Windows", cta2="For Android phones",
        facts=["Works offline", "6 languages", "Version @V"],
        again="Print another receipt", videos="Videos (Arabic)", dlnav="Download",
        strip=["Barcode sales", "Credit book", "Stock with expiry", "Purchases", "Reports", "Backups", "Several tills", "Phone as scanner"],
        day_h="A day in the shop", day_p="From opening the door to closing the till, Tajer is with you at every step.",
        day=[
            ("08:00", "Open the shift", "Count the cash in the drawer and type the amount. The program keeps count all day."),
            ("09:30", "The goods arrive", "Receive the delivery from the supplier's PDF or Excel invoice, with quantities and expiry dates."),
            ("11:00", "Rush at the till", "Scan the barcode and the price shows. Everything on the keyboard, the receipt prints at once."),
            ("13:00", "A customer buys on credit", "Pick the customer and the amount goes into their book. Each has a limit and a printed statement."),
            ("17:00", "A customer returns an item", "Find the receipt and pick the item. Stock and drawer correct themselves."),
            ("20:00", "Close the day", "The day report in one press: sales, credit, cash in the drawer. Then a backup."),
        ],
        show_h="A clear screen, no manual needed", show_p="Big buttons, plain words, everything on the keyboard.",
        tabs=[("Till", "desktop-checkout-fr.png"), ("Home", "desktop-home-fr.png"), ("Reports", "desktop-reports-fr.png")],
        say=("Your data stays in your shop. ", "No cloud, no tracking."),
        keep_n="Privacy",
        stats=[("0", "internet needed"), ("6", "languages"), ("58/80", "mm receipt printer"), ("5+", "Android on the phone")],
        dl_p="Pick your device. The file downloads directly.", get="Download",
        rc=[
            dict(shop="El Amel Grocery", meta="13/11/2026 10:42 · 000128", totalLabel="Total", total="1.345,00",
                 rows=[["Whole milk 1 L", "240,00", "× 2"], ["Bread", "40,00", ""], ["Olive oil 750 ml", "950,00", ""], ["Sugar 1 kg", "115,00", ""]],
                 after=[["Cash", "1.500,00"], ["Change", "155,00"]], note="", thanks="Thank you for your visit"),
            dict(shop="El Amel Grocery", meta="13/11/2026 13:05 · 000131", totalLabel="Total", total="1.570,00",
                 rows=[["Semolina 10 kg", "1.150,00", ""], ["Coffee 250 g", "420,00", ""]],
                 after=[["Customer balance after the sale", "4.320,00"]], note="On credit: Karim Benali", thanks="Thank you for your visit"),
            dict(shop="El Amel Grocery", meta="13/11/2026 17:20 · 000139", totalLabel="Cash given back", total="950,00",
                 rows=[["Return: olive oil 750 ml", "-950,00", ""]],
                 after=[], note="Item put back in stock", ok=True, thanks="Original receipt 000128"),
        ],
    ),
}


def render(k, t, bl, c):
    """k: language key; t: T[k] of build.py; bl: BL[k]; c: dict of build constants."""
    n = N[k]
    root = "" if k == "ar" else "../"
    img = root + "assets/img/"
    ver = c["version"]

    def head(no, title, sub=""):
        p = f"<p>{sub}</p>" if sub else ""
        return f'<div class="sec-h rv"><span class="sec-n num">{no:02d}</span><h2>{title}</h2>{p}</div>'

    def ticket(key, name, note, main=False):
        f, size = c["files"][key]
        h = c["sums"].get(f)
        href = (c["release_url"] if f.endswith(".exe") else root + "downloads/") + f
        sha = (f'<div class="sha">SHA256 <code>{h[:16]}</code><button type="button" class="cp" data-h="{h}">{c["cp"]}</button></div>') if h else ""
        return (f'<div class="tk{" main" if main else ""} rv"><a class="hit" href="{href}" download><span class="hole"></span>'
                f'<span class="name">{t[name]}</span><span class="note">{t[note]}</span>'
                f'<span class="get"><small>{f} · {size}</small><span class="arrow" aria-hidden="true">&#8595;</span></span></a>{sha}</div>')

    beta = ""
    if c["beta_version"]:
        h1, h2, n64, _ = c["beta_txt"][k]
        f, size = c["beta_files"]["win64"]
        beta = (f'<div class="beta rv" id="beta"><div><h3>{h1 % ('<span class="num">' + c["beta_version"] + '</span>')}</h3><p>{h2}</p></div>'
                f'<a class="btn" href="{c["beta_url"] + f}" download>{n64} <small class="num">{size}</small></a></div>')

    facts = "".join(f'<span><i class="nq"></i>{x.replace("@V", ver)}</span>' for x in n["facts"])
    strip = "".join(f"<span>{x}</span>" for x in n["strip"])
    day = "".join(f'<li class="rv"><time class="num">{a}</time><h3>{b}</h3><p>{d}</p></li>' for a, b, d in n["day"])
    tabs = "".join(f'<button type="button" class="tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-src="{img}{s}">{lab}</button>'
                   for i, (lab, s) in enumerate(n["tabs"]))
    feats = "".join(
        f'<li class="rv"><div class="top"><span class="n num">{i:02d}</span><span class="ic" style="-webkit-mask-image:url({img}icons/{ICONS[i - 1]}.svg);mask-image:url({img}icons/{ICONS[i - 1]}.svg)"></span></div>'
        f"<h3>{h}</h3><p>{p}</p></li>" for i, (h, p) in enumerate(t["f"], 1))
    stats = "".join(f'<li class="rv"><b class="num">{a}</b><span>{b}</span></li>' for a, b in n["stats"])
    reqs = "".join(f"<li>{r}</li>" for r in t["reqs"])
    hows = "".join(f"<li><span>{r}</span></li>" for r in t["hows"])
    l1, l2 = c["links"]
    rc = json.dumps(n["rc"], ensure_ascii=False).replace("</", "<\\/")

    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['tag']}">
<meta name="theme-color" content="#F5F2EA">
<link rel="icon" href="{img}tajer-tile-32.png">
<link rel="stylesheet" href="{root}assets/home.css">
</head>
<body>
<header class="bar"><div class="wrap bar-in">
  <a class="brand" href="{root}"><img src="{img}tajer-tile.svg" alt="" width="40" height="40"><span>{n['brand']}</span></a>
  <nav>
    <a class="opt" href="{c['vid_link']}">{n['videos']}</a>
    <a class="opt" href="blocked/">{bl['nav']}</a>
    <a class="lang" href="{l1}">{t['other']}</a>
    <a class="lang" href="{l2}">{t['other2']}</a>
    <a class="btn go" href="#download">{n['dlnav']}</a>
  </nav>
</div></header>
<main>
<section class="hero"><div class="wrap hero-in">
  <div>
    <span class="kicker"><i class="nq"></i>{n['kicker']}</span>
    <div class="h1box"><h1>{n['h1'][0]}<span class="mk">{n['h1'][1]}</span>{n['h1'][2]}</h1></div>
    <p class="lead">{t['lead']}</p>
    <div class="cta"><a class="btn go" href="#download">{n['cta1']}</a><a class="btn" href="#download">{n['cta2']}</a></div>
    <div class="facts">{facts}</div>
  </div>
  <div class="printer" aria-hidden="true">
    <div class="slot"></div>
    <div class="paper" id="paper" data-mark="{img}tajer-mark.svg"></div>
    <button type="button" class="btn again" id="again" tabindex="-1">{n['again']}</button>
  </div>
</div></section>
<div class="strip" aria-hidden="true"><div class="strip-in">{strip}{strip}</div></div>

<section class="sec"><div class="wrap">
  {head(1, n['day_h'], n['day_p'])}
  <ol class="day">{day}</ol>
</div></section>

<section class="sec show"><div class="wrap">
  {head(2, n['show_h'], n['show_p'])}
  <div class="tabs" role="tablist">{tabs}</div>
  <div class="stage rv">
    <div class="screen"><div class="screen-top"><i></i><i></i></div><img id="shot" src="{img}{n['tabs'][0][1]}" alt="" width="2049" height="1152"></div>
    <img class="phone" src="{img}android-checkout-api34.png" alt="" loading="lazy" width="1080" height="2340">
  </div>
</div></section>

<section class="sec"><div class="wrap">
  {head(3, t['feat'])}
  <ul class="feats">{feats}</ul>
</div></section>

<section class="sec keep on-ink"><div class="wrap">
  <div class="sec-h rv"><span class="sec-n num">04</span><h2 class="say">{n['say'][0]}<em>{n['say'][1]}</em></h2></div>
  <ul class="stats">{stats}</ul>
</div></section>

<section class="sec" id="download"><div class="wrap">
  {head(5, t['dl'] + ' <small class="num">v' + ver + '</small>', n['dl_p'])}
  <div class="tix">{ticket('win64', 'win64', 'win64n', True)}{ticket('win32', 'win32', 'win32n')}{ticket('apk', 'apk', 'apkn')}</div>
  {beta}
  <p class="help-link"><a href="blocked/">{bl['nav']}</a></p>
  <div class="two">
    <div class="rv"><h3>{t['req']}</h3><ul class="reqs">{reqs}</ul></div>
    <div class="rv"><h3>{t['how']}</h3><ol class="steps">{hows}</ol></div>
  </div>
</div></section>

<section class="wrap legal"><p>{t['legaltxt']}</p>
<p><a href="{root}legal/SOURCE_OFFER.txt">{t['l1']}</a><a href="{root}legal/LICENSE-MRPL.txt">{t['l2']}</a><a href="{root}legal/THIRD_PARTY_LICENSES.md">{t['l3']}</a></p></section>
</main>
<footer class="foot"><div class="wrap foot-in"><div class="giant" aria-hidden="true">{n['brand']}</div><small>Tajer · تاجر — <span class="num">v{ver}</span></small></div></footer>
<script type="application/json" id="rc">{rc}</script>
<script src="{root}assets/home.js"></script>
</body>
</html>
"""
