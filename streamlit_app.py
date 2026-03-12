import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Evolio+ Hyper Arena",
    page_icon="🧬",
    layout="wide",
)

st.title("Evolio+ Hyper Arena")
st.caption(
    "A faster and more balanced evolution arena: adaptive difficulty director, "
    "deeper specialization, skill-based dash/pulse combat, and cleaner readability."
)


GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    :root {
      --panel-bg: rgba(10, 17, 30, 0.74);
      --panel-border: rgba(118, 170, 255, 0.32);
      --text-main: #eaf3ff;
      --text-soft: #9ab4d5;
      --accent: #59f7b3;
      --danger: #ff7a7a;
      --energy: #58c2ff;
    }

    html, body {
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: #030811;
      font-family: Inter, Segoe UI, Arial, sans-serif;
      color: var(--text-main);
    }

    #shell {
      position: relative;
      width: 100%;
      height: 880px;
      background: radial-gradient(circle at 30% 25%, #0b1930 0%, #02060f 65%);
      border: 1px solid rgba(100, 156, 255, 0.15);
      border-radius: 14px;
      overflow: hidden;
      user-select: none;
    }

    canvas {
      width: 100%;
      height: 100%;
      display: block;
      cursor: crosshair;
      outline: none;
    }

    .panel {
      position: absolute;
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      backdrop-filter: blur(6px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
    }

    #hud-left {
      left: 14px;
      top: 14px;
      width: 420px;
      padding: 10px 12px;
    }

    #hud-right {
      right: 14px;
      top: 14px;
      width: 280px;
      padding: 10px 12px;
    }

    #meta-panel {
      left: 14px;
      bottom: 52px;
      width: 420px;
      padding: 10px 12px;
      max-height: 355px;
      overflow: auto;
    }

    #ranking-panel {
      right: 14px;
      bottom: 52px;
      width: 320px;
      padding: 10px 12px;
      max-height: 355px;
      overflow: auto;
    }

    #hint {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      bottom: 12px;
      font-size: 13px;
      color: #d0e1ff;
      background: rgba(12, 20, 36, 0.7);
      border: 1px solid rgba(123, 160, 220, 0.28);
      border-radius: 10px;
      padding: 7px 12px;
      letter-spacing: 0.2px;
    }

    .row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin: 6px 0;
      font-size: 13px;
    }

    .label {
      min-width: 88px;
      color: var(--text-soft);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.6px;
    }

    .bar {
      flex: 1;
      height: 11px;
      border-radius: 100px;
      border: 1px solid rgba(176, 201, 238, 0.35);
      background: rgba(18, 28, 47, 0.9);
      overflow: hidden;
      position: relative;
    }

    .bar i {
      display: block;
      height: 100%;
      width: 0%;
      transition: width 100ms linear;
      border-radius: inherit;
      box-shadow: 0 0 16px currentColor;
    }

    .bar.hp i {
      color: var(--danger);
      background: linear-gradient(90deg, #ff6e6e 0%, #ff9a7f 100%);
    }

    .bar.energy i {
      color: var(--energy);
      background: linear-gradient(90deg, #54a8ff 0%, #50e1ff 100%);
    }

    .bar.bio i {
      background: linear-gradient(90deg, #6dd6ff 0%, #bbd3ff 100%);
      color: #74b9ff;
    }

    .value {
      min-width: 82px;
      text-align: right;
      font-weight: 700;
      font-size: 12px;
    }

    #event-banner {
      position: absolute;
      left: 50%;
      top: 84px;
      transform: translateX(-50%);
      color: #dff3ff;
      font-weight: 700;
      font-size: 16px;
      text-shadow: 0 0 18px rgba(125, 203, 255, 0.6);
      pointer-events: none;
      opacity: 0;
      transition: opacity 220ms ease;
      white-space: nowrap;
    }

    .stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px 10px;
      margin-top: 4px;
      font-size: 13px;
    }

    .stat-grid .k {
      color: var(--text-soft);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .stat-grid .v {
      font-weight: 700;
    }

    .meta-title {
      margin: 0 0 8px;
      font-size: 12px;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      color: #9cc7ff;
    }

    .meta-line {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      margin: 5px 0;
      color: #cce0ff;
    }

    .meta-line span {
      color: #9cb5d8;
    }

    .pilot-row {
      display: flex;
      gap: 8px;
      margin-bottom: 8px;
    }

    .pilot-row input {
      flex: 1;
      border-radius: 8px;
      border: 1px solid rgba(130, 170, 236, 0.4);
      background: rgba(8, 14, 25, 0.9);
      color: #f0f6ff;
      padding: 6px 8px;
      font-size: 12px;
      outline: none;
    }

    .mini-btn {
      border-radius: 8px;
      border: 1px solid rgba(125, 214, 185, 0.65);
      background: linear-gradient(180deg, #42dc98, #1fae72);
      color: #052013;
      font-size: 11px;
      font-weight: 800;
      padding: 6px 9px;
      cursor: pointer;
    }

    .mini-btn:disabled {
      background: rgba(74, 99, 124, 0.5);
      border-color: rgba(113, 134, 155, 0.45);
      color: #9eb2c7;
      cursor: not-allowed;
    }

    .contract-list {
      margin-top: 8px;
      display: grid;
      gap: 6px;
    }

    .contract-item {
      border: 1px solid rgba(124, 154, 211, 0.35);
      border-radius: 8px;
      background: rgba(10, 20, 35, 0.65);
      padding: 6px 7px;
      font-size: 11px;
    }

    .contract-item.done {
      border-color: rgba(103, 218, 173, 0.58);
      background: rgba(16, 37, 31, 0.67);
    }

    .contract-top {
      display: flex;
      justify-content: space-between;
      color: #dcecff;
      margin-bottom: 3px;
      gap: 8px;
    }

    .contract-progress {
      color: #8ec8ff;
    }

    .upgrade-board {
      margin-top: 8px;
      display: grid;
      gap: 6px;
    }

    .upgrade-item {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 6px;
      border: 1px solid rgba(121, 153, 212, 0.33);
      border-radius: 8px;
      background: rgba(9, 18, 32, 0.72);
      padding: 7px;
      align-items: center;
    }

    .upgrade-item .name {
      color: #def0ff;
      font-size: 11px;
      font-weight: 700;
    }

    .upgrade-item .desc {
      color: #9cb7da;
      font-size: 10px;
      margin-top: 2px;
    }

    .rank-list {
      display: grid;
      gap: 5px;
      margin-top: 6px;
    }

    .rank-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 7px;
      font-size: 11px;
      border-radius: 7px;
      border: 1px solid rgba(119, 148, 205, 0.35);
      background: rgba(9, 17, 31, 0.66);
      padding: 6px 7px;
    }

    .rank-item strong {
      color: #eaf5ff;
    }

    .rank-item .sub {
      color: #9ebbe1;
      font-size: 10px;
    }

    .overlay {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at 50% 35%, rgba(13, 26, 51, 0.52), rgba(2, 5, 10, 0.88));
      z-index: 10;
    }

    .card {
      width: min(720px, 90vw);
      padding: 20px 22px;
      border-radius: 16px;
      border: 1px solid rgba(121, 177, 255, 0.32);
      background: rgba(9, 16, 31, 0.88);
      box-shadow: 0 20px 42px rgba(0, 0, 0, 0.4);
    }

    .card h2 {
      margin: 0 0 10px;
      font-size: 32px;
      letter-spacing: 0.7px;
    }

    .card p {
      margin: 4px 0;
      color: #b8cbe6;
      line-height: 1.45;
    }

    .points {
      margin: 10px 0 14px;
      font-size: 14px;
    }

    .points li {
      margin: 6px 0;
      color: #deebff;
    }

    .cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 11px 16px;
      border-radius: 10px;
      border: 1px solid rgba(124, 235, 191, 0.6);
      background: linear-gradient(180deg, #39de95 0%, #1dbf7d 100%);
      color: #042015;
      font-weight: 900;
      letter-spacing: 0.4px;
      cursor: pointer;
      margin-top: 8px;
    }

    #game-over {
      display: none;
    }

    #game-over .card h2 {
      color: #ffc8c8;
    }
  </style>
</head>
<body>
  <div id="shell">
    <canvas id="game" tabindex="0"></canvas>

    <div id="hud-left" class="panel">
      <div class="row">
        <div class="label">HP</div>
        <div class="bar hp"><i id="hp-fill"></i></div>
        <div class="value" id="hp-text">0 / 0</div>
      </div>
      <div class="row">
        <div class="label">Energy</div>
        <div class="bar energy"><i id="energy-fill"></i></div>
        <div class="value" id="energy-text">0 / 0</div>
      </div>
      <div class="row">
        <div class="label">Biomarker Mix</div>
        <div class="bar bio"><i id="bio-fill"></i></div>
        <div class="value" id="bio-text">Hybrid</div>
      </div>
    </div>

    <div id="hud-right" class="panel">
      <div class="stat-grid">
        <div class="k">Wave</div><div class="v" id="wave-text">1</div>
        <div class="k">Mass</div><div class="v" id="mass-text">0</div>
        <div class="k">Stage</div><div class="v" id="stage-text">1</div>
        <div class="k">Score</div><div class="v" id="score-text">0</div>
        <div class="k">Combo</div><div class="v" id="combo-text">x1</div>
        <div class="k">Enemies</div><div class="v" id="enemy-count-text">0</div>
        <div class="k">Director</div><div class="v" id="director-text">50%</div>
      </div>
    </div>

    <div id="meta-panel" class="panel">
      <div class="meta-title">Persistent Lab (Auto Save)</div>
      <div class="pilot-row">
        <input id="pilot-input" type="text" maxlength="16" placeholder="Pilot name" />
        <button class="mini-btn" id="pilot-save-btn">SAVE</button>
      </div>
      <div class="meta-line"><span>Shards</span><strong id="shard-text">0</strong></div>
      <div class="meta-line"><span>Runs</span><strong id="runs-text">0</strong></div>
      <div class="meta-line"><span>Best Run</span><strong id="best-run-text">0</strong></div>
      <div class="meta-line"><span>Lifetime Score</span><strong id="lifetime-score-text">0</strong></div>
      <div class="meta-line"><span>Checkpoint</span><strong id="checkpoint-text">-</strong></div>
      <div id="contract-list" class="contract-list"></div>
      <div id="upgrade-board" class="upgrade-board"></div>
    </div>

    <div id="ranking-panel" class="panel">
      <div class="meta-title">Season Ranking (Local)</div>
      <div id="ranking-list" class="rank-list"></div>
    </div>

    <div id="event-banner">Ready</div>

    <div id="hint">
      Move: Mouse or WASD | Dash: Space | Bio Pulse: E | Restart after defeat: R | Save + Ranking + Upgrades enabled
    </div>

    <div id="start" class="overlay">
      <div class="card">
        <h2>Evolio+ Hyper Arena</h2>
        <p>
          Designed to be more intense and better balanced than a basic cell arena:
          less random swing, clearer progression, and stronger combat feedback.
        </p>
        <ul class="points">
          <li>Adaptive threat director scales challenge by your momentum and health.</li>
          <li>Four enemy archetypes with different pressure profiles.</li>
          <li>Specialization from nutrient choices: Speedster / Predator / Tank / Hybrid.</li>
          <li>Skill expression with dash invulnerability and timed bio pulse.</li>
          <li>Persistent Lab: upgrade with shards, clear daily contracts, and climb local season ranking.</li>
        </ul>
        <button class="cta" id="start-btn">START BATTLE (ENTER)</button>
      </div>
    </div>

    <div id="game-over" class="overlay">
      <div class="card">
        <h2>Cell Collapse</h2>
        <p id="final-line">Score: 0</p>
        <p>Your run ended, but your build data is preserved in this session.</p>
        <button class="cta" id="restart-btn">TRY AGAIN (R)</button>
      </div>
    </div>
  </div>

  <script>
    (() => {
      'use strict';

      const shell = document.getElementById('shell');
      const canvas = document.getElementById('game');
      const ctx = canvas.getContext('2d');
      const startOverlay = document.getElementById('start');
      const gameOverOverlay = document.getElementById('game-over');
      const startBtn = document.getElementById('start-btn');
      const restartBtn = document.getElementById('restart-btn');
      const finalLine = document.getElementById('final-line');
      const eventBanner = document.getElementById('event-banner');

      const hpFill = document.getElementById('hp-fill');
      const energyFill = document.getElementById('energy-fill');
      const bioFill = document.getElementById('bio-fill');
      const hpText = document.getElementById('hp-text');
      const energyText = document.getElementById('energy-text');
      const bioText = document.getElementById('bio-text');
      const waveText = document.getElementById('wave-text');
      const massText = document.getElementById('mass-text');
      const stageText = document.getElementById('stage-text');
      const scoreText = document.getElementById('score-text');
      const comboText = document.getElementById('combo-text');
      const enemyCountText = document.getElementById('enemy-count-text');
      const directorText = document.getElementById('director-text');
      const pilotInput = document.getElementById('pilot-input');
      const pilotSaveBtn = document.getElementById('pilot-save-btn');
      const shardText = document.getElementById('shard-text');
      const runsText = document.getElementById('runs-text');
      const bestRunText = document.getElementById('best-run-text');
      const lifetimeScoreText = document.getElementById('lifetime-score-text');
      const checkpointText = document.getElementById('checkpoint-text');
      const contractList = document.getElementById('contract-list');
      const upgradeBoard = document.getElementById('upgrade-board');
      const rankingList = document.getElementById('ranking-list');

      const SAVE_KEY = 'evolio_hyper_arena_save_v2';
      const SAVE_VERSION = 2;
      const UPGRADE_DEFS = [
        { id: 'core', name: 'Cytoplasm Core', desc: 'Attack +8% / level', baseCost: 45, max: 12 },
        { id: 'shell', name: 'Membrane Shell', desc: 'Max HP +10%, Armor +2.5 / level', baseCost: 50, max: 12 },
        { id: 'reactor', name: 'ATP Reactor', desc: 'Energy regen +10%, cooldowns shorter', baseCost: 55, max: 10 },
        { id: 'hunter', name: 'Hunter Genome', desc: 'Score +6%, shard gain +8% / level', baseCost: 60, max: 10 }
      ];

      const SPEC_COLOR = {
        Hybrid: '#55f1b1',
        Speedster: '#ffe95d',
        Predator: '#ff7f7f',
        Tank: '#76b8ff'
      };

      const WORLD_RADIUS = 2100;
      const DPR = Math.min(window.devicePixelRatio || 1, 2);

      const view = { width: 1, height: 1 };
      const camera = { x: 0, y: 0, zoom: 1 };
      const mouse = { x: 0, y: 0, worldX: 0, worldY: 0, active: false };
      const keys = {};

      let running = false;
      let gameOver = false;
      let rafId = null;
      let lastTime = 0;
      let hudTimer = 0;
      let ambientDropTimer = 0;
      let announceTimer = 0;
      let announceText = '';

      function safeReadStorage() {
        try {
          return window.localStorage.getItem(SAVE_KEY);
        } catch (error) {
          return null;
        }
      }

      function safeWriteStorage(value) {
        try {
          window.localStorage.setItem(SAVE_KEY, value);
          return true;
        } catch (error) {
          return false;
        }
      }

      function todayKey() {
        return new Date().toISOString().slice(0, 10);
      }

      function buildContracts(day) {
        const hashSeed = day.split('-').join('');
        const seedNum = Number(hashSeed) || 20260101;
        const rotA = (seedNum % 3);
        const rotB = ((Math.floor(seedNum / 7)) % 3);
        const waveGoal = 4 + rotA;
        const killGoal = 45 + rotB * 20;
        const nutrientGoal = 95 + rotA * 30;
        return [
          { id: 'kill', title: 'Predator Census', target: killGoal, reward: 70 + rotA * 20, progress: 0, done: false },
          { id: 'wave', title: 'Tidal Escalation', target: waveGoal, reward: 90 + rotB * 15, progress: 0, done: false },
          { id: 'nutrient', title: 'Nutrient Hoarder', target: nutrientGoal, reward: 80 + rotB * 18, progress: 0, done: false }
        ];
      }

      function defaultMetaSave() {
        return {
          version: SAVE_VERSION,
          pilot: 'CellPilot',
          shards: 0,
          upgrades: { core: 0, shell: 0, reactor: 0, hunter: 0 },
          stats: {
            runs: 0,
            totalScore: 0,
            totalKills: 0,
            totalNutrients: 0,
            totalPlaySec: 0,
            bestScore: 0,
            bestWave: 1,
            bestStage: 1,
            bestMass: 110
          },
          rankings: [],
          contracts: {
            day: todayKey(),
            items: buildContracts(todayKey())
          },
          activeSession: null,
          lastRun: null
        };
      }

      function ensureContracts(metaObj) {
        if (!metaObj.contracts || metaObj.contracts.day !== todayKey()) {
          metaObj.contracts = {
            day: todayKey(),
            items: buildContracts(todayKey())
          };
        }
      }

      function normalizeMeta(raw) {
        const d = defaultMetaSave();
        const src = raw && typeof raw === 'object' ? raw : {};
        const out = {
          version: SAVE_VERSION,
          pilot: typeof src.pilot === 'string' && src.pilot.trim() ? src.pilot.slice(0, 16) : d.pilot,
          shards: Number.isFinite(src.shards) ? Math.max(0, Math.floor(src.shards)) : d.shards,
          upgrades: {
            core: Math.max(0, Math.min(12, Math.floor(src.upgrades?.core || 0))),
            shell: Math.max(0, Math.min(12, Math.floor(src.upgrades?.shell || 0))),
            reactor: Math.max(0, Math.min(10, Math.floor(src.upgrades?.reactor || 0))),
            hunter: Math.max(0, Math.min(10, Math.floor(src.upgrades?.hunter || 0)))
          },
          stats: {
            runs: Math.max(0, Math.floor(src.stats?.runs || 0)),
            totalScore: Math.max(0, Math.floor(src.stats?.totalScore || 0)),
            totalKills: Math.max(0, Math.floor(src.stats?.totalKills || 0)),
            totalNutrients: Math.max(0, Math.floor(src.stats?.totalNutrients || 0)),
            totalPlaySec: Math.max(0, Math.floor(src.stats?.totalPlaySec || 0)),
            bestScore: Math.max(0, Math.floor(src.stats?.bestScore || 0)),
            bestWave: Math.max(1, Math.floor(src.stats?.bestWave || 1)),
            bestStage: Math.max(1, Math.floor(src.stats?.bestStage || 1)),
            bestMass: Math.max(110, Math.floor(src.stats?.bestMass || 110))
          },
          rankings: Array.isArray(src.rankings)
            ? src.rankings.slice(0, 40).map((r) => ({
              pilot: typeof r?.pilot === 'string' && r.pilot ? r.pilot.slice(0, 16) : 'Pilot',
              score: Math.max(0, Math.floor(r?.score || 0)),
              wave: Math.max(1, Math.floor(r?.wave || 1)),
              stage: Math.max(1, Math.floor(r?.stage || 1)),
              mass: Math.max(0, Math.floor(r?.mass || 0)),
              spec: typeof r?.spec === 'string' ? r.spec : 'Hybrid',
              kills: Math.max(0, Math.floor(r?.kills || 0)),
              duration: Math.max(1, Math.floor(r?.duration || 1)),
              shards: Math.max(0, Math.floor(r?.shards || 0)),
              date: typeof r?.date === 'string' ? r.date : new Date().toISOString()
            }))
            : [],
          contracts: src.contracts,
          activeSession: src.activeSession && typeof src.activeSession === 'object' ? src.activeSession : null,
          lastRun: src.lastRun && typeof src.lastRun === 'object' ? src.lastRun : null
        };
        ensureContracts(out);
        return out;
      }

      function loadMetaSave() {
        const raw = safeReadStorage();
        if (!raw) return defaultMetaSave();
        try {
          const parsed = JSON.parse(raw);
          return normalizeMeta(parsed);
        } catch (error) {
          return defaultMetaSave();
        }
      }

      function persistMetaSave() {
        safeWriteStorage(JSON.stringify(meta));
      }

      function fmtNumber(value) {
        return Number(value || 0).toLocaleString();
      }

      function shortSpec(spec) {
        if (spec === 'Speedster') return 'SPD';
        if (spec === 'Predator') return 'PRED';
        if (spec === 'Tank') return 'TANK';
        return 'HYB';
      }

      function formatDate(isoString) {
        if (!isoString) return '-';
        const d = new Date(isoString);
        if (Number.isNaN(d.getTime())) return '-';
        return d.toISOString().slice(5, 10);
      }

      let meta = loadMetaSave();

      const state = {
        score: 0,
        time: 0,
        wave: 1,
        waveTime: 0,
        director: 0.5,
        combo: 0,
        comboTimer: 0,
        spawnTimer: 0,
        shake: 0,
        killsRecent: [],
        floatingTexts: [],
        particles: [],
        nutrients: [],
        enemies: [],
        enemyProjectiles: [],
        playerProjectiles: [],
        saveTick: 0,
        runStats: {
          kills: 0,
          nutrients: 0,
          elites: 0,
          damageTaken: 0,
          highestCombo: 0,
          contractShardBonus: 0
        }
      };

      const player = {
        x: 0,
        y: 0,
        vx: 0,
        vy: 0,
        radius: 24,
        mass: 110,
        hp: 240,
        maxHp: 240,
        energy: 130,
        maxEnergy: 130,
        stage: 1,
        specialization: 'Hybrid',
        biomarkers: { glucose: 0, amino: 0, lipid: 0, atp: 0 },
        stats: {
          speed: 230,
          attack: 24,
          armor: 12,
          crit: 0.1,
          lifeSteal: 0.03,
          energyRegen: 20,
          dashCooldown: 3.2,
          pulseCooldown: 5.2,
          contactDps: 56,
          pulseDamage: 96
        },
        dashCd: 0,
        pulseCd: 0,
        boltCd: 0,
        dashTime: 0,
        dashDirX: 1,
        dashDirY: 0,
        invuln: 0,
        shield: 0,
        lastDamageAt: 0
      };

      function upgradeCost(def, level) {
        return Math.round(def.baseCost * Math.pow(1.62, level + 0.05));
      }

      function scoreMetaMultiplier() {
        return 1 + meta.upgrades.hunter * 0.06;
      }

      function shardMetaMultiplier() {
        return 1 + meta.upgrades.hunter * 0.08;
      }

      function renderRankingBoard() {
        if (!rankingList) return;
        const list = Array.isArray(meta.rankings) ? meta.rankings : [];
        if (!list.length) {
          rankingList.innerHTML = '<div class="rank-item"><strong>No runs yet</strong><span class="sub">Start your first run</span></div>';
          return;
        }

        rankingList.innerHTML = '';
        list.slice(0, 8).forEach((r, idx) => {
          const item = document.createElement('div');
          item.className = 'rank-item';
          const left = document.createElement('div');
          const pilotName = (r.pilot || 'Pilot').slice(0, 12);
          left.innerHTML = '<strong>#' + (idx + 1) + ' ' + fmtNumber(r.score) + '</strong><div class="sub">' + pilotName + ' · W' + r.wave + ' · S' + r.stage + ' · ' + shortSpec(r.spec) + '</div>';
          const right = document.createElement('div');
          right.className = 'sub';
          right.textContent = formatDate(r.date);
          item.appendChild(left);
          item.appendChild(right);
          rankingList.appendChild(item);
        });
      }

      function renderContractBoard() {
        if (!contractList) return;
        ensureContracts(meta);
        contractList.innerHTML = '';
        meta.contracts.items.forEach((c) => {
          const item = document.createElement('div');
          item.className = 'contract-item' + (c.done ? ' done' : '');
          const progress = Math.min(c.target, Math.floor(c.progress || 0));
          item.innerHTML = ''
            + '<div class="contract-top"><span>' + c.title + '</span><strong>+' + c.reward + ' shards</strong></div>'
            + '<div class="contract-progress">' + progress + ' / ' + c.target + (c.done ? ' · completed' : '') + '</div>';
          contractList.appendChild(item);
        });
      }

      function renderUpgradeBoard() {
        if (!upgradeBoard) return;
        upgradeBoard.innerHTML = '';
        UPGRADE_DEFS.forEach((def) => {
          const current = meta.upgrades[def.id] || 0;
          const atMax = current >= def.max;
          const cost = atMax ? 0 : upgradeCost(def, current);

          const row = document.createElement('div');
          row.className = 'upgrade-item';

          const left = document.createElement('div');
          left.innerHTML = ''
            + '<div class="name">' + def.name + ' Lv.' + current + ' / ' + def.max + '</div>'
            + '<div class="desc">' + def.desc + '</div>';

          const btn = document.createElement('button');
          btn.className = 'mini-btn';
          btn.disabled = atMax || meta.shards < cost;
          btn.textContent = atMax ? 'MAX' : ('UP ' + cost);
          btn.addEventListener('click', () => {
            if (running) {
              showBanner('Upgrade between runs only', 1.2);
              return;
            }
            const nowLevel = meta.upgrades[def.id] || 0;
            if (nowLevel >= def.max) return;
            const nowCost = upgradeCost(def, nowLevel);
            if (meta.shards < nowCost) {
              showBanner('Not enough shards', 1.1);
              return;
            }
            meta.shards -= nowCost;
            meta.upgrades[def.id] = nowLevel + 1;
            persistMetaSave();
            rebuildPlayerStats();
            renderMetaPanels();
            showBanner(def.name + ' upgraded', 1.2);
          });

          row.appendChild(left);
          row.appendChild(btn);
          upgradeBoard.appendChild(row);
        });
      }

      function renderMetaPanels() {
        shardText.textContent = fmtNumber(meta.shards);
        runsText.textContent = fmtNumber(meta.stats.runs);
        bestRunText.textContent = fmtNumber(meta.stats.bestScore) + ' (W' + meta.stats.bestWave + ')';
        lifetimeScoreText.textContent = fmtNumber(meta.stats.totalScore);
        if (checkpointText) {
          if (meta.activeSession && meta.activeSession.wave) {
            checkpointText.textContent = 'W' + meta.activeSession.wave + ' · ' + fmtNumber(meta.activeSession.score);
          } else {
            checkpointText.textContent = '-';
          }
        }
        if (pilotInput && document.activeElement !== pilotInput) {
          pilotInput.value = meta.pilot;
        }
        renderContractBoard();
        renderUpgradeBoard();
        renderRankingBoard();
      }

      function applyContractProgress(contractId, amount, useMax = false) {
        ensureContracts(meta);
        const contract = meta.contracts.items.find((it) => it.id === contractId);
        if (!contract || contract.done) return;

        if (useMax) {
          contract.progress = Math.max(contract.progress || 0, amount);
        } else {
          contract.progress = (contract.progress || 0) + amount;
        }

        if (contract.progress >= contract.target) {
          contract.done = true;
          contract.progress = contract.target;
          meta.shards += contract.reward;
          state.runStats.contractShardBonus += contract.reward;
          showBanner('Contract complete: +' + contract.reward + ' shards', 1.6);
          spawnBurst(player.x, player.y, '#7df3be', 26, 1.0);
        }

        persistMetaSave();
        renderContractBoard();
        shardText.textContent = fmtNumber(meta.shards);
      }

      function recordRunResult() {
        const score = Math.floor(state.score);
        const wave = state.wave;
        const stage = player.stage;
        const mass = Math.floor(player.mass);
        const duration = Math.max(1, Math.floor(state.time));
        const killCount = state.runStats.kills;

        const baseShard = Math.max(
          12,
          Math.floor(score / 240 + wave * 5 + stage * 4 + killCount * 0.4)
        );
        const shardGain = Math.floor(baseShard * shardMetaMultiplier());
        meta.shards += shardGain;

        meta.stats.runs += 1;
        meta.stats.totalScore += score;
        meta.stats.totalKills += killCount;
        meta.stats.totalNutrients += state.runStats.nutrients;
        meta.stats.totalPlaySec += duration;
        meta.stats.bestScore = Math.max(meta.stats.bestScore, score);
        meta.stats.bestWave = Math.max(meta.stats.bestWave, wave);
        meta.stats.bestStage = Math.max(meta.stats.bestStage, stage);
        meta.stats.bestMass = Math.max(meta.stats.bestMass, mass);

        const row = {
          pilot: meta.pilot,
          score,
          wave,
          stage,
          mass,
          spec: player.specialization,
          kills: killCount,
          duration,
          shards: shardGain + state.runStats.contractShardBonus,
          date: new Date().toISOString()
        };

        meta.rankings.push(row);
        meta.rankings.sort((a, b) => {
          if (b.score !== a.score) return b.score - a.score;
          if (b.wave !== a.wave) return b.wave - a.wave;
          return b.stage - a.stage;
        });
        meta.rankings = meta.rankings.slice(0, 40);
        meta.lastRun = row;
        meta.activeSession = null;

        persistMetaSave();
        renderMetaPanels();

        return row;
      }

      function clamp(v, lo, hi) {
        return Math.max(lo, Math.min(hi, v));
      }

      function rand(min, max) {
        return Math.random() * (max - min) + min;
      }

      function length(x, y) {
        return Math.hypot(x, y);
      }

      function normalize(x, y) {
        const n = Math.hypot(x, y) || 1;
        return { x: x / n, y: y / n };
      }

      function worldToScreen(x, y) {
        return {
          x: (x - camera.x) * camera.zoom + view.width / 2,
          y: (y - camera.y) * camera.zoom + view.height / 2
        };
      }

      function screenToWorld(x, y) {
        return {
          x: (x - view.width / 2) / camera.zoom + camera.x,
          y: (y - view.height / 2) / camera.zoom + camera.y
        };
      }

      function showBanner(message, seconds = 1.8) {
        announceText = message;
        announceTimer = seconds;
        eventBanner.textContent = message;
        eventBanner.style.opacity = '1';
      }

      function hideBanner() {
        eventBanner.style.opacity = '0';
      }

      function updateCanvasSize() {
        const rect = shell.getBoundingClientRect();
        view.width = Math.max(1, Math.floor(rect.width));
        view.height = Math.max(1, Math.floor(rect.height));
        canvas.width = Math.floor(view.width * DPR);
        canvas.height = Math.floor(view.height * DPR);
        ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      }

      function specializationFromBiomarkers() {
        const b = player.biomarkers;
        const total = b.glucose + b.amino + b.lipid;
        if (total < 10) {
          return 'Hybrid';
        }

        const mix = [
          { k: 'Speedster', v: b.glucose },
          { k: 'Predator', v: b.amino },
          { k: 'Tank', v: b.lipid }
        ].sort((a, b2) => b2.v - a.v);

        if (mix[0].v / total < 0.42) {
          return 'Hybrid';
        }
        return mix[0].k;
      }

      function stageFromMass(mass) {
        const thresholds = [0, 160, 320, 560, 860, 1240];
        let stage = 1;
        for (let i = 1; i < thresholds.length; i += 1) {
          if (mass >= thresholds[i]) {
            stage = i + 1;
          }
        }
        return stage;
      }

      function rebuildPlayerStats() {
        const nextStage = stageFromMass(player.mass);
        if (nextStage > player.stage) {
          player.stage = nextStage;
          player.invuln = Math.max(player.invuln, 0.45);
          player.hp = Math.min(player.maxHp, player.hp + 38);
          state.shake = Math.max(state.shake, 12);
          showBanner('Stage ' + player.stage + ' reached');
          spawnBurst(player.x, player.y, SPEC_COLOR[player.specialization], 40, 1.3);
        }

        const nextSpec = specializationFromBiomarkers();
        if (nextSpec !== player.specialization) {
          player.specialization = nextSpec;
          showBanner('Specialization: ' + nextSpec, 1.6);
          spawnBurst(player.x, player.y, SPEC_COLOR[nextSpec], 26, 1.0);
        }

        let speed = 228 * (1 + (player.stage - 1) * 0.03);
        let attack = 24 * (1 + (player.stage - 1) * 0.09);
        let armor = 12 + (player.stage - 1) * 2.2;
        let maxHp = 240 * (1 + (player.stage - 1) * 0.14);
        let crit = 0.09 + (player.stage - 1) * 0.01;
        let lifeSteal = 0.03 + (player.stage - 1) * 0.005;
        let energyRegen = 20 * (1 + (player.stage - 1) * 0.03);
        let dashCooldown = 3.2;
        let pulseCooldown = 5.2;

        if (player.specialization === 'Speedster') {
          speed *= 1.22;
          attack *= 0.95;
          armor -= 2;
          crit += 0.02;
          energyRegen *= 1.16;
          dashCooldown *= 0.78;
          pulseCooldown *= 1.08;
        } else if (player.specialization === 'Predator') {
          speed *= 1.07;
          attack *= 1.28;
          crit += 0.09;
          lifeSteal += 0.05;
          armor += 1;
          dashCooldown *= 0.92;
        } else if (player.specialization === 'Tank') {
          speed *= 0.86;
          attack *= 1.05;
          armor += 18;
          maxHp *= 1.3;
          pulseCooldown *= 0.78;
          crit -= 0.01;
        } else {
          speed *= 1.08;
          attack *= 1.08;
          armor += 6;
          energyRegen *= 1.1;
          lifeSteal += 0.015;
        }

        const coreLv = meta.upgrades.core || 0;
        const shellLv = meta.upgrades.shell || 0;
        const reactorLv = meta.upgrades.reactor || 0;
        attack *= 1 + coreLv * 0.08;
        maxHp *= 1 + shellLv * 0.1;
        armor += shellLv * 2.5;
        energyRegen *= 1 + reactorLv * 0.1;
        speed *= 1 + reactorLv * 0.015;
        dashCooldown *= Math.pow(0.96, reactorLv);
        pulseCooldown *= Math.pow(0.95, reactorLv);

        const veteranTier = Math.min(0.25, (meta.stats.runs || 0) * 0.0022);
        attack *= 1 + veteranTier * 0.55;
        maxHp *= 1 + veteranTier * 0.7;
        energyRegen *= 1 + veteranTier * 0.4;

        const oldMax = player.maxHp;
        player.maxHp = Math.round(maxHp);
        if (player.maxHp > oldMax) {
          player.hp += (player.maxHp - oldMax) * 0.55;
        }
        player.hp = clamp(player.hp, 0, player.maxHp);
        player.maxEnergy = Math.round(130 + (player.stage - 1) * 12);
        player.energy = clamp(player.energy, 0, player.maxEnergy);
        player.radius = clamp(20 + Math.sqrt(player.mass) * 0.62, 20, 70);

        player.stats.speed = speed;
        player.stats.attack = attack;
        player.stats.armor = Math.max(0, armor);
        player.stats.crit = clamp(crit, 0, 0.75);
        player.stats.lifeSteal = clamp(lifeSteal, 0, 0.42);
        player.stats.energyRegen = energyRegen;
        player.stats.dashCooldown = clamp(dashCooldown, 1.25, 4.2);
        player.stats.pulseCooldown = clamp(pulseCooldown, 2.6, 6.4);
        player.stats.contactDps = attack * 2.35;
        player.stats.pulseDamage = attack * 3.65 + player.mass * 0.045;
      }

      function spawnBurst(x, y, color, count, scale = 1.0) {
        for (let i = 0; i < count; i += 1) {
          const a = rand(0, Math.PI * 2);
          const speed = rand(35, 240) * scale;
          state.particles.push({
            x,
            y,
            vx: Math.cos(a) * speed,
            vy: Math.sin(a) * speed,
            r: rand(1.8, 3.9),
            life: rand(0.35, 0.95),
            maxLife: 1,
            color
          });
        }
      }

      function addFloatText(text, x, y, color = '#d4f0ff') {
        state.floatingTexts.push({
          text,
          x,
          y,
          vy: -36,
          life: 1.0,
          color
        });
      }

      function spawnNutrient(x, y, type, outward = false) {
        const angle = rand(0, Math.PI * 2);
        const mag = outward ? rand(25, 95) : rand(0, 20);
        const radius = type === 'atp' ? 8 : 7;

        state.nutrients.push({
          x,
          y,
          type,
          radius,
          vx: Math.cos(angle) * mag,
          vy: Math.sin(angle) * mag,
          life: rand(18, 35)
        });
      }

      function dropFromEnemy(enemy) {
        const baseDrops = enemy.type === 'bruiser' ? 2 : 1;
        const bonus = state.combo >= 5 && Math.random() < 0.42 ? 1 : 0;
        const totalDrops = baseDrops + bonus;

        for (let i = 0; i < totalDrops; i += 1) {
          const roll = Math.random();
          let type = 'glucose';
          if (roll < 0.33) type = 'glucose';
          else if (roll < 0.62) type = 'amino';
          else if (roll < 0.9) type = 'lipid';
          else type = 'atp';
          spawnNutrient(enemy.x, enemy.y, type, true);
        }
      }

      function enemyTypeForWave() {
        const w = state.wave;
        const t = Math.random();
        if (w < 2) {
          return t < 0.72 ? 'chaser' : 'bruiser';
        }
        if (w < 4) {
          if (t < 0.48) return 'chaser';
          if (t < 0.73) return 'bruiser';
          if (t < 0.92) return 'spitter';
          return 'splitter';
        }
        if (t < 0.38) return 'chaser';
        if (t < 0.62) return 'bruiser';
        if (t < 0.82) return 'spitter';
        return 'splitter';
      }

      function makeEnemy(type, x, y, elite = false, splitDepth = 1) {
        let radius = 18;
        let hp = 88;
        let speed = 105;
        let damage = 14;
        let fireCd = rand(1.1, 2.0);

        if (type === 'chaser') {
          radius = 16; hp = 72; speed = 140; damage = 11;
        } else if (type === 'bruiser') {
          radius = 28; hp = 230; speed = 75; damage = 24;
        } else if (type === 'spitter') {
          radius = 19; hp = 108; speed = 92; damage = 13;
        } else if (type === 'splitter') {
          radius = 20; hp = 124; speed = 110; damage = 13;
        }

        const waveHpMul = 1 + state.wave * 0.16 + state.director * 0.27;
        const waveDmgMul = 1 + state.wave * 0.085 + state.director * 0.14;
        const waveSpdMul = 1 + Math.min(0.5, state.wave * 0.028 + state.director * 0.12);
        const eliteMul = elite ? 1.65 : 1;

        return {
          id: Math.random().toString(36).slice(2, 10),
          type,
          x,
          y,
          vx: 0,
          vy: 0,
          radius: radius * (1 + state.wave * 0.01) * (elite ? 1.2 : 1),
          hp: hp * waveHpMul * eliteMul,
          maxHp: hp * waveHpMul * eliteMul,
          speed: speed * waveSpdMul,
          damage: damage * waveDmgMul * (elite ? 1.22 : 1),
          touchCd: 0,
          fireCd: fireCd / (1 + state.wave * 0.018),
          splitDepth,
          elite
        };
      }

      function spawnEnemy(elite = false, forceType = null, aroundX = player.x, aroundY = player.y) {
        const angle = rand(0, Math.PI * 2);
        const distance = rand(620, 980);
        let x = aroundX + Math.cos(angle) * distance;
        let y = aroundY + Math.sin(angle) * distance;

        const d = length(x, y);
        const safeR = WORLD_RADIUS - 100;
        if (d > safeR) {
          x = (x / d) * safeR;
          y = (y / d) * safeR;
        }

        const type = forceType || enemyTypeForWave();
        const splitDepth = type === 'splitter' ? (state.wave >= 5 ? 2 : 1) : 0;
        state.enemies.push(makeEnemy(type, x, y, elite, splitDepth));
      }

      function spawnEliteWaveMarker() {
        showBanner('Wave ' + state.wave + ' elite pressure', 1.9);
        spawnEnemy(true, 'bruiser');
        if (state.wave >= 4) spawnEnemy(true, 'spitter');
      }

      function clearWorldArrays() {
        state.nutrients.length = 0;
        state.enemies.length = 0;
        state.enemyProjectiles.length = 0;
        state.playerProjectiles.length = 0;
        state.particles.length = 0;
        state.floatingTexts.length = 0;
      }

      function resetRun() {
        clearWorldArrays();
        state.score = 0;
        state.time = 0;
        state.wave = 1;
        state.waveTime = 0;
        state.director = 0.5;
        state.combo = 0;
        state.comboTimer = 0;
        state.spawnTimer = 0;
        state.shake = 0;
        state.killsRecent.length = 0;
        state.saveTick = 0;
        state.runStats.kills = 0;
        state.runStats.nutrients = 0;
        state.runStats.elites = 0;
        state.runStats.damageTaken = 0;
        state.runStats.highestCombo = 0;
        state.runStats.contractShardBonus = 0;
        ambientDropTimer = 0;
        announceTimer = 0;
        hideBanner();

        player.x = 0;
        player.y = 0;
        player.vx = 0;
        player.vy = 0;
        player.mass = 110;
        player.hp = 240;
        player.maxHp = 240;
        player.energy = 130;
        player.maxEnergy = 130;
        player.stage = 1;
        player.specialization = 'Hybrid';
        player.biomarkers.glucose = 0;
        player.biomarkers.amino = 0;
        player.biomarkers.lipid = 0;
        player.biomarkers.atp = 0;
        player.dashCd = 0;
        player.pulseCd = 0;
        player.boltCd = 0;
        player.dashTime = 0;
        player.invuln = 0;
        player.shield = 0;
        player.lastDamageAt = 0;
        rebuildPlayerStats();

        for (let i = 0; i < 45; i += 1) {
          const a = rand(0, Math.PI * 2);
          const r = rand(80, WORLD_RADIUS - 140);
          const typeRoll = Math.random();
          const type = typeRoll < 0.35 ? 'glucose' : typeRoll < 0.67 ? 'amino' : typeRoll < 0.92 ? 'lipid' : 'atp';
          spawnNutrient(Math.cos(a) * r, Math.sin(a) * r, type, false);
        }

        for (let i = 0; i < 6; i += 1) {
          spawnEnemy(false);
        }
      }

      function startRun() {
        ensureContracts(meta);
        resetRun();
        meta.activeSession = {
          startedAt: new Date().toISOString(),
          score: 0,
          wave: 1,
          stage: 1
        };
        persistMetaSave();
        startOverlay.style.display = 'none';
        gameOverOverlay.style.display = 'none';
        running = true;
        gameOver = false;
        showBanner('Survive and evolve');
        canvas.focus();
        lastTime = performance.now();
        if (rafId) cancelAnimationFrame(rafId);
        rafId = requestAnimationFrame(loop);
      }

      function endRun() {
        running = false;
        gameOver = true;
        const run = recordRunResult();
        finalLine.textContent =
          'Score: ' + fmtNumber(run.score) +
          ' | Wave: ' + run.wave +
          ' | Stage: ' + run.stage +
          ' | Spec: ' + run.spec +
          ' | Shards +' + fmtNumber(run.shards);
        gameOverOverlay.style.display = 'flex';
      }

      function triggerDash() {
        if (player.dashCd > 0 || player.energy < 28) return;
        let dx = 0;
        let dy = 0;

        if (keys['KeyW'] || keys['ArrowUp']) dy -= 1;
        if (keys['KeyS'] || keys['ArrowDown']) dy += 1;
        if (keys['KeyA'] || keys['ArrowLeft']) dx -= 1;
        if (keys['KeyD'] || keys['ArrowRight']) dx += 1;

        if (dx === 0 && dy === 0) {
          dx = mouse.worldX - player.x;
          dy = mouse.worldY - player.y;
        }
        const n = normalize(dx, dy);
        player.dashDirX = n.x;
        player.dashDirY = n.y;
        player.dashTime = 0.22;
        player.invuln = Math.max(player.invuln, 0.22);
        player.energy -= 28;
        player.dashCd = player.stats.dashCooldown;
        state.shake = Math.max(state.shake, 9);
        spawnBurst(player.x, player.y, SPEC_COLOR[player.specialization], 20, 0.9);
      }

      function triggerPulse() {
        if (player.pulseCd > 0 || player.energy < 42) return;
        player.energy -= 42;
        player.pulseCd = player.stats.pulseCooldown;
        const radius = 210 + player.radius * 0.8;
        const baseDamage = player.stats.pulseDamage;
        const knockback = player.specialization === 'Tank' ? 320 : 250;
        state.shake = Math.max(state.shake, 14);

        for (const enemy of state.enemies) {
          const dx = enemy.x - player.x;
          const dy = enemy.y - player.y;
          const d = Math.hypot(dx, dy);
          if (d <= radius + enemy.radius) {
            const falloff = 1 - clamp(d / radius, 0, 0.9);
            let damage = baseDamage * (0.65 + falloff * 0.65);
            if (Math.random() < player.stats.crit * 0.55) {
              damage *= 1.8;
              addFloatText('CRIT', enemy.x, enemy.y - enemy.radius - 8, '#ffc06d');
            }
            enemy.hp -= damage;
            const n = normalize(dx, dy);
            enemy.vx += n.x * knockback;
            enemy.vy += n.y * knockback;
            spawnBurst(enemy.x, enemy.y, SPEC_COLOR[player.specialization], 8, 0.6);
          }
        }

        spawnBurst(player.x, player.y, SPEC_COLOR[player.specialization], 55, 1.4);
      }

      function takePlayerDamage(rawDamage) {
        if (player.invuln > 0) return;
        const mitigation = 100 / (100 + player.stats.armor);
        let damage = rawDamage * mitigation;
        if (player.shield > 0) {
          const blocked = Math.min(player.shield, damage);
          player.shield -= blocked;
          damage -= blocked;
        }
        if (damage > 0) {
          player.hp -= damage;
          state.runStats.damageTaken += damage;
          player.lastDamageAt = state.time;
          state.shake = Math.max(state.shake, 6);
          spawnBurst(player.x, player.y, '#ff8f8f', 8, 0.5);
          addFloatText('-' + Math.round(damage), player.x, player.y - player.radius - 12, '#ffaaaa');
        }
        if (player.hp <= 0) {
          player.hp = 0;
          endRun();
        }
      }

      function spawnPlayerBolt() {
        if (player.boltCd > 0) return;
        let target = null;
        let best = Infinity;
        for (const enemy of state.enemies) {
          const dx = enemy.x - player.x;
          const dy = enemy.y - player.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < 480 * 480 && d2 < best) {
            best = d2;
            target = enemy;
          }
        }
        if (!target) return;

        const n = normalize(target.x - player.x, target.y - player.y);
        const speed = 520;
        state.playerProjectiles.push({
          x: player.x + n.x * player.radius,
          y: player.y + n.y * player.radius,
          vx: n.x * speed,
          vy: n.y * speed,
          radius: 4.5,
          life: 1.05,
          damage: player.stats.attack * 1.45
        });
        player.boltCd = clamp(0.42 - (player.stage - 1) * 0.025, 0.2, 0.42);
      }

      function spawnEnemyShot(enemy) {
        const n = normalize(player.x - enemy.x, player.y - enemy.y);
        const speed = 290 + state.wave * 6;
        state.enemyProjectiles.push({
          x: enemy.x + n.x * enemy.radius,
          y: enemy.y + n.y * enemy.radius,
          vx: n.x * speed,
          vy: n.y * speed,
          radius: 5.3,
          life: 2.2,
          damage: enemy.damage * 0.88
        });
      }

      function enemyColor(enemy) {
        if (enemy.type === 'chaser') return '#ff8484';
        if (enemy.type === 'bruiser') return '#b485ff';
        if (enemy.type === 'spitter') return '#ffbf75';
        return '#8ee1ff';
      }

      function onEnemyKilled(enemy) {
        dropFromEnemy(enemy);
        spawnBurst(enemy.x, enemy.y, enemyColor(enemy), enemy.elite ? 28 : 18, enemy.elite ? 1.4 : 1.0);

        const now = state.time;
        state.killsRecent.push(now);
        while (state.killsRecent.length && now - state.killsRecent[0] > 8) {
          state.killsRecent.shift();
        }

        if (state.comboTimer > 0) {
          state.combo += 1;
        } else {
          state.combo = 1;
        }
        state.comboTimer = 3.8;
        state.runStats.highestCombo = Math.max(state.runStats.highestCombo, state.combo);
        state.runStats.kills += 1;
        if (enemy.elite) state.runStats.elites += 1;
        applyContractProgress('kill', 1, false);

        const comboMult = 1 + state.combo * 0.07;
        const scoreGain = Math.round((enemy.maxHp * 0.23 + 14) * comboMult * scoreMetaMultiplier());
        state.score += scoreGain;
        player.mass += 5 + enemy.radius * 0.82;
        player.hp = Math.min(player.maxHp, player.hp + enemy.maxHp * 0.03 * player.stats.lifeSteal);

        addFloatText('+' + scoreGain, enemy.x, enemy.y - enemy.radius, '#9bf5ff');
        if (enemy.elite) {
          showBanner('Elite neutralized', 1.3);
          player.energy = Math.min(player.maxEnergy, player.energy + 24);
        }

        if (enemy.type === 'splitter' && enemy.splitDepth > 0) {
          for (let i = 0; i < 2; i += 1) {
            const angle = rand(0, Math.PI * 2);
            const child = makeEnemy('chaser', enemy.x + Math.cos(angle) * 30, enemy.y + Math.sin(angle) * 30, false, enemy.splitDepth - 1);
            child.radius *= 0.78;
            child.maxHp *= 0.58;
            child.hp = child.maxHp;
            child.damage *= 0.75;
            child.speed *= 1.16;
            state.enemies.push(child);
          }
        }
      }

      function collectNutrient(n) {
        let massGain = 8;
        if (n.type === 'glucose') {
          player.biomarkers.glucose += 1;
          massGain = 7;
        } else if (n.type === 'amino') {
          player.biomarkers.amino += 1;
          massGain = 9;
        } else if (n.type === 'lipid') {
          player.biomarkers.lipid += 1;
          massGain = 8;
          player.shield = Math.min(90, player.shield + 6);
        } else if (n.type === 'atp') {
          player.biomarkers.atp += 1;
          massGain = 6;
          player.energy = Math.min(player.maxEnergy, player.energy + 28);
          player.hp = Math.min(player.maxHp, player.hp + 6);
        }
        player.mass += massGain;
        state.runStats.nutrients += 1;
        applyContractProgress('nutrient', 1, false);
        state.score += Math.round((5 + massGain) * (1 + state.combo * 0.05) * scoreMetaMultiplier());
        state.particles.push({
          x: n.x, y: n.y, vx: rand(-45, 45), vy: rand(-65, -15),
          r: 2.2, life: 0.5, maxLife: 1, color: '#e6f4ff'
        });
      }

      function updateDirector(dt) {
        const now = state.time;
        while (state.killsRecent.length && now - state.killsRecent[0] > 8) {
          state.killsRecent.shift();
        }
        const killRate = state.killsRecent.length / 8;
        const hpRatio = player.hp / Math.max(1, player.maxHp);
        const target =
          0.36 +
          clamp((killRate - 1.05) * 0.18, -0.18, 0.42) +
          clamp((hpRatio - 0.65) * 0.44, -0.32, 0.35);
        state.director += (target - state.director) * clamp(dt * 1.8, 0, 1);
        state.director = clamp(state.director, 0.12, 0.96);
      }

      function spawnSystem(dt) {
        const maxEnemies = Math.round(12 + state.wave * 2.4 + state.director * 8);
        if (state.enemies.length >= maxEnemies) return;

        const spawnInterval = clamp(1.2 - state.wave * 0.048 - state.director * 0.34, 0.2, 1.24);
        state.spawnTimer += dt;
        if (state.spawnTimer < spawnInterval) return;
        state.spawnTimer = 0;

        spawnEnemy(false);
        if (state.wave >= 4 && Math.random() < 0.18 + state.director * 0.2) {
          spawnEnemy(false);
        }
      }

      function updateWave(dt) {
        state.waveTime += dt;
        if (state.waveTime >= 34) {
          state.wave += 1;
          applyContractProgress('wave', state.wave, true);
          state.waveTime = 0;
          player.hp = Math.min(player.maxHp, player.hp + player.maxHp * 0.18);
          player.energy = Math.min(player.maxEnergy, player.energy + 30);
          showBanner('Wave ' + state.wave, 1.8);
          if (state.wave % 3 === 0) {
            spawnEliteWaveMarker();
          }
        }
      }

      function updatePlayer(dt) {
        player.energy += player.stats.energyRegen * dt;
        if (state.time - player.lastDamageAt > 5.4) {
          player.hp += player.maxHp * 0.012 * dt;
        }
        player.energy = clamp(player.energy, 0, player.maxEnergy);
        player.hp = clamp(player.hp, 0, player.maxHp);

        player.dashCd = Math.max(0, player.dashCd - dt);
        player.pulseCd = Math.max(0, player.pulseCd - dt);
        player.boltCd = Math.max(0, player.boltCd - dt);
        player.invuln = Math.max(0, player.invuln - dt);

        if (player.dashTime > 0) {
          player.dashTime = Math.max(0, player.dashTime - dt);
          const dashSpeed = player.stats.speed * 4.8;
          player.vx = player.dashDirX * dashSpeed;
          player.vy = player.dashDirY * dashSpeed;
        } else {
          let dx = 0;
          let dy = 0;

          if (keys['KeyW'] || keys['ArrowUp']) dy -= 1;
          if (keys['KeyS'] || keys['ArrowDown']) dy += 1;
          if (keys['KeyA'] || keys['ArrowLeft']) dx -= 1;
          if (keys['KeyD'] || keys['ArrowRight']) dx += 1;

          if (dx === 0 && dy === 0 && mouse.active) {
            dx = mouse.worldX - player.x;
            dy = mouse.worldY - player.y;
          }

          if (Math.abs(dx) + Math.abs(dy) > 0) {
            const n = normalize(dx, dy);
            const targetVx = n.x * player.stats.speed;
            const targetVy = n.y * player.stats.speed;
            player.vx += (targetVx - player.vx) * clamp(dt * 9, 0, 1);
            player.vy += (targetVy - player.vy) * clamp(dt * 9, 0, 1);
            if (length(n.x, n.y) > 0.01) {
              player.dashDirX = n.x;
              player.dashDirY = n.y;
            }
          } else {
            player.vx *= Math.max(0, 1 - dt * 8);
            player.vy *= Math.max(0, 1 - dt * 8);
          }
        }

        player.x += player.vx * dt;
        player.y += player.vy * dt;

        const d = length(player.x, player.y);
        const boundary = WORLD_RADIUS - player.radius - 6;
        if (d > boundary) {
          player.x = (player.x / d) * boundary;
          player.y = (player.y / d) * boundary;
          player.vx *= 0.2;
          player.vy *= 0.2;
        }

        spawnPlayerBolt();
      }

      function updateEnemies(dt) {
        for (let i = state.enemies.length - 1; i >= 0; i -= 1) {
          const e = state.enemies[i];

          let dx = player.x - e.x;
          let dy = player.y - e.y;
          let dist = Math.hypot(dx, dy) || 1;
          let nx = dx / dist;
          let ny = dy / dist;

          if (e.type === 'spitter') {
            if (dist < 240) {
              nx = -nx;
              ny = -ny;
            } else if (dist > 580) {
              // close gap
            } else {
              nx *= 0.35;
              ny *= 0.35;
            }
            e.fireCd -= dt;
            if (e.fireCd <= 0 && dist < 700) {
              e.fireCd = rand(1.1, 1.8) / (1 + state.wave * 0.02);
              spawnEnemyShot(e);
            }
          }

          const targetVx = nx * e.speed;
          const targetVy = ny * e.speed;
          e.vx += (targetVx - e.vx) * clamp(dt * 4, 0, 1);
          e.vy += (targetVy - e.vy) * clamp(dt * 4, 0, 1);
          e.x += e.vx * dt;
          e.y += e.vy * dt;

          const fromCenter = length(e.x, e.y);
          const bound = WORLD_RADIUS - e.radius - 5;
          if (fromCenter > bound) {
            e.x = (e.x / fromCenter) * bound;
            e.y = (e.y / fromCenter) * bound;
            e.vx *= 0.6;
            e.vy *= 0.6;
          }

          e.touchCd = Math.max(0, e.touchCd - dt);

          dx = player.x - e.x;
          dy = player.y - e.y;
          dist = Math.hypot(dx, dy) || 1;
          nx = dx / dist;
          ny = dy / dist;
          const overlap = player.radius + e.radius + 4 - dist;
          if (overlap > 0) {
            if (e.touchCd <= 0) {
              e.touchCd = 0.52;
              takePlayerDamage(e.damage);
            }

            const dps = player.stats.contactDps * (player.dashTime > 0 ? 2.4 : 1.0);
            let damage = dps * dt;
            if (Math.random() < player.stats.crit * dt * 3.8) {
              damage *= 1.9;
              addFloatText('CRIT', e.x, e.y - e.radius - 10, '#ffce85');
            }
            e.hp -= damage;

            const push = (player.dashTime > 0 ? 320 : 86) * dt;
            e.x -= nx * push;
            e.y -= ny * push;
          }

          if (e.hp <= 0) {
            onEnemyKilled(e);
            state.enemies.splice(i, 1);
          }
        }
      }

      function updateProjectiles(dt) {
        for (let i = state.playerProjectiles.length - 1; i >= 0; i -= 1) {
          const p = state.playerProjectiles[i];
          p.x += p.vx * dt;
          p.y += p.vy * dt;
          p.life -= dt;

          let hit = false;
          for (const enemy of state.enemies) {
            const dx = enemy.x - p.x;
            const dy = enemy.y - p.y;
            const rr = enemy.radius + p.radius;
            if (dx * dx + dy * dy <= rr * rr) {
              let dmg = p.damage;
              if (Math.random() < player.stats.crit) {
                dmg *= 1.75;
                addFloatText('CRIT', enemy.x, enemy.y - enemy.radius - 8, '#ffcd78');
              }
              enemy.hp -= dmg;
              spawnBurst(p.x, p.y, '#b2eeff', 5, 0.45);
              hit = true;
              break;
            }
          }

          const d = length(p.x, p.y);
          if (hit || p.life <= 0 || d > WORLD_RADIUS + 90) {
            state.playerProjectiles.splice(i, 1);
          }
        }

        for (let i = state.enemyProjectiles.length - 1; i >= 0; i -= 1) {
          const p = state.enemyProjectiles[i];
          p.x += p.vx * dt;
          p.y += p.vy * dt;
          p.life -= dt;

          const dx = player.x - p.x;
          const dy = player.y - p.y;
          const rr = player.radius + p.radius;
          if (dx * dx + dy * dy <= rr * rr) {
            takePlayerDamage(p.damage);
            spawnBurst(p.x, p.y, '#ffba94', 7, 0.55);
            state.enemyProjectiles.splice(i, 1);
            continue;
          }

          const d = length(p.x, p.y);
          if (p.life <= 0 || d > WORLD_RADIUS + 90) {
            state.enemyProjectiles.splice(i, 1);
          }
        }
      }

      function updateNutrients(dt) {
        for (let i = state.nutrients.length - 1; i >= 0; i -= 1) {
          const n = state.nutrients[i];
          n.x += n.vx * dt;
          n.y += n.vy * dt;
          n.vx *= Math.max(0, 1 - dt * 3.5);
          n.vy *= Math.max(0, 1 - dt * 3.5);
          n.life -= dt;

          const dx = player.x - n.x;
          const dy = player.y - n.y;
          const rr = player.radius + n.radius + 4;
          if (dx * dx + dy * dy < rr * rr) {
            collectNutrient(n);
            state.nutrients.splice(i, 1);
            continue;
          }

          if (n.life <= 0) {
            state.nutrients.splice(i, 1);
          }
        }

        ambientDropTimer += dt;
        if (ambientDropTimer > 1.18) {
          ambientDropTimer = 0;
          if (state.nutrients.length < 140) {
            const a = rand(0, Math.PI * 2);
            const r = rand(120, WORLD_RADIUS - 120);
            const t = Math.random();
            const type = t < 0.35 ? 'glucose' : t < 0.66 ? 'amino' : t < 0.92 ? 'lipid' : 'atp';
            spawnNutrient(Math.cos(a) * r, Math.sin(a) * r, type, false);
          }
        }
      }

      function updateVisualEffects(dt) {
        for (let i = state.particles.length - 1; i >= 0; i -= 1) {
          const p = state.particles[i];
          p.x += p.vx * dt;
          p.y += p.vy * dt;
          p.vx *= Math.max(0, 1 - dt * 1.8);
          p.vy *= Math.max(0, 1 - dt * 1.8);
          p.life -= dt;
          if (p.life <= 0) {
            state.particles.splice(i, 1);
          }
        }

        for (let i = state.floatingTexts.length - 1; i >= 0; i -= 1) {
          const f = state.floatingTexts[i];
          f.y += f.vy * dt;
          f.life -= dt * 1.25;
          if (f.life <= 0) {
            state.floatingTexts.splice(i, 1);
          }
        }

        if (state.comboTimer > 0) {
          state.comboTimer -= dt;
          if (state.comboTimer <= 0) {
            state.combo = 0;
          }
        }

        if (announceTimer > 0) {
          announceTimer -= dt;
          if (announceTimer <= 0) {
            hideBanner();
          }
        }

        state.shake = Math.max(0, state.shake - dt * 22);
      }

      function gameStep(dt) {
        state.time += dt;
        rebuildPlayerStats();
        updateDirector(dt);
        updateWave(dt);
        spawnSystem(dt);
        updatePlayer(dt);
        updateEnemies(dt);
        updateProjectiles(dt);
        updateNutrients(dt);
        updateVisualEffects(dt);

        state.saveTick += dt;
        if (state.saveTick >= 8) {
          state.saveTick = 0;
          meta.activeSession = {
            startedAt: meta.activeSession?.startedAt || new Date().toISOString(),
            score: Math.floor(state.score),
            wave: state.wave,
            stage: player.stage
          };
          persistMetaSave();
          if (checkpointText) {
            checkpointText.textContent = 'W' + state.wave + ' · ' + fmtNumber(Math.floor(state.score));
          }
        }

        camera.x += (player.x - camera.x) * clamp(dt * 5.5, 0, 1);
        camera.y += (player.y - camera.y) * clamp(dt * 5.5, 0, 1);
        const targetZoom = clamp(1.08 - player.radius / 160, 0.55, 1.06);
        camera.zoom += (targetZoom - camera.zoom) * clamp(dt * 2.4, 0, 1);
      }

      function nutrientStyle(type) {
        if (type === 'glucose') return '#ffe66d';
        if (type === 'amino') return '#ff7f8b';
        if (type === 'lipid') return '#79b6ff';
        return '#6ef3ff';
      }

      function drawBackground(shakeX, shakeY) {
        const g = ctx.createLinearGradient(0, 0, 0, view.height);
        g.addColorStop(0, '#061024');
        g.addColorStop(1, '#03070f');
        ctx.fillStyle = g;
        ctx.fillRect(0, 0, view.width, view.height);

        ctx.save();
        ctx.translate(shakeX, shakeY);
        const gridStep = 74;
        const ox = ((-camera.x * camera.zoom) % gridStep + gridStep) % gridStep;
        const oy = ((-camera.y * camera.zoom) % gridStep + gridStep) % gridStep;
        ctx.strokeStyle = 'rgba(100, 145, 210, 0.13)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let x = ox; x < view.width; x += gridStep) {
          ctx.moveTo(x, 0);
          ctx.lineTo(x, view.height);
        }
        for (let y = oy; y < view.height; y += gridStep) {
          ctx.moveTo(0, y);
          ctx.lineTo(view.width, y);
        }
        ctx.stroke();
        ctx.restore();
      }

      function drawWorld() {
        const shakeX = (Math.random() - 0.5) * state.shake;
        const shakeY = (Math.random() - 0.5) * state.shake;
        drawBackground(shakeX, shakeY);

        ctx.save();
        ctx.translate(view.width / 2 + shakeX, view.height / 2 + shakeY);
        ctx.scale(camera.zoom, camera.zoom);
        ctx.translate(-camera.x, -camera.y);

        // World boundary
        ctx.beginPath();
        ctx.arc(0, 0, WORLD_RADIUS, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(110, 190, 255, 0.48)';
        ctx.lineWidth = 6;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(0, 0, WORLD_RADIUS, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(195, 232, 255, 0.5)';
        ctx.lineWidth = 1.5;
        ctx.stroke();

        for (const n of state.nutrients) {
          ctx.beginPath();
          const pulse = 1 + Math.sin(state.time * 6 + n.x * 0.03) * 0.15;
          ctx.fillStyle = nutrientStyle(n.type);
          ctx.globalAlpha = 0.95;
          ctx.arc(n.x, n.y, n.radius * pulse, 0, Math.PI * 2);
          ctx.fill();
          ctx.globalAlpha = 1;
        }

        // Player projectiles
        for (const p of state.playerProjectiles) {
          ctx.beginPath();
          ctx.fillStyle = '#b7eeff';
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();
        }

        // Enemy projectiles
        for (const p of state.enemyProjectiles) {
          ctx.beginPath();
          ctx.fillStyle = '#ffc18e';
          ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
          ctx.fill();
        }

        // Enemies
        for (const e of state.enemies) {
          const col = enemyColor(e);
          const hpRatio = clamp(e.hp / e.maxHp, 0, 1);

          ctx.beginPath();
          ctx.fillStyle = col;
          ctx.globalAlpha = e.elite ? 0.98 : 0.9;
          ctx.arc(e.x, e.y, e.radius, 0, Math.PI * 2);
          ctx.fill();
          ctx.globalAlpha = 1;

          if (e.type === 'spitter') {
            ctx.beginPath();
            ctx.fillStyle = '#2b1b08';
            ctx.arc(e.x, e.y, e.radius * 0.34, 0, Math.PI * 2);
            ctx.fill();
          } else if (e.type === 'splitter') {
            ctx.beginPath();
            ctx.strokeStyle = '#d6fbff';
            ctx.lineWidth = 2;
            ctx.arc(e.x, e.y, e.radius * 0.62, 0, Math.PI * 2);
            ctx.stroke();
          } else if (e.type === 'bruiser') {
            ctx.beginPath();
            ctx.strokeStyle = '#f1d7ff';
            ctx.lineWidth = 2.5;
            ctx.arc(e.x, e.y, e.radius * 0.68, 0, Math.PI * 2);
            ctx.stroke();
          }

          if (e.elite) {
            ctx.beginPath();
            ctx.strokeStyle = '#ffd9a5';
            ctx.lineWidth = 3;
            ctx.arc(e.x, e.y, e.radius + 4 + Math.sin(state.time * 5) * 2, 0, Math.PI * 2);
            ctx.stroke();
          }

          // enemy hp bar
          const w = e.radius * 1.6;
          const h = 4;
          ctx.fillStyle = 'rgba(0,0,0,0.45)';
          ctx.fillRect(e.x - w / 2, e.y - e.radius - 10, w, h);
          ctx.fillStyle = '#7ff0bf';
          ctx.fillRect(e.x - w / 2, e.y - e.radius - 10, w * hpRatio, h);
        }

        // Player
        const specColor = SPEC_COLOR[player.specialization];
        ctx.beginPath();
        ctx.fillStyle = specColor;
        ctx.globalAlpha = 0.26;
        ctx.arc(player.x, player.y, player.radius * 1.55, 0, Math.PI * 2);
        ctx.fill();
        ctx.globalAlpha = 1;

        ctx.beginPath();
        const pulse = 1 + Math.sin(state.time * 4.7) * 0.03;
        ctx.fillStyle = specColor;
        ctx.arc(player.x, player.y, player.radius * pulse, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.fillStyle = '#f7feff';
        ctx.arc(player.x + player.dashDirX * player.radius * 0.24, player.y + player.dashDirY * player.radius * 0.24, player.radius * 0.31, 0, Math.PI * 2);
        ctx.fill();

        if (player.invuln > 0) {
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(160, 240, 255, 0.9)';
          ctx.lineWidth = 3;
          ctx.arc(player.x, player.y, player.radius + 10 + Math.sin(state.time * 20) * 1.8, 0, Math.PI * 2);
          ctx.stroke();
        }

        if (player.shield > 1) {
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(145, 188, 255, 0.65)';
          ctx.lineWidth = 2;
          ctx.arc(player.x, player.y, player.radius + 4, 0, Math.PI * 2);
          ctx.stroke();
        }

        // Particles
        for (const p of state.particles) {
          const alpha = clamp(p.life / p.maxLife, 0, 1);
          ctx.globalAlpha = alpha;
          ctx.beginPath();
          ctx.fillStyle = p.color;
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.globalAlpha = 1;

        // Floating text
        for (const f of state.floatingTexts) {
          ctx.globalAlpha = clamp(f.life, 0, 1);
          ctx.fillStyle = f.color;
          ctx.font = 'bold 14px Inter, Segoe UI, Arial';
          ctx.textAlign = 'center';
          ctx.fillText(f.text, f.x, f.y);
        }
        ctx.globalAlpha = 1;

        ctx.restore();
      }

      function updateHud(force = false) {
        hudTimer += force ? 999 : 0.016;
        if (!force && hudTimer < 0.07) return;
        hudTimer = 0;

        const hpRatio = clamp(player.hp / player.maxHp, 0, 1);
        const enRatio = clamp(player.energy / player.maxEnergy, 0, 1);
        const b = player.biomarkers;
        const totalBio = Math.max(1, b.glucose + b.amino + b.lipid);
        const dominant = Math.max(b.glucose, b.amino, b.lipid);
        const dominantPct = Math.round((dominant / totalBio) * 100);

        hpFill.style.width = (hpRatio * 100).toFixed(1) + '%';
        energyFill.style.width = (enRatio * 100).toFixed(1) + '%';
        bioFill.style.width = dominantPct + '%';
        bioFill.style.background =
          player.specialization === 'Speedster'
            ? 'linear-gradient(90deg,#ffdf47 0%,#ffeeb0 100%)'
            : player.specialization === 'Predator'
              ? 'linear-gradient(90deg,#ff7f8a 0%,#ffb9c0 100%)'
              : player.specialization === 'Tank'
                ? 'linear-gradient(90deg,#72b5ff 0%,#b0d6ff 100%)'
                : 'linear-gradient(90deg,#50e7a9 0%,#aefbd6 100%)';

        hpText.textContent = Math.round(player.hp) + ' / ' + Math.round(player.maxHp);
        energyText.textContent = Math.round(player.energy) + ' / ' + Math.round(player.maxEnergy);
        bioText.textContent = player.specialization + ' (' + dominantPct + '%)';
        waveText.textContent = String(state.wave);
        massText.textContent = String(Math.round(player.mass));
        stageText.textContent = String(player.stage);
        scoreText.textContent = String(Math.round(state.score));
        comboText.textContent = state.combo > 0 ? ('x' + state.combo) : 'x1';
        enemyCountText.textContent = String(state.enemies.length);
        directorText.textContent = Math.round(state.director * 100) + '%';
      }

      function loop(ts) {
        if (!running) return;
        const dt = clamp((ts - lastTime) / 1000, 0.001, 0.033);
        lastTime = ts;

        const worldMouse = screenToWorld(mouse.x, mouse.y);
        mouse.worldX = worldMouse.x;
        mouse.worldY = worldMouse.y;

        gameStep(dt);
        drawWorld();
        updateHud(false);

        if (gameOver) return;
        rafId = requestAnimationFrame(loop);
      }

      function onKeyDown(e) {
        keys[e.code] = true;
        if (e.code === 'Space') {
          e.preventDefault();
          if (running) triggerDash();
        } else if (e.code === 'KeyE') {
          if (running) triggerPulse();
        } else if (e.code === 'Enter') {
          if (!running) startRun();
        } else if (e.code === 'KeyR') {
          if (gameOver) startRun();
        }
      }

      function onKeyUp(e) {
        keys[e.code] = false;
      }

      function bindInput() {
        window.addEventListener('resize', updateCanvasSize);
        updateCanvasSize();

        canvas.addEventListener('mousemove', (e) => {
          const rect = canvas.getBoundingClientRect();
          mouse.x = e.clientX - rect.left;
          mouse.y = e.clientY - rect.top;
          mouse.active = true;
        });

        canvas.addEventListener('mouseleave', () => {
          mouse.active = false;
        });

        canvas.addEventListener('mousedown', () => {
          canvas.focus();
          mouse.active = true;
          if (running) triggerDash();
        });

        window.addEventListener('keydown', onKeyDown);
        window.addEventListener('keyup', onKeyUp);

        startBtn.addEventListener('click', startRun);
        restartBtn.addEventListener('click', startRun);

        pilotSaveBtn.addEventListener('click', () => {
          const nextName = (pilotInput.value || '').trim().slice(0, 16);
          if (!nextName) {
            showBanner('Pilot name cannot be empty', 1.1);
            return;
          }
          meta.pilot = nextName;
          persistMetaSave();
          renderMetaPanels();
          showBanner('Pilot profile saved', 1.0);
        });
        pilotInput.addEventListener('keydown', (e) => {
          if (e.code === 'Enter') {
            e.preventDefault();
            pilotSaveBtn.click();
          }
        });
      }

      function drawIdleScreen() {
        drawBackground(0, 0);
        updateHud(true);
      }

      bindInput();
      renderMetaPanels();
      if (meta.activeSession && meta.activeSession.wave) {
        showBanner('Checkpoint detected: W' + meta.activeSession.wave + ' · ' + fmtNumber(meta.activeSession.score), 2.4);
      }
      resetRun();
      drawIdleScreen();
    })();
  </script>
</body>
</html>
"""


components.html(GAME_HTML, height=900, scrolling=False)
