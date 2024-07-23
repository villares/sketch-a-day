// Transcrypt'ed from Python, 2019-05-27 10:47:20
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {combinations, combinations_with_replacement, permutations, product} from './itertools.js';
import {shuffle} from './random.js';
import {BOTTOM, CENTER, CLOSE, CMYK, DEGREES, HALF_PI, HSB, LEFT, PI, QUARTER_PI, RADIANS, RGB, RIGHT, SHIFT, TAU, TOP, TWO_PI, WEBGL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
export var num = null;
export var H = null;
export var W = null;
export var line_combos = null;
export var space = 15;
export var position = 0;
export var setup = function () {
	createCanvas (1045, 700);
	var __left0__ = tuple ([1045, 700]);
	var width = __left0__ [0];
	var height = __left0__ [1];
	frameRate (5);
	rectMode (CENTER);
	strokeWeight (2);
	var grid = product (range (-(1), 2), __kwargtrans__ ({repeat: 2}));
	var lines = combinations (grid, 2);
	var short_lines = list ([]);
	for (var l of lines) {
		var __left0__ = tuple ([l [0], l [1]]);
		var x0 = __left0__ [0][0];
		var y0 = __left0__ [0][1];
		var x1 = __left0__ [1][0];
		var y1 = __left0__ [1][1];
		if (dist (x0, y0, x1, y1) < 3) {
			short_lines.append (l);
		}
	}
	var num_short_lines = len (short_lines);
	print ('Number of possible lines: {}'.format (num_short_lines));
	line_combos = list (combinations (short_lines, 4));
	shuffle (line_combos);
	num = len (line_combos);
	print (num);
	var __left0__ = tuple ([Math.floor ((width - space) / space), Math.floor ((height - space) / space)]);
	W = __left0__ [0];
	H = __left0__ [1];
	print (tuple ([W, H, W * H]));
};
export var draw = function () {
	background (240);
	var i = position;
	for (var y = 0; y < H; y++) {
		for (var x = 0; x < W; x++) {
			if (i < len (line_combos)) {
				push ();
				translate (space + space * x, space + space * y);
				draw_combo (i);
				py_pop ();
				i++;
			}
		}
	}
	if (i < len (line_combos)) {
		position += W;
	}
};
export var draw_combo = function (n) {
	var siz = space / 3.0;
	for (var [i, sl] of enumerate (line_combos [n])) {
		colorMode (HSB, 255, 255, 255);
		stroke (i * 64, 160, 160);
		var __left0__ = tuple ([sl [0], sl [1]]);
		var x0 = __left0__ [0][0];
		var y0 = __left0__ [0][1];
		var x1 = __left0__ [1][0];
		var y1 = __left0__ [1][1];
		line (x0 * siz, y0 * siz, x1 * siz, y1 * siz);
	}
};
export var keyPressed = function () {
	if (key == 's') {
		saveFrame ('####.png');
	}
};
export var event_functions = dict ({'keyPressed': keyPressed});
start_p5 (setup, draw, event_functions);

//# sourceMappingURL=sketch_190525b.map