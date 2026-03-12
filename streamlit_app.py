import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="EVOLIO: Frontier Protocol",
    page_icon="🧬",
    layout="wide",
)

st.title("EVOLIO: Frontier Protocol")
st.caption(
    "스토리는 유지하고, 최신 웹게임 BM 루프(시즌패스/일일·주간 미션/로테이션 상점/캡슐/메타 성장)를 "
    "통합한 2차 리빌드 버전입니다."
)


APP_HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    :root {
      --bg-0: #030814;
      --bg-1: #09172d;
      --panel: rgba(11, 21, 38, 0.85);
      --panel-2: rgba(16, 29, 52, 0.82);
      --line: rgba(126, 171, 244, 0.26);
      --txt: #eaf3ff;
      --sub: #99b4d8;
      --mint: #59f2ba;
      --cyan: #63c9ff;
      --warn: #ffc27d;
      --danger: #ff8484;
    }

    html, body {
      margin: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 20% 20%, #0a1730 0%, #02050d 65%);
      color: var(--txt);
      font-family: Inter, Segoe UI, Pretendard, Arial, sans-serif;
      overflow: hidden;
    }

    #app {
      height: 1020px;
      border: 1px solid rgba(133, 177, 249, 0.2);
      border-radius: 14px;
      overflow: hidden;
      position: relative;
      background: linear-gradient(180deg, rgba(7, 14, 27, 0.96), rgba(4, 9, 18, 0.96));
    }

    .top-bar {
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 12px;
      border-bottom: 1px solid var(--line);
      background: rgba(5, 12, 24, 0.88);
      backdrop-filter: blur(8px);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand .logo {
      font-weight: 900;
      letter-spacing: 0.7px;
      font-size: 18px;
      color: #dff2ff;
    }

    .brand .season {
      font-size: 11px;
      color: #9ec6ff;
      border: 1px solid rgba(125, 176, 248, 0.4);
      border-radius: 999px;
      padding: 3px 8px;
    }

    .resource-row {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    .pill {
      border-radius: 999px;
      padding: 5px 10px;
      border: 1px solid var(--line);
      background: rgba(12, 22, 39, 0.8);
      font-size: 12px;
      color: #d8eaff;
      white-space: nowrap;
    }

    .pill strong {
      color: #f7fbff;
      margin-left: 4px;
    }

    .btn {
      border: 1px solid rgba(124, 209, 177, 0.55);
      border-radius: 9px;
      background: linear-gradient(180deg, #45dd9b, #22b977);
      color: #042214;
      font-weight: 900;
      font-size: 12px;
      letter-spacing: 0.35px;
      padding: 8px 11px;
      cursor: pointer;
    }

    .btn:disabled {
      cursor: not-allowed;
      border-color: rgba(120, 147, 176, 0.4);
      background: rgba(69, 85, 102, 0.66);
      color: #a7b9cc;
    }

    .ghost-btn {
      border: 1px solid rgba(124, 166, 225, 0.45);
      border-radius: 8px;
      background: rgba(18, 34, 60, 0.75);
      color: #d4e8ff;
      font-size: 11px;
      padding: 7px 9px;
      cursor: pointer;
    }

    .layout {
      height: calc(100% - 64px);
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 10px;
      padding: 10px;
      box-sizing: border-box;
    }

    .panel {
      border: 1px solid var(--line);
      border-radius: 12px;
      background: var(--panel);
      backdrop-filter: blur(7px);
      box-shadow: 0 10px 24px rgba(0, 0, 0, 0.3);
    }

    #left-col {
      display: flex;
      flex-direction: column;
      gap: 10px;
      overflow: auto;
      padding-right: 2px;
    }

    .card {
      padding: 11px 12px;
    }

    .title {
      margin: 0 0 8px;
      color: #dff0ff;
      font-size: 13px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }

    .subtext {
      margin: 0;
      color: var(--sub);
      line-height: 1.45;
      font-size: 12px;
    }

    .list {
      margin: 8px 0 0;
      padding-left: 16px;
      color: #dce9ff;
      font-size: 12px;
      line-height: 1.45;
    }

    .kv {
      display: flex;
      justify-content: space-between;
      margin: 6px 0;
      font-size: 12px;
      color: #d8e9ff;
    }

    .kv span {
      color: var(--sub);
    }

    #pilot-box {
      display: flex;
      gap: 8px;
      margin-top: 8px;
    }

    #pilot-input {
      flex: 1;
      border: 1px solid rgba(123, 166, 230, 0.43);
      border-radius: 8px;
      background: rgba(8, 15, 29, 0.88);
      color: #edf5ff;
      padding: 7px 9px;
      font-size: 12px;
      outline: none;
    }

    #right-col {
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    .tabs {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }

    .tab-btn {
      border: 1px solid rgba(118, 157, 217, 0.4);
      background: rgba(16, 29, 52, 0.75);
      color: #c8dfff;
      border-radius: 8px;
      padding: 7px 10px;
      font-size: 11px;
      font-weight: 800;
      cursor: pointer;
    }

    .tab-btn.active {
      background: linear-gradient(180deg, #3c8fff, #2568c6);
      border-color: rgba(111, 175, 255, 0.78);
      color: #eef7ff;
      box-shadow: 0 0 16px rgba(82, 152, 255, 0.28);
    }

    .tab-panel {
      display: none;
      flex: 1;
      min-height: 0;
      overflow: auto;
      padding: 10px;
    }

    .tab-panel.active {
      display: block;
    }

    .h2 {
      margin: 0 0 8px;
      font-size: 14px;
      color: #e6f2ff;
    }

    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 8px;
    }

    .mission-card, .offer-card, .pass-card, .lab-card, .rank-card {
      border: 1px solid rgba(120, 159, 220, 0.35);
      border-radius: 10px;
      background: var(--panel-2);
      padding: 8px 9px;
      font-size: 12px;
    }

    .mission-card.done {
      border-color: rgba(99, 220, 168, 0.6);
      background: rgba(15, 42, 34, 0.8);
    }

    .mission-top, .offer-top, .pass-top, .rank-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
      color: #e2f1ff;
    }

    .tiny {
      font-size: 11px;
      color: #9cb8db;
      margin-top: 4px;
    }

    .track {
      margin-top: 5px;
      height: 7px;
      border-radius: 999px;
      border: 1px solid rgba(142, 182, 233, 0.3);
      background: rgba(10, 18, 32, 0.9);
      overflow: hidden;
    }

    .track > i {
      display: block;
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #54d4ff, #7dffb8);
    }

    .reward {
      color: #ffd59a;
      font-weight: 700;
      font-size: 11px;
    }

    .stack {
      display: grid;
      gap: 7px;
    }

    .badge {
      display: inline-block;
      font-size: 10px;
      border-radius: 999px;
      border: 1px solid rgba(126, 170, 242, 0.46);
      padding: 2px 7px;
      color: #bcd9ff;
      margin-right: 6px;
    }

    .headline {
      color: #f4f9ff;
      margin: 0 0 6px;
      font-size: 13px;
    }

    .hr {
      border-top: 1px solid rgba(126, 170, 242, 0.2);
      margin: 8px 0;
    }

    #run-layer {
      position: absolute;
      inset: 0;
      display: none;
      z-index: 20;
      background: radial-gradient(circle at 30% 20%, #091631, #030810 70%);
    }

    #arena {
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
    }

    .run-hud {
      position: absolute;
      left: 12px;
      right: 12px;
      top: 10px;
      display: flex;
      justify-content: space-between;
      gap: 8px;
      pointer-events: none;
    }

    .run-box {
      pointer-events: auto;
      border: 1px solid rgba(126, 169, 234, 0.36);
      background: rgba(8, 15, 26, 0.78);
      border-radius: 11px;
      padding: 7px 9px;
      min-width: 210px;
      backdrop-filter: blur(6px);
    }

    .run-row {
      display: flex;
      align-items: center;
      gap: 7px;
      margin: 5px 0;
      font-size: 11px;
    }

    .run-row .k {
      min-width: 56px;
      color: #9eb7d8;
      text-transform: uppercase;
    }

    .bar {
      flex: 1;
      height: 8px;
      border: 1px solid rgba(129, 165, 218, 0.34);
      border-radius: 999px;
      overflow: hidden;
      background: rgba(10, 18, 30, 0.85);
    }

    .bar i {
      display: block;
      height: 100%;
      width: 0%;
      border-radius: inherit;
    }

    .bar.hp i {
      background: linear-gradient(90deg, #ff7575, #ff9f8d);
    }

    .bar.en i {
      background: linear-gradient(90deg, #57acff, #65e7ff);
    }

    #toast {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      top: 84px;
      padding: 8px 13px;
      border-radius: 999px;
      border: 1px solid rgba(132, 180, 253, 0.45);
      background: rgba(9, 18, 32, 0.86);
      color: #dff0ff;
      font-weight: 700;
      font-size: 12px;
      opacity: 0;
      transition: opacity 150ms ease;
      pointer-events: none;
    }

    .modal {
      position: absolute;
      inset: 0;
      display: none;
      align-items: center;
      justify-content: center;
      background: rgba(3, 8, 15, 0.74);
      z-index: 30;
    }

    .modal-card {
      width: min(860px, 92vw);
      border: 1px solid rgba(128, 178, 252, 0.37);
      border-radius: 14px;
      background: rgba(7, 14, 27, 0.94);
      box-shadow: 0 18px 40px rgba(0, 0, 0, 0.4);
      padding: 14px;
    }

    .draft-grid {
      margin-top: 10px;
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }

    .draft-card {
      border: 1px solid rgba(121, 164, 230, 0.4);
      border-radius: 10px;
      background: rgba(14, 27, 49, 0.85);
      padding: 10px;
      cursor: pointer;
    }

    .draft-card h4 {
      margin: 0 0 5px;
      font-size: 13px;
      color: #e7f3ff;
    }

    .draft-card p {
      margin: 0;
      font-size: 11px;
      color: #9fb9dd;
      line-height: 1.4;
    }

    .note {
      margin-top: 8px;
      font-size: 11px;
      color: #a9c6e9;
    }
  </style>
</head>
<body>
  <div id="app">
    <div class="top-bar">
      <div class="brand">
        <div class="logo">EVOLIO: Frontier Protocol</div>
        <div class="season" id="season-label">SEASON 1 · FRONTIER</div>
      </div>
      <div class="resource-row">
        <div class="pill">Pilot<strong id="pilot-name-pill">CellPilot</strong></div>
        <div class="pill">Credits<strong id="credits-pill">0</strong></div>
        <div class="pill">Genesis<strong id="genesis-pill">0</strong></div>
        <div class="pill">Stamina<strong id="stamina-pill">0/8</strong></div>
        <div class="pill">Pass XP<strong id="pass-xp-pill">0</strong></div>
        <button class="ghost-btn" id="stamina-refill-btn">⚡ +3 (30 Genesis)</button>
        <button class="btn" id="start-run-btn">RUN START (1⚡)</button>
      </div>
    </div>

    <div class="layout">
      <div id="left-col">
        <div class="panel card">
          <h3 class="title">Story / Objective</h3>
          <p class="subtext" id="story-text"></p>
          <div class="hr"></div>
          <div class="kv"><span>Current Chapter</span><strong id="chapter-kv">1</strong></div>
          <div class="kv"><span>Next Objective</span><strong id="objective-kv">Sector 3 clear</strong></div>
          <div class="kv"><span>Best Run</span><strong id="best-run-kv">0</strong></div>
          <div class="kv"><span>Best Sector</span><strong id="best-sector-kv">1</strong></div>
        </div>

        <div class="panel card">
          <h3 class="title">Pilot Profile</h3>
          <div id="pilot-box">
            <input id="pilot-input" type="text" maxlength="16" placeholder="파일럿 이름" />
            <button class="btn" id="pilot-save-btn">SAVE</button>
          </div>
          <div class="kv"><span>Total Runs</span><strong id="runs-kv">0</strong></div>
          <div class="kv"><span>Total Kills</span><strong id="kills-kv">0</strong></div>
          <div class="kv"><span>Total Playtime</span><strong id="time-kv">0m</strong></div>
          <div class="kv"><span>Checkpoint</span><strong id="checkpoint-kv">-</strong></div>
          <p class="subtext">실시간 자동 저장(localStorage) 기반입니다.</p>
        </div>

        <div class="panel card">
          <h3 class="title">Core Controls</h3>
          <ul class="list">
            <li>이동: WASD</li>
            <li>대시: SPACE</li>
            <li>펄스: E</li>
            <li>중단/복귀: ESC</li>
          </ul>
        </div>
      </div>

      <div id="right-col">
        <div class="tabs" id="tabs">
          <button class="tab-btn active" data-tab="overview">Overview</button>
          <button class="tab-btn" data-tab="missions">Missions</button>
          <button class="tab-btn" data-tab="pass">Season Pass</button>
          <button class="tab-btn" data-tab="shop">Shop</button>
          <button class="tab-btn" data-tab="capsule">Capsule</button>
          <button class="tab-btn" data-tab="lab">Lab</button>
          <button class="tab-btn" data-tab="ranking">Ranking</button>
        </div>

        <div class="panel tab-panel active" id="tab-overview">
          <h3 class="h2">리빌드 설계 요약</h3>
          <div class="stack">
            <div class="offer-card">
              <p class="headline">기본 스토리 유지</p>
              <p class="subtext">원시 세포가 미시 프론티어에서 진화하며 포식 생태계를 돌파한다는 세계관을 유지합니다.</p>
            </div>
            <div class="offer-card">
              <p class="headline">최신 웹게임 BM 루프 반영</p>
              <p class="subtext">
                일일/주간 미션 → 시즌패스 XP → 상점/캡슐/코스메틱/메타강화 → 더 높은 섹터 도전으로 이어지는 장기 루프를 설계했습니다.
              </p>
            </div>
            <div class="offer-card">
              <p class="headline">세션형 로그라이트 전투</p>
              <p class="subtext">
                런마다 섹터를 돌파하며 돌연변이 3지선다를 선택합니다. 빌드(공격/생존/쿨감/드론/치명) 시너지가 전투 체감을 만듭니다.
              </p>
            </div>
          </div>
        </div>

        <div class="panel tab-panel" id="tab-missions">
          <h3 class="h2">Daily Missions</h3>
          <div id="daily-missions" class="grid-2"></div>
          <div class="hr"></div>
          <h3 class="h2">Weekly Missions</h3>
          <div id="weekly-missions" class="grid-2"></div>
        </div>

        <div class="panel tab-panel" id="tab-pass">
          <h3 class="h2">Season Pass</h3>
          <p class="subtext">
            Free / Premium 이중 보상 트랙 구조. 런/미션으로 XP를 쌓고 티어 보상을 수령합니다.
          </p>
          <div class="kv"><span>Pass Level</span><strong id="pass-level-kv">1</strong></div>
          <div class="kv"><span>Premium</span><strong id="premium-kv">OFF</strong></div>
          <button class="btn" id="buy-premium-btn">Premium Unlock (240 Genesis)</button>
          <div class="hr"></div>
          <div id="pass-track" class="stack"></div>
        </div>

        <div class="panel tab-panel" id="tab-shop">
          <h3 class="h2">Rotating Shop</h3>
          <p class="subtext">매일 오퍼가 갱신됩니다. 코스메틱은 전투력에 직접 영향을 주지 않습니다.</p>
          <div class="kv"><span>Next Refresh</span><strong id="shop-refresh-kv">-</strong></div>
          <div id="shop-offers" class="grid-2"></div>
        </div>

        <div class="panel tab-panel" id="tab-capsule">
          <h3 class="h2">Gene Capsule</h3>
          <p class="subtext">10회 누적 시 Epic 확정(pity). 중복 코스메틱은 Credits로 변환됩니다.</p>
          <div class="kv"><span>Pity</span><strong id="pity-kv">0 / 10</strong></div>
          <div class="kv"><span>Capsule Ticket</span><strong id="ticket-kv">0</strong></div>
          <div style="display:flex; gap:8px; margin-top:8px;">
            <button class="btn" id="capsule-open-credit-btn">Open (120 Credits)</button>
            <button class="ghost-btn" id="capsule-open-ticket-btn">Open (1 Ticket)</button>
          </div>
          <div class="hr"></div>
          <div id="capsule-log" class="stack"></div>
        </div>

        <div class="panel tab-panel" id="tab-lab">
          <h3 class="h2">Evolution Lab</h3>
          <p class="subtext">런 외부에서 영구 강화. 난이도는 올라가도 성장 감각이 유지되게 설계했습니다.</p>
          <div id="lab-upgrades" class="grid-2"></div>
          <div class="hr"></div>
          <h3 class="h2">Cosmetic Skins</h3>
          <div id="skin-list" class="grid-2"></div>
        </div>

        <div class="panel tab-panel" id="tab-ranking">
          <h3 class="h2">Local Leaderboard</h3>
          <div id="ranking-list" class="stack"></div>
        </div>
      </div>
    </div>

    <div id="run-layer">
      <canvas id="arena"></canvas>

      <div class="run-hud">
        <div class="run-box">
          <div class="run-row">
            <div class="k">HP</div>
            <div class="bar hp"><i id="run-hp-fill"></i></div>
            <div id="run-hp-text">0/0</div>
          </div>
          <div class="run-row">
            <div class="k">ENERGY</div>
            <div class="bar en"><i id="run-en-fill"></i></div>
            <div id="run-en-text">0/0</div>
          </div>
        </div>
        <div class="run-box">
          <div class="kv"><span>Sector</span><strong id="run-sector-kv">1</strong></div>
          <div class="kv"><span>Score</span><strong id="run-score-kv">0</strong></div>
          <div class="kv"><span>Kills</span><strong id="run-kills-kv">0</strong></div>
          <div class="kv"><span>Build</span><strong id="run-build-kv">-</strong></div>
        </div>
      </div>

      <div id="toast">Ready</div>

      <div class="modal" id="draft-modal">
        <div class="modal-card">
          <h3 class="h2">Mutation Draft</h3>
          <p class="subtext">3개 중 1개 선택. 현재 빌드 시너지를 보고 고르세요.</p>
          <div class="draft-grid" id="draft-grid"></div>
          <p class="note">팁: 섹터 3, 6은 보스 압력이 강하므로 생존 카드 1장은 확보하는 것이 안정적입니다.</p>
        </div>
      </div>

      <div class="modal" id="end-modal">
        <div class="modal-card">
          <h3 class="h2" id="end-title">Run End</h3>
          <div id="end-summary" class="stack"></div>
          <div style="margin-top:10px; display:flex; gap:8px;">
            <button class="btn" id="end-retry-btn">다시 시작</button>
            <button class="ghost-btn" id="end-lobby-btn">로비로</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    (() => {
      'use strict';

      // ---------- constants ----------
      const SAVE_KEY = 'evolio_frontier_protocol_v1';
      const SAVE_VERSION = 1;
      const STAMINA_MAX = 8;
      const STAMINA_REGEN_MS = 20 * 60 * 1000;
      const PASS_TIER_XP = 120;
      const CANVAS_WORLD_RADIUS = 1700;
      const DPR = Math.min(window.devicePixelRatio || 1, 2);

      const STORY_CHAPTERS = [
        '태초의 세포는 프론티어 해역으로 유입되었다. 모든 것은 흡수와 진화의 속도로 결정된다.',
        '아미노 사냥군이 증식했다. 포식형 군집은 느린 개체를 우선적으로 제거한다.',
        '지질 장벽 군락이 형성되었다. 정면 교전보다 빌드 시너지가 생존을 좌우한다.',
        'ATP 폭풍이 시작됐다. 과부하 구역에서는 쿨다운 관리가 승률을 지배한다.',
        '프론티어 심연 코어가 깨어난다. 이제 네트워크의 최상위 포식자를 넘어서야 한다.'
      ];

      const SKINS = [
        { id: 'proto', name: 'Proto Cell', rarity: 'Common', color: '#58f0ba' },
        { id: 'amber', name: 'Amber Predator', rarity: 'Rare', color: '#ff9f6e' },
        { id: 'azure', name: 'Azure Tank', rarity: 'Rare', color: '#73b6ff' },
        { id: 'violet', name: 'Violet Surge', rarity: 'Epic', color: '#bd8dff' },
        { id: 'obsidian', name: 'Obsidian Maw', rarity: 'Epic', color: '#ff758f' },
        { id: 'neon', name: 'Neon Frontier', rarity: 'Legend', color: '#7dfff6' }
      ];

      const LAB_DEFS = [
        { id: 'core', name: 'Core Genome', desc: '공격력 +7% / Lv', baseCost: 130, max: 15 },
        { id: 'membrane', name: 'Membrane Matrix', desc: '최대HP +9%, 방어 +2 / Lv', baseCost: 145, max: 15 },
        { id: 'reactor', name: 'ATP Reactor', desc: '에너지회복 +10%, 스킬쿨감 / Lv', baseCost: 160, max: 12 },
        { id: 'drone', name: 'Nano Drone', desc: '자동탄막 성능 +8% / Lv', baseCost: 150, max: 12 }
      ];

      const MUTATION_POOL = [
        { id: 'atk_1', name: 'Predator Spikes', tags: ['ATK'], desc: '공격력 +25%', apply: (r) => { r.player.stats.attack *= 1.25; } },
        { id: 'atk_2', name: 'Razor Enzyme', tags: ['ATK'], desc: '치명타 확률 +12%', apply: (r) => { r.player.stats.crit += 0.12; } },
        { id: 'spd_1', name: 'Flagella Burst', tags: ['SPD'], desc: '이동속도 +20%', apply: (r) => { r.player.stats.speed *= 1.2; } },
        { id: 'spd_2', name: 'Blink Reflex', tags: ['SPD'], desc: '대시 쿨다운 -18%', apply: (r) => { r.player.stats.dashCd *= 0.82; } },
        { id: 'tank_1', name: 'Lipid Armor', tags: ['DEF'], desc: '최대 HP +24%', apply: (r) => { r.player.maxHp *= 1.24; r.player.hp = Math.min(r.player.maxHp, r.player.hp + 40); } },
        { id: 'tank_2', name: 'Adaptive Shell', tags: ['DEF'], desc: '방어 +14', apply: (r) => { r.player.stats.armor += 14; } },
        { id: 'eng_1', name: 'ATP Converter', tags: ['ENG'], desc: '에너지 재생 +25%', apply: (r) => { r.player.stats.energyRegen *= 1.25; } },
        { id: 'eng_2', name: 'Pulse Resonance', tags: ['ENG'], desc: '펄스 피해 +35%', apply: (r) => { r.player.stats.pulseDamage *= 1.35; } },
        { id: 'drone_1', name: 'Hunter Swarm', tags: ['DRN'], desc: '자동 탄환 수 +1', apply: (r) => { r.player.stats.multishot += 1; } },
        { id: 'drone_2', name: 'Neuro Targeting', tags: ['DRN'], desc: '발사속도 +18%', apply: (r) => { r.player.stats.fireRate *= 1.18; } },
        { id: 'leech', name: 'Bio Leech', tags: ['ATK','DEF'], desc: '흡혈 +5%', apply: (r) => { r.player.stats.lifeSteal += 0.05; } },
        { id: 'overclock', name: 'Overclock', tags: ['ATK','SPD'], desc: '공격/속도 +12%', apply: (r) => { r.player.stats.attack *= 1.12; r.player.stats.speed *= 1.12; } }
      ];

      const PASS_TIERS = Array.from({ length: 30 }, (_, i) => {
        const tier = i + 1;
        const freeReward = (tier % 5 === 0)
          ? { type: 'ticket', value: 1 }
          : { type: 'credits', value: 120 + tier * 24 };
        const premiumReward = (tier % 10 === 0)
          ? { type: 'skin', value: tier === 10 ? 'amber' : tier === 20 ? 'violet' : 'neon' }
          : (tier % 3 === 0 ? { type: 'genesis', value: 18 + tier } : { type: 'credits', value: 190 + tier * 30 });
        return { tier, freeReward, premiumReward };
      });

      // ---------- elements ----------
      const el = {
        pilotNamePill: document.getElementById('pilot-name-pill'),
        creditsPill: document.getElementById('credits-pill'),
        genesisPill: document.getElementById('genesis-pill'),
        staminaPill: document.getElementById('stamina-pill'),
        passXpPill: document.getElementById('pass-xp-pill'),
        seasonLabel: document.getElementById('season-label'),
        startRunBtn: document.getElementById('start-run-btn'),
        staminaRefillBtn: document.getElementById('stamina-refill-btn'),
        storyText: document.getElementById('story-text'),
        chapterKv: document.getElementById('chapter-kv'),
        objectiveKv: document.getElementById('objective-kv'),
        bestRunKv: document.getElementById('best-run-kv'),
        bestSectorKv: document.getElementById('best-sector-kv'),
        runsKv: document.getElementById('runs-kv'),
        killsKv: document.getElementById('kills-kv'),
        timeKv: document.getElementById('time-kv'),
        checkpointKv: document.getElementById('checkpoint-kv'),
        pilotInput: document.getElementById('pilot-input'),
        pilotSaveBtn: document.getElementById('pilot-save-btn'),
        tabs: document.getElementById('tabs'),
        tabPanels: {
          overview: document.getElementById('tab-overview'),
          missions: document.getElementById('tab-missions'),
          pass: document.getElementById('tab-pass'),
          shop: document.getElementById('tab-shop'),
          capsule: document.getElementById('tab-capsule'),
          lab: document.getElementById('tab-lab'),
          ranking: document.getElementById('tab-ranking')
        },
        dailyMissions: document.getElementById('daily-missions'),
        weeklyMissions: document.getElementById('weekly-missions'),
        passLevelKv: document.getElementById('pass-level-kv'),
        premiumKv: document.getElementById('premium-kv'),
        buyPremiumBtn: document.getElementById('buy-premium-btn'),
        passTrack: document.getElementById('pass-track'),
        shopRefreshKv: document.getElementById('shop-refresh-kv'),
        shopOffers: document.getElementById('shop-offers'),
        pityKv: document.getElementById('pity-kv'),
        ticketKv: document.getElementById('ticket-kv'),
        capsuleOpenCreditBtn: document.getElementById('capsule-open-credit-btn'),
        capsuleOpenTicketBtn: document.getElementById('capsule-open-ticket-btn'),
        capsuleLog: document.getElementById('capsule-log'),
        labUpgrades: document.getElementById('lab-upgrades'),
        skinList: document.getElementById('skin-list'),
        rankingList: document.getElementById('ranking-list'),
        runLayer: document.getElementById('run-layer'),
        arena: document.getElementById('arena'),
        toast: document.getElementById('toast'),
        runHpFill: document.getElementById('run-hp-fill'),
        runEnFill: document.getElementById('run-en-fill'),
        runHpText: document.getElementById('run-hp-text'),
        runEnText: document.getElementById('run-en-text'),
        runSectorKv: document.getElementById('run-sector-kv'),
        runScoreKv: document.getElementById('run-score-kv'),
        runKillsKv: document.getElementById('run-kills-kv'),
        runBuildKv: document.getElementById('run-build-kv'),
        draftModal: document.getElementById('draft-modal'),
        draftGrid: document.getElementById('draft-grid'),
        endModal: document.getElementById('end-modal'),
        endTitle: document.getElementById('end-title'),
        endSummary: document.getElementById('end-summary'),
        endRetryBtn: document.getElementById('end-retry-btn'),
        endLobbyBtn: document.getElementById('end-lobby-btn')
      };

      const ctx = el.arena.getContext('2d');

      // ---------- util ----------
      const clamp = (v, min, max) => Math.max(min, Math.min(max, v));
      const rand = (min, max) => Math.random() * (max - min) + min;
      const chance = (p) => Math.random() < p;
      const nfmt = (n) => Number(n || 0).toLocaleString();
      const nowMs = () => Date.now();

      function weekKey() {
        const d = new Date();
        const oneJan = new Date(d.getFullYear(), 0, 1);
        const day = Math.floor((d - oneJan) / 86400000);
        return d.getFullYear() + '-W' + Math.ceil((day + oneJan.getDay() + 1) / 7);
      }

      function dateKey() {
        return new Date().toISOString().slice(0, 10);
      }

      function nextDateLabel() {
        const n = new Date();
        n.setUTCDate(n.getUTCDate() + 1);
        return n.toISOString().slice(5, 10);
      }

      function toast(msg, sec = 1.4) {
        el.toast.textContent = msg;
        el.toast.style.opacity = '1';
        clearTimeout(toast._t);
        toast._t = setTimeout(() => { el.toast.style.opacity = '0'; }, sec * 1000);
      }

      function readStorage() {
        try { return localStorage.getItem(SAVE_KEY); } catch (e) { return null; }
      }

      function writeStorage(raw) {
        try { localStorage.setItem(SAVE_KEY, raw); return true; } catch (e) { return false; }
      }

      function staminaRefresh(meta) {
        const now = nowMs();
        if (!Number.isFinite(meta.resources.staminaTs)) {
          meta.resources.staminaTs = now;
        }
        if (meta.resources.stamina >= STAMINA_MAX) {
          meta.resources.stamina = STAMINA_MAX;
          meta.resources.staminaTs = now;
          return false;
        }
        const elapsed = now - meta.resources.staminaTs;
        if (elapsed < STAMINA_REGEN_MS) return false;
        const gain = Math.floor(elapsed / STAMINA_REGEN_MS);
        meta.resources.stamina = Math.min(STAMINA_MAX, meta.resources.stamina + gain);
        meta.resources.staminaTs += gain * STAMINA_REGEN_MS;
        return true;
      }

      function missionRewardText(rew) {
        const items = [];
        if (rew.credits) items.push('Credits ' + rew.credits);
        if (rew.genesis) items.push('Genesis ' + rew.genesis);
        if (rew.passXp) items.push('PassXP ' + rew.passXp);
        if (rew.ticket) items.push('Ticket ' + rew.ticket);
        return items.join(' · ');
      }

      function makeDailyMissions(seed) {
        const seedNum = Number(seed.replaceAll('-', '')) || 20260211;
        const shiftA = seedNum % 3;
        const shiftB = (Math.floor(seedNum / 7)) % 3;
        return [
          {
            id: 'd_run',
            title: 'Daily Run',
            type: 'run',
            target: 1 + shiftA,
            progress: 0,
            claimed: false,
            reward: { credits: 360 + shiftA * 60, passXp: 90 }
          },
          {
            id: 'd_kill',
            title: 'Daily Hunt',
            type: 'kill',
            target: 60 + shiftB * 20,
            progress: 0,
            claimed: false,
            reward: { credits: 280 + shiftB * 80, genesis: 14 }
          },
          {
            id: 'd_sector',
            title: 'Daily Sector Push',
            type: 'sector',
            target: 3 + shiftA,
            progress: 0,
            claimed: false,
            reward: { credits: 260, passXp: 120, ticket: 1 }
          }
        ];
      }

      function makeWeeklyMissions(seed) {
        const sum = seed.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
        const shift = sum % 3;
        return [
          {
            id: 'w_score',
            title: 'Weekly Score Break',
            type: 'score',
            target: 18000 + shift * 6000,
            progress: 0,
            claimed: false,
            reward: { credits: 1800, genesis: 45, passXp: 250 }
          },
          {
            id: 'w_run',
            title: 'Weekly Expedition',
            type: 'run',
            target: 9 + shift * 2,
            progress: 0,
            claimed: false,
            reward: { credits: 1500, passXp: 210 }
          },
          {
            id: 'w_capsule',
            title: 'Weekly Capsule Lab',
            type: 'capsule',
            target: 6 + shift,
            progress: 0,
            claimed: false,
            reward: { genesis: 58, ticket: 2, passXp: 180 }
          }
        ];
      }

      function shopSeedOffers(seed) {
        const catalog = [
          { kind: 'skin', id: 'amber', costC: 1350, costG: 0, title: 'Amber Predator Skin' },
          { kind: 'skin', id: 'azure', costC: 1350, costG: 0, title: 'Azure Tank Skin' },
          { kind: 'skin', id: 'violet', costC: 0, costG: 110, title: 'Violet Surge Skin' },
          { kind: 'skin', id: 'obsidian', costC: 0, costG: 120, title: 'Obsidian Maw Skin' },
          { kind: 'bundle', id: 'starter', costC: 0, costG: 80, title: 'Starter Bundle (+1400C, +2T)' },
          { kind: 'bundle', id: 'stamina', costC: 0, costG: 35, title: 'Stamina Pack (+4⚡)' },
          { kind: 'bundle', id: 'ticket', costC: 650, costG: 0, title: 'Capsule Ticket x2' },
          { kind: 'bundle', id: 'credit', costC: 0, costG: 25, title: 'Credit Pack (+900C)' }
        ];
        const value = seed.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
        const out = [];
        for (let i = 0; i < 4; i++) {
          const idx = (value + i * 3) % catalog.length;
          out.push({ ...catalog[idx], offerId: seed + '_' + i + '_' + idx, bought: false });
        }
        return out;
      }

      function emptyMeta() {
        return {
          version: SAVE_VERSION,
          season: 1,
          pilot: 'CellPilot',
          resources: {
            credits: 1200,
            genesis: 120,
            stamina: 6,
            staminaTs: nowMs(),
            passXp: 0,
            capsuleTicket: 1
          },
          story: {
            chapter: 1
          },
          inventory: {
            skinsUnlocked: ['proto'],
            equippedSkin: 'proto'
          },
          lab: {
            core: 0,
            membrane: 0,
            reactor: 0,
            drone: 0
          },
          bm: {
            premiumPass: false,
            pity: 0
          },
          missions: {
            dailyKey: dateKey(),
            daily: makeDailyMissions(dateKey()),
            weeklyKey: weekKey(),
            weekly: makeWeeklyMissions(weekKey())
          },
          pass: {
            claimedFree: [],
            claimedPremium: []
          },
          shop: {
            key: dateKey(),
            offers: shopSeedOffers(dateKey())
          },
          stats: {
            totalRuns: 0,
            totalKills: 0,
            totalPlaySec: 0,
            bestScore: 0,
            bestSector: 1
          },
          leaderboard: [],
          capsuleLog: [],
          activeSession: null
        };
      }

      function normalizeMeta(raw) {
        const d = emptyMeta();
        const src = raw && typeof raw === 'object' ? raw : {};
        const out = {
          version: SAVE_VERSION,
          season: Number.isFinite(src.season) ? Math.max(1, Math.floor(src.season)) : d.season,
          pilot: typeof src.pilot === 'string' && src.pilot.trim() ? src.pilot.slice(0, 16) : d.pilot,
          resources: {
            credits: Math.max(0, Math.floor(src.resources?.credits ?? d.resources.credits)),
            genesis: Math.max(0, Math.floor(src.resources?.genesis ?? d.resources.genesis)),
            stamina: Math.max(0, Math.min(STAMINA_MAX, Math.floor(src.resources?.stamina ?? d.resources.stamina))),
            staminaTs: Number.isFinite(src.resources?.staminaTs) ? src.resources.staminaTs : nowMs(),
            passXp: Math.max(0, Math.floor(src.resources?.passXp ?? d.resources.passXp)),
            capsuleTicket: Math.max(0, Math.floor(src.resources?.capsuleTicket ?? d.resources.capsuleTicket))
          },
          story: {
            chapter: Math.max(1, Math.min(STORY_CHAPTERS.length, Math.floor(src.story?.chapter ?? d.story.chapter)))
          },
          inventory: {
            skinsUnlocked: Array.isArray(src.inventory?.skinsUnlocked) ? src.inventory.skinsUnlocked.filter((s) => SKINS.some((k) => k.id === s)) : ['proto'],
            equippedSkin: typeof src.inventory?.equippedSkin === 'string' ? src.inventory.equippedSkin : 'proto'
          },
          lab: {
            core: Math.max(0, Math.min(15, Math.floor(src.lab?.core ?? 0))),
            membrane: Math.max(0, Math.min(15, Math.floor(src.lab?.membrane ?? 0))),
            reactor: Math.max(0, Math.min(12, Math.floor(src.lab?.reactor ?? 0))),
            drone: Math.max(0, Math.min(12, Math.floor(src.lab?.drone ?? 0)))
          },
          bm: {
            premiumPass: Boolean(src.bm?.premiumPass),
            pity: Math.max(0, Math.min(9, Math.floor(src.bm?.pity ?? 0)))
          },
          missions: src.missions || d.missions,
          pass: {
            claimedFree: Array.isArray(src.pass?.claimedFree) ? src.pass.claimedFree.slice(0, 200) : [],
            claimedPremium: Array.isArray(src.pass?.claimedPremium) ? src.pass.claimedPremium.slice(0, 200) : []
          },
          shop: src.shop || d.shop,
          stats: {
            totalRuns: Math.max(0, Math.floor(src.stats?.totalRuns ?? 0)),
            totalKills: Math.max(0, Math.floor(src.stats?.totalKills ?? 0)),
            totalPlaySec: Math.max(0, Math.floor(src.stats?.totalPlaySec ?? 0)),
            bestScore: Math.max(0, Math.floor(src.stats?.bestScore ?? 0)),
            bestSector: Math.max(1, Math.floor(src.stats?.bestSector ?? 1))
          },
          leaderboard: Array.isArray(src.leaderboard) ? src.leaderboard.slice(0, 60) : [],
          capsuleLog: Array.isArray(src.capsuleLog) ? src.capsuleLog.slice(0, 20) : [],
          activeSession: src.activeSession && typeof src.activeSession === 'object' ? src.activeSession : null
        };

        if (!out.inventory.skinsUnlocked.includes('proto')) out.inventory.skinsUnlocked.push('proto');
        if (!out.inventory.skinsUnlocked.includes(out.inventory.equippedSkin)) out.inventory.equippedSkin = 'proto';
        return out;
      }

      function loadMeta() {
        const raw = readStorage();
        if (!raw) return emptyMeta();
        try { return normalizeMeta(JSON.parse(raw)); } catch (e) { return emptyMeta(); }
      }

      function saveMeta() {
        writeStorage(JSON.stringify(meta));
      }

      function ensureMissionReset() {
        const dKey = dateKey();
        const wKey = weekKey();
        let changed = false;
        if (!meta.missions || meta.missions.dailyKey !== dKey) {
          meta.missions.dailyKey = dKey;
          meta.missions.daily = makeDailyMissions(dKey);
          changed = true;
        }
        if (!meta.missions || meta.missions.weeklyKey !== wKey) {
          meta.missions.weeklyKey = wKey;
          meta.missions.weekly = makeWeeklyMissions(wKey);
          changed = true;
        }
        if (!meta.shop || meta.shop.key !== dKey) {
          meta.shop = { key: dKey, offers: shopSeedOffers(dKey) };
          changed = true;
        }
        if (changed) saveMeta();
      }

      function missionTrack(type, amount) {
        const groups = [meta.missions.daily, meta.missions.weekly];
        for (const list of groups) {
          for (const m of list) {
            if (m.type !== type) continue;
            m.progress = clamp((m.progress || 0) + amount, 0, m.target);
          }
        }
      }

      function missionClaim(scope, id) {
        const list = scope === 'daily' ? meta.missions.daily : meta.missions.weekly;
        const m = list.find((x) => x.id === id);
        if (!m || m.claimed || m.progress < m.target) return;
        m.claimed = true;
        grantReward(m.reward, 'mission');
        toast('미션 보상 수령 완료');
        saveMeta();
        renderAll();
      }

      function grantReward(reward, reason = 'reward') {
        if (reward.credits) meta.resources.credits += reward.credits;
        if (reward.genesis) meta.resources.genesis += reward.genesis;
        if (reward.passXp) meta.resources.passXp += reward.passXp;
        if (reward.ticket) meta.resources.capsuleTicket += reward.ticket;
        if (reward.skin) {
          if (!meta.inventory.skinsUnlocked.includes(reward.skin)) {
            meta.inventory.skinsUnlocked.push(reward.skin);
            toast('신규 스킨 해금: ' + skinName(reward.skin));
          } else {
            meta.resources.credits += 380;
            toast('중복 스킨 변환: +380 Credits');
          }
        }
        if (reason !== 'mission') saveMeta();
      }

      function passLevel() {
        return Math.floor(meta.resources.passXp / PASS_TIER_XP) + 1;
      }

      function hasPassClaimed(type, tier) {
        const key = type === 'free' ? meta.pass.claimedFree : meta.pass.claimedPremium;
        return key.includes(tier);
      }

      function passClaim(type, tier) {
        const lv = passLevel();
        if (lv < tier) return;
        if (hasPassClaimed(type, tier)) return;
        if (type === 'premium' && !meta.bm.premiumPass) return;
        const row = PASS_TIERS.find((x) => x.tier === tier);
        if (!row) return;
        const reward = type === 'free' ? row.freeReward : row.premiumReward;
        grantReward(reward, 'pass');
        if (type === 'free') meta.pass.claimedFree.push(tier);
        else meta.pass.claimedPremium.push(tier);
        saveMeta();
        renderAll();
      }

      function skinName(id) {
        const s = SKINS.find((k) => k.id === id);
        return s ? s.name : id;
      }

      function labCost(def, lv) {
        return Math.floor(def.baseCost * Math.pow(1.44, lv + 0.08));
      }

      // ---------- render ----------
      let activeTab = 'overview';

      function renderTabs() {
        [...el.tabs.querySelectorAll('.tab-btn')].forEach((b) => {
          b.classList.toggle('active', b.dataset.tab === activeTab);
        });
        Object.keys(el.tabPanels).forEach((k) => {
          el.tabPanels[k].classList.toggle('active', k === activeTab);
        });
      }

      function renderTop() {
        staminaRefresh(meta);
        el.pilotNamePill.textContent = meta.pilot;
        el.creditsPill.textContent = nfmt(meta.resources.credits);
        el.genesisPill.textContent = nfmt(meta.resources.genesis);
        el.staminaPill.textContent = meta.resources.stamina + '/' + STAMINA_MAX;
        el.passXpPill.textContent = nfmt(meta.resources.passXp);
        el.seasonLabel.textContent = 'SEASON ' + meta.season + ' · FRONTIER';
        el.startRunBtn.disabled = meta.resources.stamina <= 0 || runState.running;
      }

      function renderStory() {
        const chapter = clamp(meta.story.chapter, 1, STORY_CHAPTERS.length);
        const objective = chapter === 1 ? 'Sector 3 clear'
          : chapter === 2 ? 'Sector 4 clear'
            : chapter === 3 ? 'Sector 5 clear'
              : chapter === 4 ? 'Sector 6 clear'
                : 'High score 30,000';
        el.storyText.textContent = STORY_CHAPTERS[chapter - 1];
        el.chapterKv.textContent = String(chapter);
        el.objectiveKv.textContent = objective;
        el.bestRunKv.textContent = nfmt(meta.stats.bestScore);
        el.bestSectorKv.textContent = String(meta.stats.bestSector);
      }

      function renderPilot() {
        if (document.activeElement !== el.pilotInput) el.pilotInput.value = meta.pilot;
        el.runsKv.textContent = nfmt(meta.stats.totalRuns);
        el.killsKv.textContent = nfmt(meta.stats.totalKills);
        el.timeKv.textContent = Math.floor(meta.stats.totalPlaySec / 60) + 'm';
        el.checkpointKv.textContent = meta.activeSession
          ? ('S' + (meta.activeSession.sector || 1) + ' · ' + nfmt(meta.activeSession.score || 0))
          : '-';
      }

      function renderMissionList(container, list, scope) {
        container.innerHTML = '';
        list.forEach((m) => {
          const done = m.progress >= m.target;
          const claimed = Boolean(m.claimed);
          const item = document.createElement('div');
          item.className = 'mission-card' + (done ? ' done' : '');
          const pct = Math.floor((m.progress / m.target) * 100);
          item.innerHTML = ''
            + '<div class="mission-top"><strong>' + m.title + '</strong><span class="reward">' + missionRewardText(m.reward) + '</span></div>'
            + '<div class="tiny">' + m.progress + ' / ' + m.target + (claimed ? ' · CLAIMED' : '') + '</div>'
            + '<div class="track"><i style="width:' + clamp(pct, 0, 100) + '%"></i></div>'
            + '<div style="margin-top:7px;">'
            + '<button class="ghost-btn mission-claim-btn" data-scope="' + scope + '" data-id="' + m.id + '" ' + ((done && !claimed) ? '' : 'disabled') + '>'
            + (claimed ? '수령 완료' : '보상 수령')
            + '</button></div>';
          container.appendChild(item);
        });
      }

      function renderMissions() {
        renderMissionList(el.dailyMissions, meta.missions.daily, 'daily');
        renderMissionList(el.weeklyMissions, meta.missions.weekly, 'weekly');
      }

      function renderPass() {
        const level = passLevel();
        el.passLevelKv.textContent = String(level);
        el.premiumKv.textContent = meta.bm.premiumPass ? 'ON' : 'OFF';
        el.buyPremiumBtn.disabled = meta.bm.premiumPass || meta.resources.genesis < 240;
        el.buyPremiumBtn.textContent = meta.bm.premiumPass ? 'Premium Activated' : 'Premium Unlock (240 Genesis)';

        el.passTrack.innerHTML = '';
        PASS_TIERS.forEach((row) => {
          const unlocked = level >= row.tier;
          const fClaimed = hasPassClaimed('free', row.tier);
          const pClaimed = hasPassClaimed('premium', row.tier);
          const card = document.createElement('div');
          card.className = 'pass-card';
          card.innerHTML = ''
            + '<div class="pass-top"><strong>Tier ' + row.tier + '</strong><span class="badge">' + (unlocked ? 'UNLOCKED' : 'LOCKED') + '</span></div>'
            + '<div class="tiny">Free: ' + missionRewardText(row.freeReward) + '</div>'
            + '<div class="tiny">Premium: ' + missionRewardText(row.premiumReward) + '</div>'
            + '<div style="margin-top:7px; display:flex; gap:6px;">'
            + '<button class="ghost-btn pass-claim-btn" data-type="free" data-tier="' + row.tier + '" ' + ((unlocked && !fClaimed) ? '' : 'disabled') + '>'
            + (fClaimed ? 'Free claimed' : 'Claim Free') + '</button>'
            + '<button class="ghost-btn pass-claim-btn" data-type="premium" data-tier="' + row.tier + '" '
            + ((unlocked && meta.bm.premiumPass && !pClaimed) ? '' : 'disabled') + '>'
            + (pClaimed ? 'Premium claimed' : 'Claim Premium') + '</button>'
            + '</div>';
          el.passTrack.appendChild(card);
        });
      }

      function renderShop() {
        const refreshText = nextDateLabel() + ' 00:00 UTC';
        el.shopRefreshKv.textContent = refreshText;
        el.shopOffers.innerHTML = '';
        meta.shop.offers.forEach((offer) => {
          const canAfford = offer.costC > 0
            ? meta.resources.credits >= offer.costC
            : meta.resources.genesis >= offer.costG;
          const card = document.createElement('div');
          card.className = 'offer-card';
          card.innerHTML = ''
            + '<div class="offer-top"><strong>' + offer.title + '</strong><span class="badge">' + (offer.kind === 'skin' ? 'Cosmetic' : 'Bundle') + '</span></div>'
            + '<div class="tiny">Cost: ' + (offer.costC > 0 ? ('Credits ' + offer.costC) : ('Genesis ' + offer.costG)) + '</div>'
            + '<div style="margin-top:7px;">'
            + '<button class="ghost-btn offer-buy-btn" data-offer="' + offer.offerId + '" ' + ((!offer.bought && canAfford) ? '' : 'disabled') + '>'
            + (offer.bought ? '구매 완료' : '구매')
            + '</button>'
            + '</div>';
          el.shopOffers.appendChild(card);
        });
      }

      function renderCapsule() {
        el.pityKv.textContent = meta.bm.pity + ' / 10';
        el.ticketKv.textContent = String(meta.resources.capsuleTicket);
        el.capsuleOpenCreditBtn.disabled = meta.resources.credits < 120;
        el.capsuleOpenTicketBtn.disabled = meta.resources.capsuleTicket < 1;

        el.capsuleLog.innerHTML = '';
        if (!meta.capsuleLog.length) {
          el.capsuleLog.innerHTML = '<div class="offer-card"><div class="tiny">최근 기록 없음</div></div>';
          return;
        }
        meta.capsuleLog.forEach((r) => {
          const card = document.createElement('div');
          card.className = 'offer-card';
          card.innerHTML = '<div class="offer-top"><strong>' + r.label + '</strong><span class="badge">' + r.rarity + '</span></div>'
            + '<div class="tiny">' + r.time + '</div>';
          el.capsuleLog.appendChild(card);
        });
      }

      function renderLab() {
        el.labUpgrades.innerHTML = '';
        LAB_DEFS.forEach((def) => {
          const lv = meta.lab[def.id] || 0;
          const maxed = lv >= def.max;
          const cost = maxed ? 0 : labCost(def, lv);
          const card = document.createElement('div');
          card.className = 'lab-card';
          card.innerHTML = ''
            + '<div><strong>' + def.name + ' Lv.' + lv + '/' + def.max + '</strong></div>'
            + '<div class="tiny">' + def.desc + '</div>'
            + '<div style="margin-top:7px;">'
            + '<button class="ghost-btn lab-up-btn" data-up="' + def.id + '" ' + ((!maxed && meta.resources.credits >= cost) ? '' : 'disabled') + '>'
            + (maxed ? 'MAX' : ('Upgrade · ' + cost + ' Credits'))
            + '</button></div>';
          el.labUpgrades.appendChild(card);
        });

        el.skinList.innerHTML = '';
        SKINS.forEach((skin) => {
          const unlocked = meta.inventory.skinsUnlocked.includes(skin.id);
          const equipped = meta.inventory.equippedSkin === skin.id;
          const card = document.createElement('div');
          card.className = 'lab-card';
          card.innerHTML = ''
            + '<div><strong>' + skin.name + '</strong> <span class="badge">' + skin.rarity + '</span></div>'
            + '<div class="tiny">Color ' + skin.color + '</div>'
            + '<div style="margin-top:7px;">'
            + '<button class="ghost-btn skin-equip-btn" data-skin="' + skin.id + '" ' + ((unlocked && !equipped) ? '' : 'disabled') + '>'
            + (equipped ? '장착 중' : (unlocked ? '장착' : '잠김'))
            + '</button></div>';
          el.skinList.appendChild(card);
        });
      }

      function renderRanking() {
        el.rankingList.innerHTML = '';
        if (!meta.leaderboard.length) {
          el.rankingList.innerHTML = '<div class="rank-card"><div class="tiny">아직 기록이 없습니다.</div></div>';
          return;
        }
        meta.leaderboard.slice(0, 12).forEach((r, i) => {
          const card = document.createElement('div');
          card.className = 'rank-card';
          card.innerHTML = ''
            + '<div class="rank-top"><strong>#' + (i + 1) + ' · ' + nfmt(r.score) + '</strong><span class="badge">S' + r.sector + '</span></div>'
            + '<div class="tiny">' + r.pilot + ' · Kills ' + r.kills + ' · ' + r.date + '</div>';
          el.rankingList.appendChild(card);
        });
      }

      function renderAll() {
        ensureMissionReset();
        renderTop();
        renderStory();
        renderPilot();
        renderMissions();
        renderPass();
        renderShop();
        renderCapsule();
        renderLab();
        renderRanking();
        renderTabs();
      }

      // ---------- shop / capsule / lab actions ----------
      function buyPremium() {
        if (meta.bm.premiumPass) return;
        if (meta.resources.genesis < 240) {
          toast('Genesis 부족');
          return;
        }
        meta.resources.genesis -= 240;
        meta.bm.premiumPass = true;
        saveMeta();
        renderAll();
        toast('Premium Pass 활성화');
      }

      function buyShopOffer(offerId) {
        const offer = meta.shop.offers.find((x) => x.offerId === offerId);
        if (!offer || offer.bought) return;
        if (offer.costC > 0 && meta.resources.credits < offer.costC) return;
        if (offer.costG > 0 && meta.resources.genesis < offer.costG) return;
        if (offer.costC > 0) meta.resources.credits -= offer.costC;
        else meta.resources.genesis -= offer.costG;

        if (offer.kind === 'skin') {
          if (!meta.inventory.skinsUnlocked.includes(offer.id)) {
            meta.inventory.skinsUnlocked.push(offer.id);
            toast('스킨 구매: ' + skinName(offer.id));
          } else {
            meta.resources.credits += 260;
            toast('이미 보유: 중복 보상 +260 Credits');
          }
        } else {
          if (offer.id === 'starter') {
            meta.resources.credits += 1400;
            meta.resources.capsuleTicket += 2;
          } else if (offer.id === 'stamina') {
            meta.resources.stamina = Math.min(STAMINA_MAX, meta.resources.stamina + 4);
          } else if (offer.id === 'ticket') {
            meta.resources.capsuleTicket += 2;
          } else if (offer.id === 'credit') {
            meta.resources.credits += 900;
          }
          toast('번들 구매 완료');
        }
        offer.bought = true;
        missionTrack('purchase', 1);
        saveMeta();
        renderAll();
      }

      function capsuleDrop() {
        const pityHit = meta.bm.pity >= 9;
        const roll = Math.random();
        let rarity = 'Common';
        let reward = { type: 'credits', value: Math.floor(rand(85, 210)) };

        if (pityHit || roll > 0.94) {
          rarity = 'Epic';
          const lockedSkins = SKINS.filter((s) => s.rarity !== 'Common' && !meta.inventory.skinsUnlocked.includes(s.id));
          if (lockedSkins.length) {
            reward = { type: 'skin', value: lockedSkins[Math.floor(Math.random() * lockedSkins.length)].id };
          } else {
            reward = { type: 'genesis', value: Math.floor(rand(35, 65)) };
          }
          meta.bm.pity = 0;
        } else if (roll > 0.72) {
          rarity = 'Rare';
          reward = chance(0.5)
            ? { type: 'genesis', value: Math.floor(rand(10, 22)) }
            : { type: 'ticket', value: 1 };
          meta.bm.pity += 1;
        } else {
          rarity = 'Common';
          reward = chance(0.75)
            ? { type: 'credits', value: Math.floor(rand(85, 210)) }
            : { type: 'passXp', value: Math.floor(rand(25, 58)) };
          meta.bm.pity += 1;
        }

        if (reward.type === 'skin') {
          if (!meta.inventory.skinsUnlocked.includes(reward.value)) {
            meta.inventory.skinsUnlocked.push(reward.value);
          } else {
            reward = { type: 'credits', value: 420 };
            rarity = 'Duplicate';
          }
        }

        if (reward.type === 'credits') meta.resources.credits += reward.value;
        if (reward.type === 'genesis') meta.resources.genesis += reward.value;
        if (reward.type === 'ticket') meta.resources.capsuleTicket += reward.value;
        if (reward.type === 'passXp') meta.resources.passXp += reward.value;

        const label = reward.type === 'skin'
          ? ('Skin · ' + skinName(reward.value))
          : (reward.type.charAt(0).toUpperCase() + reward.type.slice(1) + ' +' + reward.value);
        meta.capsuleLog.unshift({ label, rarity, time: new Date().toISOString().slice(5, 16).replace('T', ' ') });
        meta.capsuleLog = meta.capsuleLog.slice(0, 20);
        missionTrack('capsule', 1);
        saveMeta();
        renderAll();
        toast('Capsule: ' + label);
      }

      function openCapsuleByCredit() {
        if (meta.resources.credits < 120) return;
        meta.resources.credits -= 120;
        capsuleDrop();
      }

      function openCapsuleByTicket() {
        if (meta.resources.capsuleTicket < 1) return;
        meta.resources.capsuleTicket -= 1;
        capsuleDrop();
      }

      function refillStamina() {
        if (meta.resources.genesis < 30) {
          toast('Genesis 부족');
          return;
        }
        meta.resources.genesis -= 30;
        meta.resources.stamina = Math.min(STAMINA_MAX, meta.resources.stamina + 3);
        saveMeta();
        renderAll();
        toast('Stamina +3');
      }

      function upgradeLab(id) {
        const def = LAB_DEFS.find((x) => x.id === id);
        if (!def) return;
        const lv = meta.lab[id] || 0;
        if (lv >= def.max) return;
        const cost = labCost(def, lv);
        if (meta.resources.credits < cost) return;
        meta.resources.credits -= cost;
        meta.lab[id] = lv + 1;
        saveMeta();
        renderAll();
        toast(def.name + ' 업그레이드');
      }

      function equipSkin(id) {
        if (!meta.inventory.skinsUnlocked.includes(id)) return;
        meta.inventory.equippedSkin = id;
        saveMeta();
        renderAll();
        toast('스킨 장착: ' + skinName(id));
      }

      // ---------- run ----------
      const runState = {
        running: false,
        paused: false,
        ended: false,
        result: null,
        frame: 0
      };

      const input = {
        keys: {},
        dashPressed: false,
        pulsePressed: false
      };

      const arenaView = { w: 1, h: 1 };

      function resizeArena() {
        const rect = el.runLayer.getBoundingClientRect();
        arenaView.w = Math.max(1, Math.floor(rect.width));
        arenaView.h = Math.max(1, Math.floor(rect.height));
        el.arena.width = Math.floor(arenaView.w * DPR);
        el.arena.height = Math.floor(arenaView.h * DPR);
        ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      }

      function buildPlayer() {
        const coreLv = meta.lab.core || 0;
        const memLv = meta.lab.membrane || 0;
        const reactorLv = meta.lab.reactor || 0;
        const droneLv = meta.lab.drone || 0;
        const baseHp = 240 * (1 + memLv * 0.09);
        const baseAtk = 28 * (1 + coreLv * 0.07);
        const fireRate = 4.5 * (1 + droneLv * 0.08);
        const pulseCd = 5.2 * Math.pow(0.96, reactorLv);
        const dashCd = 2.2 * Math.pow(0.96, reactorLv);
        const enRegen = 20 * (1 + reactorLv * 0.1);

        return {
          x: 0,
          y: 0,
          vx: 0,
          vy: 0,
          radius: 22,
          hp: baseHp,
          maxHp: baseHp,
          energy: 130,
          maxEnergy: 130,
          dashTimer: 0,
          dashCdTimer: 0,
          pulseCdTimer: 0,
          shootTimer: 0,
          invuln: 0,
          stats: {
            speed: 235 + reactorLv * 3,
            attack: baseAtk,
            crit: 0.11 + coreLv * 0.004,
            armor: 10 + memLv * 2,
            lifeSteal: 0.03 + coreLv * 0.002,
            fireRate,
            enRegen,
            pulseCd,
            dashCd,
            pulseDamage: baseAtk * 3.1,
            projectileSpeed: 520 + droneLv * 14,
            multishot: 1,
            buildTags: []
          },
          color: (SKINS.find((s) => s.id === meta.inventory.equippedSkin) || SKINS[0]).color
        };
      }

      function makeEnemy(sector, type = null, elite = false) {
        const t = type || (Math.random() < 0.55 ? 'chaser' : (Math.random() < 0.7 ? 'shooter' : 'tank'));
        let hp = 80, speed = 95, dmg = 11, radius = 16, fireRate = 1.2;
        if (t === 'chaser') { hp = 72; speed = 130; dmg = 10; radius = 14; }
        if (t === 'shooter') { hp = 90; speed = 88; dmg = 12; radius = 16; fireRate = 1.45; }
        if (t === 'tank') { hp = 170; speed = 62; dmg = 18; radius = 23; }
        if (t === 'splitter') { hp = 110; speed = 108; dmg = 12; radius = 17; }
        if (t === 'boss') { hp = 860; speed = 76; dmg = 20; radius = 42; fireRate = 0.8; }

        const mHp = 1 + sector * 0.22;
        const mDmg = 1 + sector * 0.12;
        const eliteMul = elite ? 1.7 : 1.0;

        const angle = rand(0, Math.PI * 2);
        const distance = rand(700, 1200);
        const x = Math.cos(angle) * distance;
        const y = Math.sin(angle) * distance;

        return {
          id: Math.random().toString(36).slice(2, 9),
          type: t,
          elite,
          x,
          y,
          vx: 0,
          vy: 0,
          hp: hp * mHp * eliteMul,
          maxHp: hp * mHp * eliteMul,
          damage: dmg * mDmg * (elite ? 1.22 : 1),
          speed: speed * (1 + sector * 0.03),
          radius: radius * (elite ? 1.14 : 1),
          fireCd: rand(0.4, fireRate),
          splitCount: t === 'splitter' ? 2 : 0
        };
      }

      function createRun() {
        const player = buildPlayer();
        const targetKills = 18;
        return {
          sector: 1,
          score: 0,
          kills: 0,
          elapsed: 0,
          combo: 0,
          comboTimer: 0,
          player,
          enemies: [],
          bullets: [],
          enemyBullets: [],
          particles: [],
          floating: [],
          paused: false,
          phase: 'battle',
          spawnTimer: 0,
          spawned: 0,
          targetKills,
          bossSpawned: false,
          draftChoices: [],
          buildNames: [],
          saveTick: 0
        };
      }

      let run = null;
      let raf = null;
      let lastTs = 0;

      function startRun() {
        if (runState.running) return;
        staminaRefresh(meta);
        if (meta.resources.stamina <= 0) {
          toast('Stamina 부족');
          return;
        }
        meta.resources.stamina -= 1;
        meta.resources.staminaTs = nowMs();
        saveMeta();

        run = createRun();
        runState.running = true;
        runState.ended = false;
        runState.result = null;
        el.runLayer.style.display = 'block';
        el.endModal.style.display = 'none';
        el.draftModal.style.display = 'none';
        resizeArena();
        toast('Run 시작');
        lastTs = performance.now();
        raf = requestAnimationFrame(loop);
        renderAll();
      }

      function leaveRunToLobby() {
        runState.running = false;
        runState.ended = false;
        runState.result = null;
        run = null;
        if (raf) cancelAnimationFrame(raf);
        raf = null;
        el.runLayer.style.display = 'none';
        renderAll();
      }

      function finishRun(victory = false) {
        if (!run || runState.ended) return;
        runState.ended = true;
        runState.running = false;

        const sector = run.sector;
        const score = Math.floor(run.score);
        const kills = run.kills;
        const sec = Math.floor(run.elapsed);

        const rewards = {
          credits: Math.floor(score / 18 + sector * 80 + kills * 1.7),
          genesis: Math.max(0, Math.floor((sector - 2) * 2 + (victory ? 8 : 0))),
          passXp: Math.floor(80 + sector * 34 + kills * 0.8),
          ticket: (victory ? 1 : 0)
        };

        missionTrack('run', 1);
        missionTrack('kill', kills);
        missionTrack('sector', sector);
        missionTrack('score', score);

        grantReward(rewards, 'run');

        meta.stats.totalRuns += 1;
        meta.stats.totalKills += kills;
        meta.stats.totalPlaySec += sec;
        meta.stats.bestScore = Math.max(meta.stats.bestScore, score);
        meta.stats.bestSector = Math.max(meta.stats.bestSector, sector);

        if (victory && meta.story.chapter < STORY_CHAPTERS.length) {
          meta.story.chapter += 1;
          toast('스토리 챕터 상승');
        } else if (!victory && sector >= meta.story.chapter + 2 && meta.story.chapter < STORY_CHAPTERS.length) {
          meta.story.chapter += 1;
          toast('중간 돌파: 챕터 진척');
        }

        const row = {
          pilot: meta.pilot,
          score,
          sector,
          kills,
          date: new Date().toISOString().slice(5, 16).replace('T', ' ')
        };
        meta.leaderboard.push(row);
        meta.leaderboard.sort((a, b) => b.score - a.score || b.sector - a.sector);
        meta.leaderboard = meta.leaderboard.slice(0, 60);
        meta.activeSession = null;
        saveMeta();

        el.endTitle.textContent = victory ? 'RUN CLEAR' : 'CELL COLLAPSE';
        el.endSummary.innerHTML = ''
          + '<div class="offer-card"><div class="kv"><span>Score</span><strong>' + nfmt(score) + '</strong></div>'
          + '<div class="kv"><span>Sector</span><strong>' + sector + '</strong></div>'
          + '<div class="kv"><span>Kills</span><strong>' + kills + '</strong></div>'
          + '<div class="kv"><span>Time</span><strong>' + sec + 's</strong></div>'
          + '<div class="kv"><span>Rewards</span><strong>Credits ' + rewards.credits + ' · Genesis ' + rewards.genesis + ' · XP ' + rewards.passXp + (rewards.ticket ? ' · Ticket 1' : '') + '</strong></div></div>';
        el.endModal.style.display = 'flex';
        renderAll();
      }

      function chooseMutations() {
        const pool = [...MUTATION_POOL];
        const picks = [];
        while (picks.length < 3 && pool.length) {
          const idx = Math.floor(Math.random() * pool.length);
          picks.push(pool.splice(idx, 1)[0]);
        }
        run.draftChoices = picks;
      }

      function showDraft() {
        chooseMutations();
        el.draftGrid.innerHTML = '';
        run.draftChoices.forEach((m, idx) => {
          const card = document.createElement('div');
          card.className = 'draft-card';
          card.innerHTML = '<h4>' + m.name + '</h4><p>' + m.desc + '</p><p class="tiny">Tags: ' + m.tags.join(', ') + '</p>';
          card.addEventListener('click', () => {
            m.apply(run);
            run.buildNames.push(m.name);
            run.player.stats.buildTags.push(...m.tags);
            run.phase = 'battle';
            run.sector += 1;
            run.spawned = 0;
            run.targetKills = 16 + run.sector * 10;
            run.bossSpawned = false;
            run.spawnTimer = 0.2;
            el.draftModal.style.display = 'none';
            toast('Mutation: ' + m.name);
          });
          el.draftGrid.appendChild(card);
        });
        el.draftModal.style.display = 'flex';
      }

      function nearestEnemy(x, y) {
        let best = null;
        let bestD = Infinity;
        for (const e of run.enemies) {
          const dx = e.x - x;
          const dy = e.y - y;
          const d = dx * dx + dy * dy;
          if (d < bestD) { bestD = d; best = e; }
        }
        return best;
      }

      function spawnPlayerBullets() {
        const p = run.player;
        const target = nearestEnemy(p.x, p.y);
        if (!target) return;
        const baseAng = Math.atan2(target.y - p.y, target.x - p.x);
        const shots = p.stats.multishot;
        for (let i = 0; i < shots; i++) {
          const spread = shots === 1 ? 0 : ((i - (shots - 1) / 2) * 0.08);
          const ang = baseAng + spread;
          run.bullets.push({
            x: p.x + Math.cos(ang) * (p.radius + 4),
            y: p.y + Math.sin(ang) * (p.radius + 4),
            vx: Math.cos(ang) * p.stats.projectileSpeed,
            vy: Math.sin(ang) * p.stats.projectileSpeed,
            r: 4,
            dmg: p.stats.attack,
            life: 1.4
          });
        }
      }

      function fireEnemyBullet(e) {
        const p = run.player;
        const ang = Math.atan2(p.y - e.y, p.x - e.x);
        const speed = e.type === 'boss' ? 270 : 230;
        run.enemyBullets.push({
          x: e.x + Math.cos(ang) * (e.radius + 2),
          y: e.y + Math.sin(ang) * (e.radius + 2),
          vx: Math.cos(ang) * speed,
          vy: Math.sin(ang) * speed,
          r: e.type === 'boss' ? 6 : 4.5,
          dmg: e.damage * 0.8,
          life: 2.6
        });
      }

      function bossRingFire(e) {
        for (let i = 0; i < 12; i++) {
          const ang = (Math.PI * 2 * i) / 12 + rand(-0.02, 0.02);
          run.enemyBullets.push({
            x: e.x + Math.cos(ang) * (e.radius + 2),
            y: e.y + Math.sin(ang) * (e.radius + 2),
            vx: Math.cos(ang) * 190,
            vy: Math.sin(ang) * 190,
            r: 5,
            dmg: e.damage * 0.72,
            life: 2.2
          });
        }
      }

      function hitPlayer(rawDamage) {
        const p = run.player;
        if (p.invuln > 0) return;
        const mitig = 100 / (100 + p.stats.armor);
        const dmg = rawDamage * mitig;
        p.hp -= dmg;
        p.invuln = 0.1;
        if (p.hp <= 0) {
          p.hp = 0;
          finishRun(false);
        }
      }

      function killEnemy(e, index) {
        const p = run.player;
        run.enemies.splice(index, 1);
        run.kills += 1;
        run.combo += 1;
        run.comboTimer = 2.4;

        const bonus = 1 + run.combo * 0.04;
        run.score += Math.floor((e.maxHp * 1.25 + 30) * bonus);
        p.hp = Math.min(p.maxHp, p.hp + e.maxHp * p.stats.lifeSteal * 0.11);

        if (e.type === 'splitter' && e.splitCount > 0) {
          for (let i = 0; i < 2; i++) {
            const child = makeEnemy(run.sector, 'chaser', false);
            child.x = e.x + rand(-25, 25);
            child.y = e.y + rand(-25, 25);
            child.hp = e.maxHp * 0.34;
            child.maxHp = child.hp;
            child.radius *= 0.76;
            child.damage *= 0.7;
            run.enemies.push(child);
          }
        }
      }

      function spawnEnemyWave(dt) {
        if (run.phase !== 'battle') return;
        run.spawnTimer -= dt;
        if (run.spawnTimer > 0) return;

        const isBossSector = run.sector % 3 === 0;
        if (isBossSector && !run.bossSpawned) {
          run.enemies.push(makeEnemy(run.sector, 'boss', true));
          run.bossSpawned = true;
          run.spawned += 1;
          run.spawnTimer = 3.0;
          toast('Boss spawn');
          return;
        }

        if (run.spawned < run.targetKills + 6) {
          const burst = run.sector >= 4 ? 2 : 1;
          for (let i = 0; i < burst; i++) {
            const typeRoll = Math.random();
            const type = typeRoll < 0.46 ? 'chaser' : typeRoll < 0.74 ? 'shooter' : typeRoll < 0.92 ? 'tank' : 'splitter';
            run.enemies.push(makeEnemy(run.sector, type, run.sector >= 5 && Math.random() < 0.08));
            run.spawned += 1;
          }
        }
        run.spawnTimer = clamp(1.1 - run.sector * 0.1, 0.25, 1.1);
      }

      function updatePlayer(dt) {
        const p = run.player;
        p.invuln = Math.max(0, p.invuln - dt);
        p.energy = clamp(p.energy + p.stats.enRegen * dt, 0, p.maxEnergy);
        p.shootTimer -= dt;
        p.pulseCdTimer -= dt;
        p.dashCdTimer -= dt;

        let dx = 0;
        let dy = 0;
        if (input.keys['KeyW']) dy -= 1;
        if (input.keys['KeyS']) dy += 1;
        if (input.keys['KeyA']) dx -= 1;
        if (input.keys['KeyD']) dx += 1;
        const mag = Math.hypot(dx, dy) || 1;
        const speed = p.stats.speed * (p.dashTimer > 0 ? 3.1 : 1.0);
        const tvx = (dx / mag) * speed;
        const tvy = (dy / mag) * speed;
        p.vx += (tvx - p.vx) * clamp(dt * 10, 0, 1);
        p.vy += (tvy - p.vy) * clamp(dt * 10, 0, 1);

        p.x += p.vx * dt;
        p.y += p.vy * dt;
        p.dashTimer = Math.max(0, p.dashTimer - dt);

        const d = Math.hypot(p.x, p.y);
        const b = CANVAS_WORLD_RADIUS - p.radius - 8;
        if (d > b) {
          p.x = (p.x / d) * b;
          p.y = (p.y / d) * b;
          p.vx *= 0.2;
          p.vy *= 0.2;
        }

        if (input.dashPressed && p.dashCdTimer <= 0 && p.energy >= 26) {
          p.energy -= 26;
          p.dashCdTimer = p.stats.dashCd;
          p.dashTimer = 0.2;
          p.invuln = 0.2;
          toast('Dash');
        }

        if (input.pulsePressed && p.pulseCdTimer <= 0 && p.energy >= 40) {
          p.energy -= 40;
          p.pulseCdTimer = p.stats.pulseCd;
          const pulseR = 220;
          for (const e of run.enemies) {
            const ex = e.x - p.x;
            const ey = e.y - p.y;
            const dist = Math.hypot(ex, ey);
            if (dist <= pulseR + e.radius) {
              const fall = 1 - clamp(dist / pulseR, 0.1, 0.95);
              let damage = p.stats.pulseDamage * (0.7 + fall * 0.6);
              if (chance(p.stats.crit * 0.6)) damage *= 1.8;
              e.hp -= damage;
              e.vx += (ex / (dist || 1)) * 240;
              e.vy += (ey / (dist || 1)) * 240;
            }
          }
          toast('Bio Pulse');
        }

        if (p.shootTimer <= 0) {
          spawnPlayerBullets();
          p.shootTimer = 1 / p.stats.fireRate;
        }

        input.dashPressed = false;
        input.pulsePressed = false;
      }

      function updateEnemies(dt) {
        const p = run.player;
        for (let i = run.enemies.length - 1; i >= 0; i--) {
          const e = run.enemies[i];
          const dx = p.x - e.x;
          const dy = p.y - e.y;
          const dist = Math.hypot(dx, dy) || 1;
          const nx = dx / dist;
          const ny = dy / dist;

          if (e.type === 'shooter') {
            if (dist < 200) {
              e.vx += (-nx * e.speed - e.vx) * clamp(dt * 3, 0, 1);
              e.vy += (-ny * e.speed - e.vy) * clamp(dt * 3, 0, 1);
            } else {
              e.vx += (nx * e.speed - e.vx) * clamp(dt * 2, 0, 1);
              e.vy += (ny * e.speed - e.vy) * clamp(dt * 2, 0, 1);
            }
            e.fireCd -= dt;
            if (e.fireCd <= 0 && dist < 680) {
              fireEnemyBullet(e);
              e.fireCd = rand(0.9, 1.4);
            }
          } else if (e.type === 'boss') {
            e.vx += (nx * e.speed - e.vx) * clamp(dt * 1.8, 0, 1);
            e.vy += (ny * e.speed - e.vy) * clamp(dt * 1.8, 0, 1);
            e.fireCd -= dt;
            if (e.fireCd <= 0) {
              fireEnemyBullet(e);
              bossRingFire(e);
              e.fireCd = 1.25;
            }
          } else {
            e.vx += (nx * e.speed - e.vx) * clamp(dt * 3.2, 0, 1);
            e.vy += (ny * e.speed - e.vy) * clamp(dt * 3.2, 0, 1);
          }

          e.x += e.vx * dt;
          e.y += e.vy * dt;

          const fromCenter = Math.hypot(e.x, e.y);
          const bound = CANVAS_WORLD_RADIUS - e.radius - 4;
          if (fromCenter > bound) {
            e.x = (e.x / fromCenter) * bound;
            e.y = (e.y / fromCenter) * bound;
            e.vx *= 0.4;
            e.vy *= 0.4;
          }

          const overlap = p.radius + e.radius - dist;
          if (overlap > 0) {
            hitPlayer(e.damage * dt * 4.5);
            const dmg = p.stats.attack * dt * (p.dashTimer > 0 ? 9.2 : 2.6);
            e.hp -= dmg;
          }

          if (e.hp <= 0) {
            killEnemy(e, i);
          }
        }
      }

      function updateBullets(dt) {
        const p = run.player;
        for (let i = run.bullets.length - 1; i >= 0; i--) {
          const b = run.bullets[i];
          b.x += b.vx * dt;
          b.y += b.vy * dt;
          b.life -= dt;
          let removed = false;

          for (const e of run.enemies) {
            const dx = e.x - b.x;
            const dy = e.y - b.y;
            const rr = e.radius + b.r;
            if (dx * dx + dy * dy <= rr * rr) {
              let damage = b.dmg;
              if (chance(p.stats.crit)) damage *= 1.75;
              e.hp -= damage;
              removed = true;
              break;
            }
          }

          const d = Math.hypot(b.x, b.y);
          if (removed || b.life <= 0 || d > CANVAS_WORLD_RADIUS + 120) {
            run.bullets.splice(i, 1);
          }
        }

        for (let i = run.enemyBullets.length - 1; i >= 0; i--) {
          const b = run.enemyBullets[i];
          b.x += b.vx * dt;
          b.y += b.vy * dt;
          b.life -= dt;
          const dx = p.x - b.x;
          const dy = p.y - b.y;
          const rr = p.radius + b.r;
          if (dx * dx + dy * dy <= rr * rr) {
            hitPlayer(b.dmg);
            run.enemyBullets.splice(i, 1);
            continue;
          }
          const d = Math.hypot(b.x, b.y);
          if (b.life <= 0 || d > CANVAS_WORLD_RADIUS + 120) {
            run.enemyBullets.splice(i, 1);
          }
        }
      }

      function runBuildLabel() {
        const tags = run.player.stats.buildTags;
        const count = {};
        tags.forEach((t) => { count[t] = (count[t] || 0) + 1; });
        const sorted = Object.entries(count).sort((a, b) => b[1] - a[1]);
        if (!sorted.length) return 'Balanced';
        return sorted.slice(0, 2).map((x) => x[0] + 'x' + x[1]).join(' · ');
      }

      function updateRunHud() {
        const p = run.player;
        const hpRatio = clamp(p.hp / p.maxHp, 0, 1);
        const enRatio = clamp(p.energy / p.maxEnergy, 0, 1);
        el.runHpFill.style.width = (hpRatio * 100).toFixed(1) + '%';
        el.runEnFill.style.width = (enRatio * 100).toFixed(1) + '%';
        el.runHpText.textContent = Math.floor(p.hp) + '/' + Math.floor(p.maxHp);
        el.runEnText.textContent = Math.floor(p.energy) + '/' + Math.floor(p.maxEnergy);
        el.runSectorKv.textContent = String(run.sector);
        el.runScoreKv.textContent = nfmt(Math.floor(run.score));
        el.runKillsKv.textContent = nfmt(run.kills);
        el.runBuildKv.textContent = runBuildLabel();
      }

      function runStep(dt) {
        if (!run || runState.ended) return;
        if (run.paused) return;

        run.elapsed += dt;
        run.comboTimer -= dt;
        if (run.comboTimer <= 0) run.combo = 0;

        updatePlayer(dt);
        spawnEnemyWave(dt);
        updateEnemies(dt);
        updateBullets(dt);

        if (run.phase === 'battle' && run.kills >= run.targetKills && run.enemies.length === 0) {
          if (run.sector >= 6) {
            finishRun(true);
            return;
          }
          run.phase = 'draft';
          showDraft();
        }

        run.saveTick += dt;
        if (run.saveTick >= 8) {
          run.saveTick = 0;
          meta.activeSession = {
            score: Math.floor(run.score),
            sector: run.sector,
            stamp: new Date().toISOString()
          };
          saveMeta();
          el.checkpointKv.textContent = 'S' + run.sector + ' · ' + nfmt(Math.floor(run.score));
        }
      }

      function drawBackground(camX, camY) {
        const g = ctx.createLinearGradient(0, 0, 0, arenaView.h);
        g.addColorStop(0, '#051029');
        g.addColorStop(1, '#030710');
        ctx.fillStyle = g;
        ctx.fillRect(0, 0, arenaView.w, arenaView.h);

        const step = 72;
        const ox = ((-camX) % step + step) % step;
        const oy = ((-camY) % step + step) % step;
        ctx.beginPath();
        ctx.strokeStyle = 'rgba(113, 152, 214, 0.18)';
        ctx.lineWidth = 1;
        for (let x = ox; x < arenaView.w; x += step) {
          ctx.moveTo(x, 0);
          ctx.lineTo(x, arenaView.h);
        }
        for (let y = oy; y < arenaView.h; y += step) {
          ctx.moveTo(0, y);
          ctx.lineTo(arenaView.w, y);
        }
        ctx.stroke();
      }

      function drawRun() {
        if (!run) return;
        const p = run.player;
        const camX = p.x - arenaView.w / 2;
        const camY = p.y - arenaView.h / 2;

        drawBackground(camX * 0.3, camY * 0.3);

        const toScreen = (x, y) => ({ x: x - camX, y: y - camY });
        const center = toScreen(0, 0);

        // boundary
        ctx.beginPath();
        ctx.arc(center.x, center.y, CANVAS_WORLD_RADIUS, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(122, 188, 255, 0.42)';
        ctx.lineWidth = 6;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(center.x, center.y, CANVAS_WORLD_RADIUS, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(198, 231, 255, 0.55)';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        // bullets
        ctx.fillStyle = '#bdf2ff';
        for (const b of run.bullets) {
          const s = toScreen(b.x, b.y);
          ctx.beginPath();
          ctx.arc(s.x, s.y, b.r, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.fillStyle = '#ffbe8c';
        for (const b of run.enemyBullets) {
          const s = toScreen(b.x, b.y);
          ctx.beginPath();
          ctx.arc(s.x, s.y, b.r, 0, Math.PI * 2);
          ctx.fill();
        }

        // enemies
        for (const e of run.enemies) {
          const s = toScreen(e.x, e.y);
          let col = '#ff8787';
          if (e.type === 'tank') col = '#b993ff';
          else if (e.type === 'shooter') col = '#ffc27a';
          else if (e.type === 'splitter') col = '#9be5ff';
          else if (e.type === 'boss') col = '#ff6ca8';
          ctx.beginPath();
          ctx.fillStyle = col;
          ctx.globalAlpha = e.elite ? 1 : 0.92;
          ctx.arc(s.x, s.y, e.radius, 0, Math.PI * 2);
          ctx.fill();
          ctx.globalAlpha = 1;
          if (e.type === 'boss') {
            ctx.beginPath();
            ctx.strokeStyle = 'rgba(255, 210, 225, 0.8)';
            ctx.lineWidth = 3;
            ctx.arc(s.x, s.y, e.radius + 6 + Math.sin(run.elapsed * 5) * 1.8, 0, Math.PI * 2);
            ctx.stroke();
          }
          const hp = clamp(e.hp / e.maxHp, 0, 1);
          ctx.fillStyle = 'rgba(0,0,0,0.45)';
          ctx.fillRect(s.x - e.radius, s.y - e.radius - 12, e.radius * 2, 4);
          ctx.fillStyle = '#7ef5bc';
          ctx.fillRect(s.x - e.radius, s.y - e.radius - 12, e.radius * 2 * hp, 4);
        }

        // player
        const sp = toScreen(p.x, p.y);
        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.globalAlpha = 0.26;
        ctx.arc(sp.x, sp.y, p.radius * 1.55, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;

        ctx.beginPath();
        ctx.fillStyle = p.color;
        ctx.arc(sp.x, sp.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.fillStyle = '#f7fcff';
        ctx.arc(sp.x + p.radius * 0.24, sp.y, p.radius * 0.32, 0, Math.PI * 2);
        ctx.fill();

        if (p.invuln > 0) {
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(162, 241, 255, 0.92)';
          ctx.lineWidth = 3;
          ctx.arc(sp.x, sp.y, p.radius + 10 + Math.sin(run.elapsed * 20) * 1.3, 0, Math.PI * 2);
          ctx.stroke();
        }
      }

      function loop(ts) {
        if (!runState.running || !run) return;
        const dt = clamp((ts - lastTs) / 1000, 0.001, 0.033);
        lastTs = ts;
        runStep(dt);
        drawRun();
        updateRunHud();
        if (!runState.ended) {
          raf = requestAnimationFrame(loop);
        }
      }

      // ---------- events ----------
      function bindUI() {
        el.tabs.addEventListener('click', (e) => {
          const btn = e.target.closest('.tab-btn');
          if (!btn) return;
          activeTab = btn.dataset.tab;
          renderTabs();
        });

        document.addEventListener('click', (e) => {
          const mBtn = e.target.closest('.mission-claim-btn');
          if (mBtn) missionClaim(mBtn.dataset.scope, mBtn.dataset.id);

          const pBtn = e.target.closest('.pass-claim-btn');
          if (pBtn) passClaim(pBtn.dataset.type, Number(pBtn.dataset.tier));

          const oBtn = e.target.closest('.offer-buy-btn');
          if (oBtn) buyShopOffer(oBtn.dataset.offer);

          const lBtn = e.target.closest('.lab-up-btn');
          if (lBtn) upgradeLab(lBtn.dataset.up);

          const sBtn = e.target.closest('.skin-equip-btn');
          if (sBtn) equipSkin(sBtn.dataset.skin);
        });

        el.startRunBtn.addEventListener('click', startRun);
        el.buyPremiumBtn.addEventListener('click', buyPremium);
        el.capsuleOpenCreditBtn.addEventListener('click', openCapsuleByCredit);
        el.capsuleOpenTicketBtn.addEventListener('click', openCapsuleByTicket);
        el.staminaRefillBtn.addEventListener('click', refillStamina);

        el.pilotSaveBtn.addEventListener('click', () => {
          const v = (el.pilotInput.value || '').trim().slice(0, 16);
          if (!v) { toast('파일럿 이름을 입력하세요'); return; }
          meta.pilot = v;
          saveMeta();
          renderAll();
          toast('파일럿 저장 완료');
        });
        el.pilotInput.addEventListener('keydown', (ev) => {
          if (ev.code === 'Enter') {
            ev.preventDefault();
            el.pilotSaveBtn.click();
          }
        });

        el.endRetryBtn.addEventListener('click', () => {
          el.endModal.style.display = 'none';
          startRun();
        });
        el.endLobbyBtn.addEventListener('click', () => {
          el.endModal.style.display = 'none';
          leaveRunToLobby();
        });

        window.addEventListener('resize', resizeArena);

        window.addEventListener('keydown', (ev) => {
          input.keys[ev.code] = true;
          if (!runState.running || !run) return;
          if (ev.code === 'Space') {
            ev.preventDefault();
            input.dashPressed = true;
          } else if (ev.code === 'KeyE') {
            input.pulsePressed = true;
          } else if (ev.code === 'Escape') {
            run.paused = !run.paused;
            toast(run.paused ? 'PAUSED' : 'RESUMED');
          }
        });
        window.addEventListener('keyup', (ev) => { input.keys[ev.code] = false; });
      }

      // ---------- bootstrap ----------
      let meta = loadMeta();
      ensureMissionReset();
      staminaRefresh(meta);
      saveMeta();
      bindUI();
      renderAll();
      setInterval(() => {
        const changed = staminaRefresh(meta);
        if (changed) saveMeta();
        renderTop();
      }, 20000);

      if (meta.activeSession && meta.activeSession.sector) {
        toast('저장된 체크포인트: S' + meta.activeSession.sector + ' · ' + nfmt(meta.activeSession.score || 0), 2.4);
      }
    })();
  </script>
</body>
</html>
"""


components.html(APP_HTML, height=1040, scrolling=False)
