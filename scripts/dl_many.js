// usage: node dl_many.js <plan.json> <outdir>
// plan.json: [{"id": "<experiment guid>", "labels": ["CRF_CFT70_VITALS", ...]}]
const fs = require('fs');
const { chromium } = require('playwright');
(async () => {
  const plan = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const outdir = process.argv[3];
  const b = await chromium.launch();
  const ctx = await b.newContext({ acceptDownloads: true });
  const p = await ctx.newPage();
  for (const item of plan) {
    await p.goto(`https://nlsp.nasa.gov/explore/data/details/${item.id}?dataType=EXPERIMENTS`, { waitUntil: 'networkidle', timeout: 60000 });
    await p.waitForTimeout(1500);
    for (const label of item.labels) {
      const btn = await p.$(`button[aria-label*="(${label})"]`);
      if (!btn) { console.log('NOT FOUND', label); continue; }
      try {
        await btn.scrollIntoViewIfNeeded();
        const [dl] = await Promise.all([p.waitForEvent('download', { timeout: 60000 }), btn.click()]);
        const dest = `${outdir}/${label}.zip`;
        await dl.saveAs(dest);
        console.log('OK', label, fs.statSync(dest).size, 'bytes');
      } catch (e) { console.log('FAIL', label, e.message.slice(0, 120)); }
      await p.waitForTimeout(2000);
    }
  }
  await b.close();
})();
