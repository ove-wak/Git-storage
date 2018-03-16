$(window).resize(function () {      //当浏览器大小变化时页面自适应大小
    var whdef = 100/2160;// 表示2160的设计图,使用100PX的默认值
    var hwdef = 100/1400;
    body_height = $(document.body).height();
    body_width = $(document.body).width();
    if(body_height/body_width <= 1400/2160){
        var rem = body_height * hwdef;// 以默认比例值乘以当前窗口宽度,得到该宽度下的相应FONT-SIZE值
        $('html').css('font-size', rem + "px");
        $(".content").height(body_height);
        $(".content").width((body_height/1400)*2160);
        $(".content").offset({top:0,left:(body_width-(body_height/1400)*2160)/2});
        $(".content").css('display','block');
    }else{
        var rem = body_width * whdef;// 以默认比例值乘以当前窗口宽度,得到该宽度下的相应FONT-SIZE值
        $('html').css('font-size', rem + "px");
        $(".content").height((body_width/2160)*1400);
        $(".content").width(body_width);
        $(".content").offset({top:(body_height-(body_width/2160)*1400)/2,left:0});
        $(".content").css('display','block');
    }
    
});

$(document).ready(function(){
    // 页面自适应大小 
    var whdef = 100/2160;// 表示2160的设计图,使用100PX的默认值
    var hwdef = 100/1400;
    body_height = $(document.body).height();
    body_width = $(document.body).width();
    if(body_height/body_width <= 1400/2160){
        var rem = body_height * hwdef;// 以默认比例值乘以当前窗口宽度,得到该宽度下的相应FONT-SIZE值
        $('html').css('font-size', rem + "px");
        $(".content").height(body_height);
        $(".content").width((body_height/1400)*2160);
        $(".content").offset({top:0,left:(body_width-(body_height/1400)*2160)/2});
        $(".content").css('display','block');
    }else{
        var rem = body_width * whdef;// 以默认比例值乘以当前窗口宽度,得到该宽度下的相应FONT-SIZE值
        $('html').css('font-size', rem + "px");
        $(".content").height((body_width/2160)*1400);
        $(".content").width(body_width);
        $(".content").offset({top:(body_height-(body_width/2160)*1400)/2,left:0});
        $(".content").css('display','block');
    }
    

});