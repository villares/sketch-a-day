// Transcrypt'ed from Python, 2020-09-07 22:08:42
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, isinstance, issubclass, len, list, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {shuffle} from './random.js';
import {ADD, ALT, ARROW, AUDIO, AUTO, AXES, BACKSPACE, BASELINE, BEVEL, BEZIER, BLEND, BLUR, BOLD, BOLDITALIC, BOTTOM, BURN, CENTER, CHORD, CLAMP, CLOSE, CONTROL, CORNER, CORNERS, CROSS, CURVE, DARKEST, DEGREES, DEG_TO_RAD, DELETE, DIFFERENCE, DILATE, DODGE, DOWN_ARROW, ENTER, ERODE, ESCAPE, EXCLUSION, FILL, GRAY, GRID, HALF_PI, HAND, HARD_LIGHT, HSB, HSL, IMAGE, IMMEDIATE, INVERT, ITALIC, LANDSCAPE, LEFT, LEFT_ARROW, LIGHTEST, LINEAR, LINES, LINE_LOOP, LINE_STRIP, MIRROR, MITER, MOVE, MULTIPLY, NEAREST, NORMAL, OPAQUE, OPEN, OPTION, OVERLAY, P2D, PI, PIE, POINTS, PORTRAIT, POSTERIZE, PROJECT, QUADRATIC, QUADS, QUAD_STRIP, QUARTER_PI, RADIANS, RADIUS, RAD_TO_DEG, REPEAT, REPLACE, RETURN, RGB, RIGHT, RIGHT_ARROW, ROUND, SCREEN, SHIFT, SOFT_LIGHT, SQUARE, STROKE, SUBTRACT, TAB, TAU, TEXT, TEXTURE, THRESHOLD, TOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, TWO_PI, UP_ARROW, VIDEO, WAIT, WEBGL, _CTX_MIDDLE, _DEFAULT_FILL, _DEFAULT_LEADMULT, _DEFAULT_STROKE, _DEFAULT_TEXT_FILL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, add_library, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, changed, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createA, createAudio, createButton, createCamera, createCanvas, createCapture, createCheckbox, createColorPicker, createDiv, createElement, createFileInput, createGraphics, createImage, createImg, createInput, createNumberDict, createP, createRadio, createSelect, createShader, createSlider, createSpan, createStringDict, createVector, createVideo, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, erase, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, input, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, logOnloaded, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noErase, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, popMatrix, popStyle, pow, pre_draw, preload, push, pushMatrix, pushStyle, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, removeElements, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, select, selectAll, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, sin, size, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pyp5js.js';
var __name__ = 'sketch_2020_09_07pyp5js';
export var seed_value = 1;
export var sf = 1;
export var gliphs = [(function __lambda__ (x, y, s) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 's': var s = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return rect (x, y, s, s);
}), (function __lambda__ (x, y, s) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 's': var s = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return ellipse (x, y, s, s);
}), (function __lambda__ (x, y, s) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 's': var s = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return triangle (x - s, y, x - s, y + s, x, y + s);
}), (function __lambda__ (x, y, s) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 's': var s = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	return triangle (x + s, y, x + s, y - s, x, y - s);
})];
export var colors = tuple ([tuple ([0, 50, 50, 150]), tuple ([200, 0, 0, 150])]);
export var setup = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	createCanvas (600, 400);
};
export var draw = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	randomSeed (seed_value);
	background (240, 240, 240);
	grid (width / 2, height / 2, 5, 150 * sf, ensamble, 5);
	if (__mod__ (frameCount, 100) == 0) {
		shuffle (gliphs);
	}
};
export var keyPressed = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
	}
	else {
	}
	seed_value = mouseX + 1000 * mouseY;
};
export var ensamble = function (ex, ey, eo) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'ex': var ex = __allkwargs0__ [__attrib0__]; break;
					case 'ey': var ey = __allkwargs0__ [__attrib0__]; break;
					case 'eo': var eo = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	noStroke ();
	for (var i = 0; i < eo; i++) {
		fill (colors [__mod__ (i, len (colors))]);
		var __left0__ = tuple ([int (random (3, 7)), 14, 7]);
		var order = __left0__ [0];
		var spacing = __left0__ [1];
		var side = __left0__ [2];
		var x = ((1 + int (random (-(5), 5))) * side) * sf;
		var y = ((1 + int (random (-(5), 5))) * side) * sf;
		grid (ex + x, ey + y, order, spacing * sf, gliphs [int (random (len (gliphs)))], side * sf);
	}
};
export var grid = function (x, y, order, spacing, func, args) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'x': var x = __allkwargs0__ [__attrib0__]; break;
					case 'y': var y = __allkwargs0__ [__attrib0__]; break;
					case 'order': var order = __allkwargs0__ [__attrib0__]; break;
					case 'spacing': var spacing = __allkwargs0__ [__attrib0__]; break;
					case 'func': var func = __allkwargs0__ [__attrib0__]; break;
					case 'args': var args = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	if (py_typeof (order) === tuple) {
		var __left0__ = order;
		var cols = __left0__ [0];
		var rows = __left0__ [1];
	}
	else {
		var __left0__ = order;
		var cols = __left0__;
		var rows = __left0__;
	}
	var __left0__ = tuple ([x - (cols * spacing) / 2, y - (rows * spacing) / 2]);
	var xo = __left0__ [0];
	var yo = __left0__ [1];
	for (var i = 0; i < cols; i++) {
		var gx = spacing / 2 + i * spacing;
		for (var j = 0; j < rows; j++) {
			var gy = spacing / 2 + j * spacing;
			func (xo + gx, yo + gy, args);
		}
	}
};

//# sourceMappingURL=sketch_2020_09_07pyp5js.map