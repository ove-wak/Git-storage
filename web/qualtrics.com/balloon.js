//可配置参数
var timing = 10;//爆破时间正计时
var questionTime = 15;//回答问题倒计时
var failureTime = 5;//爆破失败倒计时
var countdown = 3;//任务完成倒计时
var rounds = 2;//总轮数
var balloons = 5;//每轮气球个数
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
});

function loadHtml(){
    balloonNum +=1;
    var content = document.createElement('div');
    content.id = "loadHtml";
    content.style.textAlign = "center";
    content.style.clear = "both";
    content.innerHTML="<div style='font-size:20px;'>已用时:<span style='font-size:36px;font-weight:bold;' id='timing'></span>秒</div>";
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
        if (clickNum === 1) {
            startTime = new Date().getTime();
        }
        else if (clickNum === BlastClicks) {
            endTime = new Date().getTime();
            var time = Math.round((endTime - startTime) / 100) / 10;
            var el = document.getElementById('loadHtml');
            window.clearInterval(int);
            el.parentNode.removeChild(el);
            timeInput.value += time+",  ";
            console.log(timeInput.value);
            if(balloonNum - balloons <= 0){
                question();
            }else if(balloonNum % balloons == 0){
                if(parseInt(balloonNum/balloons) == rounds){
                    successAll(); 
                }else{
                   success(); 
                }              
            }else{
                next();
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
    content.innerHTML="<div style='font-size:20px;'>爆破失败，任务结束(<span id='time2'></span>秒后回到主页面)</div>";  
    that.questionContainer.appendChild(content);
    var timingSpan = document.getElementById('time2');
    var tt = failureTime;
    timingSpan.innerHTML = tt;
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt;
        if(tt==0){
            window.clearInterval(int2);
            that.clickNextButton();
        }
    },1000);
}
//问题页面
function question(){
    var content = document.createElement('div');
    content.id = "question";
    content.style.textAlign = "center";
    content.innerHTML="<div style='font-size:20px;'><span id='time2'></span>秒后页面自动跳转</div>"; 
    content.innerHTML+="<div style='font-size:30px;'>爆破成功，请回答（在问题后输入数字即可）：</div>" ;
    content.innerHTML+="<div style='font-size:30px;'>此刻，你感觉这个任务有多难？（1=非常难，9=非常简单） <input width='30px' id='q1'/></div>" ;
    content.innerHTML+="<div style='font-size:30px;'>此刻，你对这个任务有多适应？（1=非常不适应，9=非常适应）<input width='30px' id='q2'/></div>" ;
    content.innerHTML+="<button id='close' style='color: #fff;background-color: #DC143C;border-color: #DC143C;padding: 2.5px 10px;float:right;margin-right:150px;'>结束任务</button>"; 
    that.questionContainer.appendChild(content);
    var timingSpan = document.getElementById('time2');
    var close = document.getElementById('close');
    var tt = questionTime;
    timingSpan.innerHTML = tt;
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt;
        if(tt==0){
            timeInput.value += document.getElementById('q1').value + ",  ";
            timeInput.value += document.getElementById('q2').value + ",  ";
            console.log(timeInput.value);
            window.clearInterval(int2);
            var el = document.getElementById('question');
            el.parentNode.removeChild(el);
            if(balloonNum - balloons == 0){
                success();
            }else{
               qnext(); 
            }          
        }
    },1000);
    close.onclick = function(){
        that.clickNextButton();
    };
}
//问题后下一个页面
function qnext(){
    var content = document.createElement('div');
    content.id = "qnext";
    content.style.textAlign = "center";
    content.innerHTML="<div style='font-size:20px;'>回答结束,下一轮加载中(倒计时<span id='time2'></span>秒)</div>";  
    content.innerHTML+="<button id='close' style='color: #fff;background-color: #DC143C;border-color: #DC143C;padding: 2.5px 10px;float:right;margin-right:150px;'>结束任务</button>"; 
    that.questionContainer.appendChild(content);
    var close = document.getElementById('close');
    var timingSpan = document.getElementById('time2');
    var tt = countdown;
    timingSpan.innerHTML = tt;
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt;
        if(tt==0){
            window.clearInterval(int2);
            var el = document.getElementById('qnext');
            el.parentNode.removeChild(el);
            loadHtml();
        }
    },1000);
    close.onclick = function(){
        that.clickNextButton();
    };
}
//无问题后下一个页面
function next(){
    var content = document.createElement('div');
    content.id = "next";
    content.style.textAlign = "center";
    content.innerHTML="<div style='font-size:20px;'>爆破成功,下一轮加载中(倒计时<span id='time2'></span>秒)</div>";  
    content.innerHTML+="<button id='close' style='color: #fff;background-color: #DC143C;border-color: #DC143C;padding: 2.5px 10px;float:right;margin-right:150px;'>结束任务</button>"; 
    that.questionContainer.appendChild(content);
    var close = document.getElementById('close');
    var timingSpan = document.getElementById('time2');
    var tt = countdown;
    timingSpan.innerHTML = tt;
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt;
        if(tt==0){
            window.clearInterval(int2);
            var el = document.getElementById('next');
            el.parentNode.removeChild(el);
            loadHtml();
        }
    },1000);
    close.onclick = function(){
        that.clickNextButton();
    };
}
//任务完成页面
function success(){
    var content = document.createElement('div');
    content.id = "success";
    content.style.textAlign = "center";
    content.innerHTML="<div style='font-size:20px;'>任务完成，您可以获得"+pay+"元报酬。我们的系统里还有一些气球，你可以选择继续爆破，也可结束任务。如果继续爆破，你可以在接下来任何时候退出，不影响您的报酬</div>";  
    content.innerHTML+="<button id='goOn' style='color: #fff;background-color: blue;border-color: blue;padding: 2.5px 10px;float:left;margin-left:150px;'>继续爆破</button>"; 
    content.innerHTML+="<button id='close' style='color: #fff;background-color: #DC143C;border-color: #DC143C;padding: 2.5px 10px;float:right;margin-right:150px;'>结束任务</button>"; 
    that.questionContainer.appendChild(content);
    var goOn = document.getElementById('goOn');
    var close = document.getElementById('close');
    goOn.onclick = function(){
        var el = document.getElementById('success');
        el.parentNode.removeChild(el);
        loadHtml();
    };
    close.onclick = function(){
        that.clickNextButton();
    };
}
//全部任务完成界面
function successAll(){
    var content = document.createElement('div');
    content.id = "successAll";
    content.style.textAlign = "center";
    content.innerHTML="<div style='font-size:20px;'>任务完成，您可以获得"+pay+"元报酬。(<span id='time2'></span>秒后回到主页面)</div>";  
    that.questionContainer.appendChild(content);
    var timingSpan = document.getElementById('time2');
    var tt = failureTime;
    timingSpan.innerHTML = tt;
    int2=setInterval(function(){
        tt -=1;
        timingSpan.innerHTML = tt;
        if(tt==0){
            window.clearInterval(int2);
            that.clickNextButton();
        }
    },1000);
}

//正计时
function timingCount(){
    var timingSpan = document.getElementById('timing');
    var tt = 0;
    timingSpan.innerHTML = tt;
    int=setInterval(function(){
        tt +=1;
        timingSpan.innerHTML = tt;
        if(tt>=timing){
            var el = document.getElementById('loadHtml');
            window.clearInterval(int);
            el.parentNode.removeChild(el);
            timeInput.value += "failure";
            console.log(timeInput.value);
            loadClose();
        }
    },1000);
}
