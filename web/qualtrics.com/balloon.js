//可配置参数
var timing = 10;//爆破时间正计时
var questionTime = 15;//回答问题倒计时
var failureTime = 5;//爆破失败倒计时
var countdown = 3;//任务完成倒计时
var rounds = 20;//总轮数
var balloons = 30;//每轮气球个数
var BlastClicks = 40;//爆破需要的点击次数
var pay = 10;//任务完成报酬,单位:元

//全局变量
var startTime, endTime, clickNum, balloonNum, that, quesId;
clickNum = 0;//点击次数
balloonNum = 0;//已爆破的气球数

Qualtrics.SurveyEngine.addOnload(function()
{
    that = this;
    quesId = that.questionId;
    that.hideNextButton();   
    var inner = document.getElementsByClassName("Inner");
    inner[0].style.display = "none";
    loadHtml();
    // loadCanvas.call(this);
    // drawCircle();
    // var canvas = document.getElementById('balloon');
    // canvas.on('click', clickEvent);
    // console.log(Qualtrics.SurveyEngine.QuestionInfo[this.questionId]);
});

function loadHtml(){
    balloonNum +=1;
    var content = document.createElement('div');
    content.id = "loadHtml";
    content.style.textAlign = "center";
    content.style.clear = "both";
    content.innerHTML="<div>已用时:<span id='timing'></span></div>";
    content.innerHTML+="<div style='position:relative;'><span id='clickNum'  onselectstart='return false;' style='position: absolute;left: 309px;top: 28px;font-size: 54px;font-weight: bold;width:152px;height:152px;line-height:152px;cursor:pointer;text-align:center;border-radius:76px;'></span><img id='balloon' border='0' src='https://rucsb.asia.qualtrics.com/WRQualtricsControlPanel/Graphic.php?IM=IM_7Oo1i47qgXZCaWN' alt='Balloon' data-image-state='ready'></div>";
    content.innerHTML+="<button id='close' style='color: #fff;background-color: #DC143C;border-color: #DC143C;padding: 2.5px 10px;float:right;margin-right:150px;'>结束任务</button>"; 
    setTimeout(function(){
        timeInput.value += "*******"+balloonNum+":  ";       
        that.questionContainer.appendChild(content);
        loadHtmlEvent();
    },"150"); 
}
function loadHtmlEvent(){
    clickNum = 0;//点击次数
    var balloon = document.getElementById('balloon');
    var clickNumSpan = document.getElementById('clickNum');
    var close = document.getElementById('close');
    clickNumSpan.onclick = function(){
        clickNum ++;
        clickNumSpan.innerHTML=clickNum;
        balloon.style.marginLeft = "-20px";
        clickNumSpan.style.left = "289px";
            setTimeout(function () {
                balloon.style.marginLeft = "-10px";
                clickNumSpan.style.left = "299px";
            },30);
            setTimeout(function () {
                balloon.style.marginLeft = "0px";
                clickNumSpan.style.left = "309px";
            },60);
        console.log(clickNum);
        if (clickNum === 1) {
            startTime = new Date().getTime();
        }
        else if (clickNum === BlastClicks) {
            endTime = new Date().getTime();
            var time = Math.round((endTime - startTime) / 100) / 10;
            var el = document.getElementById('loadHtml');
            window.clearInterval(int);
            el.parentNode.removeChild(el);
            timeInput.value += time;
            if(balloonNum > balloons){
                next();
            }else{
                question();
            }
        }
    };
    close.onclick = function(){
        that.clickNextButton();
    };
    timingCount();
}
//失败页面
function loadClose(){
    var content = document.createElement('div');
    content.id = "loadClose";
    content.style.textAlign = "center";
    content.innerHTML="<div>爆破失败，任务结束（<span id='time2'></span>后回到主页面)</div>";  
    that.questionContainer.appendChild(content);
    var timingSpan = document.getElementById('time2');
    var tt = failureTime;
    timingSpan.innerHTML = tt+"秒";
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt+"秒";
        if(tt==0){
            window.clearInterval(int2);
            that.clickNextButton();
        }
    },1000);
}
//问题页面
function question(){

}
//问题后下一个页面
function qnext(){

}
//无问题后下一个页面
function next(){

}
//任务完成页面
function success(){
    
}
//全部任务完成界面
function successAll(){

}

//正计时
function timingCount(){
    var timingSpan = document.getElementById('timing');
    var tt = 0;
    timingSpan.innerHTML = tt+"秒";
    int=setInterval(function(){
        tt +=1;
        timingSpan.innerHTML = tt+"秒";
        if(tt>=timing){
            var el = document.getElementById('loadHtml');
            window.clearInterval(int);
            // el.parentNode.removeChild(el);
            timeInput.value += "failure";
            console.log(timeInput.value);
            // loadClose();
        }
    },1000);
}
