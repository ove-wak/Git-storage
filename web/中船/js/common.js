$(window).resize(function () {      //当浏览器大小变化时页面自适应大小
    body_height = $(document.body).height();
    body_width = $(document.body).width();
    if(body_height/body_width <= 1400/2160){
        $(".content").height(body_height);
        $(".content").width((body_height/1400)*2160);
        $(".content").offset({top:0,left:(body_width-(body_height/1400)*2160)/2});
        $(".content").css('display','block');
    }else{
        $(".content").height((body_width/2160)*1400);
        $(".content").width(body_width);
        $(".content").offset({top:(body_height-(body_width/2160)*1400)/2,left:0});
        $(".content").css('display','block');
    }
});

$(document).ready(function(){
    // 页面自适应大小 
    body_height = $(document.body).height();
    body_width = $(document.body).width();
    if(body_height/body_width <= 1400/2160){
        $(".content").height(body_height);
        $(".content").width((body_height/1400)*2160);
        $(".content").offset({top:0,left:(body_width-(body_height/1400)*2160)/2});
        $(".content").css('display','block');
    }else{
        $(".content").height((body_width/2160)*1400);
        $(".content").width(body_width);
        $(".content").offset({top:(body_height-(body_width/2160)*1400)/2,left:0});
        $(".content").css('display','block');
    }


    

});