import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SAATHI | Liquid Glass Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [data-testid="stAppViewContainer"] {
  background: #080d18;
  color: #f4f7ff;
  font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif;
}
[data-testid="stHeader"], [data-testid="stToolbar"], footer {visibility:hidden}
.block-container {padding:0!important;max-width:100%!important}
iframe {border:0!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{box-sizing:border-box}
:root{
 --ink:#f6f7fb;--muted:#a9b2c6;--subtle:#77839c;
 --glass:rgba(255,255,255,.075);--glass2:rgba(255,255,255,.11);
 --stroke:rgba(255,255,255,.15);--cyan:#82eaff;--blue:#82aaff;
 --mint:#a5f4dc;--pink:#f1b8e2;--shadow:0 18px 60px rgba(0,0,0,.32);
}
body{margin:0;color:var(--ink);font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
 background:#080d18}
button{font:inherit}
.shell{position:relative;isolation:isolate;overflow:hidden;min-height:1180px;padding:25px clamp(15px,3vw,42px) 36px;
 background:
 radial-gradient(ellipse at 8% 8%,rgba(103,170,255,.23),transparent 31%),
 radial-gradient(ellipse at 90% 12%,rgba(191,132,255,.17),transparent 28%),
 radial-gradient(ellipse at 53% 83%,rgba(65,210,220,.13),transparent 35%),
 linear-gradient(145deg,#0b1322,#101a2b 48%,#0a1220)}
.shell:before,.shell:after{content:"";position:absolute;z-index:-1;border-radius:50%;filter:blur(2px);pointer-events:none}
.shell:before{width:370px;height:370px;left:-210px;top:450px;background:rgba(80,178,255,.13);filter:blur(75px)}
.shell:after{width:420px;height:420px;right:-240px;top:620px;background:rgba(204,139,255,.13);filter:blur(90px)}
.glass{background:linear-gradient(135deg,rgba(255,255,255,.13),rgba(255,255,255,.045));
 border:1px solid var(--stroke);box-shadow:var(--shadow),inset 0 1px 0 rgba(255,255,255,.17);
 backdrop-filter:blur(26px) saturate(155%);-webkit-backdrop-filter:blur(26px) saturate(155%);
 border-radius:24px}
.header{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:15px 19px;margin-bottom:24px}
.brand{display:flex;align-items:center;gap:13px}.logo{width:42px;height:42px;border-radius:15px;
 display:grid;place-items:center;font-size:21px;color:#fff;background:linear-gradient(145deg,rgba(119,224,255,.42),rgba(130,145,255,.2));
 border:1px solid rgba(255,255,255,.3);box-shadow:inset 0 1px 10px #fff3,0 5px 25px #68dfff24}
.brand strong{font-size:15px;letter-spacing:.16em}.brand small{display:block;color:var(--muted);font-size:9px;letter-spacing:.16em;margin-top:4px}
.live{font-size:10px;letter-spacing:.12em;color:#a5f4dc;padding:9px 13px;border:1px solid #a5f4dc35;border-radius:99px;background:#a5f4dc0d}
.live i{display:inline-block;width:6px;height:6px;border-radius:50%;background:#8df1cb;box-shadow:0 0 12px #8df1cb;margin-right:7px}
.hero{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin:24px 5px 25px}
.kicker{font-size:10px;letter-spacing:.2em;color:#9ceaff;text-transform:uppercase;font-weight:700}
.hero h1{font-size:clamp(34px,5vw,58px);letter-spacing:-.055em;line-height:.99;margin:12px 0}
.hero h1 span{background:linear-gradient(100deg,#9aefff,#b5c4ff 55%,#f0b9e8);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{color:#b4bfd2;max-width:680px;font-size:13px;line-height:1.7;margin:0}
.hero-meta{text-align:right;color:#8d9bb2;font-size:10px;letter-spacing:.12em;line-height:1.8}
.nav{display:flex;gap:7px;padding:6px;width:max-content;max-width:100%;margin-bottom:23px;border-radius:17px}
.nav button{border:0;border-radius:12px;padding:11px 17px;color:#aeb9cc;background:transparent;font-size:11px;font-weight:700;letter-spacing:.04em;cursor:pointer;transition:.25s}
.nav button.active{color:#fff;background:linear-gradient(130deg,rgba(255,255,255,.22),rgba(255,255,255,.09));box-shadow:inset 0 1px 0 #ffffff36,0 4px 16px #0002}
.page{display:none;animation:appear .35s ease}.page.active{display:block}
@keyframes appear{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.section-head{display:flex;justify-content:space-between;align-items:end;gap:12px;margin:8px 3px 15px}
.section-head h2{font-size:22px;letter-spacing:-.035em;margin:5px 0}
.section-head p{font-size:11px;color:var(--muted);margin:0}
.micro{font-size:9px;letter-spacing:.17em;color:#9ceaff;text-transform:uppercase;font-weight:700}
.parts-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.part-card{min-height:160px;padding:17px;cursor:pointer;position:relative;overflow:hidden;transition:.25s}
.part-card:before{content:"";position:absolute;width:120px;height:120px;right:-55px;top:-65px;border-radius:50%;background:var(--orb,rgba(130,234,255,.14));filter:blur(5px)}
.part-card:hover,.part-card.selected{transform:translateY(-4px);border-color:#b3efff75;background:linear-gradient(140deg,rgba(255,255,255,.17),rgba(255,255,255,.065))}
.part-num{font-size:9px;color:#9caac0;letter-spacing:.15em}
.part-icon{width:38px;height:38px;border-radius:13px;display:grid;place-items:center;font-size:20px;margin:13px 0 10px;
 background:linear-gradient(145deg,rgba(255,255,255,.18),rgba(255,255,255,.055));border:1px solid #ffffff20}
.part-card h3{font-size:12px;margin:0 0 6px;position:relative}
.part-card p{font-size:10px;line-height:1.5;color:#aab7ca;margin:0;position:relative}
.detail{margin-top:14px;padding:21px;display:grid;grid-template-columns:.8fr 2fr;gap:20px}
.detail h3{font-size:20px;letter-spacing:-.03em;margin:8px 0}
.detail p{font-size:12px;line-height:1.7;color:#b7c3d5;margin:8px 0}
.demo-box{min-height:116px;margin-top:12px;padding:12px;border-radius:17px;border:1px solid #b9edff25;background:radial-gradient(ellipse at 50% 40%,#70cfff1b,transparent 70%),#0713238a;position:relative;overflow:hidden}
.demo-head{display:flex;justify-content:space-between;align-items:center;font-size:8px;letter-spacing:.15em;color:#aeeeff;margin-bottom:8px}
.demo-head button{font-size:8px;padding:6px 9px;border-radius:9px;border:1px solid #b9edff35;color:#d9f7ff;background:#b9edff10;cursor:pointer}
.demo-stage{height:67px;display:flex;align-items:center;justify-content:center;gap:18px;position:relative;overflow:hidden}
.demo-object{width:43px;height:43px;border-radius:13px;display:grid;place-items:center;font-size:23px;color:#dffaff;border:1px solid #b9edff55;background:linear-gradient(145deg,#a5eaff30,#a5aaff12);box-shadow:0 0 25px #76dfff25;animation:demoPulse 1.8s ease-in-out infinite}
.demo-beam{height:2px;width:70px;background:linear-gradient(90deg,transparent,#8cecff,transparent);position:relative;animation:beamMove 1.4s linear infinite}
.demo-caption{font-size:9px;color:#aabbd0;text-align:center;margin-top:3px}
@keyframes demoPulse{0%,100%{transform:scale(.86);filter:brightness(.85);box-shadow:0 0 8px #76dfff18}50%{transform:scale(1.08);filter:brightness(1.4);box-shadow:0 0 25px #76dfff70}}
@keyframes beamMove{0%{opacity:.25;transform:scaleX(.35)}50%{opacity:1;transform:scaleX(1.2)}100%{opacity:.25;transform:scaleX(.35)}}
@keyframes demoFloat{0%,100%{transform:translateY(5px) rotate(-5deg)}50%{transform:translateY(-6px) rotate(5deg)}}
@keyframes demoSpin{to{transform:rotate(360deg)}}
.pill{display:inline-block;padding:7px 10px;border-radius:99px;border:1px solid #b9edff30;background:#b9edff0d;color:#c5f3ff;font-size:9px;letter-spacing:.06em}
.assembly-grid{display:grid;grid-template-columns:245px minmax(320px,1fr) 245px;gap:13px;align-items:stretch}
.side{padding:17px;min-width:0}
.side h3{font-size:12px;letter-spacing:.08em;margin:8px 0 14px}
.part-row{display:flex;align-items:center;justify-content:space-between;gap:7px;padding:9px 0;border-bottom:1px solid #ffffff13}
.part-row strong{font-size:10px;font-weight:600;display:block}
.part-row small{font-size:8px;color:#9aa9bf;display:block;margin-top:4px}
.add{width:29px;height:29px;flex:none;border-radius:10px;border:1px solid #c2efff3d;background:#b6eaff12;color:#d5f8ff;cursor:pointer}
.add:disabled{opacity:.36;cursor:default}
.stage-wrap{min-width:0}
.stage{height:560px;position:relative;overflow:hidden;border-radius:25px;
 background:radial-gradient(ellipse at 50% 48%,rgba(91,198,255,.14),transparent 54%),linear-gradient(150deg,rgba(255,255,255,.10),rgba(255,255,255,.025));
 border:1px solid #d7f6ff28;box-shadow:inset 0 1px 0 #ffffff22,0 20px 60px #0004}
.stage:before{content:"";position:absolute;inset:0;opacity:.45;background-image:linear-gradient(#a5eaff0c 1px,transparent 1px),linear-gradient(90deg,#a5eaff0c 1px,transparent 1px);background-size:32px 32px;mask-image:radial-gradient(ellipse,#000,transparent 80%)}
.stage-top{position:absolute;z-index:2;top:15px;left:17px;right:17px;display:flex;justify-content:space-between;pointer-events:none}
.stage-top span{font-size:9px;letter-spacing:.16em;color:#b7eaff}
#pendantCanvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none;cursor:grab}
#pendantCanvas:active{cursor:grabbing}
.stage-bottom{position:absolute;bottom:14px;left:16px;right:16px;display:flex;justify-content:space-between;pointer-events:none;color:#9db1c8;font-size:8px;letter-spacing:.12em}
.actions{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}
.action{padding:10px 12px;border-radius:12px;border:1px solid #ffffff24;color:#dbe9fa;background:linear-gradient(140deg,#ffffff18,#ffffff08);font-size:9px;letter-spacing:.06em;font-weight:700;cursor:pointer;transition:.2s}
.action:hover{background:#ffffff22;transform:translateY(-2px)}
.action.primary{background:linear-gradient(120deg,#5c9ef4aa,#a37ce8aa);border-color:#d9caff65;color:white;box-shadow:0 7px 24px #728bff25}
.meter{height:5px;background:#ffffff15;border-radius:9px;overflow:hidden;margin:13px 0 8px}
.meter i{height:100%;display:block;width:0;background:linear-gradient(90deg,#83e9ff,#b8c7ff,#e7b9ec);border-radius:9px;transition:width .35s}
.progress-label{font-size:8px;letter-spacing:.1em;color:#b4c5d9}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin:13px 0}
.stat{padding:11px;border-radius:14px;background:#ffffff0a;border:1px solid #ffffff13}
.stat b{font-size:19px;display:block;letter-spacing:-.04em}.stat small{font-size:8px;color:#9aaac0;letter-spacing:.1em}
.signal{padding:13px;border-radius:15px;background:#07132365;border:1px solid #ffffff15;margin-top:12px}
.signal-row{display:flex;gap:8px;align-items:center;margin:10px 0;font-size:9px;color:#b5c4d8}
.dot{width:7px;height:7px;border-radius:50%;background:#526078;flex:none}.dot.on{background:#a5f4dc;box-shadow:0 0 12px #a5f4dc}
.log{min-height:45px;font-size:9px;line-height:1.6;color:#a8c5d8;margin-top:12px}
.note{font-size:9px;line-height:1.6;color:#8494ab;margin-top:12px}
.footer{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:25px;padding:14px 4px;border-top:1px solid #ffffff18;color:#8593a9;font-size:8px;letter-spacing:.13em}
@media(max-width:1050px){.parts-grid{grid-template-columns:repeat(3,1fr)}.assembly-grid{grid-template-columns:220px minmax(300px,1fr)}.inspector{grid-column:1/-1}}
@media(max-width:720px){.shell{padding:15px;min-height:100vh}.header{padding:12px}.live{font-size:0}.live i{margin:0}.hero{display:block}.hero-meta{text-align:left;margin-top:14px}.parts-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.detail{grid-template-columns:1fr}.assembly-grid{grid-template-columns:1fr}.stage{height:440px;grid-row:1}.inspector{grid-column:auto}.nav{width:100%}.nav button{flex:1;padding:10px 8px}.side{padding:15px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;transition-duration:.01ms!important}}
</style>
</head>
<body>
<div class="shell" id="saathi">
 <header class="header glass">
  <div class="brand"><div class="logo">✦</div><div><strong>SAATHI</strong><small>PERSONAL SAFETY SYSTEM · DESIGN LAB</small></div></div>
  <div class="live"><i></i> SYSTEM READY</div>
 </header>
 <section class="hero">
  <div><div class="kicker">A companion, engineered around care</div><h1>Build safety.<br><span>Beautifully.</span></h1><p>Explore the hardware behind SAATHI, then assemble a wearable emergency pendant in an interactive holographic workbench. Select a part, watch it move into place, and inspect how the signal travels.</p></div>
  <div class="hero-meta">ENGINEERING STUDIO<br>HARDWARE PROTOTYPE · 01 / 02</div>
 </section>
 <nav class="nav glass" aria-label="Main pages">
  <button class="active" data-page="explore">01 &nbsp; Components</button>
  <button data-page="assembly">02 &nbsp; Assembly lab</button>
 </nav>

 <main class="page active" id="explore">
  <div class="section-head"><div><div class="micro">Hardware library</div><h2>Every part has a purpose.</h2><p>Select a component to inspect its function in the SAATHI system.</p></div><span class="pill">09 COMPONENTS</span></div>
  <div class="parts-grid" id="partsGrid"></div>
  <section class="detail glass">
   <div><div class="micro">Component inspector</div><h3 id="detailName">Pendant enclosure</h3><span class="pill" id="detailGroup">MECHANICAL / OUTER BODY</span></div>
   <div><div class="micro">What it does</div><p id="detailText"></p><div class="micro">System role</div><p id="detailRole"></p><div class="demo-box"><div class="demo-head"><span>COMPONENT IN ACTION · LOOPING PREVIEW</span><button id="replayDemo">REPLAY</button></div><div class="demo-stage" id="demoStage"></div><div class="demo-caption" id="demoCaption">Tap a component to watch its function.</div></div></div>
  </section>
 </main>

 <main class="page" id="assembly">
  <div class="section-head"><div><div class="micro">Interactive engineering workbench</div><h2>Assemble the pendant.</h2><p>Tap components to attach them. Drag the model to orbit and scroll to zoom.</p></div><span class="pill">LIVE 3D VIEWPORT</span></div>
  <div class="assembly-grid">
   <aside class="side glass">
    <div class="micro">01 / Parts tray</div><h3>PENDANT COMPONENTS</h3><div id="partTray"></div>
    <div class="actions"><button class="action primary" id="autoBuild">AUTO BUILD</button><button class="action" id="resetBuild">RESET</button></div>
    <div class="meter"><i id="buildProgress"></i></div><div class="progress-label" id="progressText">0 / 9 PARTS INSTALLED</div>
    <p class="note">Each part begins in an exploded position. Attach it to see the component travel into the pendant assembly.</p>
   </aside>
   <section class="stage-wrap">
    <div class="stage">
     <div class="stage-top"><span>SAATHI / PENDANT MK-I</span><span id="viewLabel">EXPLODED VIEW</span></div>
     <canvas id="pendantCanvas" aria-label="Interactive rotatable pendant assembly visualization"></canvas>
     <div class="stage-bottom"><span>DRAG TO ROTATE · SCROLL TO ZOOM</span><span>SCHEMATIC 3D PROJECTION</span></div>
    </div>
    <div class="actions">
     <button class="action" id="explodeBtn">EXPLODED VIEW</button><button class="action" id="assembledBtn">ASSEMBLED VIEW</button><button class="action" id="rotateBtn">AUTO ROTATE · ON</button><button class="action primary" id="sosBtn">TEST SOS SIGNAL ↗</button>
    </div>
   </section>
   <aside class="side glass">
    <div class="micro">02 / Live inspector</div><h3 id="inspectTitle">PENDANT OVERVIEW</h3><p class="note" id="inspectDesc">Choose a component from the tray or tap a highlighted part in the viewport to inspect it.</p><div class="demo-box"><div class="demo-head"><span>LIVE COMPONENT PREVIEW</span><button id="replayDemo2">REPLAY</button></div><div class="demo-stage" id="demoStage2"></div><div class="demo-caption" id="demoCaption2">Select a part to view its action.</div></div>
    <div class="stats"><div class="stat"><b id="installedCount">0/9</b><small>INSTALLED</small></div><div class="stat"><b id="buildState">Draft</b><small>BUILD STATUS</small></div></div>
    <div class="signal"><div class="micro">Signal pathway</div>
     <div id="signalSteps">
      <div class="signal-row"><i class="dot"></i>01 &nbsp; SOS / impact trigger</div>
      <div class="signal-row"><i class="dot"></i>02 &nbsp; Energy harvesting</div>
      <div class="signal-row"><i class="dot"></i>03 &nbsp; Capacitor + MCU</div>
      <div class="signal-row"><i class="dot"></i>04 &nbsp; 433 MHz RF packet</div>
      <div class="signal-row"><i class="dot"></i>05 &nbsp; Hub receives signal</div>
     </div>
     <div class="log" id="eventLog" aria-live="polite">Standby. Complete the pendant to run the SOS signal simulation.</div>
    </div>
    <p class="note">The pendant concept uses a kinetic harvester, rectifier and storage capacitor, low-power MCU, RF transmitter and manual SOS control. The detailed physical layout is illustrative, not manufacturing CAD.</p>
   </aside>
  </div>
 </main>
 <footer class="footer"><span>SAATHI · YOUR DAILY SAFETY COMPANION</span><span>CONCEPT VISUALIZATION · NOT A VALIDATED ELECTRONICS SIMULATOR</span></footer>
</div>

<script>
(function(){
const root=document.getElementById('saathi');
const parts=[
{id:'shell',name:'Pendant enclosure',icon:'⬡',group:'MECHANICAL / OUTER BODY',role:'Protective housing',desc:'A two-piece wearable enclosure designed to protect the electronics while keeping the emergency control easy to locate. The transparent concept shell lets you inspect the internal stack.'},
{id:'sos',name:'Large tactile SOS button',icon:'◎',group:'USER INPUT',role:'Manual emergency trigger',desc:'A prominent physical button gives the wearer a direct way to raise an alert. It is designed to be easy to find and press, including during stressful situations.'},
{id:'harvester',name:'Kinetic energy harvester',icon:'ϟ',group:'POWER / ENERGY HARVESTING',role:'Converts movement or impact into electrical energy',desc:'A piezo element or small coil converts movement or a pendant impact into a short burst of electrical energy. This is the proposed self-powered source for the pendant.'},
{id:'storage',name:'Rectifier + storage capacitor',icon:'▤',group:'POWER CONDITIONING',role:'Stores energy for a short radio burst',desc:'The rectifier conditions the harvested output and the capacitor stores enough energy to power a brief event transmission.'},
{id:'mcu',name:'Low-power microcontroller',icon:'▦',group:'CONTROL ELECTRONICS',role:'Identifies and prepares the event',desc:'The controller identifies whether the event is a manual SOS or detected impact, then prepares the event packet for wireless transmission.'},
{id:'rf',name:'433 MHz RF transmitter',icon:'⌁',group:'WIRELESS COMMUNICATION',role:'Sends an event packet to the Hub',desc:'A short-range radio transmitter sends the event to the SAATHI Hub. The harvested-energy radio range remains to be tested.'},
{id:'antenna',name:'RF antenna',icon:'〰',group:'WIRELESS COMMUNICATION',role:'Radiates the RF packet',desc:'A compact antenna is represented as part of the RF transmission assembly. Final antenna geometry and tuning are prototype engineering tasks.'},
{id:'pull',name:'Optional pull-cord',icon:'◌',group:'MECHANICAL / USER INPUT',role:'Alternative accessible trigger',desc:'The pendant can be worn, clipped or hung by the bed. An optional pull-cord provides another way to raise an alert.'},
{id:'back',name:'Rear cover + mounting loop',icon:'◉',group:'MECHANICAL / OUTER BODY',role:'Closes and supports the pendant',desc:'The rear cover closes the enclosure and the mounting loop supports wearing or clipping the pendant.'}
];
const byId=Object.fromEntries(parts.map(p=>[p.id,p]));
const palette=['#a9ecff','#ff8294','#f3cf8c','#9be8d5','#9dbdff','#c1a7ff','#f4b4e4','#a5e9c9','#c0d3ed'];
let selected='shell',installed=new Set(),exploded=true,autoRotate=true,rotation=.55,tilt=-.14,zoom=1,drag=null,tweens=[],sosTimer=[];
const $=id=>document.getElementById(id);
const grid=$('partsGrid');
parts.forEach((p,i)=>{
 let el=document.createElement('article');el.className='part-card glass'+(i===0?' selected':'');
 el.innerHTML=`<div class="part-num">COMPONENT · 0${i+1}</div><div class="part-icon">${p.icon}</div><h3>${p.name}</h3><p>${p.role}</p>`;
 el.addEventListener('click',()=>selectPart(p.id));grid.appendChild(el);
});
function selectPart(id){
 selected=id;let p=byId[id],i=parts.findIndex(x=>x.id===id);
 document.querySelectorAll('.part-card').forEach((e,n)=>e.classList.toggle('selected',n===i));
 $('detailName').textContent=p.name;$('detailGroup').textContent=p.group;$('detailText').textContent=p.desc;$('detailRole').textContent=p.role;
 inspect(id);runDemo(id);
}
function inspect(id){selected=id;let p=byId[id];$('inspectTitle').textContent=p.name.toUpperCase();$('inspectDesc').textContent=p.desc;runDemo(id);}
const demoCaptions={shell:'Protective enclosure keeps the wearable electronics together.',sos:'Press the tactile control to initiate an emergency event.',harvester:'Movement creates a brief electrical energy pulse.',storage:'The rectifier conditions energy and the capacitor stores it.',mcu:'The controller reads the trigger and prepares an event packet.',rf:'The radio sends the alert packet wirelessly to the hub.',antenna:'The antenna radiates the outgoing radio signal.',pull:'Pulling the cord provides an alternative manual trigger.',back:'The rear cover closes the body and supports mounting.'};
function runDemo(id){
 const p=byId[id];if(!p)return;
 const markup=`<div class="demo-object" style="animation:${id==='antenna'?'demoSpin 2.4s linear infinite':id==='pull'?'demoFloat 1.2s ease-in-out infinite':'demoPulse 1.8s ease-in-out infinite'}">${p.icon}</div><div class="demo-beam"></div><div class="demo-object" style="animation-delay:.35s">${id==='rf'||id==='antenna'?'⌂':id==='sos'?'!':id==='storage'?'⚡':'✓'}</div>`;
 ['demoStage','demoStage2'].forEach(k=>{let el=$(k);if(el)el.innerHTML=markup;});
 ['demoCaption','demoCaption2'].forEach(k=>{let el=$(k);if(el)el.textContent=demoCaptions[id];});
}
document.querySelectorAll('.nav button').forEach(btn=>btn.addEventListener('click',()=>{
 document.querySelectorAll('.nav button').forEach(b=>b.classList.toggle('active',b===btn));
 document.querySelectorAll('.page').forEach(p=>p.classList.toggle('active',p.id===btn.dataset.page));
 if(btn.dataset.page==='assembly')setTimeout(()=>{resizeCanvas();drawOnceIfNeeded();},80);
}));
$('replayDemo').addEventListener('click',()=>runDemo(selected));$('replayDemo2').addEventListener('click',()=>runDemo(selected));
const tray=$('partTray');
parts.forEach((p,i)=>{
 let row=document.createElement('div');row.className='part-row';
 row.innerHTML=`<div><strong>${p.icon} &nbsp;${p.name}</strong><small>${p.group}</small></div><button class="add" data-add="${p.id}" aria-label="Install ${p.name}">+</button>`;
 row.addEventListener('click',e=>{if(e.target.tagName!=='BUTTON'){selectPart(p.id);install(p.id);}});row.querySelector('button').addEventListener('click',()=>{selectPart(p.id);install(p.id);});tray.appendChild(row);
});
const canvas=$('pendantCanvas'),ctx=canvas.getContext('2d');
const components3d=[
 {id:'shell',center:[0,0,0],size:[1.52,2.04,.30],kind:'shell'},
 {id:'sos',center:[0,.55,.27],size:[.62,.62,.20],kind:'button'},
 {id:'harvester',center:[-.53,.22,-.16],size:[.68,.68,.13],kind:'coil'},
 {id:'storage',center:[.47,.37,-.17],size:[.76,.48,.13],kind:'capacitor'},
 {id:'mcu',center:[0,-.20,-.20],size:[.86,.60,.13],kind:'chip'},
 {id:'rf',center:[.46,-.72,-.18],size:[.70,.40,.12],kind:'rf'},
 {id:'antenna',center:[.70,-.66,-.06],size:[.20,.80,.08],kind:'antenna'},
 {id:'pull',center:[-.68,-.76,.10],size:[.40,.56,.10],kind:'cord'},
 {id:'back',center:[0,0,-.52],size:[1.48,2,.16],kind:'back'}
];
const off={
 shell:[0,1.9,0],sos:[0,2.7,1.1],harvester:[-2.0,1.25,-.7],storage:[2.0,1.15,-.7],
 mcu:[0,-1.8,-1.0],rf:[2.0,-1.35,-.6],antenna:[2.7,.5,-1.0],pull:[-2.0,-1.2,.7],back:[0,-2.5,-1.3]
};
let positions={};components3d.forEach(c=>positions[c.id]=c.center.slice());
const lerp=(a,b,t)=>a+(b-a)*t;
function destination(id){let c=components3d.find(x=>x.id===id);return exploded?c.center.map((v,i)=>v+off[id][i]):c.center.slice();}
function animatePart(id,to,dur=780){let from=positions[id].slice();tweens.push({id,from,to:to.slice(),t:0,dur});}
function install(id){
 if(installed.has(id))return;
 installed.add(id);
 let start=positions[id].slice();
 let assembledTarget=components3d.find(c=>c.id===id).center.slice();
 positions[id]=start;
 animatePart(id,assembledTarget,850);
 updateUI();inspect(id);$('eventLog').textContent='COMPONENT ATTACHED · '+byId[id].name.toUpperCase();
}
function updateUI(){
 $('installedCount').textContent=installed.size+'/9';$('buildState').textContent=installed.size===9?'Complete':installed.size?'Building':'Draft';
 $('buildProgress').style.width=(installed.size/9*100)+'%';$('progressText').textContent=installed.size+' / 9 PARTS INSTALLED';
 document.querySelectorAll('[data-add]').forEach(b=>{let done=installed.has(b.dataset.add);b.disabled=done;b.textContent=done?'✓':'+'});
}
function autoBuild(){parts.forEach((p,i)=>setTimeout(()=>install(p.id),i*270));}
$('autoBuild').addEventListener('click',autoBuild);
$('resetBuild').addEventListener('click',()=>{
 installed.clear();tweens=[];parts.forEach(p=>positions[p.id]=destination(p.id));
 updateUI();$('eventLog').textContent='ASSEMBLY RESET · PARTS RETURNED TO INVENTORY';$('signalSteps').querySelectorAll('.dot').forEach(d=>d.classList.remove('on'));
});
function changeView(isExploded){
 exploded=isExploded;$('viewLabel').textContent=exploded?'EXPLODED VIEW':'ASSEMBLED VIEW';
 installed.forEach(id=>{
  const c=components3d.find(x=>x.id===id);
  const target=exploded?c.center.map((v,i)=>v+off[id][i]):c.center.slice();
  animatePart(id,target,650);
 });
}
$('explodeBtn').addEventListener('click',()=>changeView(true));
$('assembledBtn').addEventListener('click',()=>changeView(false));
$('rotateBtn').addEventListener('click',()=>{autoRotate=!autoRotate;$('rotateBtn').textContent='AUTO ROTATE · '+(autoRotate?'ON':'OFF')});
$('sosBtn').addEventListener('click',()=>{
 if(installed.size!==9){$('eventLog').textContent='ASSEMBLY INCOMPLETE · INSTALL ALL 9 COMPONENTS FIRST';return;}
 $('signalSteps').querySelectorAll('.dot').forEach(d=>d.classList.remove('on'));
 $('eventLog').textContent='SOS INPUT REGISTERED · SIGNAL TRACE STARTED';
 const lines=['SOS / IMPACT TRIGGER','ENERGY HARVESTING','CAPACITOR + MCU','433 MHz RF PACKET','SAATHI HUB RECEIVES'];
 const dots=[...$('signalSteps').querySelectorAll('.dot')];
 lines.forEach((line,i)=>setTimeout(()=>{dots[i].classList.add('on');$('eventLog').textContent='SIGNAL TRACE · '+line+' ✓';if(i===4)$('eventLog').textContent='SIMULATION COMPLETE · HUB RECEIVED THE EVENT PACKET. FAMILY ALERT PATH READY.'},i*650));
});
function resizeCanvas(){let r=canvas.getBoundingClientRect();if(!r.width||!r.height)return;let dpr=Math.min(window.devicePixelRatio||1,2);canvas.width=Math.round(r.width*dpr);canvas.height=Math.round(r.height*dpr);ctx.setTransform(dpr,0,0,dpr,0,0);}
window.addEventListener('resize',resizeCanvas);setTimeout(resizeCanvas,100);
function rotate3(v){let [x,y,z]=v;let c=Math.cos(rotation),s=Math.sin(rotation);let x1=x*c-z*s,z1=x*s+z*c;let ct=Math.cos(tilt),st=Math.sin(tilt);return [x1,y*ct-z1*st,y*st+z1*ct];}
function project(v){let [x,y,z]=rotate3(v);let w=canvas.clientWidth,h=canvas.clientHeight;let scale=Math.min(w/5.7,h/5.2)*zoom;let perspective=1/(1+z*.055);return [w/2+x*scale*perspective,h/2-y*scale*perspective];}
function poly(points,fill,stroke='rgba(200,245,255,.55)',lw=1){ctx.beginPath();points.forEach((p,i)=>{let q=project(p);if(i)ctx.lineTo(q[0],q[1]);else ctx.moveTo(q[0],q[1]);});ctx.closePath();ctx.fillStyle=fill;ctx.fill();ctx.strokeStyle=stroke;ctx.lineWidth=lw;ctx.stroke();}
function line3(a,b,color,width=1){let p=project(a),q=project(b);ctx.beginPath();ctx.moveTo(...p);ctx.lineTo(...q);ctx.strokeStyle=color;ctx.lineWidth=width;ctx.stroke();}
function boxFaces(c,size,color,alpha=1){
 let [x,y,z]=c,[w,h,d]=size.map(v=>v/2);
 let v=[[-w,-h,-d],[w,-h,-d],[w,h,-d],[-w,h,-d],[-w,-h,d],[w,-h,d],[w,h,d],[-w,h,d]].map(p=>[p[0]+x,p[1]+y,p[2]+z]);
 ctx.globalAlpha=alpha;
 poly([v[0],v[1],v[2],v[3]],color,'rgba(191,237,255,.55)',1);
 poly([v[4],v[5],v[6],v[7]],'rgba(99,208,242,.14)','rgba(181,239,255,.8)',1.2);
 poly([v[1],v[2],v[6],v[5]],'rgba(112,178,238,.24)','rgba(191,237,255,.48)',1);
 poly([v[2],v[3],v[7],v[6]],'rgba(255,255,255,.09)','rgba(191,237,255,.4)',1);
 ctx.globalAlpha=1;
}
function drawCircle(center,r,color,fill=true){let p=project(center),edge=project([center[0]+r,center[1],center[2]]),rr=Math.hypot(edge[0]-p[0],edge[1]-p[1]);ctx.beginPath();ctx.arc(p[0],p[1],Math.max(2,rr),0,Math.PI*2);if(fill){ctx.fillStyle=color;ctx.fill()}ctx.strokeStyle='rgba(219,248,255,.9)';ctx.lineWidth=1.5;ctx.stroke();}
function drawPart(c){
 let id=c.id, pos=positions[id], selectedPart=id===selected, col=palette[parts.findIndex(p=>p.id===id)];
 ctx.save();ctx.shadowColor=col;ctx.shadowBlur=selectedPart?24:10;
 if(c.kind==='shell'){
  boxFaces(pos,c.size,'rgba(103,178,221,.12)',.8);
  let front=[pos[0],pos[1],pos[2]+.17];
  // translucent front window and outline
  let w=.67,h=.91;poly([[front[0]-w,front[1]-h,front[2]],[front[0]+w,front[1]-h,front[2]],[front[0]+w,front[1]+h,front[2]],[front[0]-w,front[1]+h,front[2]]],'rgba(133,225,255,.07)',col,selectedPart?2.5:1.2);
  drawCircle([front[0],front[1]+.57,front[2]+.02],.27,'rgba(98,221,255,.14)',false);
  // subtle internal guide rails
  line3([front[0]-.48,front[1]-.73,front[2]+.02],[front[0]+.48,front[1]-.73,front[2]+.02],'rgba(165,228,255,.55)');
 }else if(c.kind==='button'){
  drawCircle([pos[0],pos[1],pos[2]],.31,'rgba(255,86,112,.32)');
  drawCircle([pos[0],pos[1],pos[2]+.02],.22,'#f17c91');
  drawCircle([pos[0],pos[1],pos[2]+.04],.15,'#ffb5c0');
 }else if(c.kind==='coil'){
  drawCircle(pos,.34,'rgba(255,203,119,.16)');
  for(let r=.28;r>.07;r-=.055)drawCircle([pos[0],pos[1],pos[2]+.02],r,'rgba(255,210,139,.12)',false);
  drawCircle([pos[0],pos[1],pos[2]+.03],.055,'#f7d28b');
 }else if(c.kind==='capacitor'){
  boxFaces(pos,c.size,'rgba(95,225,190,.22)');
  for(let i=0;i<3;i++){let x=pos[0]-.23+i*.23;drawCircle([x,pos[1],pos[2]+.09],.065,'#e9c47d');}
 }else if(c.kind==='chip'){
  boxFaces(pos,c.size,'rgba(91,222,187,.24)');
  let cc=[pos[0],pos[1],pos[2]+.09];boxFaces(cc,[.36,.31,.08],'rgba(17,34,48,.95)');
  for(let i=-3;i<=3;i++){line3([pos[0]+i*.1,pos[1]-.35,pos[2]+.02],[pos[0]+i*.1,pos[1]-.43,pos[2]+.02],'#eacb8a',2);line3([pos[0]+i*.1,pos[1]+.35,pos[2]+.02],[pos[0]+i*.1,pos[1]+.43,pos[2]+.02],'#eacb8a',2);}
 }else if(c.kind==='rf'){
  boxFaces(pos,c.size,'rgba(98,157,245,.28)');
  boxFaces([pos[0],pos[1],pos[2]+.08],[.22,.20,.07],'rgba(25,41,68,.95)');
 }else if(c.kind==='antenna'){
  let a=[pos[0],pos[1]-.35,pos[2]],b=[pos[0]+.08,pos[1]+.35,pos[2]];
  line3(a,b,'#e9d08e',4);drawCircle(b,.045,'#9deaff');
 }else if(c.kind==='cord'){
  let p=project(pos),r=24*zoom;ctx.beginPath();ctx.ellipse(p[0],p[1],r*.7,r,0,0,Math.PI*2);ctx.strokeStyle='#c4d5e8';ctx.lineWidth=4;ctx.stroke();line3([pos[0],pos[1]-.28,pos[2]],[pos[0],pos[1]-.55,pos[2]],'#ef8b9b',3);
 }else if(c.kind==='back'){
  boxFaces(pos,c.size,'rgba(139,169,207,.22)');
  let p=project([pos[0],pos[1]+.95,pos[2]+.1]);ctx.beginPath();ctx.arc(p[0],p[1],12*zoom,Math.PI,Math.PI*2);ctx.strokeStyle='#e3c98d';ctx.lineWidth=4;ctx.stroke();
 }
 if(selectedPart){let p=project(pos);ctx.shadowBlur=0;ctx.beginPath();ctx.arc(p[0],p[1],8,0,Math.PI*2);ctx.fillStyle='#fff';ctx.fill();ctx.beginPath();ctx.arc(p[0],p[1],15,0,Math.PI*2);ctx.strokeStyle=col;ctx.lineWidth=1.3;ctx.stroke();}
 ctx.restore();
}
function draw(){
 requestAnimationFrame(draw);
 let w=canvas.clientWidth,h=canvas.clientHeight;
 if(!w||!h)return;
 ctx.clearRect(0,0,w,h);
 // holographic ground rings
 for(let i=0;i<3;i++){let p=project([0,-1.55-i*.035,0]);ctx.beginPath();ctx.ellipse(p[0],p[1],(85+i*22)*zoom,(17+i*5)*zoom,0,0,Math.PI*2);ctx.strokeStyle=`rgba(120,221,255,${.18-i*.04})`;ctx.lineWidth=1;ctx.stroke();}
 // subtle vertical scan beam
 let beam=ctx.createLinearGradient(0,0,0,h);beam.addColorStop(0,'rgba(123,229,255,0)');beam.addColorStop(.5,'rgba(123,229,255,.045)');beam.addColorStop(1,'rgba(123,229,255,0)');ctx.fillStyle=beam;ctx.fillRect(w*.15,0,w*.7,h);
 const ordered=components3d.slice().sort((a,b)=>rotate3(positions[a.id])[2]-rotate3(positions[b.id])[2]);
 ordered.forEach(c=>drawPart(c));
 // numbered component labels remain visible in both exploded and assembled views
 components3d.forEach((c,i)=>{let p=project(positions[c.id]);let short=['ENCLOSURE','SOS BUTTON','HARVESTER','CAPACITOR','MCU','RF TX','ANTENNA','PULL-CORD','REAR COVER'][i];let tx=p[0]+13,ty=p[1]-12;ctx.font='8px Inter, sans-serif';let tw=ctx.measureText(short).width+13;ctx.fillStyle='rgba(5,15,29,.78)';ctx.strokeStyle=palette[i];ctx.lineWidth=1;ctx.beginPath();ctx.roundRect(tx,ty-9,tw,16,5);ctx.fill();ctx.stroke();ctx.fillStyle='#e6f7ff';ctx.fillText(short,tx+6,ty+2);});
 if(autoRotate&&!drag)rotation+=.0025;
}
function tickTweens(){let now=performance.now();for(let i=tweens.length-1;i>=0;i--){let t=tweens[i];t.t+=16;let k=Math.min(1,t.t/t.dur);k=1-Math.pow(1-k,3);positions[t.id]=t.from.map((v,n)=>v+(t.to[n]-v)*k);if(k>=1)tweens.splice(i,1);}requestAnimationFrame(tickTweens);}
canvas.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,moved:false};canvas.setPointerCapture(e.pointerId);});
canvas.addEventListener('pointermove',e=>{if(!drag)return;let dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>2)drag.moved=true;rotation+=dx*.008;tilt=Math.max(-.8,Math.min(.8,tilt+dy*.006));drag.x=e.clientX;drag.y=e.clientY;});
canvas.addEventListener('pointerup',e=>{
 if(drag&&!drag.moved){let rect=canvas.getBoundingClientRect(),mx=e.clientX-rect.left,my=e.clientY-rect.top,best=null,bd=Infinity;
 components3d.forEach(c=>{if(!installed.has(c.id))return;let p=project(positions[c.id]),d=Math.hypot(p[0]-mx,p[1]-my);if(d<bd){bd=d;best=c.id;}});
 if(best&&bd<70)selectPart(best);
 }drag=null;
});
canvas.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.65,Math.min(1.65,zoom*(e.deltaY>0?.94:1.06)));},{passive:false});
function drawOnceIfNeeded(){
 if(canvas.clientWidth>0 && canvas.clientHeight>0) {
  // The animation loop is persistent; this immediate paint removes any tab-switch blank frame.
  drawFrame();
 }
}
function drawFrame(){
 let w=canvas.clientWidth,h=canvas.clientHeight;
 if(!w||!h)return;
 ctx.clearRect(0,0,w,h);
 for(let i=0;i<3;i++){let p=project([0,-1.55-i*.035,0]);ctx.beginPath();ctx.ellipse(p[0],p[1],(85+i*22)*zoom,(17+i*5)*zoom,0,0,Math.PI*2);ctx.strokeStyle=`rgba(120,221,255,${.18-i*.04})`;ctx.lineWidth=1;ctx.stroke();}
 const ordered=components3d.slice().sort((a,b)=>rotate3(positions[a.id])[2]-rotate3(positions[b.id])[2]);
 ordered.forEach(c=>drawPart(c));
}
function init(){
 components3d.forEach(c=>positions[c.id]=destination(c.id));
 selectPart('shell');updateUI();resizeCanvas();draw();tickTweens();
}
init();
})();
</script>
</body>
</html>
"""

components.html(HTML, height=1600, scrolling=True)
