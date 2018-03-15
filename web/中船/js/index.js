$(document).ready(function(){ 
    var echart = echarts.init(document.getElementById('pie-doughnut-1'));  
    mylabel={
                show:true,                  //是否显示标签。
                position:"right",          //标签的位置。// 绝对的像素值[10, 10],// 相对的百分比['50%', '50%'].'top','left','right','bottom','inside','insideLeft','insideRight','insideTop','insideBottom','insideTopLeft','insideBottomLeft','insideTopRight','insideBottomRight'
                offset:[30, 40],             //是否对文字进行偏移。默认不偏移。例如：[30, 40] 表示文字在横向上偏移 30，纵向上偏移 40。
                formatter:'{b}',       //标签内容格式器。模板变量有 {a}、{b}、{c}，分别表示系列名，数据名，数据值。
            };
    option = {
            
            series: [
                {
                    name:'目标管控',
                    type:'pie',
                    radius: ['50%', '70%'],
                    avoidLabelOverlap: false,
                    silent:true,
                    itemStyle: {
                    normal : { //normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                            label : {  //饼图图形上的文本标签
                                show : true, 
                                formatter: "{d}" 
                            },
                            labelLine : {     //标签的视觉引导线样式
                                show : true ,
                                position:"right" 
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
