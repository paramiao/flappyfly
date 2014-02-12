var canvas = document.getElementById('canvas'),
	context = canvas.getContext('2d');
	ctx = canvas.getContext('2d');
ctx.strokeStyle = "#666"; 
function useBeginPath() { 
for (var i = 0; i < 5; ++i) { 
ctx.beginPath(); 
ctx.rect(10 + i*20, 10 + i*20, 210 - i*40, 210 - i*40); 
ctx.stroke(); 
} 
} 
function notUseBeginPath() { 
ctx.beginPath(); 
for (var i = 0; i < 5; ++i) { 
ctx.rect(240 + i*20, 10 + i*20, 210 - i*40, 210 - i*40); 
ctx.stroke(); }}

var img = new Image();
img.src = 'http://flapmmo.com/atlas.png';

var spriteWidth  = 350,
	spriteHeight = 170,
	pixelsLeft   = 170,
	pixelsTop    = 10,

	canvasPosX   = 20,
	canvasPosY   = 20
	;

	context.drawImage(img, 
			pixelsLeft,
			pixelsTop,
			spriteWidth,
			spriteHeight,
			canvasPosX,
			canvasPosY,
			spriteWidth,
			spriteHeight
			);


	function Sprite(img, width, height, positions){
		this.img = img;
		this.width = width;
		this.height = height;
		this.positions = positions;

	}
Sprite.prototype = {
draw: function(position, x, y){
		  var pos = this.positions[position];
		  context.drawImage( 
				  this.img,
				  pos[0],
				  pos[1],
				  this.width,
				  this.height,
				  x, y,
				  this.width,
				  this.height
				  );

	  }

};

var sprite = new Sprite(img, 32, 16, [
		[10, 523],  // green
		[131, 523], // pink
		[191, 523]  // hit

		]);
sprite.draw(0, 10, 200);
sprite.draw(1, 50, 200);
sprite.draw(2, 90, 200);


//$(document).ready(function() {  
//	$img.box2d({'y-velocity':5});
//});
console.log('hello')
