var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
var head = document.getElementsByTagName('head')[0];
head.insertBefore( script, head.firstChild );
var lastKeyTime = 0;//上次按键时间
var thisKeyTime = 0;//当前按键时间
var isInput = false;//暂时未用到，看聚焦的需求
var questionId;
var that;
var COUNTDOWNTIME = 3;//倒计时,单位s
var countdownTime = COUNTDOWNTIME;
var flag = 0;//标记无'a'为0,首中为1,其次为2;
var uppercaseLetter = false;//当前有无'a'
var arr1 = [1,3,5]//有a的单词顺序
var arr2 = ["anfec","initial","rado"]//含a的单词
var arr3 = ["snidel","text"]//不含a的单词
var arrText = [];//字符数组
var text;//当前字符
var textArr = [];//当前字符删除空格的有效数组存储
var count = 0;//当前字符计数
var upperCount = 0;//'a'字母计数
var countdown;//计时
var totalReward = 0;//总积分
var inputArr;//输入框数组，其长度与textArry应该相等
var fontAnima = 200;//单次动画时间（从最小到最大算一次），单位ms
var fontWait = 400;//在字体最大时等待时间，单位ms
var maxFont = 70;//最大时字体大小
Qualtrics.SurveyEngine.addOnload(function()
{
    this.disableNextButton();
    that = this;
    questionId = this.questionId;
    setTimeout(function(){
        var script=document.createElement("script");  
        script.type="text/javascript";  
        script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
        var head = document.getElementsByTagName('head')[0];
        head.insertBefore( script, head.firstChild );
        var divBody =  document.getElementById(questionId);
        divBody.setAttribute("style","font-size:30px;");
        divBody.setAttribute("align","center");
        console.log(questionId);
        loadHtml();
        countdown(-1);    
    },500);
});

function loadPromptMsg() {
    uppercaseLetter = false;
    $("#"+questionId+" .QuestionBody").html("");
    $("#"+questionId+" .QuestionBody").css("font-size","32px");
    var questionBody = "";
    var showInput = "";
    var text = arrText[count];
    count++;
    flag = 0;//重置flag
    timeInput.value += count + ": ";
    textArr = [];
    for(var i = 0;i<text.length;i++){
        if(text[i] == "a"){//字母a
           uppercaseLetter = true;
           upperCount++;
           showInput += "<input id='input"+upperCount+"' style='width:36px;margin:0px 5px;font-size:30px;'></input>";
           textArr.push(text[i]);
        }else if(text[i] >= "b" && text[i] <= "z"){//之外的字母
            showInput += "<input style='width:36px;margin:0px 5px;font-size:30px;'></input>";
            textArr.push(text[i]);
        }else if(text[i] == " "){ 
            showInput += "<div style='display:inline-block;width:40px;margin:0px 5px;'></div>";
        }else{
            console.log("特殊字符");
        }
    }
    questionBody += "<div>" + text + "</div>"+"<div style='margin-top:30px;' class='input-div'>"+ showInput + "</div>";
    $("#"+questionId+" .QuestionBody").append(questionBody);    
    thisKeyTime = new Date().getTime();
    lastKeyTime = thisKeyTime;
    setTimeout(function(){
        inputArr = $(".input-div input"); 
        inputArr[0].focus();
    },10);
}   

window.onkeydown = function (e) {
    thisKeyTime = new Date().getTime();   
    console.log(timeInput.value)
    var $inputFocus = $(".input-div input:focus");
    var inputIndex = $inputFocus.index(".input-div input");//当前input的位置
    var value = $inputFocus.val();
    var keyCode  =  e.keyCode||e.which; // 按键的keyCode
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
        default:
        {
            if($inputFocus.length !== 0 &&(keyCode===32||(keyCode>=48&&keyCode<=57)||(keyCode>=65&&keyCode<=90)||(keyCode>=96&&keyCode<=107)||(keyCode>=186&&keyCode<=192)||(keyCode>=219&&keyCode<=222))){//焦点在文本框内且输入的是看见字符
                if(value.length === 0){
                    keyTimeGap = thisKeyTime - lastKeyTime;//按键时间差
                    inputValue($inputFocus,inputIndex,e,keyTimeGap);
                }else{//限制一个input最多只有一个字母
                    lastKeyTime = thisKeyTime;
                    return false;
                }
            }
        }
    }
    lastKeyTime = thisKeyTime;

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

function inputValue($inputFocus,inputIndex,e,keyTimeGap){
    setTimeout(function () {  
        if($inputFocus.attr("id")){//'a'位置
            var inputId = $inputFocus.attr("id");
            var idNum = inputId.substring(5,inputId.length);
            if($inputFocus.val() == textArr[inputIndex]){//是否输入正确
                $inputFocus.attr("disabled",true);//设置不可编辑
                if(flag == 2){
                    timeInput.value += keyTimeGap/1000 +"s-correct;  ";
                }else{
                    flag = 1;
                    timeInput.value += keyTimeGap/1000 +"s-right;  ";
                }
            }else{
                flag = 2;
                timeInput.value += keyTimeGap/1000 +"s-"+$inputFocus.val()+";  ";
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
             if(!uppercaseLetter){
                flag = 0;
                timeInput.value += "no-a;  ";
            }
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
    body.style.position = "relative";
    body.appendChild(div);
}

//单词加载中倒计时
//flag:标记无'a'为0,第一次输入'a'成功为1,修改成功为2,第一个加载页面为-1;
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
        console.log(flag);
        if(flag == 1){
            var reward = 10;
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
            // alert("test");
            divAlert.innerHTML = "<div style='width:100%;text-align:center;height:120px;position:relative;'><p style='position:absolute;width:100%;bottom:0px;line-height:60px;font-size:24px'>加载中(倒计时:<span id='countdown-span'>" + countdownTime + "</span>)</p></div>";
        }
        // alert("2222");
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

//单词排序
function wordSort(){
    arrText = arr3;
    arr2 = arr2.sort(randomSort);
    for(var x = 0;x < arr1.length;x++){
       arrText.splice(arr1[x] - 1, 0, arr2.pop());
    }
    console.log(arrText);
}

function randomSort(a, b) { return Math.random() - 0.5; }