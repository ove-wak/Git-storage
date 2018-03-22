$(document).ready(function(){ 
    var urlinfo = window.location.href;//获取url 
    var urlcontent = urlinfo.split('?')[1].split('&');//拆分url得到”=”后面的参数 
    // 目标管控四级页面进入
    var myid1=urlcontent[0].split("=")[1];
    var myid2=urlcontent[1].split("=")[1];
    var name=decodeURI(urlcontent[2].split("=")[1]);

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
    $('.dr_1').click(function(){
        // 其他关闭
        if($(this).find('.double_arrow_low').length>0){
            height = $(this).siblings('.tt').height();
            $(this).parent().css({'height':height});
            $(this).parent().css({'background-color':"#014886"});
            $(this).parent().css({'z-index':3});
            $(this).parent().parent().find(".title-big-long").css({'z-index':4});
            $(this).find(".double_arrow_low").addClass("double_arrow_top").removeClass("double_arrow_low");
        }else{
            $(this).parent().css({'height':'1.46rem'});
            $(this).parent().css({'backgroundColor':"rgba(0,210,255,0.1)"});
            $(this).parent().css({'z-index':1});
            $(this).find(".double_arrow_top").addClass("double_arrow_low").removeClass("double_arrow_top");
        }   
    });
    $(".fourth_two .back").click(function() {
            window.location.href=encodeURI("third_two_level.html?id1="+myid1+"&id2="+myid2+"&name="+name);
    });
    $(".fourth_two .close").click(function() {
            window.location.href="index.html";
    });
    
});
