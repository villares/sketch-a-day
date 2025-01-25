/******************
A small tweak on code by Vamoss
Original code link:
https://openprocessing.org/sketch/1798346

Author links:
http://vamoss.com.br
http://twitter.com/vamoss
http://github.com/vamoss
******************/

var radius;
var x, y;
var points = [];

function setup() {
	createCanvas(windowWidth, windowHeight);
	colorMode(HSB, 255, 255, 255)
	radius = min(width, height) / 2;//default is 135
	
	x = width / 3 - radius / 2;
	y = height / 3 - radius / 2 + 50;
	
	var vamoss = Vamoss(1, x, y, radius*1.5);
}

function draw() {
	background(0);
	
	noFill();
	points.forEach(p => {
		var r = p.r;
		var d = dist(p.x, p.y, mouseX, mouseY);
		if(d < 200)
			r *= map(d, 0, 200, 10, 1);
		fill(p.x % 255, 200, 200)
		circle(p.x, p.y, r);
	});
}

function Vamoss(pct, x, y, radius){
	pct = constrain(pct, 0.0001, 1);
	
	const scale = radius / 135;
	const circleRadius = 5;//small circles max size
	const space = 2.5;//space between the small circles
	
	//magic numbers
	const ampVel = 0.0017;
	const phase = 0.25;
	const freq = 1.54;
	
	var amp = 0;
	var r = 0;
	var simpleSin, simpleCos, complexSin, complexCos;
	
	for(var t = 0; t < 7.92 * pct; t += 0.01 * space){
		if(t < 5){
			if(r < circleRadius * scale)
				r += 0.01 * space * scale;
		}else{
			if(r > 0)
				r -= 0.017 * space * scale;
		}

		if(amp < 1)
			amp += ampVel * space;

		simpleSin = sin(t) * radius / 2 + radius / 2;
		complexCos = cos(t * freq + HALF_PI + phase) * amp * radius / 2 + radius / 2;

		points.push({
			x: x + simpleSin,
			y: y + complexCos,
			r
		});
		
		points.push({
			x: x + radius - simpleSin,
			y: y + complexCos,
			r
		});
	}
}