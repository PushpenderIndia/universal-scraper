// ── Bootstrap ─────────────────────────────────────────────────────────────
async function init() {
  renderUrlList([""]);         // empty URL row to start

  try {
    const res = await fetch("/api/providers");
    providers = await res.json();
    buildProviderSelect();
    await onProviderChange();
    DEFAULT_FIELDS.forEach(addField);
  } catch (e) {
    addLogLine("ERROR", "Failed to load config: " + e);
  }

  initSidebar();
}

document.addEventListener("DOMContentLoaded", init);
