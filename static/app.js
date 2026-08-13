let game = null;
let rivals = 1;
let pendingWild = null;

const $ = id => document.getElementById(id);
const sleep = ms => new Promise(r => setTimeout(r, ms));

document.querySelectorAll("[data-rivals]").forEach(btn => {
  btn.onclick = () => {
    document.querySelectorAll("[data-rivals]").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    rivals = Number(btn.dataset.rivals);
  };
});
document.querySelector("[data-rivals='1']").classList.add("active");

$("start").onclick = startGame;
$("newGame").onclick = () => {
  $("game").classList.add("hidden");
  $("menu").classList.remove("hidden");
};
$("rulesBtn").onclick = () => $("rulesModal").classList.remove("hidden");
$("closeRules").onclick = () => $("rulesModal").classList.add("hidden");
$("rulesModal").onclick = (e) => {
  if (e.target.id === "rulesModal") $("rulesModal").classList.add("hidden");
};


async function startGame(){
  const res = await fetch("/api/new", {
    method:"POST", headers:{"Content-Type":"application/json"},
    body:JSON.stringify({opponents:rivals})
  });
  const data = await res.json();
  game = data.game;
  $("menu").classList.add("hidden");
  $("game").classList.remove("hidden");
  render();
}

function cardInfo(card){
  if(card === "U") return ["W","wild"];
  if(card === "u+4") return ["+4","wild"];
  const color = {R:"red",B:"blue",G:"green",Y:"yellow"}[card[0]] || "wild";
  let value = card.slice(1);
  if(value === "reverse") value = "↻";
  if(value === "skip") value = "⊘";
  return [value, color];
}

function render(){
  if(!game) return;
  const players = $("players");
  players.innerHTML = "";
  for(let i=0;i<game.hands.length;i++){
    const name = i===0 ? "YOU" : `SYSTEM ${i}`;
    const row = document.createElement("div");
    row.className = "player-row " + (game.current===i ? "active" : "");
    row.innerHTML = `<span class="player-name">${name}</span><span class="player-count">${game.hands[i].length}</span>`;
    players.appendChild(row);
  }
  $("penalty").textContent = game.penalty;
  $("currentName").textContent = game.current===0 ? "YOU" : `SYSTEM ${game.current}`;
  $("direction").textContent = game.direction===1 ? "↻ CLOCKWISE" : "↶ REVERSE";
  $("count").textContent = `${game.hands[0].length} CARDS`;

  const [value, color] = cardInfo(game.last_card);
  $("lastCard").className = `card large ${color}`;
  $("lastCard").textContent = value;
  $("colorRing").style.setProperty("--glow", `var(--${color === "wild" ? "red" : color})`);

  const hand = $("hand");
  hand.innerHTML = "";
  game.hands[0].forEach((c, i) => {
    const [v, col] = cardInfo(c);
    const el = document.createElement("div");
    el.className = `card ${col}`;
    el.textContent = v;
    el.style.zIndex = i;
    el.onclick = () => chooseCard(c);
    hand.appendChild(el);
  });

  $("log").innerHTML = [...game.log].reverse().map(x => {
    const kind = game.last_event && x === game.last_event.text ? game.last_event.kind : "info";
    return `<div class="log-item ${kind}"><b>${escapeHtml(x)}</b></div>`;
  }).join("");

  $("turnText").textContent = game.winner !== null
    ? (game.winner === 0 ? "You won" : `System ${game.winner} won`)
    : (game.current===0 ? "Your turn" : `System ${game.current} thinking`);
  $("turnDot").style.background = game.winner !== null ? "var(--yellow)" : (game.current===0 ? "var(--green)" : "var(--red)");
}

async function chooseCard(card){
  if(!game || game.winner !== null || game.current !== 0) return;
  if(card === "U" || card === "u+4"){
    pendingWild = card;
    $("colorModal").classList.remove("hidden");
    return;
  }
  await sendAction(card);
}

document.querySelectorAll("[data-color]").forEach(btn => {
  btn.onclick = async () => {
    const color = btn.dataset.color;
    $("colorModal").classList.add("hidden");
    if(pendingWild){
      const card = pendingWild;
      pendingWild = null;
      await sendAction(card, color);
    }
  };
});

$("deckPile").onclick = async () => {
  if(!game || game.current!==0 || game.winner!==null) return;
  await sendAction("X");
};

async function sendAction(action, color=null){
  const res = await fetch("/api/action", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({game, action, color})
  });
  const data = await res.json();
  if(!data.ok && data.message){
    toast(data.message);
    return;
  }
  game = data.game;
  render();

  // Keep the latest system action visible for 2 seconds.
  if (game.current !== 0 && game.winner === null) {
    $("hint").textContent = "SYSTEM IS PLAYING...";
    await sleep(5000);
  } else if (game.last_event) {
    await sleep(3000);
  }

  render();
  animateEffect(data.game.last_event);
}

function animateEffect(ev){
  if(!ev) return;
  const e = $("effect");
  e.className = `effect ${ev.kind} show`;
  e.textContent = ev.text;
  setTimeout(()=>e.className="effect",800);
  if(ev.kind==="win") toast(ev.text);
}

function toast(text){
  const t=$("toast"); t.textContent=text; t.classList.add("show");
  clearTimeout(window.__toast); window.__toast=setTimeout(()=>t.classList.remove("show"),1800);
}
function escapeHtml(s){
  return String(s).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[m]));
}
