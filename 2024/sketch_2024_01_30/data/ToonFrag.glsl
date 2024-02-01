#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

varying vec3 vertNormal;
varying vec3 vertLightDir;

void main() {  
  float intensity;
  vec4 color;
  intensity = max(0.0, dot(vertLightDir, vertNormal));

  if (intensity > 0.95) {
    color = vec4(1.0, 0.5, 0.5, 1.0);
  } else if (intensity > 0.5) {
    color = vec4(0.6, 0.35, 0.35, 1.0);
  } else if (intensity > 0.25) {
    color = vec4(0.4, 0.25, 0.25, 1.0);
  } else {
    color = vec4(0.2, 0.15, 0.15, 1.0);
  }

  gl_FragColor = color;  
}