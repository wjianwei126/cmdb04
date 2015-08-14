  $(document).ready(function() {
      $('#oldpassword').change(function () {
          oldpass = $('#oldpassword').val();
          data = {oldpassword: oldpass};
          $.ajax({
              url:"/user/checkoldpasswd/",
              data:data,
              type:'post',
              success: function(e){
                  error_id =e;
                  if (error_id == 0) {
                      if (oldpass.length > 0){
                        $("#tip1").html("<font color=\"green\" size=\"2\">  密码正确</font>");
                      }
                      tag = 1;
                  }
                  else {
                      if (oldpass.length > 0){ //防止未填密码,鼠标掠过时报Wrong
                        $("#tip1").html("<font color=\"red\" size=\"2\">  密码错误</font>");
                      }
                  }
              },
              error: function(){
                alert(arguments[1]);
               }
          })
      });
      $('#newpassword2').mouseout(function () {
       newpass1 = $('#newpassword1').val();
       newpass2 = $('#newpassword2').val();
          if (newpass1.length > 0 && newpass2.length > 0){
           if ( newpass1 == newpass2 ){
              $("#tip2").html("<font color=\"green\" size=\"2\">  密码一致</font>");
              if ( tag == 1){
                  $('#changepasswdbt').removeAttr("disabled")
              }
          }
          else{
              $("#tip2").html("<font color=\"red\" size=\"2\">  密码不一致</font>");
          }
          }
          else{
               $("#tip2").html("<font color=\"red\" size=\"2\">  不允许为空</font>");
          }
      });
      $("#changepasswdbt").click(function(){
          data = {oldpassword: oldpass,newpassword1:newpass1,newpassword2:newpass2};
          $.ajax({
              url:"/user/changepwd/",
              data:data,
              type:'post'
          });
    });




  });

