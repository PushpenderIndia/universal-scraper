// ── Token usage bar + modal ────────────────────────────────────────────────

function updateTokenUsage(usage) {
  if (!usage) return;
  lastTokenUsage = usage;

  document.getElementById("token-bar").classList.add("visible");
  document.getElementById("token-total").textContent = fmt(usage.total_tokens);
  document.getElementById("token-in").textContent    = fmt(usage.total_prompt_tokens);
  document.getElementById("token-out").textContent   = fmt(usage.total_completion_tokens);

  const cacheEl = document.getElementById("token-cache");
  if (usage.cache_hits > 0) {
    cacheEl.style.display = "inline-block";
    cacheEl.textContent   = `${usage.cache_hits} cache hit${usage.cache_hits > 1 ? "s" : ""}`;
  } else {
    cacheEl.style.display = "none";
  }
}

function openTokenModal() {
  if (!lastTokenUsage) return;
  document.getElementById("token-modal-body").innerHTML = _buildModalBody(lastTokenUsage);
  document.getElementById("token-modal").classList.add("open");
}

function closeTokenModal() {
  document.getElementById("token-modal").classList.remove("open");
}

function onModalOverlayClick(e) {
  if (e.target === document.getElementById("token-modal")) closeTokenModal();
}

function _buildModalBody(u) {
  const statCards = [
    { label: "Total Tokens",      value: fmt(u.total_tokens),            accent: true },
    { label: "Prompt Tokens",     value: fmt(u.total_prompt_tokens),     accent: false },
    { label: "Completion Tokens", value: fmt(u.total_completion_tokens), accent: false },
    { label: "API Calls",         value: u.api_calls,                    accent: false },
  ].map(({ label, value, accent }) =>
    `<div class="stat-card">
       <div class="stat-label">${label}</div>
       <div class="stat-value${accent ? " accent" : ""}">${value}</div>
     </div>`
  ).join("");

  const calls = (u.calls || []).map((c, i) => {
    const cached = c.from_cache;
    const rows = cached ? "" : [
      ["Prompt",     fmt(c.prompt_tokens)     + " tokens"],
      ["Completion", fmt(c.completion_tokens) + " tokens"],
      ["Total",      fmt(c.total_tokens)      + " tokens"],
    ].map(([k, v]) =>
      `<div class="call-row"><span>${k}</span><span>${v}</span></div>`
    ).join("");

    return `<div class="call-card">
      <div class="call-header">
        <span class="call-num">Call #${i + 1}</span>
        <span class="call-model">${escHtml(c.model)}</span>
        <span class="call-badge ${cached ? "badge-cache" : "badge-api"}">${cached ? "Cache" : "API"}</span>
      </div>
      ${cached
        ? `<div class="call-row" style="color:var(--accent)"><span>Served from local cache — no tokens used</span></div>`
        : rows}
    </div>`;
  }).join("");

  return `
    <div class="stat-grid">${statCards}</div>
    ${u.cache_hits > 0
      ? `<p style="font-size:12px;color:var(--accent);margin-bottom:14px">
           ✓ ${u.cache_hits} request${u.cache_hits > 1 ? "s were" : " was"} served from cache.
         </p>`
      : ""}
    <div class="section-title">Call Details</div>
    ${calls || '<p style="color:var(--text3);font-size:13px">No calls recorded.</p>'}
  `;
}
