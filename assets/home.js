/* Tajer home page: the receipt printer, screen tabs, copy buttons, reveal on scroll. No network, no tracking. */
(function () {
  "use strict";
  var still = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // receipt printer
  var paper = document.getElementById("paper");
  var data = document.getElementById("rc");
  var again = document.getElementById("again");
  var sales = data ? JSON.parse(data.textContent) : [];
  var at = 0, timers = [];

  function el(cls, html) {
    var ln = document.createElement("div");
    ln.className = "ln";
    var inner = document.createElement("div");
    var box = document.createElement("div");
    box.className = cls;
    box.innerHTML = html;
    inner.appendChild(box);
    ln.appendChild(inner);
    return ln;
  }
  function num(s) { return '<b class="num">' + s + "</b>"; }

  function build(s) {
    var out = [];
    out.push(el("r-head", '<img src="' + paper.dataset.mark + '" alt=""><div class="r-shop">' + s.shop + '</div><div class="r-meta"><span class="num">' + s.meta + "</span></div>"));
    out.push(el("r-rule", ""));
    s.rows.forEach(function (r) {
      out.push(el("r-row", "<span>" + r[0] + (r[2] ? " <small>" + r[2] + "</small>" : "") + "</span>" + num(r[1])));
    });
    out.push(el("r-rule", ""));
    out.push(el("r-total", "<span>" + s.totalLabel + "</span>" + num(s.total)));
    (s.after || []).forEach(function (r) { out.push(el("r-row", "<span>" + r[0] + "</span>" + num(r[1]))); });
    if (s.note) { out.push(el("r-note" + (s.ok ? " ok" : ""), s.note)); }
    out.push(el("r-code", ""));
    out.push(el("r-thanks", s.thanks));
    return out;
  }

  function print() {
    if (!paper || !sales.length) { return; }
    timers.forEach(clearTimeout);
    timers = [];
    paper.innerHTML = "";
    var lines = build(sales[at % sales.length]);
    at++;
    lines.forEach(function (ln, i) {
      paper.appendChild(ln);
      if (still) { ln.classList.add("on"); return; }
      timers.push(setTimeout(function () { ln.classList.add("on"); }, 250 + i * 170));
    });
  }
  if (again) { again.addEventListener("click", print); }
  print();

  // screen tabs
  var tabs = document.querySelectorAll(".tab");
  var shot = document.getElementById("shot");
  Array.prototype.forEach.call(tabs, function (t) {
    t.addEventListener("click", function () {
      Array.prototype.forEach.call(tabs, function (o) { o.setAttribute("aria-selected", o === t ? "true" : "false"); });
      shot.src = t.dataset.src;
    });
  });

  // copy the full SHA256
  document.addEventListener("click", function (e) {
    var b = e.target.closest ? e.target.closest(".cp") : null;
    if (!b) { return; }
    var h = b.dataset.h, o = b.textContent;
    function ok() { b.textContent = "OK"; setTimeout(function () { b.textContent = o; }, 1500); }
    if (navigator.clipboard) { navigator.clipboard.writeText(h).then(ok, function () { prompt("SHA256", h); }); } else { prompt("SHA256", h); }
  });

  // reveal on scroll
  var rv = document.querySelectorAll(".rv");
  if (still || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(rv, function (n) { n.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    Array.prototype.forEach.call(rv, function (n) { io.observe(n); });
  }
})();
