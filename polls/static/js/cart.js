$( document ).ready(function() {
    let userinfo = JSON.parse(sessionStorage.getItem('userInfo'));
    let iduser=userinfo[2]
    
    $.ajax({
        url: '/polls/getAmountItemApi?iduser='+iduser,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            console.log(res)
            showItems(res.item_in_cart)
        },
            error: function (res) {
            console.log(res)
        }
    });
});

function showItems(res){
    let item =``

    let total_money = 0;
        $.each(res,function(k,v){
           total_money+=v[7]
           item +=
               `
                <tr>
                    <td scope="row" style="width: 40%;">
                        <div class="d-flex">
                            <div class="img mr-3">
                            <img src="/static/img/${v[4]}" class="img_item_cart" style="width: 75px; height: 75px;">
                            </div>
                            <div class="name_item_cart">
                            <p class="text_item_cart" style="font-weight: bold;"> ${v[6]}</p>
                            </div>
                        </div>
                    </td>
                    <td>
                        <div>
                         
                            <span class="_1CXksa text_item_cart">₫${v[5]}</span>
                        </div>
                    </td>
                    <td>
                        <div class="d-flex">
                            <button class="product-add product-variation mg-0" iditem='${v[0]}' idcart='${v[2]}' onclick="increase(this)">+</button>
                            <input type="number" class="product-variation value_number value_number_${v[0]} mg-0" value="${v[3]}" 
                            onchange="update_total_cart(this)" iditem='${v[0]}'
                            >
                            <button class="product-sub product-variation" iditem='${v[0]}' idcart='${v[2]}' onclick="decrease(this)">-</button>
                        </div>
                    </td>
            
                    <td>
                        <span class="_1CXksa text_item_cart" style="color: #ee4d2d;" >₫${v[7]}</span>
                    </td>
                    <td>
                        <a href="#" class="text_item_cart" style="color: #ee4d2d;" iditem='${v[0]}' onclick="deleteItem(this)">
                        Xóa
                        </a>
                    </td>
              </tr>
                `

        })

       $(".list_item").html(item)
       $(".total_price").html(`Tổng tiền thanh toán là : ${total_money} vnđ`)
   
}


function deleteItem(e){
    let id = $(e).attr("iditem")
    if(confirm("Bạn muốn xóa sản phẩm này ra khỏi giỏ hàng ?")){
        $.ajax({
            url: '/polls/deleteItemInCartApi?iditem='+id,
            method:'get',
            dataType: 'json',
            contentType: "application/json",
            success: function (res) {
                console.log(res)
                showItems(res)
                alert("Xóa sản phẩm thành công !")
            },
            error: function (res) {
                console.log(res)
            }
        });
    }

}


function increase(e){
    let iditem = $(e).attr("iditem")
    let idcart= $(e).attr("idcart")
    let className = `.value_number_`+iditem
    let number_product = parseInt($(`${className}`).val())+1
    $(`${className}`).val(number_product)
    // $(e).prop("onclick", null).off("click");
    $(e).prop( "onclick", null )
    $.ajax({
        url: '/polls/updateCartApi?iditem='+iditem+'&total_sold='+number_product,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            $(e).prop( "onclick", "increase(this)" )
            showItems(res)
        },
        error: function (res) {
            console.log(res)
        }
    });
}

function decrease(e){
    let iditem = $(e).attr("iditem")
    let idcart= $(e).attr("idcart")
    let className = `.value_number_`+iditem
    let number_product = parseInt($(`${className}`).val())-1
    number_product = (number_product>0)? number_product : 0
    $(`${className}`).val(number_product)
    $(e).prop( "onclick", null )
    $.ajax({
        url: '/polls/updateCartApi?iditem='+iditem+'&total_sold='+number_product,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            $(e).prop( "onclick", "decrease(this)" )
            showItems(res)
        },
        error: function (res) {
            console.log(res)
        }
    });
 

}

function update_total_cart(e){
    let iditem = $(e).attr("iditem")
    let number_product = $(e).val()
    $.ajax({
        url: '/polls/updateCartApi?iditem='+iditem+'&total_sold='+number_product,
        method:'get',
        dataType: 'json',
        contentType: "application/json",
        success: function (res) {
            showItems(res)
        },
        error: function (res) {
            console.log(res)
        }
    });
 
}