var geoCoordMap = {
    "aletai": [88.127, 47.842],
    "beijing": [116, 40],
    "changchun": [125.35, 43.47],
    "dalian": [121.6283, 38.9061],
    "dawu": [100.248, 34.478],
    "enshi": [109.0966, 30.1657],
    "fuzhou": [119.281, 26.091],
    "ganzi": [100.0185, 31.6102],
    "gaotai": [99.814, 39.41],
    "geermu": [94.87402, 36.4332],
    "hailaer": [119.74, 49.27],
    "hegang": [130.14, 47.21],
    "huaibeii": [116.79, 33.98],
    "jian": [115.058, 26.748],
    "jixian": [117.5314, 40.0861],
    "kunming": [102.7474, 25.1482],
    "lanzhou": [103.8, 36.1],
    "lasa": [91.1, 29.73],
    "linzih": [94.34, 29.6659],
    "liyang": [119.42, 31.349],
    "mohe": [122.339, 53.455],
    "mudanjiang": [129.5919, 44.6164],
    "qingdao": [120.55, 36.19],
    "ruoqiang": [88.17, 39.02],
    "shenyang": [123.578, 41.828],
    "shiquanhe": [80.109, 32.521],
    "songpan": [103.6, 32.483],
    "taian": [117.12, 36.2],
    "taiyuan": [112.6, 37.7],
    "tanshan": [105.6, 36.5],
    "tengchong": [98.41978, 25.02895],
    "wanzhou": [108.49, 30.77],
    "wenzhou": [120.664, 27.926],
    "wujiahe": [108.04, 41.18],
    "wushi": [79.21, 41.2],
    "wuzhou": [111.23361, 23.4812],
    "xiamen": [118.05, 24.45],
    "xian": [108.92, 34.03],
    "xiangfan": [112.043, 32.0028],
    "yinchuan": [105.55, 38.36],
    "yushu": [96.2, 33.01],
    "yutian": [81.996, 36.429],
    "zhangjiakou": [114.54, 40.49],
    "zhangzhou": [117.63, 24.45],
    "zhengzhou": [113.57, 34.63],
    "zhongdian": [99.698, 27.823],
    "zigong": [104.76, 29.35]
};

var convertData = function(data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push(geoCoord.concat(data[i].value));
        }
    }
    return res;
};

option = {
    title: {
        text: 'SNM',
        left: 'center',
        textStyle: {
            color: '#fff'
        }
    },
    backgroundColor: '#404a59',
    visualMap: {
        min: 1.0,
        max: 4.8,
        splitNumber: 5,
        inRange: {
            color: ['#d94e5d', '#eac736', '#50a3ba'].reverse()
        },
        textStyle: {
            color: '#fff'
        }
    },
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        roam: true,
        itemStyle: {
            normal: {
                areaColor: '#323c48',
                borderColor: '#111'
            },
            emphasis: {
                areaColor: '#2a333d'
            }
        }
    },
    series: [{
        name: 'AQI',
        type: 'heatmap',
        blurSize: 20, //每个点模糊的大小，在地理坐标系(coordinateSystem: 'geo')上有效。
        coordinateSystem: 'geo',
        data: convertData([{
                name: "aletai",
                value: 2.50443
            },
            {
                name: "beijing",
                value: 2.92121
            },
            {
                name: "changchun",
                value: 2.99799
            },
            {
                name: "dalian",
                value: 3.64453
            },
            {
                name: "dawu",
                value: 2.72115
            },
            {
                name: "enshi",
                value: 2.57638
            },
            {
                name: "fuzhou",
                value: 3.29196
            },
            {
                name: "ganzi",
                value: 3.65915
            },
            {
                name: "gaotai",
                value: 2.78689
            },
            {
                name: "geermu",
                value: 2.4158
            },
            {
                name: "hailaer",
                value: 2.54717
            },
            {
                name: "hegang",
                value: 2.65068
            },
            {
                name: "huaibeii",
                value: 3.00829
            },
            {
                name: "jian",
                value: 3.06309
            },
            {
                name: "jixian",
                value: 2.99721
            },
            {
                name: "kunming",
                value: 3.18325
            },
            {
                name: "lanzhou",
                value: 3.08514
            },
            {
                name: "lasa",
                value: 3.3806
            },
            {
                name: "linzih",
                value: 2.92996
            },
            {
                name: "liyang",
                value: 3.5135
            },
            {
                name: "mohe",
                value: 2.82992
            },
            {
                name: "mudanjiang",
                value: 2.53444
            },
            {
                name: "qingdao",
                value: 2.93984
            },
            {
                name: "ruoqiang",
                value: 4.71997
            },
            {
                name: "shenyang",
                value: 2.93964
            },
            {
                name: "shiquanhe",
                value: 2.23406
            },
            {
                name: "songpan",
                value: 2.49585
            },
            {
                name: "taian",
                value: 2.64239
            },
            {
                name: "taiyuan",
                value: 4.12775
            },
            {
                name: "tanshan",
                value: 3.27921
            },
            {
                name: "tengchong",
                value: 3.49498
            },
            {
                name: "wanzhou",
                value: 3.07779
            },
            {
                name: "wenzhou",
                value: 3.52944
            },
            {
                name: "wujiahe",
                value: 2.44542
            },
            {
                name: "wushi",
                value: 2.34723
            },
            {
                name: "wuzhou",
                value: 3.49355
            },
            {
                name: "xiamen",
                value: 3.67242
            },
            {
                name: "xian",
                value: 3.00496
            },
            {
                name: "xiangfan",
                value: 2.95873
            },
            {
                name: "yinchuan",
                value: 4.60018
            },
            {
                name: "yushu",
                value: 4.64329
            },
            {
                name: "yutian",
                value: 2.00453
            },
            {
                name: "zhangjiakou",
                value: 2.80634
            },
            {
                name: "zhangzhou",
                value: 3.26175
            },
            {
                name: "zhengzhou",
                value: 4.1255
            },
            {
                name: "zhongdian",
                value: 2.78507
            },
            {
                name: "zigong",
                value: 3.15692
            }
        ])
    }]
};