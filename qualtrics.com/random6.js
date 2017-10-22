var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
var head = document.getElementsByTagName('head')[0];
head.insertBefore( script, head.firstChild );
var lastKeyTime = 0;//上次按键时间*
var thisKeyTime = 0;//当前按键时间*
var isInput = false;//暂时未用到，看聚焦的需求
var questionId;
var that;
var COUNTDOWNTIME = 3;//倒计时,单位s
var countdownTime = COUNTDOWNTIME;
var flag = 0;//标记无大写为0,clrl为1,capslk为2;
var uppercaseLetter = false;//当前有无大写字母
var arrText = [ "thinkPad","Rado","Coco","snidel","Haier","mazda","Boss","meji","Escada"];//字符数组
var text;//当前字符
var textArr = [];//当前字符删除空格的有效数组存储
var count = 0;//当前字符计数
var upperCount = 0;//大写字母计数
var countdown;//计时
var totalReward = 0;//总积分
var inputArr;//输入框数组，其长度与textArry应该相等
var keyCodeAll = {65:"A",66:"B",67:"C",68:"D",69:"E",70:"F",71:"G",72:"H",73:"I",74:"J",75:"K",76:"L",77:"M",78:"N",79:"O",80:"P",81:"Q",82:"R",83:"S",84:"T",85:"U",86:"V",87:"W",88:"X",89:"Y",90:"Z",
                  97:"a",98:"b",99:"c",100:"d",101:"e",102:"f",103:"g",104:"h",105:"i",106:"j",107:"k",108:"l",109:"m",110:"n",111:"o",112:"p",113:"q",114:"r",115:"s",116:"t",117:"u",118:"v",119:"w",120:"x",121:"y",122:"z"};
var rewardPoints = 30;//常量，每组总积分
var surplusPoints = rewardPoints;
var rewardNum = 3;//常量，n个一组
var surplusNum = rewardNum;
var fontAnima = 200;//单次动画时间（从最小到最大算一次），单位ms
var fontWait = 400;//在字体最大时等待时间，单位ms
var maxFont = 70;//最大时字体大小
Qualtrics.SurveyEngine.addOnload(function()
{
    var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
var head = document.getElementsByTagName('head')[0];
head.insertBefore( script, head.firstChild );
    this.disableNextButton();
    that = this;
    questionId = this.questionId;
    var divBody =  document.getElementById(questionId);
    divBody.setAttribute("style","font-size:30px;");
    divBody.setAttribute("align","center");
    console.log(questionId);
    setTimeout(function(){
     $("#Questions").css("position","relative");
        loadHtml();
        countdown(-1);
    },100);
    
});

function loadPromptMsg() {
    uppercaseLetter = false;
    $("#"+questionId+" .QuestionBody").html("");
    $("#"+questionId+" .QuestionBody").css("font-size","32px");
    var questionBody = "";
    var showInput = "";
    var text = arrText[count];
    count++;
    timeInput.value += "***" + count + ":  ";//*
    textArr = [];
    for(var i = 0;i<text.length;i++){
        if(text[i] >= "a" && text[i] <= "z"){//小写字母
            showInput += "<input style='width:36px;margin:0px 5px;font-size:30px;'></input>";
            textArr.push(text[i]);
        }else if(text[i] >= "A" && text[i] <= "Z"){//大写字母
            uppercaseLetter = true;
            upperCount++;
            showInput += "<input id='input"+upperCount+"' style='width:36px;margin:0px 5px;font-size:30px;'></input>";
            textArr.push(text[i]);
        }else if(text[i] == " "){ 
            showInput += "<div style='display:inline-block;width:40px;margin:0px 5px;'></div>";
        }else{
            console.log("特殊字符");
        }
    }
    questionBody += "<div>" + text + "</div>"+"<div style='margin-top:30px;' class='input-div'>"+ showInput + "</div>";
    $("#"+questionId+" .QuestionBody").append(questionBody);    
    thisKeyTime = new Date().getTime();//*
    lastKeyTime = thisKeyTime;//*
    setTimeout(function(){
        inputArr = $(".input-div input"); 
        inputArr[0].focus();
    },10);
}   

window.onkeydown = function (e) {
    thisKeyTime = new Date().getTime();//*   
    console.log(timeInput.value)//*
    var $inputFocus = $(".input-div input:focus");
    var inputIndex = $inputFocus.index(".input-div input");//当前input的位置
    var value = $inputFocus.val();
    var keyCode  =  e.keyCode||e.which; // 按键的keyCode
    var isShift  =  e.shiftKey ||(keyCode  ==   16 ) || false ; // shift键是否按住
    var isCtrl  =  e.ctrlKey ||(keyCode  ==   17 ) || false ; // ctrl键是否按住
    switch(keyCode){
        case 37://左键
            left(inputIndex);
            break;
        case 39://右键
            right(inputIndex);
            break;
        case 8://删除键
            if(value.length === 0){ 
                deleteA(inputIndex);
            }   
            break;
        case 16:return false;break;
        case 17:return false;break;
        case 20:if($inputFocus.attr("id")) timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-capslock  ";break;//*

        default:
        {
            if (isShift && (keyCode>=65&&keyCode<=90)){
                if($inputFocus.attr("id"))//大写位置
                timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-shift  ";//*
                lastKeyTime = thisKeyTime;//*
                return false;//屏蔽shift+字母的复合键
            }
            if(isCtrl && (keyCode>=65&&keyCode<=90)){
                if($inputFocus.attr("id"))//大写位置
                timeInput.value += (thisKeyTime - lastKeyTime)/1000 +"s-ctrl  ";//*
                setTimeout(function(){
                    $inputFocus.val(keyCodeAll[keyCode]);//用ctrl+字母来生成大写字母
                },10);
                e.preventDefault();//屏蔽ctrl+字母复合键的默认事件
            }
            if($inputFocus.length !== 0 &&(keyCode===32||(keyCode>=48&&keyCode<=57)||(keyCode>=65&&keyCode<=90)||(keyCode>=96&&keyCode<=107)||(keyCode>=186&&keyCode<=192)||(keyCode>=219&&keyCode<=222))){//焦点在文本框内且输入的是看见字符
                if(value.length === 0){
                    inputValue($inputFocus,inputIndex,e);
                }else{//限制一个input最多只有一个字母
                    lastKeyTime = thisKeyTime;//*
                    return false;
                }
            }
        }
    }
    lastKeyTime = thisKeyTime;//*
    

};
function left(inputIndex){
    if(inputIndex > 0){
        if(!inputArr[inputIndex - 1].disabled){     
            inputArr[inputIndex - 1].focus();
            setTimeout(function(){
                inputArr[inputIndex - 1].value = inputArr[inputIndex - 1].value;
            },2);
        }else{
            left(inputIndex - 1);
        }
    }
    
}
function right(inputIndex){
    if(inputIndex < inputArr.length - 1){
        if(!inputArr[inputIndex + 1].disabled){
            inputArr[inputIndex + 1].focus();
            inputArr[inputIndex + 1].value = inputArr[inputIndex + 1].value;
        }else{
            right(inputIndex + 1);
        }
    }
}
function deleteA(inputIndex){
    if(inputIndex > 0){
        if(!inputArr[inputIndex - 1].disabled){
            inputArr[inputIndex - 1].focus();
            inputArr[inputIndex - 1].value = "";
        }else if(inputIndex > 0){
            deleteA(inputIndex - 1);
        }
    }
}
//输入完成后自动聚焦到下一个输入框
function finishNext($inputFocus,inputIndex){
    if(inputIndex + 1 < inputArr.length && !inputArr[inputIndex + 1].disabled){
        inputArr[inputIndex + 1].focus();
        inputArr[inputIndex + 1].value = inputArr[inputIndex + 1].value;
    }else if(inputIndex + 1 == inputArr.length){
        $inputFocus.blur();
    }else{
        finishNext($inputFocus,inputIndex + 1);
    }
}

function inputValue($inputFocus,inputIndex,e){
    setTimeout(function () {  
        if($inputFocus.attr("id")){//大写位置
            var inputId = $inputFocus.attr("id");
            var idNum = inputId.substring(5,inputId.length);
            if($inputFocus.val() == textArr[inputIndex]){//是否输入正确
                $inputFocus.attr("disabled",true);//设置不可编辑
                if(e.ctrlKey){
                    flag  = 1;                 
                    timeInput.value += "[right]  ";//*
                }else{
                    flag = 2;
                    timeInput.value += "[capslk-right]  ";//*
                }
            }else{
                timeInput.value += "[error]  ";//*
            }
        }
         
        finishNext($inputFocus,inputIndex);
        console.log(timeInput.value);
        //整体匹配
        var success = true;
        for(var j = 0;j<inputArr.length;j++){
            if(inputArr[j].value != textArr[j]){
                success = false;
            }
        }
        if(success){
             if(!uppercaseLetter){flag = 0;}
            console.log(flag);
            setTimeout(function(){
                nextTurn(flag); 
            },10);          
        }
    }, 10);
}

function nextTurn(flag) {
    if (count >= arrText.length) {       
           countdown(flag,1);
        }else{
            if(flag == 0){
                 loadPromptMsg();
             }else{
                countdown(flag);
             }       
        }
}

function loadHtml() {
    var body = document.getElementById('Questions');;
    var div = document.createElement('div');
    div.setAttribute("id","alert");
    div.style.position = 'absolute';
    div.style.height = "100%";
    div.style.width = "100%";
    div.style.display = "none";
    div.style.top = '0';
    div.style.zIndex = '99';
    div.style.backgroundColor = "#fff";
    body.appendChild(div);
}
//单词加载中倒计时
//flag:标记无大写为0,clrl为1,capslk为2,第一个加载页面为-1;
//isLast:1为last
function countdown(flag,isLast){
    if(countdownTime == 0){
        var divAlert = document.getElementById('alert');
        divAlert.style.display = 'none';
        if(isLast === undefined){
             loadPromptMsg();
        }else{
            $("#"+questionId+" .QuestionBody").empty();
            $("#"+questionId+" .QuestionBody").append("请点击右下角按钮进入下一部分</span></div>");
             timeInput.value += "总积分："+ totalReward;     
            console.log(timeInput.value);      
            that.enableNextButton();
        }
        countdownTime = COUNTDOWNTIME;
    }else if(countdownTime == COUNTDOWNTIME){
        countdownTime--;
        var divAlert = document.getElementById('alert');
        if(isLast === undefined)
            var text = "(下一轮加载中:<span id='countdown-span'>" + countdownTime + "</span>)";
        else
            var text = "";
        if(flag == 1){
            var reward = getRandomMoney(surplusNum, surplusPoints);
            surplusNum--;
            surplusPoints =  surplusPoints - reward;
            if(surplusNum === 0){
                surplusNum = rewardNum;
                surplusPoints = rewardPoints;
            } 
            totalReward += reward;
            divAlert.innerHTML = "<div style='width:100%;text-align:center;height:120px;position:relative;'><p  style='position:absolute;width:100%;bottom:0px;line-height:60px;font-size:24px'>恭喜你！本次获得<span id='reward-show' style='transition: all "+fontAnima+"ms linear;color:red;font-size:36px;font-weight:bold;'>"+reward+"</span>积分"+text+"</p></div>";
            setTimeout(function(){
            $("#reward-show").css('font-size',maxFont+"px");
            setTimeout(function(){
               $("#reward-show").css('font-size',"36px");
            },fontAnima+fontWait);
        },20);
        }else if(flag == 2){
            divAlert.innerHTML = "<div style='width:100%;text-align:center;height:120px;position:relative;'><p style='position:absolute;width:100%;bottom:0px;line-height:60px;font-size:24px'>输入正确"+text+"</p></div>";
        }else{
            divAlert.innerHTML = "<div style='width:100%;text-align:center;height:120px;position:relative;'><p style='position:absolute;width:100%;bottom:0px;line-height:60px;font-size:24px'>加载中(倒计时:<span id='countdown-span'>" + countdownTime + "</span>)</p></div>";
        }
        divAlert.style.display = 'flex';
        setTimeout(function() {
            countdown(flag,isLast);
        },1000);
    }else{
        countdownTime--;
        if(isLast === undefined){
             var promptText = document.querySelector('#countdown-span');
             promptText.innerHTML = countdownTime;
        }
        setTimeout(function() {
            countdown(flag,isLast);
        },1000);
    }   
}

function getRandomMoney(remainSize, remainMoney){
    if(remainSize == 1){
        return remainMoney;
    }
    var min = 1;
    var max = remainMoney/remainSize*2;
    var money = max*Math.random();
    money = money <=min?1:Math.round(money);
    return money;
}