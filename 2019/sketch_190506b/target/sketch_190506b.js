// Transcrypt'ed from Python, 2019-05-06 13:38:07
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {CLOSE, DEGREES, HALF_PI, PI, QUARTER_PI, RADIANS, TAU, TWO_PI, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceMoved, deviceOrientation, deviceShaken, deviceTurned, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, doubleClicked, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, keyPressed, keyReleased, keyTyped, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseClicked, mouseDragged, mouseIsPressed, mouseMoved, mouseReleased, mouseWheel, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touchEnded, touchMoved, touchStarted, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowResized, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
var __left0__ = tuple ([0.02, 0.01]);
export var ANGLE_STEP = __left0__ [0];
export var BETA_STEP = __left0__ [1];
var __left0__ = tuple ([100.0, PI + BETA_STEP]);
export var MAG = __left0__ [0];
export var SEGS_LIMIT = __left0__ [1];
export var PI_DOT_6 = PI * 0.6;
var __left0__ = 0.0;
export var angle = __left0__;
export var beta = __left0__;
export var paused = false;
export var knots = list ([]);
export var setup = function () {
	createCanvas (600, 600, 'webgl');
	smooth (8);
	colorMode ('hsb');
	noFill ();
	strokeWeight (8.0);
};
export var draw = function () {
	background (0);
	rect (20, 20, 20, 20);
	translate (width >> 1, height >> 1);
	rotateY (angle);
	angle += ANGLE_STEP;
	if (beta <= SEGS_LIMIT) {
		addKnot ();
	}
	beta += BETA_STEP;
	beginShape ();
	for (var k of knots) {
		stroke (k.c);
		vertex (k.v [0], k.v [1], k.v [2]);
	}
	endShape ();
};
export var mousePressed = function () {
	paused = !(paused);
	(paused ? noLoop () : loop ());
};
export var addKnot = function () {
	var r = MAG * (0.8 + 1.6 * sin (6 * beta));
	var theta = 2 * beta;
	var phi = PI_DOT_6 * sin (12 * beta);
	var rCosPhi = r * cos (phi);
	var x = rCosPhi * cos (theta);
	var y = rCosPhi * sin (theta);
	var z = r * sin (phi);
	var knot = Knot (x, y, z);
	knots.append (knot);
};
export var Knot =  __class__ ('Knot', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		var vec = tuple ([].slice.apply (arguments).slice (1));
		self.v = (len (vec) ? vec [0] : tuple (...vec));
		var __left0__ = self.v;
		var x = __left0__ [0];
		var y = __left0__ [1];
		var z = __left0__ [2];
		var mag = sqrt ((x * x + y * y) + z * z);
		self.c = color (mag, 255, 255);
	});},
	get __str__ () {return __get__ (this, function (self) {
		return __mod__ ('Vec: %s   \tHSB: %d', tuple ([self.v, self.c]));
	});}
});
start_p5 (setup, draw);

//# sourceMappingURL=sketch_190506b.map