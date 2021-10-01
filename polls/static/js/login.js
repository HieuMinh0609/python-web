
function login(){
 
    let password_login=$("#password_login").val()
    let email_login = $("#email_login").val()
    console.log(password_login+email_login)
    let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();	
    if(password_login&&email_login) {

        var data = new FormData();  
        data.append("password",password_login)  
        data.append("email",email_login)  
    	data.append("csrfmiddlewaretoken", csrf_token);
        $.ajax({
            url: '/polls/loginApi',
            method:'POST',
            data:data,
            cache: false,                                               //Upload files without caching
            processData:false,                                          //Do not serialize data
            contentType:false, 
            success: function (res) {
                console.log(res)
                
                if(res===500) alert("Thông tin tài khoản không chính xác !")
                else {
                    window.location.href="/polls/"
                    sessionStorage.setItem('userInfo', JSON.stringify(res))
                }
            },
            error: function (res) {
                console.log(res)
               // window.location.href="/polls/"
            }
        });
    }else alert("Nhập đầy đủ thông tin !")
}


function register(){
    let username =  $("#username").val()
    let password=$("#password").val()
    let email = $("#email").val()
    let fullname=($("#fullname").val())?$("#fullname").val():username
    var image = ($("#avatar").get(0).files[0])?$("#avatar").get(0).files[0].name :"userqk.jpg"
    let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();	
    console.log(username+"-"+password+"-"+email+"-"+csrf_token)
    if(checkLogin(email,username,password)) {

        var data = new FormData();  
        data.append("username",username)  
        data.append("password",password)  
        data.append("email",email)  
        data.append("image",image)  
        data.append("fullname",fullname) 
    	data.append("csrfmiddlewaretoken", csrf_token);
        $.ajax({
            url: '/polls/registerApi',
            method:'Post',
            // headers: { "X-CSRFToken": getCookie("csrftoken") },
            data:data,
            cache: false,                                               //Upload files without caching
            processData:false,                                          //Do not serialize data
            contentType:false, 
            success: function (res) {
                alert("Đăng ký tài khoản thành công !")
                location.reload()
            },
                error: function (res) {
                console.log(res)
            }
        });
    }
}
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }
function checkLogin(email,username,password){
   if(username && password && email) {
        $("#username").css("border","1px solid  #ced4da") ; 
        $("#email").css("border","1px solid  #ced4da") ; 
        $("#password").css("border","1px solid  #ced4da") ; 
        return true ;
   }else{
    // $("#username").css("border","1px solid red")
    // $("#email").css("border","1px solid red");
    // $("#password").css("border","1px solid red");
        if(username)    $("#username").css("border","1px solid #ced4da")
        else {
            $("#username").css("border","1px solid red") ; 
        }

        if(email)  $("#email").css("border","1px solid #ced4da")
        else {
            $("#email").css("border","1px solid red")
        }

        if(password) $("#password").css("border","1px solid #ced4da")
        else {
            $ ("#password").css("border","1px solid red")
            
        }
        return false
   }
}

function uploadAvatar(){
    var f_obj = $("#avatar").get(0).files[0];
    // console.log("File object:",f_obj);
    // console.log("The file name is:",f_obj.name);
    // console.log("The file size is:",f_obj.size);
    var data = new FormData();                                      //Create formdata objects to facilitate file transfer to the back end
    data.append("file",f_obj)                                        //To add (encapsulate) a file object to a formdata object
	let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();				
	console.log(csrf_token);				
	data.append("csrfmiddlewaretoken", csrf_token);
    $.ajax({
        url:'/polls/uploadFileApi',
        type:'POST',
        data:data,
        cache: false,                                               //Upload files without caching
        processData:false,                                          //Do not serialize data
        contentType:false, 
        // enctype: 'multipart/form-data',
        // beforeSend: function (xhr) {
        //     xhr.setRequestHeader('X-CSRFToken', '{{csrf_token}}');
        // },                                         //No special connection type defined
        success:function (res ) {
            $(".img_upload").attr("src","/static/img/"+res)
            console.log(res)
        },
        error: function (res) {
            console.log(res)
        }
    })
 
}

function forgetPass(){
    var email = document.getElementById('forgetPass'); 
    var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/; 
    if (!filter.test(email.value)) { 
            alert('Hay nhap dia chi email hop le.\nExample@gmail.com');
            email.focus;     
    }
    else{
        var data = new FormData();  
        let csrf_token = $('input[name="csrfmiddlewaretoken"]').val();	
        data.append("email",email.value)  
        data.append("csrfmiddlewaretoken", csrf_token);
        $.ajax({
            url: '/polls/forgetPassApi',
            method:'POST',
            data:data,
            cache: false,                                               //Upload files without caching
            processData:false,                                          //Do not serialize data
            contentType:false, 
            success: function (res) {
               if(res===200) {
                alert("Mật khẩu mới đã gửi lại qua địa chỉ email của bạn . Vui lòng kiểm tra email !")
                location.reload()
               }
               else alert("Email không tồn tại !")
            },
                error: function (res) {
                console.log(res)
            }
        });
    }
          
}