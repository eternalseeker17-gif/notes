style.css
@page { size: A4; margin: 11mm 11mm 13mm 11mm; }
:root{
  --ink:#1c2430; --muted:#5b6675; --navy:#1f3a5f; --navy-soft:#e8eef6;
  --red:#b83227; --red-bg:#fdeeec; --amber:#a86b00; --amber-bg:#fff6df;
  --green:#23724a; --green-bg:#e9f6ee; --blue:#2458a6; --blue-bg:#eaf1fb;
  --gold:#c08a00; --line:#d5dbe3; --zebra:#f6f8fb;
}
*{box-sizing:border-box}
html{font-family:"Carlito","DejaVu Sans",sans-serif;font-size:10pt;color:var(--ink);line-height:1.32}
body{margin:0}
b,strong{font-weight:700;color:#0d1520}
h1{font-size:21pt;margin:0;color:var(--navy);letter-spacing:.3px}
.sub{color:var(--muted);font-size:9.5pt;margin:2px 0 8px}
h2{font-size:13pt;color:#fff;background:var(--navy);padding:3px 8px;margin:12px 0 6px;border-radius:3px;break-after:avoid}
h2 .n{opacity:.75;margin-right:6px}
h3{font-size:11pt;color:var(--navy);border-bottom:1.5px solid var(--navy);padding-bottom:1px;margin:9px 0 5px;break-after:avoid}
p{margin:3px 0}
ul{margin:3px 0 3px 0;padding-left:15px}
li{margin:1.5px 0}
li::marker{color:var(--navy)}
.small{font-size:8.8pt;color:var(--muted)}
.ptr{font-style:italic;color:var(--muted);border-left:3px solid var(--line);padding:2px 8px;margin:4px 0}
/* tables */
table{border-collapse:collapse;width:100%;margin:4px 0 6px;font-size:9.4pt;break-inside:auto}
tr{break-inside:avoid}
th{background:var(--navy-soft);color:var(--navy);text-align:left;padding:3px 5px;border:1px solid var(--line);font-weight:700}
td{padding:2.5px 5px;border:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even) td{background:var(--zebra)}
td.k{white-space:nowrap;font-weight:700;color:var(--navy)}
/* boxes */
.box{border:1px solid;border-left-width:4px;border-radius:3px;padding:4px 8px 4px 8px;margin:5px 0;break-inside:avoid}
.box .lab{display:inline-block;font-size:7.6pt;font-weight:700;letter-spacing:.6px;padding:0 5px;border-radius:2px;color:#fff;margin-right:6px;vertical-align:1px}
.trap{border-color:var(--red);background:var(--red-bg)} .trap .lab{background:var(--red)}
.doubt{border-color:var(--amber);background:var(--amber-bg)} .doubt .lab{background:var(--amber)}
.hook{border-color:var(--green);background:var(--green-bg)} .hook .lab{background:var(--green)}
.miss{border-color:var(--blue);background:var(--blue-bg)} .miss .lab{background:var(--blue)}
.x{color:var(--red);font-weight:700} .ok{color:var(--green);font-weight:700}
.star{color:var(--gold);font-weight:700}
/* front */
.front{display:grid;grid-template-columns:1.55fr 1fr;gap:8px;margin:6px 0 4px}
.lastmin{border:2px solid var(--navy);border-radius:4px;padding:5px 9px;background:#fbfcfe}
.lastmin h4{margin:0 0 3px;color:var(--navy);font-size:10.5pt}
.lastmin ol{margin:0;padding-left:16px} .lastmin li{margin:1.5px 0}
.legend{border:1px solid var(--line);border-radius:4px;padding:5px 8px;font-size:8.7pt;background:#fafbfc}
.legend h4{margin:0 0 3px;font-size:9.5pt;color:var(--navy)}
.legend .row{margin:2px 0}
.chip{display:inline-block;font-size:7.4pt;font-weight:700;padding:0 4px;border-radius:2px;color:#fff;margin-right:4px}
/* timeline */
.tl{border-left:2.5px solid var(--navy);margin:4px 0 6px 80px;padding-left:0}
.tl .e{position:relative;padding:1.5px 0 1.5px 11px;break-inside:avoid}
.tl .e:before{content:"";position:absolute;left:-6px;top:6px;width:8px;height:8px;border-radius:50%;background:#fff;border:2px solid var(--navy)}
.tl .e.hot:before{background:var(--red);border-color:var(--red)}
.tl .d{position:absolute;left:-86px;width:76px;white-space:nowrap;text-align:right;font-weight:700;color:var(--navy);font-size:9pt;top:1.5px}
.tl .e.hot .d{color:var(--red)}
/* key-date strip */
.strip{display:flex;gap:0;margin:5px 0;break-inside:avoid}
.strip div{flex:1;text-align:center;border:1px solid var(--line);padding:3px 2px;background:#fff}
.strip div b{display:block;font-size:11pt;color:var(--navy)}
.strip div.hot{background:var(--red-bg);border-color:var(--red)} .strip div.hot b{color:var(--red)}
/* cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin:5px 0}
.card{border:1px solid var(--line);border-top:3px solid var(--navy);border-radius:3px;padding:3px 6px;break-inside:avoid;background:#fff}
.card .c{font-weight:700;color:var(--navy);font-size:10pt}
.card .h{font-size:8.3pt;color:var(--green);font-style:italic;margin-top:1px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.ladder{display:flex;align-items:stretch;gap:4px;margin:4px 0;break-inside:avoid}
.ladder div{flex:1;border:1px solid var(--line);border-radius:3px;padding:3px 5px;text-align:center;background:#fff}
.ladder div b{display:block;font-size:15pt;color:var(--navy)}
.ladder .arr{flex:0 0 14px;border:none;background:none;align-self:center;color:var(--navy);font-weight:700;padding:0}
.appx{margin-top:10px;border-top:3px double var(--navy);padding-top:4px}
.appx h2{background:#5b6675}
.section{break-inside:auto}
td.a{white-space:nowrap;font-weight:700;color:var(--navy);width:1%;text-align:right}
.cols2{column-count:2;column-gap:10px}
.cols2 table{break-inside:auto}
.tl.wide{margin-left:118px}
.tl.wide .d{left:-124px;width:114px}
