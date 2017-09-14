var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
var head = document.getElementsByTagName('head')[0];
head.insertBefore( script, head.firstChild );
var lastKeyTime = 0;//上次按键时间*
var thisKeyTime = 0;//当前按键时间*
var isInput = false;
var questionId;
var textId;
var that;
var keyCodeAll = {65:"A",66:"B",67:"C",68:"D",69:"E",70:"F",71:"G",72:"H",73:"I",74:"J",75:"K",76:"L",77:"M",78:"N",79:"O",80:"P",81:"Q",82:"R",83:"S",84:"T",85:"U",86:"V",87:"W",88:"X",89:"Y",90:"Z",
                  97:"a",98:"b",99:"c",100:"d",101:"e",102:"f",103:"g",104:"h",105:"i",106:"j",107:"k",108:"l",109:"m",110:"n",111:"o",112:"p",113:"q",114:"r",115:"s",116:"t",117:"u",118:"v",119:"w",120:"x",121:"y",122:"z"};
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
    thisKeyTime = new Date().getTime();//*   
    console.log(timeInput.value)//*
    if(isInput){    
    var keyCode  =  e.keyCode||e.which; // 按键的keyCode
    var isShift  =  e.shiftKey ||(keyCode  ==   16 ) || false ; // shift键是否按住
    var isCtrl  =  e.ctrlKey ||(keyCode  ==   17 ) || false ; // ctrl键是否按住
    if(keyCode == 20){//*
        timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-capslock  ";//*
        }//*
    if (isShift && (keyCode>=65&&keyCode<=90)){
                timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-shift  ";//*
                lastKeyTime = thisKeyTime;//*
                return false;//屏蔽shift+字母的复合键
    }
    if(isCtrl && (keyCode>=65&&keyCode<=90)){
        timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-ctrl  ";//*
            setTimeout(function(){
                    console.log(document.getElementById(textId).value);
                    document.getElementById(textId).value = document.getElementById(textId).value + keyCodeAll[keyCode];//用ctrl+字母来生成大写字母
                timeInput.value += "[right]  ";//*
                console.log(timeInput.value);
            },10);
            e.preventDefault();//屏蔽ctrl+字母复合键的默认事件
    }
    }
    lastKeyTime = thisKeyTime;//*
};

window.onkeypress = function(e){
    if(e.keyCode >= 65 && e.keyCode <= 90){
        timeInput.value += "[capslk-right]  ";//*
        console.log(timeInput.value);
    }
}