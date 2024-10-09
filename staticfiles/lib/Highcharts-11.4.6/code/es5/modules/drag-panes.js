!/**
 * Highstock JS v11.4.6 (2024-07-08)
 *
 * Drag-panes module
 *
 * (c) 2010-2024 Highsoft AS
 * Author: Kacper Madej
 *
 * License: www.highcharts.com/license
 */function(e){"object"==typeof module&&module.exports?(e.default=e,module.exports=e):"function"==typeof define&&define.amd?define("highcharts/modules/drag-panes",["highcharts","highcharts/modules/stock"],function(t){return e(t),e.Highcharts=t,e}):e("undefined"!=typeof Highcharts?Highcharts:void 0)}(function(e){"use strict";var t=e?e._modules:{};function s(t,s,i,n){t.hasOwnProperty(s)||(t[s]=n.apply(null,i),"function"==typeof CustomEvent&&e.win.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:s,module:t[s]}})))}s(t,"Extensions/DragPanes/AxisResizerDefaults.js",[],function(){return{minLength:"10%",maxLength:"100%",resize:{controlledAxis:{next:[],prev:[]},enabled:!1,cursor:"ns-resize",lineColor:"#cccccc",lineDashStyle:"Solid",lineWidth:4,x:0,y:0}}}),s(t,"Extensions/DragPanes/AxisResizer.js",[t["Extensions/DragPanes/AxisResizerDefaults.js"],t["Core/Utilities.js"]],function(e,t){var s=t.addEvent,i=t.clamp,n=t.isNumber,o=t.relativeLength;return function(){function t(e){this.init(e)}return t.prototype.init=function(e,t){this.axis=e,this.options=e.options.resize||{},this.render(),t||this.addMouseEvents()},t.prototype.render=function(){var e=this.axis,t=e.chart,s=this.options,n=s.x||0,o=s.y,r=i(e.top+e.height+o,t.plotTop,t.plotTop+t.plotHeight),a={};t.styledMode||(a={cursor:s.cursor,stroke:s.lineColor,"stroke-width":s.lineWidth,dashstyle:s.lineDashStyle}),this.lastPos=r-o,this.controlLine||(this.controlLine=t.renderer.path().addClass("highcharts-axis-resizer")),this.controlLine.add(e.axisGroup);var h=t.styledMode?this.controlLine.strokeWidth():s.lineWidth;a.d=t.renderer.crispLine([["M",e.left+n,r],["L",e.left+e.width+n,r]],h),this.controlLine.attr(a)},t.prototype.addMouseEvents=function(){var e,t,i,n=this,o=n.controlLine.element,r=n.axis.chart.container,a=[];n.mouseMoveHandler=e=function(e){return n.onMouseMove(e)},n.mouseUpHandler=t=function(e){return n.onMouseUp(e)},n.mouseDownHandler=i=function(){return n.onMouseDown()},a.push(s(r,"mousemove",e),s(r.ownerDocument,"mouseup",t),s(o,"mousedown",i),s(r,"touchmove",e),s(r.ownerDocument,"touchend",t),s(o,"touchstart",i)),n.eventsToUnbind=a},t.prototype.onMouseMove=function(e){if(!e.touches||0!==e.touches[0].pageX){var t=this.axis.chart.pointer;this.grabbed&&t&&(this.hasDragged=!0,this.updateAxes(t.normalize(e).chartY-(this.options.y||0)))}},t.prototype.onMouseUp=function(e){var t=this.axis.chart.pointer;this.hasDragged&&t&&this.updateAxes(t.normalize(e).chartY-(this.options.y||0)),this.grabbed=this.hasDragged=this.axis.chart.activeResizer=void 0},t.prototype.onMouseDown=function(){var e;null===(e=this.axis.chart.pointer)||void 0===e||e.reset(!1,0),this.grabbed=this.axis.chart.activeResizer=!0},t.prototype.updateAxes=function(e){var t=this.axis.chart,s=this.options.controlledAxis,r=0===s.next.length?[t.yAxis.indexOf(this.axis)+1]:s.next,a=[this.axis].concat(s.prev),h=[],u=t.plotTop,c=t.plotHeight,d=u+c,p=function(e){return 100*e/c+"%"},l=function(e,t,s){return Math.round(i(e,t,s))};e=i(e,u,d);var f=!1,v=e-this.lastPos;if(!(v*v<1)){for(var x=!0,g=0,y=[a,r];g<y.length;g++)for(var m=y[g],z=0;z<m.length;z++){var D=m[z],M=n(D)?t.yAxis[D]:x?D:t.get(D),P=M&&M.options,A={},E=void 0,b=void 0;if(!P||P.isInternal){x=!1;continue}b=M.top;var L=Math.round(o(P.minLength||NaN,c)),j=Math.round(o(P.maxLength||NaN,c));if(x)(E=l(e-b,L,j))===j&&(f=!0),e=b+E,h.push({axis:M,options:{height:p(E)}});else{if(v=e-this.lastPos,E=l(M.len-v,L,j),(b=M.top+v)+E>d){var w=d-E-b;e+=w,b+=w}b<u&&(b=u)+E>d&&(E=c),E===L&&(f=!0),h.push({axis:M,options:{top:p(b-u),height:p(E)}})}x=!1,A.height=E}if(!f){for(var R=0;R<h.length;R++){var C=h[R];C.axis.update(C.options,!1)}t.redraw(!1)}}},t.prototype.destroy=function(){var e=this.axis;delete e.resizer,this.eventsToUnbind&&this.eventsToUnbind.forEach(function(e){return e()}),this.controlLine.destroy();for(var t=0,s=Object.keys(this);t<s.length;t++)this[s[t]]=null},t.resizerOptions=e,t}()}),s(t,"Extensions/DragPanes/DragPanes.js",[t["Extensions/DragPanes/AxisResizer.js"],t["Core/Defaults.js"],t["Core/Utilities.js"]],function(e,t,s){var i=t.defaultOptions,n=s.addEvent,o=s.merge,r=s.wrap;function a(){var t=this.resizer,s=this.options.resize;if(s){var i=!1!==s.enabled;t?i?t.init(this,!0):t.destroy():i&&(this.resizer=new e(this))}}function h(e){!e.keepEvents&&this.resizer&&this.resizer.destroy()}function u(e){this.chart.activeResizer||e.apply(this,[].slice.call(arguments,1))}function c(e){this.chart.activeResizer||e.apply(this,[].slice.call(arguments,1))}return{compose:function(t,s){t.keepProps.includes("resizer")||(o(!0,i.yAxis,e.resizerOptions),t.keepProps.push("resizer"),n(t,"afterRender",a),n(t,"destroy",h),r(s.prototype,"runPointActions",c),r(s.prototype,"drag",u))}}}),s(t,"masters/modules/drag-panes.src.js",[t["Core/Globals.js"],t["Extensions/DragPanes/AxisResizer.js"],t["Extensions/DragPanes/DragPanes.js"]],function(e,t,s){return e.AxisResizer=t,s.compose(e.Axis,e.Pointer),e})});