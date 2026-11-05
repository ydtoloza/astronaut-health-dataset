// usage: node list_ds.js <id1,id2,...>  -> prints JSON lines {exp, datasets:[{label, info}]}
const { chromium } = require('playwright');
(async () => {
  const ids = process.argv[2].split(',');
  const b = await chromium.launch();
  const p = await b.newPage();
  for (const id of ids) {
    const url = `https://nlsp.nasa.gov/explore/data/details/${id}?dataType=EXPERIMENTS`;
    try {
      await p.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
      await p.waitForTimeout(1500);
      const t = await p.evaluate(() => document.body.innerText);
      const j = t.lastIndexOf('Open-Access Data');
      const k = t.indexOf('\nAgencies', j);
      const block = t.slice(j, k > 0 ? k : j + 4000);
      const labels = await p.$$eval('#datasets button[aria-label^="Download "]', bs => bs.map(x => x.getAttribute('aria-label')).filter(l => l !== 'Download all'));
      console.log(JSON.stringify({ id, labels, block: block.replace(/\n+/g, ' | ').slice(0, 2500) }));
    } catch (e) { console.log(JSON.stringify({ id, error: e.message.slice(0, 150) })); }
    await p.waitForTimeout(2000);
  }
  await b.close();
})();
