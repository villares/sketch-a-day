/**
 * @module Constants
 * @submodule Constants
 * @for p5
 */

var PI = Math.PI;

// module.exports = {
  // GRAPHICS RENDERER
  /**
   * @property {String} P2D
   * @final
   */
  var P2D= 'p2d';
  /**
   * @property {String} WEBGL
   * @final
   */
  var WEBGL= 'webgl';

  // ENVIRONMENT
  /**
   * @property {String} ARROW
   * @final
   */
  var ARROW= 'default';
  /**
   * @property {String} CROSS
   * @final
   */
  var CROSS= 'crosshair';
  /**
   * @property {String} HAND
   * @final
   */
  var HAND= 'pointer';
  /**
   * @property {String} MOVE
   * @final
   */
  var MOVE= 'move';
  /**
   * @property {String} TEXT
   * @final
   */
  var TEXT= 'text';
  /**
   * @property {String} WAIT
   * @final
   */
  var WAIT= 'wait';

  // TRIGONOMETRY

  /**
   * HALF_PI is a mathematical constant with the value
   * 1.57079632679489661923. It is half the ratio of the
   * circumference of a circle to its diameter. It is useful in
   * combination with the trigonometric functions <a href="#/p5/sin">sin()</a> and <a href="#/p5/cos">cos()</a>.
   *
   * @property {Number} HALF_PI
   * @final
   *
   * @example
   * <div><code>
   * arc(50; 50; 80; 80; 0; HALF_PI);
  var  * </code></div>
   *
   * @alt
   * 80x80 white quarter-circle with curve toward bottom right of canvas.
   *
   */
  var HALF_PI= PI / 2;
  /**
   * PI is a mathematical constant with the value
   * 3.14159265358979323846. It is the ratio of the circumference
   * of a circle to its diameter. It is useful in combination with
   * the trigonometric functions <a href="#/p5/sin">sin()</a> and <a href="#/p5/cos">cos()</a>.
   *
   * @property {Number} PI
   * @final
   *
   * @example
   * <div><code>
   * arc(50; 50; 80; 80; 0; PI);
  var  * </code></div>
   *
   * @alt
   * white half-circle with curve toward bottom of canvas.
   *
   */
  //var PI= PI;
  /**
   * QUARTER_PI is a mathematical constant with the value 0.7853982.
   * It is one quarter the ratio of the circumference of a circle to
   * its diameter. It is useful in combination with the trigonometric
   * functions <a href="#/p5/sin">sin()</a> and <a href="#/p5/cos">cos()</a>.
   *
   * @property {Number} QUARTER_PI
   * @final
   *
   * @example
   * <div><code>
   * arc(50; 50; 80; 80; 0; QUARTER_PI);
  var  * </code></div>
   *
   * @alt
   * white eighth-circle rotated about 40 degrees with curve bottom right canvas.
   *
   */
  var QUARTER_PI= PI / 4;
  /**
   * TAU is an alias for TWO_PI; a mathematical constant with the
   * value 6.28318530717958647693. It is twice the ratio of the
   * circumference of a circle to its diameter. It is useful in
   * combination with the trigonometric functions <a href="#/p5/sin">sin()</a> and <a href="#/p5/cos">cos()</a>.
   *
   * @property {Number} TAU
   * @final
   *
   * @example
   * <div><code>
   * arc(50; 50; 80; 80; 0; TAU);
  var  * </code></div>
   *
   * @alt
   * 80x80 white ellipse shape in center of canvas.
   *
   */
  var TAU= PI * 2;
  /**
   * TWO_PI is a mathematical constant with the value
   * 6.28318530717958647693. It is twice the ratio of the
   * circumference of a circle to its diameter. It is useful in
   * combination with the trigonometric functions <a href="#/p5/sin">sin()</a> and <a href="#/p5/cos">cos()</a>.
   *
   * @property {Number} TWO_PI
   * @final
   *
   * @example
   * <div><code>
   * arc(50; 50; 80; 80; 0; TWO_PI);
  var  * </code></div>
   *
   * @alt
   * 80x80 white ellipse shape in center of canvas.
   *
   */
  var TWO_PI= PI * 2;
  /**
   * Constant to be used with <a href="#/p5/angleMode">angleMode()</a> function; to set the mode which
   * p5.js interprates and calculates angles (either DEGREES or RADIANS).
   * @property {String} DEGREES
   * @final
   *
   * @example
   * <div class='norender'><code>
   * function setup() {
   *   angleMode(DEGREES);
  * }
   * </code></div>
   */
  var DEGREES= 'degrees';
  /**
   * Constant to be used with <a href="#/p5/angleMode">angleMode()</a> function; to set the mode which
   * p5.js interprates and calculates angles (either RADIANS or DEGREES).
   * @property {String} RADIANS
   * @final
   *
   * @example
   * <div class='norender'><code>
   * function setup() {
   *   angleMode(RADIANS);
  * }
   * </code></div>
   */
  var RADIANS= 'radians';
  var DEG_TO_RAD= PI / 180.0;
  var RAD_TO_DEG= 180.0 / PI;

  // SHAPE
  /**
   * @property {String} CORNER
   * @final
   */
  var CORNER= 'corner';
  /**
   * @property {String} CORNERS
   * @final
   */
  var CORNERS= 'corners';
  /**
   * @property {String} RADIUS
   * @final
   */
  var RADIUS= 'radius';
  /**
   * @property {String} RIGHT
   * @final
   */
  var RIGHT= 'right';
  /**
   * @property {String} LEFT
   * @final
   */
  var LEFT= 'left';
  /**
   * @property {String} CENTER
   * @final
   */
  var CENTER= 'center';
  /**
   * @property {String} TOP
   * @final
   */
  var TOP= 'top';
  /**
   * @property {String} BOTTOM
   * @final
   */
  var BOTTOM= 'bottom';
  /**
   * @property {String} BASELINE
   * @final
   * @default alphabetic
   */
  var BASELINE= 'alphabetic';
  /**
   * @property {Number} POINTS
   * @final
   * @default 0x0000
   */
  var POINTS= 0x0000;
  /**
   * @property {Number} LINES
   * @final
   * @default 0x0001
   */
  var LINES= 0x0001;
  /**
   * @property {Number} LINE_STRIP
   * @final
   * @default 0x0003
   */
  var LINE_STRIP= 0x0003;
  /**
   * @property {Number} LINE_LOOP
   * @final
   * @default 0x0002
   */
  var LINE_LOOP= 0x0002;
  /**
   * @property {Number} TRIANGLES
   * @final
   * @default 0x0004
   */
  var TRIANGLES= 0x0004;
  /**
   * @property {Number} TRIANGLE_FAN
   * @final
   * @default 0x0006
   */
  var TRIANGLE_FAN= 0x0006;
  /**
   * @property {Number} TRIANGLE_STRIP
   * @final
   * @default 0x0005
   */
  var TRIANGLE_STRIP= 0x0005;
  /**
   * @property {String} QUADS
   * @final
   */
  var QUADS= 'quads';
  /**
   * @property {String} QUAD_STRIP
   * @final
   * @default quad_strip
   */
  var QUAD_STRIP= 'quad_strip';
  /**
   * @property {String} CLOSE
   * @final
   */
  var CLOSE= 'close';
  /**
   * @property {String} OPEN
   * @final
   */
  var OPEN= 'open';
  /**
   * @property {String} CHORD
   * @final
   */
  var CHORD= 'chord';
  /**
   * @property {String} PIE
   * @final
   */
  var PIE= 'pie';
  /**
   * @property {String} PROJECT
   * @final
   * @default square
   */
  var PROJECT= 'square'; // PEND= careful this is counterintuitive
  /**
   * @property {String} SQUARE
   * @final
   * @default butt
   */
  var SQUARE= 'butt';
  /**
   * @property {String} ROUND
   * @final
   */
  var ROUND= 'round';
  /**
   * @property {String} BEVEL
   * @final
   */
  var BEVEL= 'bevel';
  /**
   * @property {String} MITER
   * @final
   */
  var MITER= 'miter';

  // COLOR
  /**
   * @property {String} RGB
   * @final
   */
  var RGB= 'rgb';
  /**
   * @property {String} HSB
   * @final
   */
  var HSB= 'hsb';
  /**
   * @property {String} HSL
   * @final
   */
  var HSL= 'hsl';

  // DOM EXTENSION
  /**
   * AUTO allows us to automatically set the width or height of an element (but not both);
  var  * based on the current height and width of the element. Only one parameter can
   * be passed to the <a href="/#/p5.Element/size">size</a> function as AUTO; at a time.
   *
   * @property {String} AUTO
   * @final
   */
  var AUTO= 'auto';

  // INPUT
  var ALT= 18;
  var BACKSPACE= 8;
  var CONTROL= 17;
  var DELETE= 46;
  var DOWN_ARROW= 40;
  var ENTER= 13;
  var ESCAPE= 27;
  var LEFT_ARROW= 37;
  var OPTION= 18;
  var RETURN= 13;
  var RIGHT_ARROW= 39;
  var SHIFT= 16;
  var TAB= 9;
  var UP_ARROW= 38;

  // RENDERING
  /**
   * @property {String} BLEND
   * @final
   * @default source-over
   */
  var BLEND= 'source-over';
  /**
   * @property {String} ADD
   * @final
   * @default lighter
   */
  var ADD= 'lighter';
  //ADD= 'add'; //
  //SUBTRACT= 'subtract'; //
  /**
   * @property {String} DARKEST
   * @final
   */
  var DARKEST= 'darken';
  /**
   * @property {String} LIGHTEST
   * @final
   * @default lighten
   */
  var LIGHTEST= 'lighten';
  /**
   * @property {String} DIFFERENCE
   * @final
   */
  var DIFFERENCE= 'difference';
  /**
   * @property {String} SUBTRACT
   * @final
   */
  var SUBTRACT= 'subtract';
  /**
   * @property {String} EXCLUSION
   * @final
   */
  var EXCLUSION= 'exclusion';
  /**
   * @property {String} MULTIPLY
   * @final
   */
  var MULTIPLY= 'multiply';
  /**
   * @property {String} SCREEN
   * @final
   */
  var SCREEN= 'screen';
  /**
   * @property {String} REPLACE
   * @final
   * @default copy
   */
  var REPLACE= 'copy';
  /**
   * @property {String} OVERLAY
   * @final
   */
  var OVERLAY= 'overlay';
  /**
   * @property {String} HARD_LIGHT
   * @final
   */
  var HARD_LIGHT= 'hard-light';
  /**
   * @property {String} SOFT_LIGHT
   * @final
   */
  var SOFT_LIGHT= 'soft-light';
  /**
   * @property {String} DODGE
   * @final
   * @default color-dodge
   */
  var DODGE= 'color-dodge';
  /**
   * @property {String} BURN
   * @final
   * @default color-burn
   */
  var BURN= 'color-burn';

  // FILTERS
  /**
   * @property {String} THRESHOLD
   * @final
   */
  var THRESHOLD= 'threshold';
  /**
   * @property {String} GRAY
   * @final
   */
  var GRAY= 'gray';
  /**
   * @property {String} OPAQUE
   * @final
   */
  var OPAQUE= 'opaque';
  /**
   * @property {String} INVERT
   * @final
   */
  var INVERT= 'invert';
  /**
   * @property {String} POSTERIZE
   * @final
   */
  var POSTERIZE= 'posterize';
  /**
   * @property {String} DILATE
   * @final
   */
  var DILATE= 'dilate';
  /**
   * @property {String} ERODE
   * @final
   */
  var ERODE= 'erode';
  /**
   * @property {String} BLUR
   * @final
   */
  var BLUR= 'blur';

  // TYPOGRAPHY
  /**
   * @property {String} NORMAL
   * @final
   */
  var NORMAL= 'normal';
  /**
   * @property {String} ITALIC
   * @final
   */
  var ITALIC= 'italic';
  /**
   * @property {String} BOLD
   * @final
   */
  var BOLD= 'bold';
  /**
   * @property {String} BOLDITALIC
   * @final
   */
  var BOLDITALIC= 'bold italic';

  // TYPOGRAPHY-INTERNAL
  var _DEFAULT_TEXT_FILL= '#000000';
  var _DEFAULT_LEADMULT= 1.25;
  var _CTX_MIDDLE= 'middle';

  // VERTICES
  var LINEAR= 'linear';
  var QUADRATIC= 'quadratic';
  var BEZIER= 'bezier';
  var CURVE= 'curve';

  // WEBGL DRAWMODES
  var STROKE= 'stroke';
  var FILL= 'fill';
  var TEXTURE= 'texture';
  var IMMEDIATE= 'immediate';

  // WEBGL TEXTURE MODE
  // NORMAL already exists for typography
  /**
   * @property {String} IMAGE
   * @final
   */
  var IMAGE= 'image';

  // WEBGL TEXTURE WRAP AND FILTERING
  // LINEAR already exists above
  var NEAREST= 'nearest';
  var REPEAT= 'repeat';
  var CLAMP= 'clamp';
  var MIRROR= 'mirror';

  // DEVICE-ORIENTATION
  /**
   * @property {String} LANDSCAPE
   * @final
   */
  var LANDSCAPE= 'landscape';
  /**
   * @property {String} PORTRAIT
   * @final
   */
  var PORTRAIT= 'portrait';

  // DEFAULTS
  var _DEFAULT_STROKE= '#000000';
  var _DEFAULT_FILL= '#FFFFFF';

  /**
   * @property {String} GRID
   * @final
   */
  var GRID= 'grid';

  /**
   * @property {String} AXES
   * @final
   */
  var AXES= 'axes'

