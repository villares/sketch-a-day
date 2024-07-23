// Transcrypt'ed from Python, 2019-05-06 22:22:55
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {BOTTOM, CENTER, CLOSE, CMYK, DEGREES, HALF_PI, HSB, LEFT, PI, QUARTER_PI, RADIANS, RGB, RIGHT, SHIFT, TAU, TOP, TWO_PI, WEBGL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceMoved, deviceOrientation, deviceShaken, deviceTurned, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, doubleClicked, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, keyPressed, keyReleased, keyTyped, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseClicked, mouseDragged, mouseIsPressed, mouseMoved, mousePressed, mouseReleased, mouseWheel, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touchEnded, touchMoved, touchStarted, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowResized, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
var __left0__ = 1;
export var w = __left0__;
export var h = __left0__;
export var d = __left0__;
export var max_w = 200;
export var max_h = 200;
export var max_d = 200;
export var pausa = 100;
export var setup = function () {
	createCanvas (500, 500, WEBGL);
	noFill ();
	strokeWeight (5);
};
export var draw = function () {
	background (200);
	rotateX ((d - 1) / 100.0);
	rotateZ ((d - 1) / 100.0);
	box (h, w, d);
	if (w < max_w) {
		if (frameCount > pausa) {
			w++;
		}
	}
	else if (h < max_h) {
		if (frameCount > 2 * pausa + max_w) {
			h++;
		}
	}
	else if (d < max_d) {
		if (frameCount > (3 * pausa + max_w) + max_h) {
			d++;
		}
	}
	else {
		noLoop ();
	}
};
start_p5 (setup, draw);

//# sourceMappingURL=sketch_190505b.map