// Transcrypt'ed from Python, 2019-10-25 23:33:08
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, isinstance, issubclass, len, list, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
var __name__ = 'pyp5js';
export var _P5_INSTANCE = null;
export var _CTX_MIDDLE = null;
export var _DEFAULT_FILL = null;
export var _DEFAULT_LEADMULT = null;
export var _DEFAULT_STROKE = null;
export var _DEFAULT_TEXT_FILL = null;
export var ADD = null;
export var ALT = null;
export var ARROW = null;
export var AUTO = null;
export var AXES = null;
export var BACKSPACE = null;
export var BASELINE = null;
export var BEVEL = null;
export var BEZIER = null;
export var BLEND = null;
export var BLUR = null;
export var BOLD = null;
export var BOLDITALIC = null;
export var BOTTOM = null;
export var BURN = null;
export var CENTER = null;
export var CHORD = null;
export var CLAMP = null;
export var CLOSE = null;
export var CONTROL = null;
export var CORNER = null;
export var CORNERS = null;
export var CROSS = null;
export var CURVE = null;
export var DARKEST = null;
export var DEG_TO_RAD = null;
export var DEGREES = null;
export var DELETE = null;
export var DIFFERENCE = null;
export var DILATE = null;
export var DODGE = null;
export var DOWN_ARROW = null;
export var ENTER = null;
export var ERODE = null;
export var ESCAPE = null;
export var EXCLUSION = null;
export var FILL = null;
export var GRAY = null;
export var GRID = null;
export var HALF_PI = null;
export var HAND = null;
export var HARD_LIGHT = null;
export var HSB = null;
export var HSL = null;
export var IMAGE = null;
export var IMMEDIATE = null;
export var INVERT = null;
export var ITALIC = null;
export var LANDSCAPE = null;
export var LEFT = null;
export var LEFT_ARROW = null;
export var LIGHTEST = null;
export var LINE_LOOP = null;
export var LINE_STRIP = null;
export var LINEAR = null;
export var LINES = null;
export var MIRROR = null;
export var MITER = null;
export var MOVE = null;
export var MULTIPLY = null;
export var NEAREST = null;
export var NORMAL = null;
export var OPAQUE = null;
export var OPEN = null;
export var OPTION = null;
export var OVERLAY = null;
export var PI = null;
export var PIE = null;
export var POINTS = null;
export var PORTRAIT = null;
export var POSTERIZE = null;
export var PROJECT = null;
export var QUAD_STRIP = null;
export var QUADRATIC = null;
export var QUADS = null;
export var QUARTER_PI = null;
export var RAD_TO_DEG = null;
export var RADIANS = null;
export var RADIUS = null;
export var REPEAT = null;
export var REPLACE = null;
export var RETURN = null;
export var RGB = null;
export var RIGHT = null;
export var RIGHT_ARROW = null;
export var ROUND = null;
export var SCREEN = null;
export var SHIFT = null;
export var SOFT_LIGHT = null;
export var SQUARE = null;
export var STROKE = null;
export var SUBTRACT = null;
export var TAB = null;
export var TAU = null;
export var TEXT = null;
export var TEXTURE = null;
export var THRESHOLD = null;
export var TOP = null;
export var TRIANGLE_FAN = null;
export var TRIANGLE_STRIP = null;
export var TRIANGLES = null;
export var TWO_PI = null;
export var UP_ARROW = null;
export var WAIT = null;
export var WEBGL = null;
export var P2D = null;
var PI = null;
export var frameCount = null;
export var focused = null;
export var displayWidth = null;
export var displayHeight = null;
export var windowWidth = null;
export var windowHeight = null;
export var width = null;
export var height = null;
export var disableFriendlyErrors = null;
export var deviceOrientation = null;
export var accelerationX = null;
export var accelerationY = null;
export var accelerationZ = null;
export var pAccelerationX = null;
export var pAccelerationY = null;
export var pAccelerationZ = null;
export var rotationX = null;
export var rotationY = null;
export var rotationZ = null;
export var pRotationX = null;
export var pRotationY = null;
export var pRotationZ = null;
export var turnAxis = null;
export var keyIsPressed = null;
export var key = null;
export var keyCode = null;
export var mouseX = null;
export var mouseY = null;
export var pmouseX = null;
export var pmouseY = null;
export var winMouseX = null;
export var winMouseY = null;
export var pwinMouseX = null;
export var pwinMouseY = null;
export var mouseButton = null;
export var mouseIsPressed = null;
export var touches = null;
export var pixels = null;
export var VIDEO = null;
export var AUDIO = null;
export var alpha = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.alpha (...args);
};
export var blue = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.blue (...args);
};
export var brightness = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.brightness (...args);
};
export var color = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.color (...args);
};
export var green = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.green (...args);
};
export var hue = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.hue (...args);
};
export var lerpColor = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.lerpColor (...args);
};
export var lightness = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.lightness (...args);
};
export var red = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.red (...args);
};
export var saturation = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saturation (...args);
};
export var background = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.background (...args);
};
export var py_clear = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.py_clear (...args);
};
export var colorMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.colorMode (...args);
};
export var fill = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.fill (...args);
};
export var noFill = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noFill (...args);
};
export var noStroke = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noStroke (...args);
};
export var stroke = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.stroke (...args);
};
export var arc = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.arc (...args);
};
export var ellipse = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ellipse (...args);
};
export var circle = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.circle (...args);
};
export var line = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.line (...args);
};
export var point = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.point (...args);
};
export var quad = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.quad (...args);
};
export var rect = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rect (...args);
};
export var square = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.square (...args);
};
export var triangle = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.triangle (...args);
};
export var plane = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.plane (...args);
};
export var box = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.box (...args);
};
export var sphere = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.sphere (...args);
};
export var cylinder = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.cylinder (...args);
};
export var cone = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.cone (...args);
};
export var ellipsoid = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ellipsoid (...args);
};
export var torus = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.torus (...args);
};
export var loadModel = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadModel (...args);
};
export var model = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.model (...args);
};
export var ellipseMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ellipseMode (...args);
};
export var noSmooth = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noSmooth (...args);
};
export var rectMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rectMode (...args);
};
export var smooth = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.smooth (...args);
};
export var strokeCap = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.strokeCap (...args);
};
export var strokeJoin = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.strokeJoin (...args);
};
export var strokeWeight = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.strokeWeight (...args);
};
export var bezier = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.bezier (...args);
};
export var bezierDetail = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.bezierDetail (...args);
};
export var bezierPoint = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.bezierPoint (...args);
};
export var bezierTangent = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.bezierTangent (...args);
};
export var curve = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curve (...args);
};
export var curveDetail = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curveDetail (...args);
};
export var curveTightness = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curveTightness (...args);
};
export var curvePoint = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curvePoint (...args);
};
export var curveTangent = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curveTangent (...args);
};
export var beginContour = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.beginContour (...args);
};
export var beginShape = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.beginShape (...args);
};
export var bezierVertex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.bezierVertex (...args);
};
export var curveVertex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.curveVertex (...args);
};
export var endContour = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.endContour (...args);
};
export var endShape = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.endShape (...args);
};
export var quadraticVertex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.quadraticVertex (...args);
};
export var vertex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.vertex (...args);
};
export var cursor = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.cursor (...args);
};
export var frameRate = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.frameRate (...args);
};
export var noCursor = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noCursor (...args);
};
export var fullscreen = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.fullscreen (...args);
};
export var pixelDensity = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.pixelDensity (...args);
};
export var displayDensity = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.displayDensity (...args);
};
export var getURL = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.getURL (...args);
};
export var getURLPath = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.getURLPath (...args);
};
export var getURLParams = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.getURLParams (...args);
};
export var preload = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.preload (...args);
};
export var setup = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.setup (...args);
};
export var draw = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.draw (...args);
};
export var remove = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.remove (...args);
};
export var noLoop = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noLoop (...args);
};
export var loop = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loop (...args);
};
export var push = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.push (...args);
};
export var redraw = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.redraw (...args);
};
export var resizeCanvas = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.resizeCanvas (...args);
};
export var noCanvas = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noCanvas (...args);
};
export var createGraphics = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createGraphics (...args);
};
export var blendMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.blendMode (...args);
};
export var setAttributes = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.setAttributes (...args);
};
export var applyMatrix = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.applyMatrix (...args);
};
export var resetMatrix = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.resetMatrix (...args);
};
export var rotate = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rotate (...args);
};
export var rotateX = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rotateX (...args);
};
export var rotateY = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rotateY (...args);
};
export var rotateZ = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.rotateZ (...args);
};
export var scale = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.scale (...args);
};
export var shearX = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shearX (...args);
};
export var shearY = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shearY (...args);
};
export var translate = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.translate (...args);
};
export var createStringDict = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createStringDict (...args);
};
export var createNumberDict = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createNumberDict (...args);
};
export var append = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.append (...args);
};
export var arrayCopy = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.arrayCopy (...args);
};
export var concat = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.concat (...args);
};
export var reverse = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.reverse (...args);
};
export var shorten = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shorten (...args);
};
export var shuffle = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shuffle (...args);
};
export var py_sort = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.py_sort (...args);
};
export var splice = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.splice (...args);
};
export var subset = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.subset (...args);
};
export var float = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.float (...args);
};
export var int = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.int (...args);
};
export var str = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.str (...args);
};
export var boolean = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.boolean (...args);
};
export var byte = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.byte (...args);
};
export var char = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.char (...args);
};
export var unchar = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.unchar (...args);
};
export var hex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.hex (...args);
};
export var unhex = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.unhex (...args);
};
export var join = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.join (...args);
};
export var match = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.match (...args);
};
export var matchAll = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.matchAll (...args);
};
export var nf = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.nf (...args);
};
export var nfc = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.nfc (...args);
};
export var nfp = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.nfp (...args);
};
export var nfs = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.nfs (...args);
};
export var py_split = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.py_split (...args);
};
export var splitTokens = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.splitTokens (...args);
};
export var trim = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.trim (...args);
};
export var setMoveThreshold = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.setMoveThreshold (...args);
};
export var setShakeThreshold = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.setShakeThreshold (...args);
};
export var keyIsDown = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.keyIsDown (...args);
};
export var createImage = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createImage (...args);
};
export var saveCanvas = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saveCanvas (...args);
};
export var saveFrames = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saveFrames (...args);
};
export var loadImage = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadImage (...args);
};
export var image = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.image (...args);
};
export var tint = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.tint (...args);
};
export var noTint = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noTint (...args);
};
export var imageMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.imageMode (...args);
};
export var blend = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.blend (...args);
};
export var copy = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.copy (...args);
};
export var filter = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.filter (...args);
};
export var py_get = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.py_get (...args);
};
export var loadPixels = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadPixels (...args);
};
export var set = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.set (...args);
};
export var updatePixels = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.updatePixels (...args);
};
export var loadJSON = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadJSON (...args);
};
export var loadStrings = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadStrings (...args);
};
export var loadTable = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadTable (...args);
};
export var loadXML = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadXML (...args);
};
export var loadBytes = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadBytes (...args);
};
export var httpGet = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.httpGet (...args);
};
export var httpPost = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.httpPost (...args);
};
export var httpDo = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.httpDo (...args);
};
export var createWriter = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createWriter (...args);
};
export var save = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.save (...args);
};
export var saveJSON = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saveJSON (...args);
};
export var saveStrings = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saveStrings (...args);
};
export var saveTable = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.saveTable (...args);
};
export var day = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.day (...args);
};
export var hour = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.hour (...args);
};
export var minute = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.minute (...args);
};
export var millis = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.millis (...args);
};
export var month = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.month (...args);
};
export var second = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.second (...args);
};
export var year = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.year (...args);
};
export var createVector = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createVector (...args);
};
export var abs = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.abs (...args);
};
export var ceil = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ceil (...args);
};
export var constrain = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.constrain (...args);
};
export var dist = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.dist (...args);
};
export var exp = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.exp (...args);
};
export var floor = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.floor (...args);
};
export var lerp = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.lerp (...args);
};
export var log = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.log (...args);
};
export var mag = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.mag (...args);
};
export var map = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.map (...args);
};
export var max = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.max (...args);
};
export var min = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.min (...args);
};
export var norm = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.norm (...args);
};
export var pow = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.pow (...args);
};
export var round = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.round (...args);
};
export var sq = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.sq (...args);
};
export var sqrt = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.sqrt (...args);
};
export var noise = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noise (...args);
};
export var noiseDetail = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noiseDetail (...args);
};
export var noiseSeed = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noiseSeed (...args);
};
export var randomSeed = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.randomSeed (...args);
};
export var random = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.random (...args);
};
export var randomGaussian = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.randomGaussian (...args);
};
export var acos = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.acos (...args);
};
export var asin = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.asin (...args);
};
export var atan = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.atan (...args);
};
export var atan2 = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.atan2 (...args);
};
export var cos = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.cos (...args);
};
export var sin = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.sin (...args);
};
export var tan = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.tan (...args);
};
export var degrees = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.degrees (...args);
};
export var radians = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.radians (...args);
};
export var angleMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.angleMode (...args);
};
export var textAlign = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textAlign (...args);
};
export var textLeading = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textLeading (...args);
};
export var textSize = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textSize (...args);
};
export var textStyle = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textStyle (...args);
};
export var textWidth = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textWidth (...args);
};
export var textAscent = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textAscent (...args);
};
export var textDescent = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textDescent (...args);
};
export var loadFont = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadFont (...args);
};
export var text = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.text (...args);
};
export var textFont = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textFont (...args);
};
export var orbitControl = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.orbitControl (...args);
};
export var debugMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.debugMode (...args);
};
export var noDebugMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.noDebugMode (...args);
};
export var ambientLight = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ambientLight (...args);
};
export var directionalLight = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.directionalLight (...args);
};
export var pointLight = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.pointLight (...args);
};
export var lights = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.lights (...args);
};
export var loadShader = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.loadShader (...args);
};
export var createShader = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createShader (...args);
};
export var shader = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shader (...args);
};
export var resetShader = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.resetShader (...args);
};
export var normalMaterial = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.normalMaterial (...args);
};
export var texture = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.texture (...args);
};
export var textureMode = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textureMode (...args);
};
export var textureWrap = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.textureWrap (...args);
};
export var ambientMaterial = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ambientMaterial (...args);
};
export var specularMaterial = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.specularMaterial (...args);
};
export var shininess = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.shininess (...args);
};
export var camera = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.camera (...args);
};
export var perspective = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.perspective (...args);
};
export var ortho = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.ortho (...args);
};
export var createCamera = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createCamera (...args);
};
export var setCamera = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.setCamera (...args);
};
export var select = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.select (...args);
};
export var selectAll = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.selectAll (...args);
};
export var removeElements = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.removeElements (...args);
};
export var changed = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.changed (...args);
};
export var input = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.input (...args);
};
export var createDiv = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createDiv (...args);
};
export var createP = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createP (...args);
};
export var createSpan = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createSpan (...args);
};
export var createImg = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createImg (...args);
};
export var createA = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createA (...args);
};
export var createSlider = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createSlider (...args);
};
export var createButton = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createButton (...args);
};
export var createCheckbox = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createCheckbox (...args);
};
export var createSelect = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createSelect (...args);
};
export var createRadio = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createRadio (...args);
};
export var createColorPicker = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createColorPicker (...args);
};
export var createInput = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createInput (...args);
};
export var createFileInput = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createFileInput (...args);
};
export var createVideo = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createVideo (...args);
};
export var createAudio = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createAudio (...args);
};
export var createCapture = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createCapture (...args);
};
export var createElement = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	return _P5_INSTANCE.createElement (...args);
};
export var createCanvas = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	var result = _P5_INSTANCE.createCanvas (...args);
	width = _P5_INSTANCE.width;
	height = _P5_INSTANCE.height;
};
export var py_pop = function () {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
			}
		}
		var args = tuple ([].slice.apply (arguments).slice (0, __ilastarg0__ + 1));
	}
	else {
		var args = tuple ();
	}
	var p5_pop = _P5_INSTANCE.pop (...args);
	return p5_pop;
};
export var pre_draw = function (p5_instance, draw_func) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'p5_instance': var p5_instance = __allkwargs0__ [__attrib0__]; break;
					case 'draw_func': var draw_func = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	_CTX_MIDDLE = p5_instance._CTX_MIDDLE;
	_DEFAULT_FILL = p5_instance._DEFAULT_FILL;
	_DEFAULT_LEADMULT = p5_instance._DEFAULT_LEADMULT;
	_DEFAULT_STROKE = p5_instance._DEFAULT_STROKE;
	_DEFAULT_TEXT_FILL = p5_instance._DEFAULT_TEXT_FILL;
	ADD = p5_instance.ADD;
	ALT = p5_instance.ALT;
	ARROW = p5_instance.ARROW;
	AUTO = p5_instance.AUTO;
	AXES = p5_instance.AXES;
	BACKSPACE = p5_instance.BACKSPACE;
	BASELINE = p5_instance.BASELINE;
	BEVEL = p5_instance.BEVEL;
	BEZIER = p5_instance.BEZIER;
	BLEND = p5_instance.BLEND;
	BLUR = p5_instance.BLUR;
	BOLD = p5_instance.BOLD;
	BOLDITALIC = p5_instance.BOLDITALIC;
	BOTTOM = p5_instance.BOTTOM;
	BURN = p5_instance.BURN;
	CENTER = p5_instance.CENTER;
	CHORD = p5_instance.CHORD;
	CLAMP = p5_instance.CLAMP;
	CLOSE = p5_instance.CLOSE;
	CONTROL = p5_instance.CONTROL;
	CORNER = p5_instance.CORNER;
	CORNERS = p5_instance.CORNERS;
	CROSS = p5_instance.CROSS;
	CURVE = p5_instance.CURVE;
	DARKEST = p5_instance.DARKEST;
	DEG_TO_RAD = p5_instance.DEG_TO_RAD;
	DEGREES = p5_instance.DEGREES;
	DELETE = p5_instance.DELETE;
	DIFFERENCE = p5_instance.DIFFERENCE;
	DILATE = p5_instance.DILATE;
	DODGE = p5_instance.DODGE;
	DOWN_ARROW = p5_instance.DOWN_ARROW;
	ENTER = p5_instance.ENTER;
	ERODE = p5_instance.ERODE;
	ESCAPE = p5_instance.ESCAPE;
	EXCLUSION = p5_instance.EXCLUSION;
	FILL = p5_instance.FILL;
	GRAY = p5_instance.GRAY;
	GRID = p5_instance.GRID;
	HALF_PI = p5_instance.HALF_PI;
	HAND = p5_instance.HAND;
	HARD_LIGHT = p5_instance.HARD_LIGHT;
	HSB = p5_instance.HSB;
	HSL = p5_instance.HSL;
	IMAGE = p5_instance.IMAGE;
	IMMEDIATE = p5_instance.IMMEDIATE;
	INVERT = p5_instance.INVERT;
	ITALIC = p5_instance.ITALIC;
	LANDSCAPE = p5_instance.LANDSCAPE;
	LEFT = p5_instance.LEFT;
	LEFT_ARROW = p5_instance.LEFT_ARROW;
	LIGHTEST = p5_instance.LIGHTEST;
	LINE_LOOP = p5_instance.LINE_LOOP;
	LINE_STRIP = p5_instance.LINE_STRIP;
	LINEAR = p5_instance.LINEAR;
	LINES = p5_instance.LINES;
	MIRROR = p5_instance.MIRROR;
	MITER = p5_instance.MITER;
	MOVE = p5_instance.MOVE;
	MULTIPLY = p5_instance.MULTIPLY;
	NEAREST = p5_instance.NEAREST;
	NORMAL = p5_instance.NORMAL;
	OPAQUE = p5_instance.OPAQUE;
	OPEN = p5_instance.OPEN;
	OPTION = p5_instance.OPTION;
	OVERLAY = p5_instance.OVERLAY;
	PI = p5_instance.PI;
	PIE = p5_instance.PIE;
	POINTS = p5_instance.POINTS;
	PORTRAIT = p5_instance.PORTRAIT;
	POSTERIZE = p5_instance.POSTERIZE;
	PROJECT = p5_instance.PROJECT;
	QUAD_STRIP = p5_instance.QUAD_STRIP;
	QUADRATIC = p5_instance.QUADRATIC;
	QUADS = p5_instance.QUADS;
	QUARTER_PI = p5_instance.QUARTER_PI;
	RAD_TO_DEG = p5_instance.RAD_TO_DEG;
	RADIANS = p5_instance.RADIANS;
	RADIUS = p5_instance.RADIUS;
	REPEAT = p5_instance.REPEAT;
	REPLACE = p5_instance.REPLACE;
	RETURN = p5_instance.RETURN;
	RGB = p5_instance.RGB;
	RIGHT = p5_instance.RIGHT;
	RIGHT_ARROW = p5_instance.RIGHT_ARROW;
	ROUND = p5_instance.ROUND;
	SCREEN = p5_instance.SCREEN;
	SHIFT = p5_instance.SHIFT;
	SOFT_LIGHT = p5_instance.SOFT_LIGHT;
	SQUARE = p5_instance.SQUARE;
	STROKE = p5_instance.STROKE;
	SUBTRACT = p5_instance.SUBTRACT;
	TAB = p5_instance.TAB;
	TAU = p5_instance.TAU;
	TEXT = p5_instance.TEXT;
	TEXTURE = p5_instance.TEXTURE;
	THRESHOLD = p5_instance.THRESHOLD;
	TOP = p5_instance.TOP;
	TRIANGLE_FAN = p5_instance.TRIANGLE_FAN;
	TRIANGLE_STRIP = p5_instance.TRIANGLE_STRIP;
	TRIANGLES = p5_instance.TRIANGLES;
	TWO_PI = p5_instance.TWO_PI;
	UP_ARROW = p5_instance.UP_ARROW;
	WAIT = p5_instance.WAIT;
	WEBGL = p5_instance.WEBGL;
	P2D = p5_instance.P2D;
	PI = p5_instance.PI;
	frameCount = p5_instance.frameCount;
	focused = p5_instance.focused;
	displayWidth = p5_instance.displayWidth;
	displayHeight = p5_instance.displayHeight;
	windowWidth = p5_instance.windowWidth;
	windowHeight = p5_instance.windowHeight;
	width = p5_instance.width;
	height = p5_instance.height;
	disableFriendlyErrors = p5_instance.disableFriendlyErrors;
	deviceOrientation = p5_instance.deviceOrientation;
	accelerationX = p5_instance.accelerationX;
	accelerationY = p5_instance.accelerationY;
	accelerationZ = p5_instance.accelerationZ;
	pAccelerationX = p5_instance.pAccelerationX;
	pAccelerationY = p5_instance.pAccelerationY;
	pAccelerationZ = p5_instance.pAccelerationZ;
	rotationX = p5_instance.rotationX;
	rotationY = p5_instance.rotationY;
	rotationZ = p5_instance.rotationZ;
	pRotationX = p5_instance.pRotationX;
	pRotationY = p5_instance.pRotationY;
	pRotationZ = p5_instance.pRotationZ;
	turnAxis = p5_instance.turnAxis;
	keyIsPressed = p5_instance.keyIsPressed;
	key = p5_instance.key;
	keyCode = p5_instance.keyCode;
	mouseX = p5_instance.mouseX;
	mouseY = p5_instance.mouseY;
	pmouseX = p5_instance.pmouseX;
	pmouseY = p5_instance.pmouseY;
	winMouseX = p5_instance.winMouseX;
	winMouseY = p5_instance.winMouseY;
	pwinMouseX = p5_instance.pwinMouseX;
	pwinMouseY = p5_instance.pwinMouseY;
	mouseButton = p5_instance.mouseButton;
	mouseIsPressed = p5_instance.mouseIsPressed;
	touches = p5_instance.touches;
	pixels = p5_instance.pixels;
	VIDEO = p5_instance.VIDEO;
	AUDIO = p5_instance.AUDIO;
	return draw_func ();
};
export var global_p5_injection = function (p5_sketch) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'p5_sketch': var p5_sketch = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var decorator = function (f) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'f': var f = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		var wrapper = function () {
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
			_P5_INSTANCE = p5_sketch;
			return pre_draw (_P5_INSTANCE, f);
		};
		return wrapper;
	};
	return decorator;
};
export var start_p5 = function (setup_func, draw_func, event_functions) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'setup_func': var setup_func = __allkwargs0__ [__attrib0__]; break;
					case 'draw_func': var draw_func = __allkwargs0__ [__attrib0__]; break;
					case 'event_functions': var event_functions = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var sketch_setup = function (p5_sketch) {
		if (arguments.length) {
			var __ilastarg0__ = arguments.length - 1;
			if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
				var __allkwargs0__ = arguments [__ilastarg0__--];
				for (var __attrib0__ in __allkwargs0__) {
					switch (__attrib0__) {
						case 'p5_sketch': var p5_sketch = __allkwargs0__ [__attrib0__]; break;
					}
				}
			}
		}
		else {
		}
		p5_sketch.setup = global_p5_injection (p5_sketch) (setup_func);
		p5_sketch.draw = global_p5_injection (p5_sketch) (draw_func);
	};
	var instance = new p5 (sketch_setup, 'sketch-holder');
	var event_function_names = list (['deviceMoved', 'deviceTurned', 'deviceShaken', 'keyPressed', 'keyReleased', 'keyTyped', 'mouseMoved', 'mouseDragged', 'mousePressed', 'mouseReleased', 'mouseClicked', 'doubleClicked', 'mouseWheel', 'touchStarted', 'touchMoved', 'touchEnded', 'windowResized']);
	for (var f_name of (function () {
		var __accu0__ = [];
		for (var f of event_function_names) {
			if (event_functions.py_get (f, null)) {
				__accu0__.append (f);
			}
		}
		return __accu0__;
	}) ()) {
		var func = event_functions [f_name];
		var event_func = global_p5_injection (instance) (func);
		setattr (instance, f_name, event_func);
	}
};
export var logOnloaded = function () {
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
	console.log ('Lib loaded!');
};
export var add_library = function (lib_name) {
	if (arguments.length) {
		var __ilastarg0__ = arguments.length - 1;
		if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
			var __allkwargs0__ = arguments [__ilastarg0__--];
			for (var __attrib0__ in __allkwargs0__) {
				switch (__attrib0__) {
					case 'lib_name': var lib_name = __allkwargs0__ [__attrib0__]; break;
				}
			}
		}
	}
	else {
	}
	var src = '';
	if (lib_name == 'p5.dom.js') {
		var src = 'static/p5.dom.js';
	}
	else {
		console.log ('Lib name is not valid: ' + lib_name);
		return ;
	}
	console.log ('Importing: ' + src);
	var script = document.createElement ('script');
	script.onload = logOnloaded;
	script.src = src;
	document.head.appendChild (script);
};

//# sourceMappingURL=pyp5js.map