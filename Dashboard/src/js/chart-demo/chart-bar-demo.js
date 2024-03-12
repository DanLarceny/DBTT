/**
 * Apex Charts Bar Chart Settings and Data for:
 * Modern JavaScript Dashboard
 * Sample themable JavaScript dashboard template that employs modern ES6, Bootstrap 4 and CSS grid.
 * @author SimpleNotSimpler
 * @version 1.0.0
 * @license MIT
 * 
 * @requires [Apex Charts](https://github.com/apexcharts/apexcharts.js)
 * 
 */ 


// based on example from:
// https://apexcharts.com/javascript-chart-demos/column-charts/basic/
// https://exceljet.net/chart/quarterly-sales-by-clustered-region


// leaving raw data in chart due to deadlines
// later may come back to and push these in appropriate arrays


// **************** SET UP CHART *******************************************
const barOptions = {

    //data
    series: [{
        name: 'Systolic Pressure',
        data: [20, 30, 40, 50]
    }, {
        name: 'Diastolic Pressure',
        data: [60, 80, 90, 100]
    }],

    //configuration
    chart: {
        type: 'bar',
        //keep at 95% so chart does not cause horizontal scrolling
        height: '95%',
        width: '95%',
        
        toolbar: {
            tools: {
                download: '<i class="fas fa-download"></i>',
                zoom: false
            }
        },
    },

    dataLabels: {
        enabled: false
    },

    title: {
        text: 'Blood Pressure',
        align: 'center'
    },

    subtitle: {
        text: 'Updated yesterday at 11:59 PM',
        align: 'center',
        margin: 10
    },

    legend: {
        position: 'bottom'
    },

    stroke: {
        show: true,
        width: 2,
        colors: ['transparent']
    },

    fill: {
        opacity: 1
    },

    xaxis: {
        categories: ['12 March', '13 March', '14 March', '15 March','16 March','17 March','18 March'],
        axisTicks: {
            show: false,
        }
    },
    yaxis: {
        labels: {
            formatter: function (value) {
                return value;

            }
        },
        title: {
            text: 'mmHg'
        }
    },

    responsive: [{
        breakpoint: 1199,
        options: {
            title: {
                text: 'Qtly Sales / Region',
                align: 'left'
            }
        }
    }]
}

const barChart = new ApexCharts(document.getElementById('bar-chart'), barOptions);

barChart.render();