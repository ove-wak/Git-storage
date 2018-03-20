var content_data = {
    "V":{
        "1":[
        "营业收入(F)",
        "利润总额(C)",
        "经济增加值(C)"
        ],
        "2":[
        "军品营业收入(G)",
        "军品承接合同(G)"
        ],
        "3":[
        "民品营业收入(G)",
        "民品承接合同(G)"
        ],
        "4":[
        "两金占流动资产比率(C)",
        "资产负债率(G)"
        ]
    },
    "C":{
        "1":[
        "完成重点型号生产任务",
        "推动海洋装备技术跨进陆空天",
        "推动对外技术引进立项及签约"
        ],
        "2":[
        "提升造船效率(G)",
        "做强非船产业"
        ],
        "3":[
        "确保质量形势平稳",
        "确保生产安全形势平稳",
        "落实节能环保任务",
        "完成保密工作任务、力保不出现重大失泄密事件",
        "完成以扶贫为核心的社会责任任务"
        ]
    },
    "P":{
        "1":[
        "完成动力板块涉军研制任务",
        "完成电子信息板块涉军研制任务",
        "完成《2045年前国防科技创新和武器装备技术发展战略研究》"
        ],
        "2":[
        "提升武器装备科研生产保障能力"
        ],
        "3":[
        "推动重大军民融合能力基地建设",
        "优化动力板块产业布局",
        "推进重点项目与军民融合产业事业群建设"
        ],
        "4":[
        "加强产业投资与管理"
        ],
        "5":[
        "推进海洋探测与开发装备技术项目",
        "提升集团公司智能制造水平",
        "推进电子信息科研项目"
        ],
        "6":[
        "推进基础研究和前沿技术研究"
        ],
        "7":[
        "推进创新平台建设"
        ],
        "8":[
        "推进资产证券化"
        ],
        "9":[
        "推进证券市场股权、债券发行"
        ],
        "10":[
        "加强资金、保险和授信等集中管理"
        ],
        "11":[
        "增加海外业务收入和布点"
        ],
        "12":[
        "加快发展军贸业务"
        ],
        "13":[
        "推进供给侧改革"
        ],
        "14":[
        "完成三供一业和厂办大集体移交任务",
        "完成“晒态势、促提升”任务",
        "推进集中采购、公车改革"
        ],
        "15":[
        "加强全面风险管理",
        "力保不出现群体性、恶性上访事件"
        ],
        "16":[
        "推进“法治船舶”建设"
        ],
        "17":[
        "加强内审和内控评价工作",
        "落实监事会工作"
        ],
        "18":[
        "加强巡视工作",
        "开展党风廉政和反腐倡廉工作"
        ]
    },
    "L":{
        "1":[
        "推进党团工作",
        "推进企业文化建设"
        ],
        "2":[
        "完善信息化发展规划"
        ],
        "3":[
        "加强领导干部检查、考核管理"
        ],
        "4":[
        "加强科技和技能领军人才队伍建设"
        ]
    }
}

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
