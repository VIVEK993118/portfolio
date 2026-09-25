<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Sky Runner</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html,body{
    width:100%;
    height:100%;
    overflow:hidden;
    background:#111;
    font-family:Arial,sans-serif;
    touch-action:none;
}

#game{
    position:relative;
    width:100%;
    height:100%;
}

canvas{
    display:block;
    width:100%;
    height:100%;
}

#hud{
    position:absolute;
    top:15px;
    left:15px;
    right:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    color:white;
    font-weight:bold;
    font-size:18px;
    z-index:5;
    pointer-events:none;
}

.stats{
    display:flex;
    gap:18px;
    flex-wrap:wrap;
}

.stat{
    background:rgba(0,0,0,.35);
    padding:8px 12px;
    border-radius:10px;
    text-shadow:1px 1px 2px #000;
}

#pauseBtn{
    pointer-events:auto;
    border:0;
    padding:9px 15px;
    border-radius:10px;
    background:rgba(0,0,0,.45);
    color:white;
    font-weight:bold;
    cursor:pointer;
}

.screen{
    position:absolute;
    inset:0;
    background:rgba(0,0,0,.67);
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    color:white;
    z-index:10;
    text-align:center;
}

.hidden{
    display:none!important;
}

.logo{
    font-size:clamp(42px,9vw,95px);
    color:#ffd60a;
    font-weight:900;
    text-shadow:5px 5px 0 #111;
    margin-bottom:12px;
}

.sub{
    font-size:18px;
    margin-bottom:28px;
}

.btn{
    border:0;
    border-radius:13px;
    padding:14px 34px;
    margin:7px;
    font-size:18px;
    font-weight:bold;
    cursor:pointer;
    background:#ff3b30;
    color:white;
}

.btn:hover{
    transform:scale(1.04);
}

.blue{
    background:#168cff;
}

.green{
    background:#27ae60;
}

.yellow{
    background:#f39c12;
}

#mobileControls{
    position:absolute;
    bottom:20px;
    left:0;
    width:100%;
    display:none;
    justify-content:space-between;
    padding:0 25px;
    z-index:6;
}

.control{
    width:78px;
    height:78px;
    border-radius:50%;
    border:2px solid rgba(255,255,255,.6);
    background:rgba(0,0,0,.3);
    color:white;
    font-size:15px;
    font-weight:bold;
}

#shop{
    max-width:500px;
}

.skinList{
    display:flex;
    gap:10px;
    margin:15px 0;
    flex-wrap:wrap;
    justify-content:center;
}

.skin{
    width:75px;
    height:75px;
    border:3px solid white;
    border-radius:12px;
    cursor:pointer;
}

#achievementText{
    margin-top:10px;
    font-size:14px;
    opacity:.9;
}

@media(max-width:700px){
    #mobileControls{
        display:flex;
    }

    #hud{
        font-size:13px;
    }

    .stats{
        gap:5px;
    }

    .stat{
        padding:6px 8px;
    }

    #pauseBtn{
        padding:7px 10px;
    }
}
</style>
</head>

<body>

<div id="game">

<canvas id="canvas"></canvas>

<div id="hud">
    <div class="stats">
        <div class="stat">🏆 <span id="score">0</span></div>
        <div class="stat">🪙 <span id="coins">0</span></div>
        <div class="stat">❤️ <span id="health">3</span></div>
        <div class="stat">⚡ <span id="speed">1</span></div>
        <div class="stat">🏅 <span id="high">0</span></div>
    </div>

    <button id="pauseBtn">PAUSE</button>
</div>

<div id="startScreen" class="screen">

    <div class="logo">SKY RUNNER</div>

    <div class="sub">
        Run • Jump • Collect • Survive
    </div>

    <button class="btn" id="startBtn">
        START GAME
    </button>

    <button class="btn blue" id="shopBtn">
        CHARACTER SHOP
    </button>

    <div id="achievementText">
        Best Score: <span id="menuHigh">0</span>
    </div>

</div>

<div id="gameOver" class="screen hidden">

    <div class="logo">GAME OVER</div>

    <div class="sub">
        Score: <span id="finalScore">0</span>
        <br>
        Coins: <span id="finalCoins">0</span>
        <br>
        Best: <span id="finalHigh">0</span>
    </div>

    <button class="btn" id="restartBtn">
        PLAY AGAIN
    </button>

    <button class="btn blue" id="menuBtn">
        MAIN MENU
    </button>

</div>

<div id="pauseScreen" class="screen hidden">

    <div class="logo">PAUSED</div>

    <button class="btn green" id="resumeBtn">
        RESUME
    </button>

    <button class="btn" id="pauseMenuBtn">
        MAIN MENU
    </button>

</div>

<div id="shop" class="screen hidden">

    <div class="logo">SKINS</div>

    <div class="sub">
        Coins: <span id="shopCoins">0</span>
    </div>

    <div class="skinList">

        <div class="skin" data-skin="red"
             style="background:#e74c3c"></div>

        <div class="skin" data-skin="blue"
             style="background:#3498db"></div>

        <div class="skin" data-skin="green"
             style="background:#2ecc71"></div>

        <div class="skin" data-skin="purple"
             style="background:#9b59b6"></div>

        <div class="skin" data-skin="gold"
             style="background:#f1c40f"></div>

    </div>

    <button class="btn blue" id="shopBack">
        BACK
    </button>

</div>

<div id="mobileControls">

    <button class="control" id="leftBtn">
        ◀
    </button>

    <button class="control" id="jumpBtn">
        JUMP
    </button>

    <button class="control" id="rightBtn">
        ▶
    </button>

</div>

</div>

<script>

/* =====================================================
   CANVAS
===================================================== */

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");

let W = 0;
let H = 0;

function resize(){

    W = canvas.width =
        window.innerWidth * devicePixelRatio;

    H = canvas.height =
        window.innerHeight * devicePixelRatio;

    canvas.style.width =
        window.innerWidth + "px";

    canvas.style.height =
        window.innerHeight + "px";

    ctx.setTransform(
        devicePixelRatio,
        0,
        0,
        devicePixelRatio,
        0,
        0
    );

    W = window.innerWidth;
    H = window.innerHeight;
}

resize();

window.addEventListener(
    "resize",
    resize
);


/* =====================================================
   DOM
===================================================== */

const scoreEl =
    document.getElementById("score");

const coinsEl =
    document.getElementById("coins");

const healthEl =
    document.getElementById("health");

const speedEl =
    document.getElementById("speed");

const highEl =
    document.getElementById("high");

const menuHigh =
    document.getElementById("menuHigh");

const startScreen =
    document.getElementById("startScreen");

const gameOver =
    document.getElementById("gameOver");

const pauseScreen =
    document.getElementById("pauseScreen");

const shop =
    document.getElementById("shop");

const finalScore =
    document.getElementById("finalScore");

const finalCoins =
    document.getElementById("finalCoins");

const finalHigh =
    document.getElementById("finalHigh");

const shopCoins =
    document.getElementById("shopCoins");


/* =====================================================
   GAME VARIABLES
===================================================== */

let running = false;
let paused = false;

let score = 0;
let coins = 0;
let health = 3;

let gameSpeed = 6;
let level = 1;

let frame = 0;

let obstacleTimer = 0;
let coinTimer = 0;
let powerTimer = 0;

let particles = [];

let obstacles = [];
let coinObjects = [];
let powerUps = [];
let clouds = [];

let worldX = 0;

let highScore =
    Number(
        localStorage.getItem(
            "skyRunnerHighScore"
        ) || 0
    );

let totalCoins =
    Number(
        localStorage.getItem(
            "skyRunnerCoins"
        ) || 0
    );

let selectedSkin =
    localStorage.getItem(
        "skyRunnerSkin"
    ) || "red";

let ownedSkins =
    JSON.parse(
        localStorage.getItem(
            "skyRunnerSkins"
        ) || '["red"]'
    );

let shield = false;
let magnet = false;
let doubleCoins = false;

let dayNight = 0;


/* =====================================================
   PLAYER
===================================================== */

const player = {

    x:120,

    y:0,

    width:48,

    height:65,

    velocityY:0,

    gravity:.82,

    jumpPower:15,

    velocityX:0,

    speed:5,

    onGround:true,

    invincible:0,

    anim:0,

    direction:1

};


/* =====================================================
   COLORS
===================================================== */

const skinColors = {

    red:"#e74c3c",

    blue:"#3498db",

    green:"#2ecc71",

    purple:"#9b59b6",

    gold:"#f1c40f"

};


/* =====================================================
   AUDIO
===================================================== */

let audioCtx = null;

function audio(){

    if(!audioCtx){

        audioCtx =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();
    }
}

function beep(
    frequency,
    duration,
    type="sine"
){

    try{

        audio();

        const osc =
            audioCtx.createOscillator();

        const gain =
            audioCtx.createGain();

        osc.frequency.value =
            frequency;

        osc.type = type;

        gain.gain.value=.04;

        osc.connect(gain);

        gain.connect(
            audioCtx.destination
        );

        osc.start();

        osc.stop(
            audioCtx.currentTime+
            duration
        );

    }catch(e){}
}


/* =====================================================
   RESET
===================================================== */

function resetGame(){

    score=0;
    coins=0;
    health=3;

    gameSpeed=6;
    level=1;

    frame=0;

    obstacleTimer=70;
    coinTimer=30;
    powerTimer=500;

    shield=false;
    magnet=false;
    doubleCoins=false;

    player.x=120;
    player.y=0;

    player.velocityY=0;
    player.velocityX=0;

    player.onGround=true;
    player.invincible=0;

    obstacles=[];
    coinObjects=[];
    powerUps=[];
    particles=[];

    updateHUD();
}


/* =====================================================
   START
===================================================== */

function startGame(){

    resetGame();

    startScreen.classList.add(
        "hidden"
    );

    gameOver.classList.add(
        "hidden"
    );

    pauseScreen.classList.add(
        "hidden"
    );

    shop.classList.add(
        "hidden"
    );

    running=true;
    paused=false;

    audio();

    createClouds();

    requestAnimationFrame(loop);
}


/* =====================================================
   MAIN LOOP
===================================================== */

function loop(){

    if(!running){
        return;
    }

    if(!paused){

        frame++;

        update();

        draw();
    }

    requestAnimationFrame(loop);
}


/* =====================================================
   UPDATE
===================================================== */

function update(){

    worldX += gameSpeed;

    score += .08;

    gameSpeed += .0015;

    level =
        Math.floor(
            score/500
        )+1;

    dayNight += .0005;

    updatePlayer();

    spawnObjects();

    updateObstacles();

    updateCoins();

    updatePowerUps();

    updateParticles();

    updateClouds();

    checkCollisions();

    updateHUD();

}


/* =====================================================
   PLAYER UPDATE
===================================================== */

function updatePlayer(){

    player.velocityY -=
        player.gravity;

    player.y +=
        player.velocityY;

    if(player.y <= 0){

        player.y=0;

        player.velocityY=0;

        player.onGround=true;

    }else{

        player.onGround=false;
    }

    player.x +=
        player.velocityX;

    player.velocityX *= .82;

    const groundLeft=25;

    const groundRight=
        W-80;

    if(player.x<groundLeft)
        player.x=groundLeft;

    if(player.x>groundRight)
        player.x=groundRight;

    if(player.invincible>0)
        player.invincible--;

    player.anim +=
        .25 + gameSpeed*.01;
}


/* =====================================================
   JUMP
===================================================== */

function jump(){

    if(!running || paused)
        return;

    if(player.onGround){

        player.velocityY =
            player.jumpPower;

        player.onGround=false;

        beep(
            500,
            .08,
            "square"
        );

        createParticles(
            player.x+20,
            groundY(),
            8,
            "#fff"
        );
    }
}


/* =====================================================
   MOVEMENT
===================================================== */

function moveLeft(){

    if(!running || paused)
        return;

    player.velocityX=-player.speed;
    player.direction=-1;
}


function moveRight(){

    if(!running || paused)
        return;

    player.velocityX=player.speed;
    player.direction=1;
}


/* =====================================================
   GROUND
===================================================== */

function groundY(){

    return H-105;
}


/* =====================================================
   SPAWN
===================================================== */

function spawnObjects(){

    obstacleTimer--;

    if(obstacleTimer<=0){

        createObstacle();

        let minimum =
            Math.max(
                38,
                95-level*2
            );

        obstacleTimer =
            Math.floor(
                Math.random()*65
            )+
            minimum;
    }


    coinTimer--;

    if(coinTimer<=0){

        createCoinPattern();

        coinTimer =
            Math.floor(
                Math.random()*80
            )+
            55;
    }


    powerTimer--;

    if(powerTimer<=0){

        createPowerUp();

        powerTimer =
            Math.floor(
                Math.random()*700
            )+
            700;
    }
}


/* =====================================================
   OBSTACLE
===================================================== */

function createObstacle(){

    const types=[
        "rock",
        "box",
        "spike",
        "barrel"
    ];

    const type =
        types[
            Math.floor(
                Math.random()*types.length
            )
        ];

    obstacles.push({

        x:W+100,

        y:groundY(),

        width:
            type==="spike"
            ?50:45,

        height:
            type==="rock"
            ?40:
            type==="spike"
            ?48:
            type==="barrel"
            ?55:55,

        type:type,

        passed:false
    });
}


/* =====================================================
   COINS
===================================================== */

function createCoinPattern(){

    const pattern =
        Math.floor(
            Math.random()*4
        );

    const startX =
        W+80;

    if(pattern===0){

        for(let i=0;i<6;i++){

            coinObjects.push({

                x:startX+i*42,

                y:groundY()-
                    70,

                size:16,

                rotation:0
            });
        }

    }else if(pattern===1){

        for(let i=0;i<7;i++){

            coinObjects.push({

                x:startX+i*42,

                y:
                    groundY()-
                    50-
                    Math.sin(i/2)*55,

                size:16,

                rotation:0
            });
        }

    }else if(pattern===2){

        for(let i=0;i<5;i++){

            coinObjects.push({

                x:startX+i*42,

                y:
                    groundY()-
                    100-

                    i*20,

                size:16,

                rotation:0
            });
        }

    }else{

        for(let i=0;i<10;i++){

            coinObjects.push({

                x:startX+i*38,

                y:
                    groundY()-
                    70,

                size:16,

                rotation:0
            });
        }
    }
}


/* =====================================================
   POWER UPS
===================================================== */

function createPowerUp(){

    const types=[
        "shield",
        "magnet",
        "double"
    ];

    const type =
        types[
            Math.floor(
                Math.random()*types.length
            )
        ];

    powerUps.push({

        x:W+100,

        y:
            groundY()-
            150-

            Math.random()*80,

        size:24,

        type:type
    });
}


/* =====================================================
   UPDATE OBSTACLES
===================================================== */

function updateObstacles(){

    for(
        let i=obstacles.length-1;
        i>=0;
        i--
    ){

        const o =
            obstacles[i];

        o.x -= gameSpeed;

        if(
            !o.passed &&
            o.x+o.width<
            player.x
        ){

            o.passed=true;

            score+=5;
        }

        if(
            o.x<
            -100
        ){

            obstacles.splice(i,1);
        }
    }
}


/* =====================================================
   UPDATE COINS
===================================================== */

function updateCoins(){

    for(
        let i=coinObjects.length-1;
        i>=0;
        i--
    ){

        const c =
            coinObjects[i];

        c.x-=gameSpeed;

        c.rotation +=
            .12;

        if(magnet){

            const dx =
                player.x-c.x;

            const dy =
                (
                    groundY()-
                    player.y-
                    player.height/2
                )-
                c.y;

            const distance =
                Math.sqrt(
                    dx*dx+dy*dy
                );

            if(distance<180){

                c.x +=
                    dx*.08;

                c.y +=
                    dy*.08;
            }
        }

        if(c.x<-100){

            coinObjects.splice(i,1);
        }
    }
}


/* =====================================================
   UPDATE POWER
===================================================== */

function updatePowerUps(){

    for(
        let i=powerUps.length-1;
        i>=0;
        i--
    ){

        const p =
            powerUps[i];

        p.x -= gameSpeed;

        if(p.x<-100){

            powerUps.splice(i,1);
        }
    }
}


/* =====================================================
   COLLISION
===================================================== */

function checkCollisions(){

    const px=
        player.x;

    const py=
        groundY()-
        player.y-
        player.height;

    const pw=
        player.width;

    const ph=
        player.height;


    for(const o of obstacles){

        const ox=o.x;
        const oy=
            o.y-o.height;

        if(

            px<ox+o.width &&
            px+pw>ox &&
            py<oy+o.height &&
            py+ph>oy

        ){

            if(
                player.invincible<=0
            ){

                hitObstacle(o);
            }

            break;
        }
    }


    for(
        let i=coinObjects.length-1;
        i>=0;
        i--
    ){

        const c=
            coinObjects[i];

        const cx=c.x;
        const cy=c.y;

        const distance=
            Math.sqrt(

                (px+pw/2-cx)*
                (px+pw/2-cx)+

                (py+ph/2-cy)*
                (py+ph/2-cy)

            );

        if(distance<35){

            collectCoin(i);
        }
    }


    for(
        let i=powerUps.length-1;
        i>=0;
        i--
    ){

        const p=
            power