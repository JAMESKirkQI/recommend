//通过给定的ID来发送请求
console.log("start")
let data1 = []
axios.get('http://127.0.0.1:8000/recommend/count101/')
    .then(function (response) {
        let x = JSON.parse(response.data).data;

        console.log(x);
        for (var a = 0; a < x.length; a++) {
            console.log(x[a].pk, x[a].fields.num)
            data1.push({"value": x[a].fields.num, "name": x[a].pk})

        }
    })
    .catch(function (err) {
        console.log(err);
    });

console.log(data1)
console.log(typeof(data1))
console.log("stop")

var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom, null, {
    width: 600,
    height: 400
});
option = {
    title: {
        text: 'Referer of a Website',
        subtext: 'Fake Data',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'left'
    },
    series: [
        {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: data1,
            // data: [
            //     {value: 1674, name: "其他"},
            //     {value: 396612, name: "知识内容页"},
            //     {value: 7776, name: "知识列表页"},
            //     {value: 5603, name: "知识首页"},
            // ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
setTimeout(function (){
    option && myChart.setOption(option);
},3000)


