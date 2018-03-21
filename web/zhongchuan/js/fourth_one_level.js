$(document).ready(function(){ 
    // var urlinfo = window.location.href;//获取url 
    // var urlcontent = urlinfo.split('?')[1].split('&');//拆分url得到”=”后面的参数 
    // // 公司治理三级页面进入
    // var myid1=urlcontent[0].split("=")[1];
    // var myid2=urlcontent[1].split("=")[1];
    // var name=decodeURI(urlcontent[2].split("=")[1]);

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
    // $(".third_two .back").click(function() {
    //         window.location.href="second_level.html?id=mbgk";
    // });
    // $(".third_two .close").click(function() {
    //         window.location.href="second_level.html?id=mbgk";
    // });
    
});
