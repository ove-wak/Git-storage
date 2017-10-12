var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
var head = document.getElementsByTagName('head')[0];
head.insertBefore( script, head.firstChild );
var lastKeyTime = 0;//数字按键时间
var thisKeyTime = 0;//当前按键时间
var isInput = false;
var questionId;
var textId;
var that;
var alphabet = 0;
var keyCodeAll = {65:"a",66:"b",67:"c",68:"d",69:"e",70:"f",71:"g",72:"h",73:"i",74:"j",75:"k",76:"l",77:"m",78:"n",79:"o",80:"p",81:"q",82:"r",83:"s",84:"t",85:"u",86:"v",87:"w",88:"x",89:"y",90:"z"};
Qualtrics.SurveyEngine.addOnload(function()
{
    that = this;
    questionId = this.questionId;
    textId = "QR~"+questionId;
    var divBody =  document.getElementById(questionId);
    var input =  document.getElementById(textId);
    divBody.setAttribute("style","font-size:30px;");
    divBody.setAttribute("align","center");
    input.style.display = "none";
    console.log(questionId);
    var script=document.createElement("script");  
    script.type="text/javascript";  
    script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
    var head = document.getElementsByTagName('head')[0];
    head.insertBefore( script, head.firstChild );
    setTimeout(function(){
        input.style.display = "";
        input.focus();
        thisKeyTime = new Date().getTime();//*
        lastKeyTime = thisKeyTime;//*
    },50);
    input.onfocus = function () {
        isInput = true;
        console.log(isInput);
    }
    input.onblur = function () {
        isInput = false;
        console.log(isInput);
    }
});
window.onkeydown = function (e) {
    thisKeyTime = new Date().getTime();
    if(isInput){    
        var keyCode  =  e.keyCode||e.which; // 按键的keyCode
        if(keyCode >=48 && keyCode <= 57){//数字
            lastKeyTime = thisKeyTime;
        }else if(keyCode >=66 && keyCode <= 90 && alphabet ==0){//除'a'以外的字母
            timeInput.value += (thisKeyTime - lastKeyTime)/1000 + 's-' + keyCodeAll[keyCode] + '; ';
            alphabet++;
        }else if(keyCode == 65){//'a'
            timeInput.value += (thisKeyTime - lastKeyTime)/1000 + 's-' + keyCodeAll[keyCode] + '; ';
        }
    }    
    console.log(timeInput.value)
};