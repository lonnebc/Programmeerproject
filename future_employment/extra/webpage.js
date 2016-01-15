// programmeerproject
// by Lonneke Lammers

d3.custom = {};
d3.custom.slopegraph = function() {

    var opts = {
        width: 400,
        height: 2000,
        margin: {top: 20, right: 50, bottom: 50, left: 50},
        labelLength: 50
    };

    function exports(selection) {
        selection.each(function (dataset) {
            var chartHeight = opts.height - opts.margin.top - opts.margin.bottom;
            var chartWidth = opts.width - opts.margin.right - opts.margin.left;

            var parent = d3.select(this);
            var svg = parent.selectAll("svg.chart-root").data([0]);
            svg.enter().append("svg").attr("class", "chart-root")
                    .append('g').attr('class', 'chart-group');
            svg.attr({width: opts.width, height: opts.height});
            svg.exit().remove();
            var chartSvg = svg.select('.chart-group');

            var data = d3.transpose(dataset.data);
            var scale = d3.scale.linear().domain(d3.extent(d3.merge(data))).range([0, chartHeight]);

            var lines = chartSvg.selectAll('line.slope-line')
                .data(data);
            lines.enter().append("line")
            lines.attr({
                    class: 'slope-line',
                    x1: opts.margin.left + opts.labelLength,
                    x2: opts.width - opts.margin.right - opts.labelLength,
                    y1: function(d) { return opts.margin.top + scale(d[0]); },
                    y2: function(d) { return opts.margin.top + scale(d[1]); }});
            lines.exit().remove();

            var leftLabels = chartSvg.selectAll('text.left_labels')
                .data(data);
            leftLabels.enter().append('text');
            leftLabels.attr({
                    class: 'left_labels slope-label',
                    x: opts.margin.left + opts.labelLength,
                    y: function(d,i) { return opts.margin.top + scale(d[0]); },
                    dy: '.35em',
                    'text-anchor': 'end'})
                .text(function(d,i) { return dataset.label[0][i] });
            leftLabels.exit().remove();

            var rightLabels = chartSvg.selectAll('text.right_labels')
                .data(data);
            rightLabels.enter().append('text');
            rightLabels.attr({
                    class: 'right_labels slope-label',
                    x: opts.width - opts.margin.right - opts.labelLength,
                    y: function(d,i) { return opts.margin.top + scale(d[1]); },
                    dy: '.35em'})
                .text(function(d,i) { return dataset.label[0][i] });
            rightLabels.exit().remove();
        });
    }

    exports.opts = opts;
    createAccessors(exports);

    return exports;
}


createAccessors = function(visExport) {
    for (var n in visExport.opts) {
        if (!visExport.opts.hasOwnProperty(n)) continue;
        visExport[n] = (function(n) {
            return function(v) {
                return arguments.length ? (visExport.opts[n] = v, this) : visExport.opts[n];
            }
        })(n);
    }
};


	// // function to get values for barchart
	// chart = function(sector){
		
	// 	// loop over dataset
	// 	// get values
	// 	for (var i = 0; i < alldata.length; i++){	
	// 		sector = alldata[i][0]
	// 		jobs = (alldata[i][1][0:])
	// 		year14 = (alldata[i][1][5])
	// 		year24 = (alldata[i][1][4])
	// 		percent = (alldata[i][1][3])
	// 		job_openings = (alldata[i][1][2])
	// 		change1424 = (alldata[i][1][1])
	// 		median_wage = (alldata[i][1][0])

	// 		if (sector == id2){
	// 		 	console.log(year13, year10, year07)
	// 		 	console.log(geo_id)
	//  			draw_chart(sector)
	// 		}	
	// 	}
	// }

// 	// barchart visualisation function
// 	draw_chart = function(year07, year08, year09, year10, year11, year12, year13){
		
// 		var data = [year07, year08, year09, year10, year11, year12, year13]

// 		// barcharts
// 		var width = 420,
// 		    barHeight = 30;

// 		var x = d3.scale.linear()
// 		    .domain([0, d3.max(data)])
// 		    .range([0, width]);

// 		var chart = d3.select(".chart")
// 		    .attr("width", width)
// 		    .attr("height", barHeight * data.length);

// 		var bar = chart.selectAll("g")
// 	    	.data(data)
// 	  		.enter().append("g")
// 	    	.attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")";})
// 	    	.attr("class", "makechart");
	    	
// 	    // append bars
// 		bar.append("rect")
// 		    .attr("width", x)
// 		    .attr("height", barHeight - 1);
		    
// 		// append text in bars
// 		bar.append("text")
// 		    .attr("x", function(d) { return x(d) - 3; })
// 		    .attr("y", barHeight / 2)
// 		    .attr("dy", ".35em")
// 		    .text(function(d) { return d; });
// 		}
// 	});
	
// }


	