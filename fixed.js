
var script=document.createElement("script");  
script.type="text/javascript";  
script.src="https://code.jquery.com/jquery-3.0.0.min.js";  
document.getElementsByTagName('head')[0].appendChild(script);
var isInput = false;//暂时未用到，看聚焦的需求
var questionId;
var that;
var arrText = ["Saint Laurent", "Fila", "Christian Dior", "pinKo", "Clavin Klein", "Piaget", "Xtecher", "CliniQue", "Povos", "YoutuBe", "Das Auto", "Moussy", "CocaCola", "McDonald", 
			   "Rado", "Jaguar", "Michael Kors", "ViVo", "Guerlain", "Zegna", "Kate Spade", "Puma", "Swatch", "Hugo Boss", "Paul Frank", "Vans", "Land Rover", "Diesel"];//字符数组
var text;//当前字符
var textArr = [];//当前字符删除空格的有效数组存储
var count = 0;//当前字符计数
var upperCount = 0;//大写字母计数
var countdown;//计时
var totalReward = 0;//总积分
var inputArr;//输入框数组，其长度与textArry应该相等
var img = '<img class="Graphic" src="https://fdsm.az1.qualtrics.com/WRQualtricsControlPanel/Graphic.php?IM=IM_eniPxTvMe3e1BVX" style="display:none;width: 50px;position: absolute;left:0px;z-index: 0;"/>';
var keyCodeAll = {65:"A",66:"B",67:"C",68:"D",69:"E",70:"F",71:"G",72:"H",73:"I",74:"J",75:"K",76:"L",77:"M",78:"N",79:"O",80:"P",81:"Q",82:"R",83:"S",84:"T",85:"U",86:"V",87:"W",88:"X",89:"Y",90:"Z",
				  97:"a",98:"b",99:"c",100:"d",101:"e",102:"f",103:"g",104:"h",105:"i",106:"j",107:"k",108:"l",109:"m",110:"n",111:"o",112:"p",113:"q",114:"r",115:"s",116:"t",117:"u",118:"v",119:"w",120:"x",121:"y",122:"z"};
var fontAnima = 300;//单次动画时间（从最小到最大算一次），单位ms
var fontWait = 100;//在字体最大时等待时间，单位ms
var maxFont = 50;//最大时字体大小
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
    		showScore += "<div style='display:inline-block;width:50px;height:65px;'></div>";
    		showInput += "<input style='width:36px;margin:0px 5px;font-size:30px;'></input>";
    		textArr.push(text[i]);
    	}else if(text[i] >= "A" && text[i] <= "Z"){//大写字母
    		upperCount++;
			showScore += "<div id='span"+upperCount+"' style='display:inline-block;width:50px;height:65px;position:relative;'>"+img+"<div style='position: absolute;z-index: 1;left:0px;bottom:13px;width:50px;'><span style='-webkit-transition: all "+fontAnima+"ms linear;-moz-transition: all "+fontAnima+"ms linear;-o-transition: all "+fontAnima+"ms linear;-ms-transition: all "+fontAnima+"ms linear;transition: all "+fontAnima+"ms linear;'></span></div></div>";
    		showInput += "<input id='input"+upperCount+"' style='width:36px;margin:0px 5px;font-size:30px;'></input>";
    		textArr.push(text[i]);
    	}else if(text[i] == " "){ 
    		showScore += "<div style='display:inline-block;width:50px;height:65px;'></div>";
    		showInput += "<div style='display:inline-block;width:40px;margin:0px 5px;'></div>";
    	}else{
    		console.log("特殊字符");
    	}
    }
    showScore += "<div style='clear:both;'></div>";
	questionBody += "<div>" + text + "</div>"+"<div style='color:#ffd700;font-size:24px;font-weight:bold;height:65px;margin-top:50px;'>" + showScore + "</div>"+"<div class='input-div'>"+ showInput + "</div>";
	$("#"+questionId+" .QuestionBody").append(questionBody);	
	setTimeout(function(){
		inputArr = $(".input-div input"); 
		inputArr[0].focus();
	},10);
	//textCountdown();
}	
// document.onkeypress = function(e){
// 	var $inputFocus = $(".input-div input:focus");
// 	if($inputFocus.length !== 0){
// 		var inputIndex = $inputFocus.index(".input-div input");//当前input的位置
// 		var value = $inputFocus.val();
// 		if(value.length === 0){
// 			// var keyCode  =  e.keyCode||e.which; // 按键的keyCode
// 			// var isShift  =  e.shiftKey ||(keyCode  ==   16 ) || false ; // shift键是否按住
// 			// var isCtrl  =  e.ctrlKey ||(keyCode  ==   17 ) || false ; // ctrl键是否按住
    		
   			 
//    // 			 	if(isCtrl && ((keyCode>=65&&keyCode<=90)||(keyCode >=97&&keyCode<=122))){
//    // 			 	if(keyCode>=65&&keyCode<=90){
//    // 			 		keyCode += 32;
//    // 			 	}else{
//    // 			 		keyCode -= 32;
//    // 			 	}
   			 	
   			 	
   			 	 
//    // 			 }
// 			inputValue($inputFocus,inputIndex,e);
// 		}else{//限制一个input最多只有一个字母
// 			return false;
// 		}
// 	}
	
// };

window.onkeydown = function (e) {
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
		case 20:break;
		default:
		{
			if (isShift && (keyCode>=65&&keyCode<=90)){
    			return false;//屏蔽shift+字母的复合键
   			}
   			if(isCtrl && (keyCode>=65&&keyCode<=90)){
   				setTimeout(function(){
					$inputFocus.val(keyCodeAll[keyCode]);//用ctrl+字母来生成大写字母
   				},10);
   				e.preventDefault();//屏蔽ctrl+字母复合键的默认事件
   			}
   			if($inputFocus.length !== 0 &&(keyCode===32||(keyCode>=48&&keyCode<=57)||(keyCode>=65&&keyCode<=90)||(keyCode>=96&&keyCode<=107)||(keyCode>=186&&keyCode<=192)||(keyCode>=219&&keyCode<=222))){//焦点在文本框内且输入的是看见字符
				if(value.length === 0){
					inputValue($inputFocus,inputIndex,e);
				}else{//限制一个input最多只有一个字母
					return false;
				}
			}
		}
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

function inputValue($inputFocus,inputIndex,e){
	setTimeout(function () {
		if($inputFocus.attr("id")){//大写位置
			var inputId = $inputFocus.attr("id");
			var idNum = inputId.substring(5,inputId.length);
			if($inputFocus.val() == textArr[inputIndex]){//是否输入正确
				$inputFocus.attr("disabled",true);//设置不可编辑
				if(e.ctrlKey){
					$("#span" + idNum +" div span").html("+5");
					$("#span" + idNum +" img").show();
					//字体动画
					$("#span" + idNum +" div span").css('font-size',maxFont+"px");
					setTimeout(function(){
						$("#span" + idNum +" div span").css('font-size',"24px");
					},fontAnima+fontWait);
					
					timeInput.value += idNum +":right;";
					totalReward += 5;
				}else{
					$("#span" + idNum +" div span").html("+0");
					$("#span" + idNum +" img").show();
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
			//clearTimeout(timeLimit);
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
// function textCountdown() {
// 	timeLimit = setTimeout(function () {
// 		console.log(count + ":timeout");
// 		nextTurn();
// 	}, 20000);
// }
