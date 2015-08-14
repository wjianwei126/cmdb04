function Consts(){}Consts.id="TViePlayer";Consts.player="Player.swf";Consts.loader="Loader.swf";Consts.shareServer="share_server.php";Consts.sharePlayer="TVieShare.html";Consts.bgcolor="#7B8EAF";Consts.validDomain="validDomain.txt";Consts.logMode="UIMode";Consts.componentsLayout="Vertical";Consts.videoScaleMode="fill";Consts.swfVersionStr="10.1";Consts.xiSwfUrlStr="AdobeFlashPlayerInstall.swf";Consts.allowScriptAccess="always";Consts.HttpProgressiveDownload="HttpProgressiveDownload";
Consts.Streaming="Streaming";Consts.SmoothStreaming="SmoothStreaming";Consts.TVieVod="TVieVod";Consts.TVieLive="TVieLive";Consts.serverVersion="2.0";Consts.vodIndexMode="start";Consts.pluginModeIsolate="isolate";Consts.pluginModeEmbeded="embeded";Consts.pluginModeEmbededPrePlayAd="prePlayAd";Consts.pluginModeEmbededOnPauseAd="onPauseAd";Consts.pluginModeEmbededOnPlayAd="onPlayAd";Consts.pluginModeEmbededOnEndAd="onEndAd";Consts.pluginModeEmbededProgressBarTips="progressBarTips";
Consts.pluginModeEmbededFacade="facade";Consts.pluginLayoutFloat="float";Consts.pluginLayoutAutoFill="autofill";Consts.pluginLayoutFloatHorizenLeft="left";Consts.pluginLayoutFloatHorizenCenter="center";Consts.pluginLayoutFloatHorizenRight="right";Consts.pluginLayoutFloatVerticalTop="top";Consts.pluginLayoutFloatVerticalMiddle="middle";Consts.pluginLayoutFloatVerticalBottom="bottom";Consts.pluginLayoutDocked="docked";Consts.pluginLayoutDockedTop="top";Consts.pluginLayoutDockedBottom="bottom";
Consts.pluginLayoutDockedLeft="left";Consts.pluginLayoutDockedRight="right";
function TViePlayer(a,b,c,d,e){if(a==void 0||a==null)throw Error("invalid container: "+a);this.container=a;if(b==void 0||b==null)throw Error("invalid skin: "+b);this.skin=b;a=b.substr(0,b.lastIndexOf("/"));a!=""&&(a+="/");this.loader=a+Consts.loader;this.player=a+Consts.player;this.shareServer=a+Consts.shareServer;this.sharePlayer=a+Consts.sharePlayer;this.validDomain=a+Consts.validDomain;this.xiSwfUrlStr=a+Consts.xiSwfUrlStr;if(e!=void 0&&e!=null){a="?";for(b=0;b<e.length-1;b+=2)a+=e[b]+"="+e[b+
1]+",";this.skin+=a}if(c==void 0||c==null)throw Error("invalid width: "+c);this.width=c;if(d==void 0||d==null)throw Error("invalid height: "+d);this.height=d;this.bgcolor=Consts.bgcolor;this.log=this.mode=null;this.logMode=Consts.logMode;this.logUIWidth=500;this.logUIHeight=300;this.netMonitor=null;this.componentsLayout=Consts.componentsLayout;this.enableSystemStartupUILog=!1;this.autostart=!0;this.volume=1;this.wmode="Window";this.videoScaleMode=Consts.videoScaleMode;this.plugins=[];this.swfVersionStr=
Consts.swfVersionStr;this.allowScriptAccess=Consts.allowScriptAccess;this.id=Consts.id}
TViePlayer.prototype.run=function(){if(this.mode==null||this.mode==void 0)throw Error("invalid mode: "+this.mode+" please invoke setHttpProgressiveMode/setStreaming/setSmoothStreaming/setTVieLive/setTVieVod to initiaize the mode first!");var a={};a.mode=this.mode;if(this.url!=void 0)a.url=this.url;if(this.host!=void 0)a.host=this.host;if(this.streams!=void 0)a.streams=this.streams;if(this.server!=void 0)a.server=this.server;if(this.file!=void 0)a.file=this.file;if(this.channelId!=void 0)a.channelId=
this.channelId;if(this.startTimeInMS!=void 0)a.startTimeInMS=this.startTimeInMS;if(this.unSeekableChannels!=void 0)a.unSeekableChannels=this.unSeekableChannels;if(this.timeShiftDisabledChannels!=void 0)a.timeShiftDisabledChannels=this.timeShiftDisabledChannels;if(this.serverVersion!=void 0)a.serverVersion=this.serverVersion;if(this.apiParams!=void 0)a.apiParams=this.apiParams;if(this.requestApiServerWithDomain!=void 0)a.requestApiServerWithDomain=this.requestApiServerWithDomain;if(this.vodIndexMode!=
void 0)a.vodIndexMode=this.vodIndexMode;if(this.forceBase64!=void 0)a.forceBase64=this.forceBase64;if(this.smoothAutoSwitch!=void 0)a.smoothAutoSwitch=this.smoothAutoSwitch;if(this.vodDirectlyAccessUrl!=void 0)a.vodDirectlyAccessUrl=this.vodDirectlyAccessUrl;if(this.highDefinition!=void 0)a.highDefinition=this.highDefinition;if(this.playWhenChangeChannel!=void 0)a.playWhenChangeChannel=this.playWhenChangeChannel;if(this.switchStreamWhenBuffer!=void 0)a.switchStreamWhenBuffer=this.switchStreamWhenBuffer;
if(this.bufferTime!=void 0)a.bufferTime=this.bufferTime;var b=this.skin.substr(0,this.sharePlayer.lastIndexOf("/"));b!=""&&(b+="/");if(b.toLowerCase().indexOf("http://")!=0&&(b=location.href,b!=null&&b!=void 0&&b.toLowerCase().indexOf("http://")>=0))this.sharePlayer=b.substr(0,b.lastIndexOf("/"))+"/"+this.sharePlayer;a.player=this.player;a.loader=this.loader;a.shareServer=this.shareServer;a.sharePlayer=this.sharePlayer;a.validDomain=this.validDomain;a.skin=this.skin;a.width=this.width;a.height=this.height;
a.componentsLayout=this.componentsLayout;a.supportSnapshot=this.supportSnapshot;a.supportAudioScreen=this.supportAudioScreen;a.enableSystemStartupUILog=this.enableSystemStartupUILog;a.autostart=this.autostart;a.volume=this.volume;a.videoScaleMode=this.videoScaleMode;if(this.log!=null)a.log=this.log;a.logMode=this.logMode;a.logUIWidth=this.logUIWidth;a.logUIHeight=this.logUIHeight;if(this.netMonitor!=null)a.netMonitor=this.netMonitor;if(this.onPlayComplete!=void 0)a.onPlayComplete=this.onPlayComplete;
if(this.onLightOn!=void 0)a.onLightOn=this.onLightOn;if(this.onLightOff!=void 0)a.onLightOff=this.onLightOff;if(this.onLiveProgramComplete!=void 0)a.onLiveProgramComplete=this.onLiveProgramComplete;if(this.onUserClickVideo!=void 0)a.onUserClickVideo=this.onUserClickVideo;if(this.onUserDoubleClickVideo!=void 0)a.onUserDoubleClickVideo=this.onUserDoubleClickVideo;if(this.plugins.length>0){a.plugins="{'plugins':[\n";for(b=0;b<this.plugins.length;b++)a.plugins+=this.plugins[b].toJSON(),b<this.plugins.length-
1&&(a.plugins+=",\n");a.plugins+="\n]}"}b={quality:"high"};b.bgcolor=this.bgcolor;b.allowscriptaccess=this.allowScriptAccess;b.allowfullscreen="true";b.wmode=this.wmode;var c={};c.id=this.id;c.name=this.id;c.align="middle";var d=this;swfobject.embedSWF(this.loader,this.container,this.width,this.height,this.swfVersionStr,this.xiSwfUrlStr,a,b,c,function(a){d.callbackObj=a})};
TViePlayer.prototype.setHttpProgressiveMode=function(a){this.mode=Consts.HttpProgressiveDownload;if(a==void 0||a==null)throw Error("invalid url: "+a);this.url=a};TViePlayer.prototype.setStreaming=function(a){this.mode=Consts.Streaming;if(a==void 0||a==null)throw Error("invalid stream url: "+a);this.url=a};
TViePlayer.prototype.setSmoothStreaming=function(a,b){this.mode=Consts.SmoothStreaming;if(a==void 0||a==null)throw Error("invalid host: "+a);this.host=a;if(b==void 0||b==null)throw Error("invalid streams: "+b);if(b.length<1)throw Error("must specify at least 1 stream.");this.streams="{'streams':[\n";for(var c=0;c<b.length;c++){var d=b[c];if(d.bitrate==void 0||d.bitrate==null)throw Error("invalid stream.bitrate:"+d.bitrate);if(d.width==void 0||d.width==null)throw Error("invalid stream.width:"+d.width);
if(d.height==void 0||d.height==null)throw Error("invalid stream.height:"+d.height);if(d.name==void 0||d.name==null)throw Error("invalid stream.name:"+d.name);this.streams+="{'bitrate':"+d.bitrate+", 'width':"+d.width+", 'height':"+d.height+", 'name':'"+d.name+"'}";c<b.length-1&&(this.streams+=",\n")}this.streams+="\n]}"};
TViePlayer.prototype.setTVieVod=function(a,b,c,d){this.mode=Consts.TVieVod;if(this.forceBase64==void 0)this.forceBase64=!1;if(a==void 0||a==null)throw Error("invalid apiServer: "+a);this.server=a;if(b==void 0||b==null)throw Error("invalid fileNameOrId: "+b);this.vodIndexMode=d==void 0||d==null?Consts.vodIndexMode:d;if(/^\d*$/.test(b))this.file=b,this.serverVersion="2.0";else{a=Math.max(b.indexOf("vod/"),b.indexOf("vod_base64/"));if(a<0)throw Error("vod must contains vod/ or vod_base64/, actual "+
b);this.file=b=b.substr(a);this.serverVersion="1.5b"}if(c!=void 0&&c!=null)this.startTimeInMS=c};
TViePlayer.prototype.setTVieLive=function(a,b,c,d){this.mode=Consts.TVieLive;if(this.requestApiServerWithDomain==void 0)this.requestApiServerWithDomain=!1;if(this.highDefinition==void 0)this.highDefinition=!0;if(a==void 0||a==null)throw Error("invalid apiServer: "+a);this.server=a;if(b!=void 0&&b!=null)this.channelId=b;this.serverVersion=c==void 0||c==null?Consts.serverVersion:c;if(d!=void 0&&d!=null)this.startTimeInMS=d};
TViePlayer.prototype.setLiveApiParameters=function(a){if(!(a==void 0||a==null)){for(var b="",c=0;c<a.length-1;c+=2)b+=a[c]+","+a[c+1]+",";if(b!="")this.apiParams=b}};TViePlayer.prototype.setTVieSmoothVod=function(a,b){this.mode="TVieSmoothVod";this.url=a;if(b!=void 0&&b!=null)this.smoothAutoSwitch=b};
TViePlayer.prototype.setTVieSmoothLive=function(a,b,c,d){this.mode="TVieSmoothLive";if(a==void 0||a==null)throw Error("invalid apiServer: "+a);this.server=a;if(b!=void 0&&b!=null)this.channelId=b;if(d!=void 0&&d!=null)this.startTimeInMS=d;if(c!=void 0&&c!=null)this.smoothAutoSwitch=c};
TViePlayer.prototype.setJSCallback=function(a,b,c,d,e,f){if(a!=void 0&&a!=null)this.onPlayComplete=a;if(b!=void 0&&b!=null)this.onLightOn=b;if(c!=void 0&&c!=null)this.onLightOff=c;if(d!=void 0&&d!=null)this.onLiveProgramComplete=d;if(e!=void 0&&e!=null)this.onUserClickVideo=e;if(f!=void 0&&f!=null)this.onUserDoubleClickVideo=f};
TViePlayer.prototype.livePlay=function(a,b){if(this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0){var c=a;if(a==null||a==void 0)c=this.channelId;var d=b;if(b==null||b==void 0)d=0;this.callbackObj.ref.tvie_live_play(c,d)}};TViePlayer.prototype.pause=function(){this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0&&this.callbackObj.ref.tvie_pause()};
TViePlayer.prototype.play=function(){this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0&&this.callbackObj.ref.tvie_play()};TViePlayer.prototype.stop=function(){this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0&&this.callbackObj.ref.tvie_stop()};TViePlayer.prototype.current_time=function(){if(this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0)return this.callbackObj.ref.tvie_current_time()};
TViePlayer.prototype.current_channel=function(){if(this.callbackObj.success&&this.callbackObj.ref!=null&&this.callbackObj.ref!=void 0&&this.callbackObj.ref.tvie_current_channel!=void 0)return this.callbackObj.ref.tvie_current_channel();return 0};
TViePlayer.prototype.addPlugin=function(a,b,c,d,e,f,g,h,i){if(a==void 0||a==null)throw Error("invalid url: "+a);var j="plugin_"+b.mode;b.type!=void 0&&(j+="_"+b.type);j+="_"+this.plugins.length;a=new TViePlugin(j,a);this.plugins.push(a);if(b.mode==Consts.pluginModeIsolate)a.setModeIsolate();else if(b.mode==Consts.pluginModeEmbeded)if(b.type==Consts.pluginModeEmbededPrePlayAd)a.setModeEmbededPrePlayAd();else if(b.type==Consts.pluginModeEmbededOnPauseAd)a.setModeEmbededOnPauseAd();else if(b.type==Consts.pluginModeEmbededOnEndAd)a.setModeEmbededOnEndAd();
else if(b.type==Consts.pluginModeEmbededProgressBarTips)a.setModeEmbededProgressBarTips();else if(b.type==Consts.pluginModeEmbededFacade)a.setModeEmbededFacade();else if(b.type==Consts.pluginModeEmbededOnPlayAd)a.setModeEmbededOnPlayAd();else throw Error("invalid mode type: "+b.type);else throw Error("invalid mode: "+b.mode);if(c.layout==Consts.pluginLayoutAutoFill&&b.type!=Consts.pluginModeEmbededPrePlayAd)c.layout=Consts.pluginLayoutFloat;if(c.layout==Consts.pluginLayoutAutoFill)a.setLayout(c.layout);
else if(c.layout==Consts.pluginLayoutFloat){a.setLayoutFloat();c.x==void 0?a.setLayoutFloatPos(0):a.setLayoutFloatPos(c.x);c.y==void 0?a.setLayoutFloatPos(null,0):a.setLayoutFloatPos(null,c.y);if(c.horizen!=void 0)if(c.horizen==Consts.pluginLayoutFloatHorizenLeft)a.setLayoutFloatAignLeft();else if(c.horizen==Consts.pluginLayoutFloatHorizenCenter)a.setLayoutFloatAignCenter();else if(c.horizen==Consts.pluginLayoutFloatHorizenRight)a.setLayoutFloatAignRight();else throw Error("invalid layout float horizen: "+
c.horizen);if(c.vertical!=void 0)if(c.vertical==Consts.pluginLayoutFloatVerticalTop)a.setLayoutFloatAignTop();else if(c.vertical==Consts.pluginLayoutFloatVerticalMiddle)a.setLayoutFloatAignMiddle();else if(c.vertical==Consts.pluginLayoutFloatVerticalBottom)a.setLayoutFloatAignBottom();else throw Error("invalid layout float vertical: "+c.vertical);}else if(c.layout==Consts.pluginLayoutDocked)if(c.position==Consts.pluginLayoutDockedTop)a.setLayoutDockedTop();else if(c.position==Consts.pluginLayoutDockedBottom)a.setLayoutDockedBottom();
else if(c.position==Consts.pluginLayoutDockedLeft)a.setLayoutDockedLeft();else if(c.position==Consts.pluginLayoutDockedRight)a.setLayoutDockedRight();else throw Error("invalid layout docked position: "+c.position);else throw Error("invalid layout: "+c.layout);if(d!=void 0&&d!=null)for(b=0;b<d.length-1;b+=2)a.addParam(d[b],d[b+1]);a.duration=e==void 0||e==null?-1:e;a.fullscreenVisible=f==void 0||f==null?!1:f;a.closable=g==void 0||g==null?!1:g;a.delay=h==void 0||h==null?0:h;a.share=i==void 0||i==null?
!1:i};function TViePlugin(a,b){this.id=a;this.url=b;this.paramKey=[];this.paramValue=[]}TViePlugin.prototype.setModeIsolate=function(){this.mode=Consts.pluginModeIsolate};TViePlugin.prototype.setModeEmbeded=function(){this.mode=Consts.pluginModeEmbeded};TViePlugin.prototype.setModeEmbededPrePlayAd=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededPrePlayAd};TViePlugin.prototype.setModeEmbededOnPauseAd=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededOnPauseAd};
TViePlugin.prototype.setModeEmbededOnPlayAd=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededOnPlayAd};TViePlugin.prototype.setModeEmbededOnEndAd=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededOnEndAd};TViePlugin.prototype.setModeEmbededProgressBarTips=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededProgressBarTips};TViePlugin.prototype.setModeEmbededFacade=function(){this.setModeEmbeded();this.modeType=Consts.pluginModeEmbededFacade};
TViePlugin.prototype.setLayoutFloat=function(){this.layout=Consts.pluginLayoutFloat};TViePlugin.prototype.setLayout=function(a){this.layout=a};TViePlugin.prototype.setLayoutFloatPos=function(a,b){this.setLayoutFloat();if(a!=void 0&&a!=null)this.layoutX=a;if(b!=void 0&&b!=null)this.layoutY=b};TViePlugin.prototype.setLayoutFloatAignLeft=function(){this.setLayoutFloat();this.layoutHorizen=Consts.pluginLayoutFloatHorizenLeft};
TViePlugin.prototype.setLayoutFloatAignRight=function(){this.setLayoutFloat();this.layoutHorizen=Consts.pluginLayoutFloatHorizenRight};TViePlugin.prototype.setLayoutFloatAignCenter=function(){this.setLayoutFloat();this.layoutHorizen=Consts.pluginLayoutFloatHorizenCenter};TViePlugin.prototype.setLayoutFloatAignTop=function(){this.setLayoutFloat();this.layoutVertical=Consts.pluginLayoutFloatVerticalTop};
TViePlugin.prototype.setLayoutFloatAignMiddle=function(){this.setLayoutFloat();this.layoutVertical=Consts.pluginLayoutFloatVerticalMiddle};TViePlugin.prototype.setLayoutFloatAignBottom=function(){this.setLayoutFloat();this.layoutVertical=Consts.pluginLayoutFloatVerticalBottom};TViePlugin.prototype.setLayoutDocked=function(){this.layout=Consts.pluginLayoutDocked};TViePlugin.prototype.setLayoutDockedLeft=function(){this.setLayoutDocked();this.layoutDockedPos=Consts.pluginLayoutDockedLeft};
TViePlugin.prototype.setLayoutDockedRight=function(){this.setLayoutDocked();this.layoutDockedPos=Consts.pluginLayoutDockedRight};TViePlugin.prototype.setLayoutDockedTop=function(){this.setLayoutDocked();this.layoutDockedPos=Consts.pluginLayoutDockedTop};TViePlugin.prototype.setLayoutDockedBottom=function(){this.setLayoutDocked();this.layoutDockedPos=Consts.pluginLayoutDockedBottom};TViePlugin.prototype.addParam=function(a,b){this.paramKey.push(a);this.paramValue.push(b)};
TViePlugin.prototype.toJSON=function(){var a="{";a+="'id':'"+this.id+"'";a+=", 'url':'"+this.url+"'";a+=", 'mode':'"+this.mode+"'";a+=", 'delay':'"+this.delay+"'";a+=", 'share':'"+this.share+"'";this.mode==Consts.pluginModeEmbeded&&(a+=", 'type':'"+this.modeType+"'");a+=", 'layout':'"+this.layout+"'";this.layout==Consts.pluginLayoutFloat?(a+=", 'x':'"+this.layoutX+"'",a+=", 'y':'"+this.layoutY+"'",this.layoutHorizen!=void 0&&(a+=", 'horizen':'"+this.layoutHorizen+"'"),this.layoutVertical!=void 0&&
(a+=", 'vertical':'"+this.layoutVertical+"'")):a+=", 'position':'"+this.layoutDockedPos+"'";a+=", 'fullscreenVisible':'"+this.fullscreenVisible+"'";a+=", 'closable':'"+this.closable+"'";this.duration!=-1&&(a+=", 'duration':'"+this.duration+"'");if(this.paramKey.length>0){a+=", 'param':'";for(var b=0;b<this.paramKey.length;b++)a+=this.paramKey[b],a+="=",a+=this.paramValue[b],b<this.paramKey.length-1&&(a+=",");a+="'"}a+="}";return a};