/*
 Highcharts JS v7.1.1 (2019-04-09)

 (c) 2014-2019 Highsoft AS
 Authors: Jon Arild Nygard / Oystein Moseng

 License: www.highcharts.com/license
*/
(function(c){"object"===typeof module&&module.exports?(c["default"]=c,module.exports=c):"function"===typeof define&&define.amd?define("highcharts/modules/treemap",["highcharts"],function(A){c(A);c.Highcharts=A;return c}):c("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(c){function A(b,m,c,f){b.hasOwnProperty(m)||(b[m]=f.apply(null,c))}c=c?c._modules:{};A(c,"mixins/tree-series.js",[c["parts/Globals.js"]],function(b){var m=b.extend,c=b.isArray,f=b.isObject,B=b.isNumber,u=b.merge,h=b.pick;
return{getColor:function(p,n){var q=n.index,m=n.mapOptionsToLevel,c=n.parentColor,f=n.parentColorIndex,E=n.series,w=n.colors,B=n.siblings,l=E.points,y=E.chart.options.chart,v,x,z,u;if(p){l=l[p.i];p=m[p.level]||{};if(m=l&&p.colorByPoint)x=l.index%(w?w.length:y.colorCount),v=w&&w[x];if(!E.chart.styledMode){w=l&&l.options.color;y=p&&p.color;if(z=c)z=(z=p&&p.colorVariation)&&"brightness"===z.key?b.color(c).brighten(q/B*z.to).get():c;z=h(w,y,v,z,E.color)}u=h(l&&l.options.colorIndex,p&&p.colorIndex,x,f,
n.colorIndex)}return{color:z,colorIndex:u}},getLevelOptions:function(b){var n=null,q,C,p,h;if(f(b))for(n={},p=B(b.from)?b.from:1,h=b.levels,C={},q=f(b.defaults)?b.defaults:{},c(h)&&(C=h.reduce(function(b,c){var n,l;f(c)&&B(c.level)&&(l=u({},c),n="boolean"===typeof l.levelIsConstant?l.levelIsConstant:q.levelIsConstant,delete l.levelIsConstant,delete l.level,c=c.level+(n?0:p-1),f(b[c])?m(b[c],l):b[c]=l);return b},{})),h=B(b.to)?b.to:1,b=0;b<=h;b++)n[b]=u({},q,f(C[b])?C[b]:{});return n},setTreeValues:function n(b,
c){var f=c.before,q=c.idRoot,B=c.mapIdToNode[q],w=c.points[b.i],u=w&&w.options||{},l=0,y=[];m(b,{levelDynamic:b.level-(("boolean"===typeof c.levelIsConstant?c.levelIsConstant:1)?0:B.level),name:h(w&&w.name,""),visible:q===b.id||("boolean"===typeof c.visible?c.visible:!1)});"function"===typeof f&&(b=f(b,c));b.children.forEach(function(f,h){var q=m({},c);m(q,{index:h,siblings:b.children.length,visible:b.visible});f=n(f,q);y.push(f);f.visible&&(l+=f.val)});b.visible=0<l||b.visible;f=h(u.value,l);m(b,
{children:y,childrenTotal:l,isLeaf:b.visible&&!l,val:f});return b},updateRootId:function(b){var c;f(b)&&(c=f(b.options)?b.options:{},c=h(b.rootNode,c.rootId,""),f(b.userOptions)&&(b.userOptions.rootId=c),b.rootNode=c);return c}}});A(c,"mixins/draw-point.js",[],function(){var b=function(b){var c=this,f=c.graphic,m=b.animatableAttribs,u=b.onComplete,h=b.css,p=b.renderer;if(c.shouldDraw())f||(c.graphic=f=p[b.shapeType](b.shapeArgs).add(b.group)),f.css(h).attr(b.attribs).animate(m,b.isNew?!1:void 0,u);
else if(f){var n=function(){c.graphic=f=f.destroy();"function"===typeof u&&u()};Object.keys(m).length?f.animate(m,void 0,function(){n()}):n()}};return function(c){(c.attribs=c.attribs||{})["class"]=this.getClassName();b.call(this,c)}});A(c,"modules/treemap.src.js",[c["parts/Globals.js"],c["mixins/tree-series.js"],c["mixins/draw-point.js"]],function(b,c,A){var f=b.seriesType,m=b.seriesTypes,u=b.addEvent,h=b.merge,p=b.extend,n=b.error,q=b.defined,C=b.noop,J=b.fireEvent,K=c.getColor,E=c.getLevelOptions,
w=b.isArray,H=b.isNumber,l=b.isObject,y=b.isString,v=b.pick,x=b.Series,z=b.stableSort,I=b.Color,L=function(a,d,e){e=e||this;b.objectEach(a,function(b,g){d.call(e,b,g,a)})},F=function(a,d,e){e=e||this;a=d.call(e,a);!1!==a&&F(a,d,e)},M=c.updateRootId;f("treemap","scatter",{allowTraversingTree:!1,animationLimit:250,showInLegend:!1,marker:!1,colorByPoint:!1,dataLabels:{defer:!1,enabled:!0,formatter:function(){var a=this&&this.point?this.point:{};return y(a.name)?a.name:""},inside:!0,verticalAlign:"middle"},
tooltip:{headerFormat:"",pointFormat:"\x3cb\x3e{point.name}\x3c/b\x3e: {point.value}\x3cbr/\x3e"},ignoreHiddenPoint:!0,layoutAlgorithm:"sliceAndDice",layoutStartingDirection:"vertical",alternateStartingDirection:!1,levelIsConstant:!0,drillUpButton:{position:{align:"right",x:-10,y:10}},traverseUpButton:{position:{align:"right",x:-10,y:10}},borderColor:"#e6e6e6",borderWidth:1,opacity:.15,states:{hover:{borderColor:"#999999",brightness:m.heatmap?0:.1,halo:!1,opacity:.75,shadow:!1}}},{pointArrayMap:["value"],
directTouch:!0,optionalAxis:"colorAxis",getSymbol:C,parallelArrays:["x","y","value","colorValue"],colorKey:"colorValue",trackerGroups:["group","dataLabelsGroup"],getListOfParents:function(a,d){a=w(a)?a:[];var e=w(d)?d:[];d=a.reduce(function(a,d,e){d=v(d.parent,"");void 0===a[d]&&(a[d]=[]);a[d].push(e);return a},{"":[]});L(d,function(a,d,b){""!==d&&-1===e.indexOf(d)&&(a.forEach(function(a){b[""].push(a)}),delete b[d])});return d},getTree:function(){var a=this.data.map(function(a){return a.id}),a=this.getListOfParents(this.data,
a);this.nodeMap=[];return this.buildNode("",-1,0,a,null)},hasData:function(){return!!this.processedXData.length},init:function(a,d){var e=b.colorSeriesMixin;b.colorSeriesMixin&&(this.translateColors=e.translateColors,this.colorAttribs=e.colorAttribs,this.axisTypes=e.axisTypes);u(this,"setOptions",function(a){a=a.userOptions;q(a.allowDrillToNode)&&!q(a.allowTraversingTree)&&(a.allowTraversingTree=a.allowDrillToNode,delete a.allowDrillToNode);q(a.drillUpButton)&&!q(a.traverseUpButton)&&(a.traverseUpButton=
a.drillUpButton,delete a.drillUpButton)});x.prototype.init.call(this,a,d);this.options.allowTraversingTree&&u(this,"click",this.onClickDrillToNode)},buildNode:function(a,d,e,b,g){var c=this,t=[],k=c.points[d],G=0,r;(b[a]||[]).forEach(function(d){r=c.buildNode(c.points[d].id,d,e+1,b,a);G=Math.max(r.height+1,G);t.push(r)});d={id:a,i:d,children:t,height:G,level:e,parent:g,visible:!1};c.nodeMap[d.id]=d;k&&(k.node=d);return d},setTreeValues:function(a){var d=this,e=d.options,b=d.nodeMap[d.rootNode],e=
"boolean"===typeof e.levelIsConstant?e.levelIsConstant:!0,g=0,c=[],D,k=d.points[a.i];a.children.forEach(function(a){a=d.setTreeValues(a);c.push(a);a.ignore||(g+=a.val)});z(c,function(a,d){return a.sortIndex-d.sortIndex});D=v(k&&k.options.value,g);k&&(k.value=D);p(a,{children:c,childrenTotal:g,ignore:!(v(k&&k.visible,!0)&&0<D),isLeaf:a.visible&&!g,levelDynamic:a.level-(e?0:b.level),name:v(k&&k.name,""),sortIndex:v(k&&k.sortIndex,-D),val:D});return a},calculateChildrenAreas:function(a,d){var e=this,
b=e.options,g=e.mapOptionsToLevel[a.level+1],c=v(e[g&&g.layoutAlgorithm]&&g.layoutAlgorithm,b.layoutAlgorithm),D=b.alternateStartingDirection,k=[];a=a.children.filter(function(a){return!a.ignore});g&&g.layoutStartingDirection&&(d.direction="vertical"===g.layoutStartingDirection?0:1);k=e[c](d,a);a.forEach(function(a,b){b=k[b];a.values=h(b,{val:a.childrenTotal,direction:D?1-d.direction:d.direction});a.pointValues=h(b,{x:b.x/e.axisRatio,width:b.width/e.axisRatio});a.children.length&&e.calculateChildrenAreas(a,
a.values)})},setPointValues:function(){var a=this,d=a.xAxis,b=a.yAxis;a.points.forEach(function(e){var g=e.node,c=g.pointValues,t,k,f=0;a.chart.styledMode||(f=(a.pointAttribs(e)["stroke-width"]||0)%2/2);c&&g.visible?(g=Math.round(d.translate(c.x,0,0,0,1))-f,t=Math.round(d.translate(c.x+c.width,0,0,0,1))-f,k=Math.round(b.translate(c.y,0,0,0,1))-f,c=Math.round(b.translate(c.y+c.height,0,0,0,1))-f,e.shapeArgs={x:Math.min(g,t),y:Math.min(k,c),width:Math.abs(t-g),height:Math.abs(c-k)},e.plotX=e.shapeArgs.x+
e.shapeArgs.width/2,e.plotY=e.shapeArgs.y+e.shapeArgs.height/2):(delete e.plotX,delete e.plotY)})},setColorRecursive:function(a,d,e,b,c){var g=this,t=g&&g.chart,t=t&&t.options&&t.options.colors,k;if(a){k=K(a,{colors:t,index:b,mapOptionsToLevel:g.mapOptionsToLevel,parentColor:d,parentColorIndex:e,series:g,siblings:c});if(d=g.points[a.i])d.color=k.color,d.colorIndex=k.colorIndex;(a.children||[]).forEach(function(d,b){g.setColorRecursive(d,k.color,k.colorIndex,b,a.children.length)})}},algorithmGroup:function(a,
d,b,c){this.height=a;this.width=d;this.plot=c;this.startDirection=this.direction=b;this.lH=this.nH=this.lW=this.nW=this.total=0;this.elArr=[];this.lP={total:0,lH:0,nH:0,lW:0,nW:0,nR:0,lR:0,aspectRatio:function(a,d){return Math.max(a/d,d/a)}};this.addElement=function(a){this.lP.total=this.elArr[this.elArr.length-1];this.total+=a;0===this.direction?(this.lW=this.nW,this.lP.lH=this.lP.total/this.lW,this.lP.lR=this.lP.aspectRatio(this.lW,this.lP.lH),this.nW=this.total/this.height,this.lP.nH=this.lP.total/
this.nW,this.lP.nR=this.lP.aspectRatio(this.nW,this.lP.nH)):(this.lH=this.nH,this.lP.lW=this.lP.total/this.lH,this.lP.lR=this.lP.aspectRatio(this.lP.lW,this.lH),this.nH=this.total/this.width,this.lP.nW=this.lP.total/this.nH,this.lP.nR=this.lP.aspectRatio(this.lP.nW,this.nH));this.elArr.push(a)};this.reset=function(){this.lW=this.nW=0;this.elArr=[];this.total=0}},algorithmCalcPoints:function(a,d,e,c){var g,t,f,k,l=e.lW,r=e.lH,h=e.plot,n,p=0,m=e.elArr.length-1;d?(l=e.nW,r=e.nH):n=e.elArr[e.elArr.length-
1];e.elArr.forEach(function(a){if(d||p<m)0===e.direction?(g=h.x,t=h.y,f=l,k=a/f):(g=h.x,t=h.y,k=r,f=a/k),c.push({x:g,y:t,width:f,height:b.correctFloat(k)}),0===e.direction?h.y+=k:h.x+=f;p+=1});e.reset();0===e.direction?e.width-=l:e.height-=r;h.y=h.parent.y+(h.parent.height-e.height);h.x=h.parent.x+(h.parent.width-e.width);a&&(e.direction=1-e.direction);d||e.addElement(n)},algorithmLowAspectRatio:function(a,d,b){var e=[],c=this,f,h={x:d.x,y:d.y,parent:d},k=0,l=b.length-1,r=new this.algorithmGroup(d.height,
d.width,d.direction,h);b.forEach(function(b){f=b.val/d.val*d.height*d.width;r.addElement(f);r.lP.nR>r.lP.lR&&c.algorithmCalcPoints(a,!1,r,e,h);k===l&&c.algorithmCalcPoints(a,!0,r,e,h);k+=1});return e},algorithmFill:function(a,d,b){var e=[],c,f=d.direction,h=d.x,k=d.y,l=d.width,r=d.height,n,p,m,q;b.forEach(function(b){c=b.val/d.val*d.height*d.width;n=h;p=k;0===f?(q=r,m=c/q,l-=m,h+=m):(m=l,q=c/m,r-=q,k+=q);e.push({x:n,y:p,width:m,height:q});a&&(f=1-f)});return e},strip:function(a,d){return this.algorithmLowAspectRatio(!1,
a,d)},squarified:function(a,d){return this.algorithmLowAspectRatio(!0,a,d)},sliceAndDice:function(a,d){return this.algorithmFill(!0,a,d)},stripes:function(a,d){return this.algorithmFill(!1,a,d)},translate:function(){var a=this,d=a.options,b=M(a),c,g;x.prototype.translate.call(a);g=a.tree=a.getTree();c=a.nodeMap[b];a.renderTraverseUpButton(b);a.mapOptionsToLevel=E({from:c.level+1,levels:d.levels,to:g.height,defaults:{levelIsConstant:a.options.levelIsConstant,colorByPoint:d.colorByPoint}});""===b||
c&&c.children.length||(a.setRootNode("",!1),b=a.rootNode,c=a.nodeMap[b]);F(a.nodeMap[a.rootNode],function(d){var b=!1,c=d.parent;d.visible=!0;if(c||""===c)b=a.nodeMap[c];return b});F(a.nodeMap[a.rootNode].children,function(a){var d=!1;a.forEach(function(a){a.visible=!0;a.children.length&&(d=(d||[]).concat(a.children))});return d});a.setTreeValues(g);a.axisRatio=a.xAxis.len/a.yAxis.len;a.nodeMap[""].pointValues=b={x:0,y:0,width:100,height:100};a.nodeMap[""].values=b=h(b,{width:b.width*a.axisRatio,
direction:"vertical"===d.layoutStartingDirection?0:1,val:g.val});a.calculateChildrenAreas(g,b);a.colorAxis?a.translateColors():d.colorByPoint||a.setColorRecursive(a.tree);d.allowTraversingTree&&(d=c.pointValues,a.xAxis.setExtremes(d.x,d.x+d.width,!1),a.yAxis.setExtremes(d.y,d.y+d.height,!1),a.xAxis.setScale(),a.yAxis.setScale());a.setPointValues()},drawDataLabels:function(){var a=this,d=a.mapOptionsToLevel,b,c;a.points.filter(function(a){return a.node.visible}).forEach(function(e){c=d[e.node.level];
b={style:{}};e.node.isLeaf||(b.enabled=!1);c&&c.dataLabels&&(b=h(b,c.dataLabels),a._hasPointLabels=!0);e.shapeArgs&&(b.style.width=e.shapeArgs.width,e.dataLabel&&e.dataLabel.css({width:e.shapeArgs.width+"px"}));e.dlOptions=h(b,e.options.dataLabels)});x.prototype.drawDataLabels.call(this)},alignDataLabel:function(a,d,c){var e=c.style;!b.defined(e.textOverflow)&&d.text&&d.getBBox().width>d.text.textWidth&&d.css({textOverflow:"ellipsis",width:e.width+="px"});m.column.prototype.alignDataLabel.apply(this,
arguments);a.dataLabel&&a.dataLabel.attr({zIndex:(a.node.zIndex||0)+1})},pointAttribs:function(a,d){var b=l(this.mapOptionsToLevel)?this.mapOptionsToLevel:{},c=a&&b[a.node.level]||{},b=this.options,g=d&&b.states[d]||{},f=a&&a.getClassName()||"";a={stroke:a&&a.borderColor||c.borderColor||g.borderColor||b.borderColor,"stroke-width":v(a&&a.borderWidth,c.borderWidth,g.borderWidth,b.borderWidth),dashstyle:a&&a.borderDashStyle||c.borderDashStyle||g.borderDashStyle||b.borderDashStyle,fill:a&&a.color||this.color};
-1!==f.indexOf("highcharts-above-level")?(a.fill="none",a["stroke-width"]=0):-1!==f.indexOf("highcharts-internal-node-interactive")?(d=v(g.opacity,b.opacity),a.fill=I(a.fill).setOpacity(d).get(),a.cursor="pointer"):-1!==f.indexOf("highcharts-internal-node")?a.fill="none":d&&(a.fill=I(a.fill).brighten(g.brightness).get());return a},drawPoints:function(){var a=this,b=a.chart,c=b.renderer,f=b.styledMode,g=a.options,l=f?{}:g.shadow,m=g.borderRadius,k=b.pointCount<g.animationLimit,n=g.allowTraversingTree;
a.points.forEach(function(b){var d=b.node.levelDynamic,e={},t={},q={},r="level-group-"+d,u=!!b.graphic,w=k&&u,v=b.shapeArgs;b.shouldDraw()&&(m&&(t.r=m),h(!0,w?e:t,u?v:{},f?{}:a.pointAttribs(b,b.selected&&"select")),a.colorAttribs&&f&&p(q,a.colorAttribs(b)),a[r]||(a[r]=c.g(r).attr({zIndex:1E3-d}).add(a.group)));b.draw({animatableAttribs:e,attribs:t,css:q,group:a[r],renderer:c,shadow:l,shapeArgs:v,shapeType:"rect"});n&&b.graphic&&(b.drillId=g.interactByLeaf?a.drillToByLeaf(b):a.drillToByGroup(b))})},
onClickDrillToNode:function(a){var b=(a=a.point)&&a.drillId;y(b)&&(a.setState(""),this.setRootNode(b,!0,{trigger:"click"}))},drillToByGroup:function(a){var b=!1;1!==a.node.level-this.nodeMap[this.rootNode].level||a.node.isLeaf||(b=a.id);return b},drillToByLeaf:function(a){var b=!1;if(a.node.parent!==this.rootNode&&a.node.isLeaf)for(a=a.node;!b;)a=this.nodeMap[a.parent],a.parent===this.rootNode&&(b=a.id);return b},drillUp:function(){var a=this.nodeMap[this.rootNode];a&&y(a.parent)&&this.setRootNode(a.parent,
!0,{trigger:"traverseUpButton"})},drillToNode:function(a,b){n("WARNING: treemap.drillToNode has been renamed to treemap.setRootNode, and will be removed in the next major version.");this.setRootNode(a,b)},setRootNode:function(a,b,c){a=p({newRootId:a,previousRootId:this.rootNode,redraw:v(b,!0),series:this},c);J(this,"setRootNode",a,function(a){var b=a.series;b.idPreviousRoot=a.previousRootId;b.rootNode=a.newRootId;b.isDirty=!0;a.redraw&&b.chart.redraw()})},renderTraverseUpButton:function(a){var b=
this,c=b.options.traverseUpButton,f=v(c.text,b.nodeMap[a].name,"\x3c Back"),g;""===a?b.drillUpButton&&(b.drillUpButton=b.drillUpButton.destroy()):this.drillUpButton?(this.drillUpButton.placed=!1,this.drillUpButton.attr({text:f}).align()):(g=(a=c.theme)&&a.states,this.drillUpButton=this.chart.renderer.button(f,null,null,function(){b.drillUp()},a,g&&g.hover,g&&g.select).addClass("highcharts-drillup-button").attr({align:c.position.align,zIndex:7}).add().align(c.position,!1,c.relativeTo||"plotBox"))},
buildKDTree:C,drawLegendSymbol:b.LegendSymbolMixin.drawRectangle,getExtremes:function(){x.prototype.getExtremes.call(this,this.colorValueData);this.valueMin=this.dataMin;this.valueMax=this.dataMax;x.prototype.getExtremes.call(this)},getExtremesFromAll:!0,bindAxes:function(){var a={endOnTick:!1,gridLineWidth:0,lineWidth:0,min:0,dataMin:0,minPadding:0,max:100,dataMax:100,maxPadding:0,startOnTick:!1,title:null,tickPositions:[]};x.prototype.bindAxes.call(this);b.extend(this.yAxis.options,a);b.extend(this.xAxis.options,
a)},setState:function(a){this.options.inactiveOtherPoints=!0;x.prototype.setState.call(this,a,!1);this.options.inactiveOtherPoints=!1},utils:{recursive:F}},{draw:A,getClassName:function(){var a=b.Point.prototype.getClassName.call(this),c=this.series,e=c.options;this.node.level<=c.nodeMap[c.rootNode].level?a+=" highcharts-above-level":this.node.isLeaf||v(e.interactByLeaf,!e.allowTraversingTree)?this.node.isLeaf||(a+=" highcharts-internal-node"):a+=" highcharts-internal-node-interactive";return a},
isValid:function(){return this.id||H(this.value)},setState:function(a){b.Point.prototype.setState.call(this,a);this.graphic&&this.graphic.attr({zIndex:"hover"===a?1:0})},setVisible:m.pie.prototype.pointClass.prototype.setVisible,shouldDraw:function(){return H(this.plotY)&&null!==this.y}})});A(c,"masters/modules/treemap.src.js",[],function(){})});

