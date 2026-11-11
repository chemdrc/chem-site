(function () {
  var EN = (document.documentElement.lang || "").indexOf("en") === 0;
  var btn = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#nav");
  if (!btn || !nav) return;

  function setOpen(open) {
    nav.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.setAttribute("aria-label", open ? (EN ? "Close menu" : "Fermer le menu") : (EN ? "Open menu" : "Ouvrir le menu"));
  }

  btn.addEventListener("click", function () {
    setOpen(!nav.classList.contains("is-open"));
  });

  nav.addEventListener("click", function (event) {
    if (event.target.closest("a")) {
      window.setTimeout(function () { setOpen(false); }, 0);
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") setOpen(false);
  });

  document.addEventListener("click", function (event) {
    if (!nav.classList.contains("is-open")) return;
    if (nav.contains(event.target) || btn.contains(event.target)) return;
    setOpen(false);
  });
})();
