// ---------- Twinkling bulbs on the hero house ----------
(function drawBulbs() {
  const NS = "http://www.w3.org/2000/svg";
  const colors = ["#ffc65c", "#ff5a6e", "#4fd18b", "#6cb6ff", "#ffc65c"];

  function bulb(group, x, y, i) {
    const c = document.createElementNS(NS, "circle");
    c.setAttribute("cx", x.toFixed(1));
    c.setAttribute("cy", y.toFixed(1));
    c.setAttribute("r", "4.2");
    const color = colors[i % colors.length];
    c.setAttribute("fill", color);
    c.setAttribute("class", "bulb");
    c.style.filter = `drop-shadow(0 0 5px ${color})`;
    c.style.animationDelay = `${(i * 0.37) % 2.4}s`;
    group.appendChild(c);
  }

  function line(group, x1, y1, x2, y2, count, offset = 0) {
    const wire = document.createElementNS(NS, "line");
    Object.entries({ x1, y1, x2, y2 }).forEach(([k, v]) => wire.setAttribute(k, v));
    wire.setAttribute("stroke", "#2b3a52");
    wire.setAttribute("stroke-width", "1.5");
    group.appendChild(wire);
    for (let i = 0; i <= count; i++) {
      const t = i / count;
      bulb(group, x1 + (x2 - x1) * t, y1 + (y2 - y1) * t + 3, i + offset);
    }
  }

  const roof = document.querySelector(".bulbs.roofline");
  const eaves = document.querySelector(".bulbs.eaves");
  const shrubs = document.querySelector(".bulbs.shrubs");
  if (!roof) return;

  line(roof, 50, 165, 210, 55, 14);
  line(roof, 210, 55, 370, 165, 14, 3);
  line(eaves, 70, 168, 350, 168, 20, 1);

  // shrub sparkles
  [[95, 312], [325, 312]].forEach(([cx, cy], s) => {
    for (let i = 0; i < 9; i++) {
      const a = (i / 9) * Math.PI * 2;
      bulb(shrubs, cx + Math.cos(a) * 22, cy + Math.sin(a) * 10 - 2, i + s * 2);
    }
  });
})();

// ---------- Price estimator ----------
(function estimator() {
  const MINIMUM = 150, MAX_COUNT = 20;
  const form = document.getElementById("estimator");
  if (!form) return;
  const total = document.getElementById("calc-total");
  const label = document.getElementById("calc-label");
  const custom = document.getElementById("calc-custom");
  const garage = document.getElementById("garage");
  const counters = [...form.querySelectorAll(".stepper output")];
  const fmt = n => "$" + n.toLocaleString("en-CA");

  // Returns { house, isCustom, price, lines } describing the current selection.
  function read() {
    const house = form.querySelector('input[name="house"]:checked');
    const isCustom = +house.dataset.price === 0;
    let price = +house.dataset.price;
    const lines = [house.value];
    if (garage.checked) { price += +garage.dataset.price; lines.push("Attached garage roofline"); }
    counters.forEach(o => {
      const n = +o.value;
      if (n > 0) { price += n * +o.dataset.price; lines.push(n + " x " + o.dataset.name.toLowerCase()); }
    });
    return { isCustom, price: Math.max(MINIMUM, price), lines };
  }

  function update() {
    const r = read();
    label.textContent = r.isCustom ? "Two-storey home:" : "Your estimate:";
    total.textContent = r.isCustom ? "Send a photo for a custom quote" : fmt(r.price);
    total.classList.toggle("is-custom", r.isCustom);
    custom.hidden = !r.isCustom;
    counters.forEach(o => {
      form.querySelector(`[data-target="${o.id}"][data-step="-1"]`).disabled = +o.value <= 0;
      form.querySelector(`[data-target="${o.id}"][data-step="1"]`).disabled = +o.value >= MAX_COUNT;
    });
  }

  counters.forEach(o => (o.value = "0"));
  form.addEventListener("change", update);
  form.addEventListener("click", e => {
    const btn = e.target.closest(".step-btn");
    if (!btn) return;
    const out = document.getElementById(btn.dataset.target);
    out.value = String(Math.min(MAX_COUNT, Math.max(0, +out.value + +btn.dataset.step)));
    update();
  });

  // "Book this" -> copy the selection into the quote form and jump there.
  document.getElementById("book-btn").addEventListener("click", () => {
    const r = read();
    const summary = r.lines.join(", ") + (r.isCustom ? " (custom quote needed)" : " - estimate " + fmt(r.price));
    document.getElementById("estimate").value = summary;
    document.getElementById("quote").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
    document.getElementById("name").focus({ preventScroll: true });
  });

  update();
})();

// ---------- Quote form -> pre-filled text message ----------
(function quoteForm() {
  const form = document.getElementById("quote-form");
  if (!form) return;
  const status = document.getElementById("form-status");
  const success = document.getElementById("form-success");
  const copyBtn = document.getElementById("copy-msg");
  const required = [form.name, form.address];
  let lastMsg = "";

  function check(input) {
    const ok = input.value.trim() !== "";
    const err = document.getElementById(input.id + "-err");
    input.setAttribute("aria-invalid", ok ? "false" : "true");
    err.hidden = ok;
    return ok;
  }
  // Validate when the person leaves a field, and clear the error as soon as they fix it.
  required.forEach(input => {
    input.addEventListener("blur", () => { if (input.value || input.hasAttribute("aria-invalid")) check(input); });
    input.addEventListener("input", () => { if (input.getAttribute("aria-invalid") === "true") check(input); });
  });

  form.addEventListener("submit", e => {
    e.preventDefault();
    const invalid = required.filter(i => !check(i));
    if (invalid.length) {
      status.textContent = "Please fix " + invalid.length + (invalid.length > 1 ? " fields" : " field") + " before sending.";
      invalid[0].focus();
      return;
    }
    status.textContent = "";
    const estimate = form.estimate.value.trim();
    const notes = form.notes.value.trim();
    lastMsg =
      "Hi Karan, I'd like to book Christmas light hanging.\n" +
      "Name: " + form.name.value.trim() + "\n" +
      "Address: " + form.address.value.trim() + ", " + form.area.value + "\n" +
      (estimate ? "House: " + estimate + "\n" : "") +
      "Lights: " + form.lights.value + "\n" +
      (form.sameday.checked ? "Same-day appointment if possible\n" : "") +
      (notes ? "Notes: " + notes + "\n" : "") +
      "I'll send a photo of my house next.";
    const sep = /iPhone|iPad|iPod|Macintosh/.test(navigator.userAgent) ? "&" : "?";
    success.hidden = false;
    success.focus({ preventScroll: true });
    success.scrollIntoView({ block: "nearest" });
    window.location.href = "sms:+15067992790" + sep + "body=" + encodeURIComponent(lastMsg);
  });

  copyBtn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(lastMsg);
      copyBtn.textContent = "Copied!";
    } catch {
      copyBtn.textContent = "Copy failed. Please call instead.";
    }
    setTimeout(() => (copyBtn.textContent = "Copy my request"), 3000);
  });
})();

// ---------- Mobile menu ----------
(function menu() {
  const btn = document.querySelector(".menu-btn");
  const panel = document.getElementById("mobile-menu");
  if (!btn) return;
  const set = open => {
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    panel.hidden = !open;
  };
  btn.addEventListener("click", () => set(panel.hidden));
  panel.addEventListener("click", e => { if (e.target.closest("a")) set(false); });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && !panel.hidden) { set(false); btn.focus(); }
  });
})();

document.getElementById("year").textContent = new Date().getFullYear();
