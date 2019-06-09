// Transcrypt'ed from Python, 2019-06-09 19:19:57
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {ADD, ALT, ARROW, AUTO, AXES, BACKSPACE, BASELINE, BEVEL, BEZIER, BLEND, BLUR, BOLD, BOLDITALIC, BOTTOM, BURN, CENTER, CHORD, CLAMP, CLOSE, CONTROL, CORNER, CORNERS, CROSS, CURVE, DARKEST, DEGREES, DEG_TO_RAD, DELETE, DIFFERENCE, DILATE, DODGE, DOWN_ARROW, ENTER, ERODE, ESCAPE, EXCLUSION, FILL, GRAY, GRID, HALF_PI, HAND, HARD_LIGHT, HSB, HSL, IMAGE, IMMEDIATE, INVERT, ITALIC, LANDSCAPE, LEFT, LEFT_ARROW, LIGHTEST, LINEAR, LINES, LINE_LOOP, LINE_STRIP, MIRROR, MITER, MOVE, MULTIPLY, NEAREST, NORMAL, OPAQUE, OPEN, OPTION, OVERLAY, P2D, PI, PIE, POINTS, PORTRAIT, POSTERIZE, PROJECT, QUADRATIC, QUADS, QUAD_STRIP, QUARTER_PI, RADIANS, RADIUS, RAD_TO_DEG, REPEAT, REPLACE, RETURN, RGB, RIGHT, RIGHT_ARROW, ROUND, SCREEN, SHIFT, SOFT_LIGHT, SQUARE, STROKE, SUBTRACT, TAB, TAU, TEXT, TEXTURE, THRESHOLD, TOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, TWO_PI, UP_ARROW, WAIT, WEBGL, _CTX_MIDDLE, _DEFAULT_FILL, _DEFAULT_LEADMULT, _DEFAULT_STROKE, _DEFAULT_TEXT_FILL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
export var pts = list ([tuple ([100, 100]), tuple ([110, 400]), tuple ([400, 400])]);
export var rds = list ([40, 40, 40, 30, 70, 50]);
export var dragged_pt = -(1);
export var setup = function () {
	createCanvas (500, 500);
	pts.append (tuple ([250, 150]));
	pts.append (tuple ([250 + 100 * cos (PI / 6.0), 250 + 100 * sin (PI / 6.0)]));
	pts.append (tuple ([250 - 100 * cos (PI / 6.0), 250 + 100 * sin (PI / 6.0)]));
};
export var draw = function () {
	background (200);
	fill (255, 100);
	b_poly_arc_augmented (pts, rds);
	fill (0, 0, 100);
	for (var pt of pts) {
		ellipse (pt [0], pt [1], 10, 10);
	}
};
export var keyPressed = function () {
	var delta = 0;
	if (key == '-') {
		var delta = -(1);
	}
	else if (key == '=' || key == '+') {
		var delta = 1;
	}
	for (var [i, pt] of enumerate (pts)) {
		if (dist (mouseX, mouseY, pt [0], pt [1]) < 10) {
			rds [i] += 5 * delta;
		}
	}
	return false;
};
export var mousePressed = function () {
	for (var [i, pt] of enumerate (pts)) {
		if (dist (mouseX, mouseY, pt [0], pt [1]) < 10) {
			dragged_pt = i;
			break;
		}
	}
};
export var mouseDragged = function () {
	if (dragged_pt >= 0) {
		pts [dragged_pt] = tuple ([mouseX, mouseY]);
	}
};
export var mouseReleased = function () {
	dragged_pt = -(1);
};
export var b_poly_arc_augmented = function (op_list, or_list) {
	var __left0__ = tuple ([list ([]), list ([]), or_list.__getslice__ (0, null, 1)]);
	var p_list = __left0__ [0];
	var r_list = __left0__ [1];
	var r2_list = __left0__ [2];
	for (var [i1, p1] of enumerate (op_list)) {
		var i2 = __mod__ (i1 + 1, len (op_list));
		var __left0__ = tuple ([op_list [i2], r2_list [i2], r2_list [i1]]);
		var p2 = __left0__ [0];
		var r2 = __left0__ [1];
		var r1 = __left0__ [2];
		if (dist (p1 [0], p1 [1], p2 [0], p2 [1]) > 1) {
			p_list.append (p1);
			r_list.append (r1);
		}
		else {
			r2_list [i2] = min (r1, r2);
		}
	}
	for (var [i1, p1] of enumerate (p_list)) {
		var i2 = __mod__ (i1 + 1, len (p_list));
		var __left0__ = tuple ([p_list [i2], r_list [i2], r_list [i1]]);
		var p2 = __left0__ [0];
		var r2 = __left0__ [1];
		var r1 = __left0__ [2];
		var __left0__ = reduce_radius (p1, p2, r1, r2);
		r_list [i1] = __left0__ [0];
		r_list [i2] = __left0__ [1];
	}
	var a_list = list ([]);
	for (var [i1, p1] of enumerate (p_list)) {
		var i2 = __mod__ (i1 + 1, len (p_list));
		var __left0__ = tuple ([p_list [i2], r_list [i2], r_list [i1]]);
		var p2 = __left0__ [0];
		var r2 = __left0__ [1];
		var r1 = __left0__ [2];
		var a = circ_circ_tangent (p1, p2, r1, r2);
		a_list.append (a);
	}
	beginShape ();
	for (var [i1, _] of enumerate (a_list)) {
		var i2 = __mod__ (i1 + 1, len (a_list));
		var __left0__ = tuple ([p_list [i1], p_list [i2], r_list [i1], r_list [i2]]);
		var p1 = __left0__ [0];
		var p2 = __left0__ [1];
		var r1 = __left0__ [2];
		var r2 = __left0__ [3];
		var __left0__ = a_list [i1];
		var a1 = __left0__ [0];
		var p11 = __left0__ [1];
		var p12 = __left0__ [2];
		var __left0__ = a_list [i2];
		var a2 = __left0__ [0];
		var p21 = __left0__ [1];
		var p22 = __left0__ [2];
		if (a1 && a2) {
			var start = (a1 < a2 ? a1 : a1 - TWO_PI);
			if (r2 < 0) {
				var a2 = a2 - TWO_PI;
			}
			b_arc (p2 [0], p2 [1], r2 * 2, r2 * 2, start, a2, 2);
		}
		else {
			if (a1) {
				vertex (p12 [0], p12 [1]);
			}
			if (a2) {
				vertex (p21 [0], p21 [1]);
			}
		}
	}
	endShape (CLOSE);
};
export var reduce_radius = function (p1, p2, r1, r2) {
	var d = dist (p1 [0], p1 [1], p2 [0], p2 [1]);
	var ri = abs (r1 - r2);
	if (d - ri < 0) {
		if (r1 > r2) {
			var r1 = map (d, ri + 1, 0, r1, r2);
		}
		else {
			var r2 = map (d, ri + 1, 0, r2, r1);
		}
	}
	return tuple ([r1, r2]);
};
export var circ_circ_tangent = function (p1, p2, r1, r2) {
	var d = dist (p1 [0], p1 [1], p2 [0], p2 [1]);
	var ri = r1 - r2;
	var line_angle = atan2 (p1 [0] - p2 [0], p2 [1] - p1 [1]);
	if (d - abs (ri) >= 0) {
		var theta = asin (ri / float (d));
		var x1 = -(cos (line_angle + theta)) * r1;
		var y1 = -(sin (line_angle + theta)) * r1;
		var x2 = -(cos (line_angle + theta)) * r2;
		var y2 = -(sin (line_angle + theta)) * r2;
		return tuple ([line_angle + theta, tuple ([p1 [0] - x1, p1 [1] - y1]), tuple ([p2 [0] - x2, p2 [1] - y2])]);
	}
	else {
		return tuple ([null, tuple ([p1 [0], p1 [1]]), tuple ([p2 [0], p2 [1]])]);
	}
};
export var b_arc = function (cx, cy, w, h, start_angle, end_angle, mode) {
	var theta = end_angle - start_angle;
	if (mode != 1 || abs (theta) < HALF_PI) {
		var x0 = cos (theta / 2.0);
		var y0 = sin (theta / 2.0);
		var x3 = x0;
		var y3 = 0 - y0;
		var x1 = (4.0 - x0) / 3.0;
		if (y0 != 0) {
			var y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0);
		}
		else {
			var y1 = 0;
		}
		var x2 = x1;
		var y2 = 0 - y1;
		var bezAng = start_angle + theta / 2.0;
		var cBezAng = cos (bezAng);
		var sBezAng = sin (bezAng);
		var rx0 = cBezAng * x0 - sBezAng * y0;
		var ry0 = sBezAng * x0 + cBezAng * y0;
		var rx1 = cBezAng * x1 - sBezAng * y1;
		var ry1 = sBezAng * x1 + cBezAng * y1;
		var rx2 = cBezAng * x2 - sBezAng * y2;
		var ry2 = sBezAng * x2 + cBezAng * y2;
		var rx3 = cBezAng * x3 - sBezAng * y3;
		var ry3 = sBezAng * x3 + cBezAng * y3;
		var __left0__ = tuple ([w / 2.0, h / 2.0]);
		var rx = __left0__ [0];
		var ry = __left0__ [1];
		var px0 = cx + rx * rx0;
		var py0 = cy + ry * ry0;
		var px1 = cx + rx * rx1;
		var py1 = cy + ry * ry1;
		var px2 = cx + rx * rx2;
		var py2 = cy + ry * ry2;
		var px3 = cx + rx * rx3;
		var py3 = cy + ry * ry3;
	}
	if (mode == 0) {
		beginShape ();
	}
	if (mode != 1) {
		vertex (px3, py3);
	}
	if (abs (theta) < HALF_PI) {
		bezierVertex (px2, py2, px1, py1, px0, py0);
	}
	else {
		b_arc (cx, cy, w, h, start_angle, end_angle - theta / 2.0, __kwargtrans__ ({mode: 1}));
		b_arc (cx, cy, w, h, start_angle + theta / 2.0, end_angle, __kwargtrans__ ({mode: 1}));
	}
	if (mode == 0) {
		endShape ();
	}
};
export var event_functions = dict ({'mousePressed': mousePressed, 'mouseDragged': mouseDragged, 'mouseReleased': mouseReleased, 'keyPressed': keyPressed});
start_p5 (setup, draw, event_functions);

//# sourceMappingURL=sketch_190606b.map