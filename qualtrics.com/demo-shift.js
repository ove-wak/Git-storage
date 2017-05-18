
var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
document.getElementsByTagName('head')[0].appendChild(script);
var isInput = false;//暂时未用到，看聚焦的需求
var questionId;
var that;
var arrText = ['Saint Laurent','Piaget'];//字符数组
var text;//当前字符
var textArr = [];//当前字符删除空格的有效数组存储
var count = 0;//当前字符计数
var upperCount = 0;//大写字母计数
var countdown;//计时
var totalReward = 0;//总积分
var inputArr;//输入框数组，其长度与textArry应该相等
Qualtrics.SurveyEngine.addOnload(function()
{
	var script=document.createElement("script");  
	script.type="text/javascript";  
	script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
	document.getElementsByTagName('head')[0].appendChild(script);
	this.disableNextButton();
	that = this;
	questionId = this.questionId;
	var divBody =  document.getElementById(questionId);
    divBody.setAttribute("style","font-size:30px;");
	divBody.setAttribute("align","center");
	console.log(questionId);
	loadPromptMsg();
});

function loadPromptMsg() {
	$("#"+questionId+" .QuestionBody").html("");
	var questionBody = "";
	var showScore = "";
	var showInput = "";
	var text = arrText[count];
	count++;
	textArr = [];
    for(var i = 0;i<text.length;i++){
    	if(text[i] >= "a" && text[i] <= "z"){//小写字母
    		showScore += "<div style='display:inline-block;width:40px;margin-right:10px;'></div>";
    		showInput += "<input style='width:36px;margin-right:10px;font-size:30px;'></input>";
    		textArr.push(text[i]);
    	}else if(text[i] >= "A" && text[i] <= "Z"){//大写字母
    		upperCount++;
			showScore += "<div style='display:inline-block;width:40px;margin-right:10px;'><span id='span"+upperCount+"''></span></div>";
    		showInput += "<input id='input"+upperCount+"' style='width:36px;margin-right:10px;font-size:30px;'></input>";
    		textArr.push(text[i]);
    	}else if(text[i] == " "){ 
    		showScore += "<div style='display:inline-block;width:40px;margin-right:10px;'></div>";
    		showInput += "<div style='display:inline-block;width:40px;margin-right:10px;'></div>";
    	}else{
    		console.log("特殊字符");
    	}
    }
	questionBody += "<div>" + text + "</div>"+"<div style='color:red;height:40px;margin-top:50px;'>" + showScore + "</div>"+"<div class='input-div'>"+ showInput + "</div>";
	$("#"+questionId+" .QuestionBody").append(questionBody);	
	setTimeout(function(){
		inputArr = $(".input-div input"); 
		inputArr[0].focus();
	},10);
	textCountdown();
}	
window.onkeypress = function(e){
	var $inputFocus = $(".input-div input:focus");
	if($inputFocus.length !== 0){
		var inputIndex = $inputFocus.index(".input-div input");//当前input的位置
		var value = $inputFocus.val();
		if(value.length === 0){
			inputValue($inputFocus,inputIndex,value,e);
		}else{//限制一个input最多只有一个字母
			return false;
		}
	}
	
};

window.onkeydown = function (e) {
	var $inputFocus = $(".input-div input:focus");
	var inputIndex = $inputFocus.index(".input-div input");//当前input的位置
	var value = $inputFocus.val();
	console.log(value);
	switch(e.keyCode){
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
	}
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

function inputValue($inputFocus,inputIndex,value,e){
	setTimeout(function () {
		if($inputFocus.attr("id")){//大写
			var inputId = $inputFocus.attr("id");
			var idNum = inputId.substring(5,inputId.length);
			if($inputFocus.val() == textArr[inputIndex]){//是否输入正确
				$inputFocus.attr("disabled",true);//设置不可编辑
				if(e.shiftKey){
					$("#span" + idNum).html("5");
					timeInput.value += idNum +":shift-right;";
					totalReward += 5;
				}else{
					$("#span" + idNum).html("0");
					timeInput.value += idNum +":capslk-right;";
				}
			}else{
				timeInput.value += idNum +":error;";
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
			clearTimeout(timeLimit);
			setTimeout(function(){
				nextTurn();	
			},10);			
		}
	}, 10);
}

function nextTurn() {
	if (count >= arrText.length) {
			timeInput.value += "总积分："+ totalReward;
			console.log(timeInput.value);			
			$("#"+questionId+" .QuestionBody").empty();
			$("#"+questionId+" .QuestionBody").append("<div>请点击右下角按钮进入下一部分</div>");
			that.enableNextButton();
		}else{
			loadPromptMsg();
		}
}

//文本输入倒计时
function textCountdown() {
	timeLimit = setTimeout(function () {
		console.log(count + ":timeout");
		nextTurn();
	}, 20000);
}
