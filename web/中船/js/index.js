$(document).ready(function(){ 
    var echart = echarts.init(document.getElementById('pie-doughnut-1'));  
    option = {
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            series: [
                {
                    name:'目标管控',
                    type:'pie',
                    radius: ['50%', '70%'],
                    avoidLabelOverlap: false,
                    itemStyle: {
                    normal : { //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                            label : {  //饼图图形上的文本标签
                                show : true, 
                                position:'right' 
                            },
                            labelLine : {     //标签的视觉引导线样式
                                show : true  
                            }
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
                        name:'17.2%'},
                        {value:24,
                        itemStyle:{
                            normal:{color:'#5ae06d'}
                        }, 
                        name:'82.8%'}
                    ]
                }
            ]
    };
                  
    echart.setOption(option);  
});
