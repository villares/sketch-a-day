// Transcrypt'ed from Python, 2019-05-04 23:51:19
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, input, isinstance, issubclass, len, list, object, ord, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {CLOSE, DEGREES, HALF_PI, PI, QUARTER_PI, RADIANS, TAU, TWO_PI, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createCamera, createCanvas, createGraphics, createImage, createNumberDict, createShader, createStringDict, createVector, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceMoved, deviceOrientation, deviceShaken, deviceTurned, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, doubleClicked, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, int, join, key, keyCode, keyIsDown, keyIsPressed, keyPressed, keyReleased, keyTyped, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseClicked, mouseDragged, mouseIsPressed, mouseMoved, mousePressed, mouseReleased, mouseWheel, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, print, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touchEnded, touchMoved, touchStarted, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowResized, windowWidth, year} from './pytop5js.js';
var __name__ = '__main__';
export var setup = function () {
	createCanvas (400, 400);
	colorMode (_P5_INSTANCE.HSB, 255, 255, 255);
	frameRate (30);
	strokeWeight (2);
};
export var draw = function () {
	background (200);
	var r = 125;
	var __left0__ = tuple ([150, 200]);
	var x1 = __left0__ [0];
	var y1 = __left0__ [1];
	var __left0__ = tuple ([250, 200]);
	var x2 = __left0__ [0];
	var y2 = __left0__ [1];
	for (var i = 0; i < 128; i++) {
		stroke (i * 2, 200, 200);
		var a1 = (i * TWO_PI) / 128 + HALF_PI;
		var sx1 = x1 + (sin (a1) * r) * cos (frameCount / 50.0);
		var sy1 = y1 + (cos (a1) * r) * sin (frameCount / 77.0);
		var a2 = (i * TWO_PI) / 128 + QUARTER_PI;
		var sx2 = x2 + (cos (a2) * r) * sin (frameCount / 141.0);
		var sy2 = y2 + (sin (a2) * r) * cos (frameCount / 30.0);
		line (sx1, sy1, sx2, sy2);
	}
};
start_p5 (setup, draw);

//# sourceMappingURL=sketch_190504a.map