function fuzhiinput(id){
	$('#input_b_'+id).zclip({
		path: '/statics/zclip/ZeroClipboard.swf',
		copy: $('#input_'+id).text(),
		afterCopy: function(){
			$("td[data-uid-input=" + id + "]").css("color","rgb(85, 26, 139)");
		}
	});
}
function fuzhiout(id){
	$('#output_b_'+id).zclip({
		path: '/statics/zclip/ZeroClipboard.swf',
		copy: $('#output_'+id).text(),
		afterCopy: function(){
			$("td[data-uid-output=" + id + "]").css("color","rgb(85, 26, 139)");
		}
	});
}