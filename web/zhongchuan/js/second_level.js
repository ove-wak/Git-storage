// var mbgk_ldgz = ['6月，国务院办公厅发文，同意在中船重工建设国家第二批双创示范基地。',
// '完成第一阶段“压减”任务，超额完成年度目标，获国资委对集团公司经营业绩考核加分。',
// '2017年新承接船舶海工项目122艘/747万吨/196亿元，吨位占全球接单量10.1%，远超集团公司2017年全球接单占比6%的指标要求。',
// '《财富》世界500强排名第一次位居全球船舶企业榜首。',
// '境外实现营业收入62.41亿元、利润22.67亿元，分别是上年的2.21倍和6.09倍，国际化经营迈开坚实步伐。',
// '完成11个事业群组建工作，与地方政府的战略合作协议金额已达20亿元。',
// '实施国内首例市场化债转股，增加中国重工资本金218.68亿元，可减少年利息支出8.48亿元，同时降低集团公司资产负债率4个百分点。',
// '中国动力低速机资源重组顺利完成。',
// '集团公司首次制定并发布“十三五”质量发展规划和安全生产发展规划，创新提出建立“质量领军型企业”和“本质安全型企业”。' ,
// '2017年发生死亡事故起数、人数，创集团公司有史以来最低。百亿产值死亡人数0.38人，创集团公司有史以来最低。',
// '推进领导干部交流工作，共计57人次的成员单位领导人员根据工作需要跨单位交流任职。',
// '入选中国企业慈善公益500强，位列第39名；集团公司2016年社会责任报告连续获金蜜蜂领袖企业奖。'
// ];
// var gszl_ldgz = [
// '6月，国务院办公厅发文，同意在中船重工建设国家第二批双创示范基地。',
// '完成第一阶段“压减”任务，超额完成年度目标，获国资委对集团公司经营业绩考核加分。',
// '2017年新承接船舶海工项目122艘/747万吨/196亿元，吨位占全球接单量10.1%，远超集团公司2017年全球接单占比6%的指标要求。',
// '《财富》世界500强排名第一次位居全球船舶企业榜首。',
// '境外实现营业收入62.41亿元、利润22.67亿元，分别是上年的2.21倍和6.09倍，国际化经营迈开坚实步伐。',
// '完成11个事业群组建工作，与地方政府的战略合作协议金额已达20亿元。',
// '实施国内首例市场化债转股，增加中国重工资本金218.68亿元，可减少年利息支出8.48亿元，同时降低集团公司资产负债率4个百分点。',
// '中国动力低速机资源重组顺利完成。',
// '集团公司首次制定并发布“十三五”质量发展规划和安全生产发展规划，创新提出建立“质量领军型企业”和“本质安全型企业”。' ,
// '2017年发生死亡事故起数、人数，创集团公司有史以来最低。百亿产值死亡人数0.38人，创集团公司有史以来最低。',
// '推进领导干部交流工作，共计57人次的成员单位领导人员根据工作需要跨单位交流任职。',
// '入选中国企业慈善公益500强，位列第39名；集团公司2016年社会责任报告连续获金蜜蜂领袖企业奖。'
// ];
// var mbgk_bhqk = {

// };
// var gszl_bhqk = {

// };

$(window).resize(function(){ 
    document.getElementById("pie-doughnut-1").removeAttribute("_echarts_instance_");
    document.getElementById("pie-doughnut-2").removeAttribute("_echarts_instance_"); 
    pie1();
    pie2();

});
$(document).ready(function(){ 
    // 目标管控和公司治理页面进入
    var myid=GetQueryString("id");
    if(myid !=null && myid.toString().length>1)
    {
       if(myid == "mbgk"){
            $(".left").css('display','inline-block'); 
            //滚动条效果
            if($('#colee').height()<$('#colee1').height())
                scoll1();
            else
                $('#colee').css('overflow-y','hidden');
            if($('#coleee').height()<$('#coleee1').height())
                scoll2();
            else
                $('#coleee').css('overflow-y','hidden');
       }else{
            $(".right").css('display','inline-block'); 
            //滚动条效果
            if($('#r-colee').height()<$('#r-colee1').height())
                scoll3();
            else
                $('#r-colee').css('overflow-y','hidden');
            if($('#r-coleee').height()<$('#r-coleee1').height())
                scoll4();
            else
                $('#r-coleee').css('overflow-y','hidden');
       }
    }

    $(".back").hover(function(){
        $(".back-img").css("background","url(static/second/backbutton_selected.png) no-repeat");
        $(".back-img").css("background-size","100% 100%");
        $(".back-img").css("margin","-0.13rem -0.13rem -0.13rem -0.13rem");
        $(".back-img").css("padding","0.13rem 0.13rem 0.13rem 0.13rem");
        },function(){
            $(".back-img").css("background","url(static/second/backbutton_normal.png) no-repeat");
            $(".back-img").css("background-size","100% 100%");
            $(".back-img").css("margin","");
            $(".back-img").css("padding","");
      });
    $(".close").hover(function(){
        $(".close-img").css("background","url(static/second/closebutton_selected.png) no-repeat");
        $(".close-img").css("background-size","100% 100%");
        $(".close-img").css("margin","-0.13rem -0.13rem -0.13rem -0.13rem");
        $(".close-img").css("padding","0.13rem 0.13rem 0.13rem 0.13rem");
        },function(){
            $(".close-img").css("background","url(static/second/closebutton_normal.png) no-repeat");
            $(".close-img").css("background-size","100% 100%");
            $(".close-img").css("margin","");
            $(".close-img").css("padding","");
      });
    $(".second .back").click(function() {
            window.location.href="index.html";
    });
    $(".second .close").click(function() {
            window.location.href="index.html";
    });
    
    //呼吸灯
    // chImg();
    //圆饼图表效果
    pie1();
    pie2();
});

function scoll1(){
    $('#colee').niceScroll({
        cursorcolor: "#00d2ff",//#CC0071 光标颜色
        cursoropacitymax: 1, //改变不透明度非常光标处于活动状态（scrollabar“可见”状态），范围从1到0
        touchbehavior: false, //使光标拖动滚动像在台式电脑触摸设备
        cursorwidth: "0.055rem", //像素光标的宽度
        cursorborder: "0rem solid #666", // 游标边框css定义
        cursorborderradius: "0.05rem",//以像素为光标边界半径
        autohidemode: "true"
    });
    var speed=40;
    var colee2=document.getElementById("colee2");
    var colee1=document.getElementById("colee1");
    var colee=document.getElementById("colee");
    colee2.innerHTML=colee1.innerHTML; //克隆colee1为colee2
    function Marquee1(){
    //当滚动至colee1与colee2交界时
    $("#colee").getNiceScroll().hide();
    if(colee2.offsetTop-colee.scrollTop<=0){
     colee.scrollTop-=colee2.offsetTop; //colee跳到最顶端
     }else{
     colee.scrollTop++;
    }
    }
    var MyMar1=setInterval(Marquee1,speed);//设置定时器
    //鼠标移上时清除定时器达到滚动停止的目的
    $('.ldgz').mouseover(function() {
        clearInterval(MyMar1);
        $("#colee").getNiceScroll().show();
    });
    $('#ascrail2000').mouseover(function() {
        clearInterval(MyMar1);
        $("#colee").getNiceScroll().show();
    });
    $('#ascrail2000').css('cursor','pointer');
    //鼠标移开时重设定时器
    $('.ldgz').mouseout(function(){
        MyMar1=setInterval(Marquee1,speed);  
    });
}
function scoll2(){
    $('#coleee').niceScroll({
        cursorcolor: "#00d2ff",//#CC0071 光标颜色
        cursoropacitymax: 1, //改变不透明度非常光标处于活动状态（scrollabar“可见”状态），范围从1到0
        touchbehavior: false, //使光标拖动滚动像在台式电脑触摸设备
        cursorwidth: "0.055rem", //像素光标的宽度
        cursorborder: "0rem solid #666", // 游标边框css定义
        cursorborderradius: "0.05rem",//以像素为光标边界半径
        autohidemode: "true"
    });
    var speed=40;
    var coleee2=document.getElementById("coleee2");
    var coleee1=document.getElementById("coleee1");
    var coleee=document.getElementById("coleee");
    coleee2.innerHTML=coleee1.innerHTML; //克隆colee1为colee2
    function Marqueee1(){
    //当滚动至colee1与colee2交界时
    $("#coleee").getNiceScroll().hide();
    if(coleee2.offsetTop-coleee.scrollTop<=0){
     coleee.scrollTop-=coleee2.offsetTop; //colee跳到最顶端
     }else{
     coleee.scrollTop++;
    }
    }
    var MyMarr1=setInterval(Marqueee1,speed);//设置定时器
    //鼠标移上时清除定时器达到滚动停止的目的
    $('.bhqk').mouseover(function() {
        clearInterval(MyMarr1);
        $("#coleee").getNiceScroll().show();
    });
    $('#ascrail2001').mouseover(function() {
        clearInterval(MyMarr1);
        $("#coleee").getNiceScroll().show();
    });
    $('#ascrail2001').css('cursor','pointer');
    //鼠标移开时重设定时器
    $('.bhqk').mouseout(function(){
        MyMarr1=setInterval(Marqueee1,speed);  
    });
}
function scoll3(){
    $('#r-colee').niceScroll({
        cursorcolor: "#00d2ff",//#CC0071 光标颜色
        cursoropacitymax: 1, //改变不透明度非常光标处于活动状态（scrollabar“可见”状态），范围从1到0
        touchbehavior: false, //使光标拖动滚动像在台式电脑触摸设备
        cursorwidth: "0.055rem", //像素光标的宽度
        cursorborder: "0rem solid #666", // 游标边框css定义
        cursorborderradius: "0.05rem",//以像素为光标边界半径
        autohidemode: "true"
    });
    var speed=40;
    var colee2=document.getElementById("r-colee2");
    var colee1=document.getElementById("r-colee1");
    var colee=document.getElementById("r-colee");
    colee2.innerHTML=colee1.innerHTML; //克隆colee1为colee2
    function Marquee1(){
    //当滚动至colee1与colee2交界时
    $("#r-colee").getNiceScroll().hide();
    if(colee2.offsetTop-colee.scrollTop<=0){
     colee.scrollTop-=colee2.offsetTop; //colee跳到最顶端
     }else{
     colee.scrollTop++;
    }
    }
    var MyMar1=setInterval(Marquee1,speed);//设置定时器
    //鼠标移上时清除定时器达到滚动停止的目的
    $('.ldgz').mouseover(function() {
        clearInterval(MyMar1);
        $("#r-colee").getNiceScroll().show();
    });
    $('#ascrail2000').mouseover(function() {
        clearInterval(MyMar1);
        $("#r-colee").getNiceScroll().show();
    });
    $('#ascrail2000').css('cursor','pointer');
    //鼠标移开时重设定时器
    $('.ldgz').mouseout(function(){
        MyMar1=setInterval(Marquee1,speed);  
    });
}
function scoll4(){
    $('#r-coleee').niceScroll({
        cursorcolor: "#00d2ff",//#CC0071 光标颜色
        cursoropacitymax: 1, //改变不透明度非常光标处于活动状态（scrollabar“可见”状态），范围从1到0
        touchbehavior: false, //使光标拖动滚动像在台式电脑触摸设备
        cursorwidth: "0.055rem", //像素光标的宽度
        cursorborder: "0rem solid #666", // 游标边框css定义
        cursorborderradius: "0.05rem",//以像素为光标边界半径
        autohidemode: "true"
    });
    var speed=40;
    var coleee2=document.getElementById("r-coleee2");
    var coleee1=document.getElementById("r-coleee1");
    var coleee=document.getElementById("r-coleee");
    coleee2.innerHTML=coleee1.innerHTML; //克隆colee1为colee2
    function Marqueee1(){
    //当滚动至colee1与colee2交界时
    $("#r-coleee").getNiceScroll().hide();
    if(coleee2.offsetTop-coleee.scrollTop<=0){
     coleee.scrollTop-=coleee2.offsetTop; //colee跳到最顶端
     }else{
     coleee.scrollTop++;
    }
    }
    var MyMarr1=setInterval(Marqueee1,speed);//设置定时器
    //鼠标移上时清除定时器达到滚动停止的目的
    $('.bhqk').mouseover(function() {
        clearInterval(MyMarr1);
        $("#r-coleee").getNiceScroll().show();
    });
    $('#ascrail2001').mouseover(function() {
        clearInterval(MyMarr1);
        $("#r-coleee").getNiceScroll().show();
    });
    $('#ascrail2001').css('cursor','pointer');
    //鼠标移开时重设定时器
    $('.bhqk').mouseout(function(){
        MyMarr1=setInterval(Marqueee1,speed);  
    });
}


// //呼吸灯
// Img1 = new Array();
// Img2 = new Array();
// for(var x=0;x<90;x++){
//     if(x<10){
//         Img1[x] = "static/left_light/light_0000"+ x +".png"
//         Img2[x] = "static/right_light/light_right_0000"+ x +".png"
//     }else{
//         Img1[x] = "static/left_light/light_000"+ x +".png"
//         Img2[x] = "static/right_light/light_right_000"+ x +".png"
//     }    
// }
// size = Img1.length;  
// i = 0;  
// function chImg(){
//     $(".picID1").attr('src',Img1[44]);
//     $(".picID2").attr('src',Img2[44]);   
//     // $(".picID1").attr('src',Img1[i]);  
//     // $(".picID2").attr('src',Img2[i]); 
//     // i++;  
//     // if (i>=size) i = 0;  
//     // setTimeout("chImg()",33);
// } 

function pie1(){
    var echart = echarts.init(document.getElementById('pie-doughnut-1'));  
    option = {
        // animation: false,
        animationDuration:1500,
        tooltip: {
            show:true,
            trigger: 'item',
            formatter: function(params, ticket, callback){
                var num = '29';
                var str = '<div style="text-align: center" id="toolTipBox"><p style="font-size:0.4rem;margin:0px">'+ num + '</p></div>'
                return str
            },
            position: function (point, params, dom, rect, size) {
                //size参数可以拿到提示框的outerWidth和outerheight，dom参数可以拿到提示框div节点。
                //console.log(dom)可以看到，提示框是用position定位
                var marginW = Math.ceil(size.contentSize[0]/2);
                var marginH = Math.ceil(size.contentSize[1]/2);
                dom.style.marginLeft='-' + marginW + 'px';
                dom.style.marginTop='-' + marginH + 'px';
                return ["50%", "50%"];
            },
            alwaysShowContent:true,
            backgroundColor:false,  //设置提示框的背景色
            textStyle:{
                color:'#00d2ff'
            }
        },          
        series: [{
            name:'目标管控',
            type:'pie',
            radius: ['60%', '90%'],
            center: ["50%", "50%"],
            avoidLabelOverlap: false,
            hoverAnimation:false,   //关闭 hover 在扇区上的放大动画效果。
            cursor:'default', //鼠标悬浮时在图形元素上时鼠标的样式是什么。同 CSS 的 cursor。
            itemStyle: {
                normal : { //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                    label : {  //饼图图形上的文本标签
                        show : false
                    },
                    labelLine : {     //标签的视觉引导线样式
                        show : false
                    }, 
                },
                emphasis: {  
                    show : false
                }  
            } ,
            data:[
                {
                    value:5,  
                    itemStyle:{
                        normal:{color:'#fff100'}
                    },
                    name:'黄色'
                },
                {
                    value:24,
                    itemStyle:{
                        normal:{color:'#5ae06d'}
                    }, 
                    name:'绿色'
                }
            ]
        }]
    };
                  
    echart.setOption(option);  
    echart.dispatchAction({
        type: 'showTip',
        seriesIndex: 0,
        dataIndex: 0
    });
    setTimeout(function () { 
        $(".d-right-1").css('display','inline-block'); 
    }, 1400);
}

function pie2(){
    var echart = echarts.init(document.getElementById('pie-doughnut-2'));  
    option = {
        animation: true,
        animationDuration:1500,
        tooltip: {
            show:true,
            trigger: 'item',
            formatter: function(params, ticket, callback){
                var num = '26';
                var str = '<div style="text-align: center" id="toolTipBox"><p style="font-size:0.4rem;margin:0px">'+ num + '</p></div>'
                return str
            },
            position: function (point, params, dom, rect, size) {
                //size参数可以拿到提示框的outerWidth和outerheight，dom参数可以拿到提示框div节点。
                //console.log(dom)可以看到，提示框是用position定位
                var marginW = Math.ceil(size.contentSize[0]/2);
                var marginH = Math.ceil(size.contentSize[1]/2);
                dom.style.marginLeft='-' + marginW + 'px';
                dom.style.marginTop='-' + marginH + 'px';
                return ["50%", "50%"];
            },
            alwaysShowContent:true,
            backgroundColor:false,  //设置提示框的背景色
            textStyle:{
                color:'#00d2ff'
            }
        },          
        series: [{
            name:'目标管控',
            type:'pie',
            radius: ['60%', '90%'],
            center: ["50%", "50%"],
            // silent:true,
            avoidLabelOverlap: false,
            hoverAnimation:false,   //关闭 hover 在扇区上的放大动画效果。
            cursor:'default', //鼠标悬浮时在图形元素上时鼠标的样式是什么。同 CSS 的 cursor。
            itemStyle: {
                normal : { //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                    label : {  //饼图图形上的文本标签
                        show : false
                    },
                    labelLine : {     //标签的视觉引导线样式
                        show : false
                    }, 
                },
                emphasis: {  
                    show : false
                }  
            } ,
            data:[
                {
                    value:6,  
                    itemStyle:{
                        normal:{color:'#fff100'}
                    },
                    name:'黄色'
                },
                {
                    value:20,
                    itemStyle:{
                        normal:{color:'#5ae06d'}
                    }, 
                    name:'绿色'
                }
            ]
        }]
    };
                  
    echart.setOption(option);  
    echart.dispatchAction({
        type: 'showTip',
        seriesIndex: 0,
        dataIndex: 0
    });
    setTimeout(function () { 
        $(".d-right-2").css('display','inline-block'); 
    }, 1400);  
}


function GetQueryString(name){
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}
