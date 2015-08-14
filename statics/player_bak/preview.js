    function preview(id,type){
        document.getElementById('playerdiv').className = '';
        document.getElementById('shade').className = 'modal-backdrop';
        var id = id;
        //var width = 400/*video*/+20/*margin*/;
        var width = 500/*video*/;
        //var height = 300/*video*/+75/*component*/;
        var height = 400/*video*/;
        var resourceRoot = '/statics/player/';
        var player = new TViePlayer("player", resourceRoot+"CBNSimpleLiveSkin.swf", width, height);
        var stream = $("td[data-uid-"+type+"=" + id + "]").text();
        player.setHttpProgressiveMode(stream);
        player.videoScaleMode = "original";
        player.run();
    }
 function fadeOut() {
       $("#playerdiv").empty();
       $("#playerdiv").append("<button type='button' class='close' onclick='fadeOut()'><span class='btn btn-danger'>关闭</span></button><div id='player'></div>");
       document.getElementById('shade').className = 'modal-backdrop hide';
       document.getElementById('playerdiv').className = 'hide';
    }